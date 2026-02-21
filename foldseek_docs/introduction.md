# Introduction to Foldseek {#fs-introduction}

Foldseek is a structure search and clustering system that keeps the throughput profile of sequence search while preserving the discriminative power needed for structural biology. It does this by converting protein structures into a structural alphabet, then running a cascaded search pipeline that aggressively prunes candidates before expensive scoring. The result is that search, clustering, and multimer analysis share one backbone, but each mode applies different scoring, filtering, and reporting layers.

This manual is organized around that backbone. The practical entry points are described in the [manual](#fs-manual) and [module chapters](#fs-modules-root), while algorithmic and implementation details are centralized in the [expert manual](#fs-expert-root) and [developer manual](#fs-dev-root).

## Structural Representation and 3Di {#fs-3di-overview}

Foldseek does not compare raw coordinates in the prefilter. During `createdb`, each chain is converted into synchronized data streams: amino-acid sequence, 3Di sequence, C-alpha coordinates, and headers. The 3Di stream is produced by feature extraction from local geometric context followed by embedding and discretization in `foldseek/lib/3di/structureto3di.cpp`. This representation is compact enough for fast k-mer indexing and prefiltering, but still captures local structural context that sequence-only scoring misses.

A key design choice is that Foldseek keeps AA and 3Di views aligned at the residue level. This enables `--alignment-type 2` (3Di+AA) to combine structural and sequence evidence in a single alignment stage instead of forcing separate post-hoc rescoring. The same design also allows fast fallback paths (`--alignment-type 0` or `1`) without changing database layout.

## Search and Clustering Backbone {#fs-backbone-overview}

The core search path is staged:

1. K-mer driven candidate generation on structural descriptors.
2. Ungapped and/or diagonal rescoring to cut candidate volume.
3. Full alignment (`structurealign` or `tmalign`) with optional TM-score/LDDT gating.
4. Optional post-processing such as multimer assignment, report creation, clustering, or conversion.

The workflow layer in `foldseek/src/workflow/StructureSearch.cpp` wires these stages and adjusts behavior based on options like `--prefilter-mode`, `--alignment-type`, and `--gpu`. The same structural backbone is reused by `search`, `cluster`, `rbh`, and multimer workflows, which is why tuning one stage often affects multiple commands.

## Structural Scoring Modes {#fs-scoring-overview}

Foldseek exposes three primary alignment modes through `--alignment-type`:

- `0` (3Di alignment): fastest structural-only local alignment path.
- `1` (TM alignment): TM-align-based global structural alignment.
- `2` (3Di+AA): combined local scoring, default for many workflows.

TM-score and LDDT can be used as explicit thresholds (`--tmscore-threshold`, `--lddt-threshold`) and also influence ranking when structure-bit sorting is enabled (`--sort-by-structure-bits 1`). Those interactions are not purely cosmetic; they affect which hits survive and how hits are ordered.

## Multimer Extension {#fs-multimer-overview}

Foldseek-Multimer extends the same single-chain backbone by adding chain expansion, chain-to-chain assignment, and complex-level scoring stages. In practice, `multimersearch` and `multimercluster` call additional modules (`expandmultimer`, `scoremultimer`, internal filtering/reporting) after base alignment so that complex-level quality is computed from concrete chain assignments rather than inferred from monomer hits.

## Database and Index Model {#fs-db-overview}

Foldseek databases are split by data role (`DB`, `DB_ss`, `DB_ca`, `DB_h`, plus indices). This split is central to performance tuning: index and coordinate exclusions can reduce memory and I/O, but they also remove capabilities needed by specific ranking or alignment settings. The practical rules and exact file layout are documented in [Database Management](#fs-db-modules), especially [Core File Formats](#fs-db-file-format), and the runtime implications are documented in [Expert Manual: Data and Performance](#fs-expert-data).

## Reading Order {#fs-reading-order}

For new users, start with [Manual](#fs-manual), then go to [Easy Workflows](#fs-easy-root) and [Structure Search](#fs-search-root). For optimization and interpretation, continue with [Expert Manual](#fs-expert-root). For source-level debugging or extension work, use [Developer Manual](#fs-dev-root).
