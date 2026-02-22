# Foldseek Expert Manual {#fs-expert-root}

This chapter explains the algorithmic and systems design decisions that determine Foldseek behavior at scale. Command syntax and user-facing workflows are covered in the [manual](#fs-manual) and [module chapters](#fs-modules-root); here the focus is model internals, scoring semantics, and data-path constraints.

## 3Di Encoding Engine {#fs-expert-3di}

Foldseek converts structure geometry to discrete 3Di symbols in `foldseek/lib/3di/structureto3di.cpp`. The implementation is a staged encoder rather than a direct heuristic labeler: virtual centers are computed from backbone/side-chain atoms, residue partners are selected, ten geometric features are assembled per pair, features are projected into a learned low-dimensional embedding, and the embedding is quantized to one of twenty centroids.

That architecture is central to throughput. The prefilter does not operate on raw coordinates, and it does not need dynamic structural superposition during candidate generation. It operates on a residue-aligned symbolic stream that preserves enough local geometry to remain discriminative while keeping indexing and k-mer operations cheap.

## Prefilter and Candidate Generation {#fs-expert-prefilter}

For large databases, the prefilter is still the main runtime gate. Foldseek inherits MMseqs-style index and k-mer mechanics, but applies them to 3Di channels (`_ss`) and Foldseek-specific workflow defaults.

Two options define most candidate behavior:

- `--target-search-mode` chooses exact k-mer search or similar-k-mer expansion.
- `--exact-kmer-matching 1` disables similar-k-mer expansion and forces strict seed matching.

`--prefilter-mode` then controls how candidates are refined before full alignment. In workflow code (`foldseek/src/workflow/StructureSearch.cpp`), GPU mode can enforce ungapped-first behavior when other prefilter combinations are incompatible. This is one reason CPU and GPU runs can produce different candidate sets under nominally similar settings.

## Alignment Core: 3Di, 3Di+AA, and TM-align {#fs-expert-alignment}

Foldseek supports three alignment families through `--alignment-type`.

Type `0` uses 3Di local alignment; type `1` uses TM-align-style structural superposition; type `2` combines 3Di and amino-acid evidence in one local alignment objective. In `foldseek/src/strucclustutils/structurealign.cpp`, type `0` and `2` run through `StructureSmithWaterman` (`foldseek/src/commons/StructureSmithWaterman.cpp`) with vectorized query profiles and forward/reverse scoring.

The combined 3Di+AA path is not a cosmetic rerank. It changes the score landscape during alignment itself, so candidate acceptance, tie-breaking, and downstream ranking can differ substantially from pure 3Di or pure TM-oriented runs.

## TM-score and LDDT in Filtering and Ranking {#fs-expert-tm-lddt}

TM-score and LDDT are integrated into runtime filtering and sorting, not only reporting. `TMaligner` (`foldseek/src/commons/TMaligner.cpp`) and `LDDTCalculator` (`foldseek/src/commons/LDDT.cpp`) are invoked in alignment workflows when thresholds or structure-aware sorting require coordinate-derived quality terms.

When `--sort-by-structure-bits 1` is active, `structurealign.cpp` applies a composite structural ranking term (`score * sqrt(lddt * tmscore)`). If required C-alpha channels are missing, Foldseek disables incompatible thresholds/sorting paths with warnings instead of silently producing invalid rankings.

## Multimer Assignment and Complex Scoring {#fs-expert-multimer}

Foldseek-Multimer builds complex scores from chain-level evidence in explicit stages.

`expandmultimer` generates expanded chain-pair candidates. `scoremultimer` then groups those hits by query/target complex and solves assignment consistency before calculating complex-level scores. In `scoremultimer.cpp`, assignment selection uses clustering and chain reuse controls so one local chain optimum does not destabilize the whole complex mapping.

Multimer filtering is implemented inside `scoremultimer.cpp` (`ComplexFilter`), not in a separate module. The filter stack combines global complex TM, coverage, per-chain TM, and interface LDDT gates. This is why thresholds such as `--multimer-tm-threshold`, `--chain-tm-threshold`, and `--interface-lddt-threshold` are complementary rather than interchangeable. For command-level details and field semantics, see [Multimer Modules](#fs-multimer-root).

## Data Layout, Storage Format, and Memory Behavior {#fs-expert-data}

Foldseek databases are multi-channel by design. A single logical entry is distributed across AA (`DB`), 3Di (`DB_ss`), coordinates (`DB_ca`), and headers (`DB_h`), all keyed by the same internal ID. This lets workflows load only the channels needed by the current stage while preserving residue alignment between AA and 3Di streams.

### On-disk Containers and Sidecars {#fs-expert-data-containers}

Every channel uses the same MMseqs container pattern: `<name>`, `<name>.index`, `<name>.dbtype`. The index stores `<id, offset, length>` triplets; `.dbtype` stores type and compression flags; optional `.lookup` and `.source` sidecars encode identifier and provenance mappings.

For format-level details (line and payload layout), see [Database Management: Core File Formats](#fs-db-file-format).

### C-alpha Encoding Trade-offs {#fs-expert-data-ca}

`DB_ca` can be stored as float32 coordinates or as delta-encoded int16 (`--coord-store-mode 2`, default). Delta mode stores one int32 start value plus int16 increments per residue and per axis, which cuts footprint and I/O while preserving enough precision for downstream scoring. If a chain overflows int16 deltas during creation, Foldseek falls back to float storage for that entry.

A practical implication is mixed storage at entry granularity: one database can contain mostly diff16 entries plus float fallbacks. The decoder (`Coordinate16::read`) handles both by inspecting entry length.

### Indexed Targets and Exclusion Flags {#fs-expert-data-index}

`createindex` on Foldseek databases is not a single index build; it is a workflow that indexes AA/3Di channels and can append coordinate channels into the `.idx` container. Exclusion flags (`--index-exclude`) and subset flags (`--index-subset`) reduce footprint but remove capabilities.

The important compatibility rule is simple: if ranking or filtering needs coordinate-derived metrics (TM/LDDT/structure-bit sorting), coordinate channels must remain reachable either as side DBs (`_ca`) or appended index components.

### Cluster-search Data Model {#fs-expert-data-cluster}

`createclusearchdb` materializes representative/member split channels (`<db>` and `<db>_seq*`) plus cluster topology (`<db>_clu`). Cluster-search workflows (`--cluster-search 1`) depend on this layout to search representatives first and expand to members without rebuilding mappings at query time.

That split is a major speed lever for very large clustered targets: representative pruning reduces expensive downstream alignment volume, while member expansion restores sensitivity in the final result set.

## GPU Paths and Constraints {#fs-expert-gpu}

Foldseek exposes two major GPU paths:

1. Search workflow acceleration with `--gpu` where compatible prefilter/alignment combinations exist.
2. ProstT5-backed 3Di prediction during `createdb` when `--prostt5-model` is provided and GPU backends are available.

Workflow code enforces compatibility constraints (especially around prefilter mode). For reproducible benchmarking, always report CPU/GPU mode, prefilter mode, and alignment type together.

## Practical Tuning Order {#fs-expert-tuning}

For production optimization, tune in dependency order instead of isolated flags.

1. Control candidate volume first (`-s`, `--max-seqs`, `--prefilter-mode`, k-mer mode).
2. Choose alignment objective (`--alignment-type`) and structural thresholds.
3. Choose ranking semantics (`--sort-by-structure-bits`, TM/LDDT columns).
4. Only then trim storage/index footprint (`--index-subset`, `--index-exclude`, coordinate mode).

Most wall-clock gains come from reducing candidate volume and avoiding incompatible scoring paths early, not from late-stage filtering changes alone.
