### Multimer Modules {#fs-multimer-root}

Foldseek-Multimer extends the single-chain Foldseek backbone into complex-level comparison. It still starts from chain-to-chain candidates, but adds complex-aware expansion, assignment discovery, global superposition scoring, and interface-aware filtering before final reporting.

Workflow orchestration is implemented in `foldseek/src/workflow/MultimerSearch.cpp`, `foldseek/src/workflow/MultimerCluster.cpp`, and shell templates under `foldseek/data/`. Assignment search, geometric clustering, and all multimer-specific filters are implemented in `foldseek/src/strucclustutils/expandmultimer.cpp`, `scoremultimer.cpp`, and `MultimerUtil.h`. `createmultimerreport.cpp` is a reporting layer that restructures already-scored assignments.

#### Complex Search Pipeline {#fs-multimer-pipeline}

In the default `multimersearch` workflow (`foldseek/data/multimersearch.sh`), the stages are executed in this order:

1. `search`: run the standard Foldseek chain-level search backbone.
2. `expandmultimer`: convert sparse chain hits into complex-consistent chain-pair candidate lists.
3. `structurealign` or `tmalign`: realign expanded chain pairs when expansion is enabled.
4. `scoremultimer`: construct chain assignments, score complex-level superposition, apply multimer filters, and emit complex-aware alignment records.
5. Optional conversion/reporting (`convertalis`, `createmultimerreport`) in the easy wrapper.

This staged design postpones one-to-one chain assignment until enough evidence has been collected. A single early chain hit does not immediately lock the complex mapping.

#### `multimersearch` {#fs-multimersearch}

**Usage**

```bash
foldseek multimersearch <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
```

`multimersearch` is the main DB-to-DB multimer pipeline. Besides standard structure-search options, the multimer-specific controls that change behavior most are `--expand-multimer-evalue`, `--min-assigned-chains-ratio`, and `--monomer-include-mode`.

Implementation detail that matters for tuning: in non-exhaustive mode, the workflow performs an initial fast search and then realigns expanded chain pairs before complex scoring. In exhaustive mode (`--exhaustive-search 1`), the expansion/re-alignment branch is skipped and scoring runs directly on exhaustive pairwise alignments.

#### `expandmultimer` {#fs-expandmultimer}

**Usage**

```bash
foldseek expandmultimer <i:queryDB> <i:targetDB> <i:alignmentDB> <o:prefilterDB> [options]
```

`expandmultimer` is the candidate-space completion step before assignment scoring. It reads query and target `.lookup` mappings to recover complex membership, then executes the following logic:

1. For each query complex, collect target complex IDs that have at least one chain hit in `alignmentDB`.
2. For each collected target complex, generate all query-chain × target-chain pairs for that complex pair.
3. Write per-query-chain candidate target-chain lists into `prefilterDB` for downstream alignment/scoring.

This step deliberately expands sparse chain evidence into complex-consistent candidate sets so later assignment can test complete mappings instead of isolated local hits.

#### `scoremultimer` {#fs-scoremultimer}

**Usage**

```bash
foldseek scoremultimer <i:queryDb> <i:targetDb> <i:alignmentDB> <o:complexDB> [options]
```

`scoremultimer` is the core multimer algorithm. It parses chain-level alignments with backtraces, builds candidate chain-to-chain alignment objects, clusters them into assignment hypotheses, computes complex-level superposition/TM, and applies multimer-specific filters.

##### Assignment construction {#fs-scoremultimer-assignment}

For each query complex and target complex pair, `scoremultimer` (`ComplexScorer` in `scoremultimer.cpp`) converts chain-level records into `ChainToChainAln` objects. Each object stores matched C-alpha coordinates, chain keys, chain-level TM score, and the 12-parameter rigid transform vector (`u` rotation and `t` translation).

Before clustering, transforms are standardized component-wise (z-score style, with low-variance dimensions damped) so geometric distance between alignments is comparable across parameters.

##### Assignment clustering and one-to-one consistency {#fs-scoremultimer-clustering}

Assignment discovery uses a DBSCAN-like clustering layer (`DBSCANCluster`):

- `--min-assigned-chains-ratio` sets the minimum cluster size as `ceil(query_chain_count * ratio)`.
- A reciprocal-best-hit-style pruning keeps alignments whose chain TM score is within `0.7 * max(best(query_chain), best(target_chain))`.
- Distance is computed in transform space. If a cluster contains repeated query or target chains, nearest-neighbor truncation enforces one-to-one chain usage.

Each surviving cluster is converted into one `Assignment`: matched residues from member chain alignments are concatenated, then a complex-level rigid transform and TM score are recomputed over the merged coordinate set.

Complex TM is normalized both ways:

`qTM = tmscore * min(qLen, tLen) / qLen`, `tTM = tmscore * min(qLen, tLen) / tLen`

so asymmetric complex sizes remain interpretable.

##### Filtering order in `scoremultimer` {#fs-scoremultimer-filter-order}

Filtering is executed in a strict order (`ComplexFilter::filterAssignment`), and early failures stop evaluation:

1. Minimum aligned chains (`--min-aligned-chains`).
2. Complex-level TM gate (`--multimer-tm-threshold`, interpreted by `--cov-mode`).
3. Complex coverage gate (`-c`, `--cov-mode`).
4. Chain-level TM gate (`--chain-tm-threshold`), also interpreted by `--cov-mode`.
5. Interface gate (`--interface-lddt-threshold`) using query-defined interface residues and LDDT on matched interface atoms.

Interface residues are precomputed on the query complex from inter-chain C-alpha proximity (8 A cutoff constant in code). If only one chain is aligned and `--interface-lddt-threshold > 0`, the assignment is rejected.

After filtering, only the best assignment per target complex is retained for output (selected by adjusted coverage according to `--cov-mode`).

##### Output fields produced by `scoremultimer` {#fs-scoremultimer-fields}

In addition to chain-level alignment fields, `scoremultimer` appends multimer fields consumed by `convertalis` and `createmultimerreport`, including:

- `complexqtmscore`, `complexttmscore`
- `complexu`, `complext`
- `qcomplexcoverage`, `tcomplexcoverage`
- `qchaintms`, `tchaintms`
- `interfacelddt`
- `complexassignid`

#### `createmultimerreport` {#fs-createmultimerreport}

**Usage**

```bash
foldseek createmultimerreport <i:queryDb> <i:targetDb> <i:complexDB> <o:complexFile> [options]
```

`createmultimerreport` groups chain-level records by assignment ID and emits one complex-level row per assignment. It is a formatter, not a rescoring stage.

The report columns are:

| Column | Meaning |
| :--- | :--- |
| `query_complex`, `target_complex` | Complex identifiers parsed from chain headers. |
| `query_chains`, `target_chains` | Chain-name lists assigned in this solution. |
| `qTM`, `tTM` | Complex TM normalized by query and target lengths. |
| `u`, `t` | 3x3 rotation and translation vector of complex superposition. |
| `qComplexCov`, `tComplexCov` | Coverage fractions computed during filtering. |
| `qChainTms`, `tChainTms` | Comma-separated per-chain TM values. |
| `interfaceLddt` | Interface LDDT for the selected assignment. |
| `assId` | Assignment identifier (stable within each query complex result set). |

#### `multimercluster` {#fs-multimercluster}

**Usage**

```bash
foldseek multimercluster <i:sequenceDB> <o:clusterDB> <tmpDir> [options]
```

`multimercluster` runs `multimersearch` followed by clustering (`clust`) on multimer-filtered edges. The command sets stricter runtime defaults than generic search (`setMultimerClusterDefaults` in `MultimerCluster.cpp`):

- `--multimer-tm-threshold 0.65`
- `--chain-tm-threshold 0.001`
- `--interface-lddt-threshold 0.5`

These gates act on different failure modes and are intentionally complementary:

| Threshold | What it screens |
| :--- | :--- |
| `--multimer-tm-threshold` | Global complex-level alignment quality. |
| `--chain-tm-threshold` | Per-chain geometric compatibility within assignments. |
| `--interface-lddt-threshold` | Interface preservation quality across assigned complexes. |

#### Easy Multimer Wrappers {#fs-multimer-easy}

- [easy-multimersearch](#fs-easy-multimersearch): raw structure input to complex search output.
- [easy-multimercluster](#fs-easy-multimercluster): raw structure input to complex clusters.

These wrappers are convenient for direct file-based workflows, but the core algorithmic stages remain `multimersearch`/`scoremultimer`/`multimercluster`. For deeper algorithm context, see [Multimer Assignment and Complex Scoring](#fs-expert-multimer).
