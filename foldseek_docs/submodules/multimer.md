### Multimer Modules {#fs-multimer-root}

Foldseek-Multimer extends single-chain search into complex-level comparison. The pipeline still begins with candidate chain alignments, but then adds complex-aware expansion, assignment, and scoring to determine whether two assemblies are globally compatible.

Workflow orchestration is in `foldseek/src/workflow/MultimerSearch.cpp` and `foldseek/src/workflow/MultimerCluster.cpp`; assignment and scoring internals are in `foldseek/src/strucclustutils/scoremultimer.cpp`, `expandmultimer.cpp`, and `filtermultimer.cpp`.

#### Complex Search Pipeline {#fs-multimer-pipeline}

A typical multimer search run consists of:

1. Chain-level search/alignment using the standard structural backbone.
2. Expansion of candidate chain pairs with `expandmultimer`.
3. Assignment and complex-level TM aggregation with `scoremultimer`.
4. Optional report emission (`createmultimerreport`) and filtering/clustering.

This design avoids forcing one chain mapping per hit too early; multiple chain assignments can be explored before final complex scoring.

#### `multimersearch` {#fs-multimersearch}

**Usage**

```bash
foldseek multimersearch <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
```

In addition to regular search controls, multimer-specific options include `--min-assigned-chains-ratio`, `--monomer-include-mode`, `--expand-multimer-evalue`, and `--multimer-report-mode`.

This command should be your default for DB-to-DB complex search because it preserves all multimer stages in one workflow.

#### `expandmultimer` {#fs-expandmultimer}

**Usage**

```bash
foldseek expandmultimer <i:queryDB> <i:targetDB> <i:alignmentDB> <o:prefilterDB> [options]
```

`expandmultimer` builds expanded chain-pair candidate sets for downstream assignment/scoring. Use it explicitly when you want to inspect or reuse expanded candidates before complex scoring.

#### `scoremultimer` {#fs-scoremultimer}

**Usage**

```bash
foldseek scoremultimer <i:queryDb> <i:targetDb> <i:alignmentDB> <o:complexDB> [options]
```

`scoremultimer` transforms chain-level alignments into complex-level assignments and scores. In source (`scoremultimer.cpp`), assignment construction enforces chain consistency and computes query- and target-normalized complex TM metrics.

Two key controls are:

- `--min-assigned-chains-ratio`: rejects assignments with insufficient chain coverage.
- `--monomer-include-mode`: controls whether monomer-like complexes are retained.

#### `createmultimerreport` {#fs-createmultimerreport}

**Usage**

```bash
foldseek createmultimerreport <i:queryDb> <i:targetDb> <i:complexDB> <o:complexFile> [options]
```

This command serializes complex assignments into a report-friendly format (text or DB via `--db-output`). Use it after `scoremultimer` when downstream analysis needs explicit chain mapping, transform matrices, and assignment IDs.

#### `multimercluster` {#fs-multimercluster}

**Usage**

```bash
foldseek multimercluster <i:sequenceDB> <o:clusterDB> <tmpDir> [options]
```

`multimercluster` chains multimer search, complex-level filtering, and clustering. Important thresholds include `--multimer-tm-threshold`, `--chain-tm-threshold`, and `--interface-lddt-threshold`.

These thresholds are not interchangeable:

| Threshold | What it screens |
| :--- | :--- |
| `--multimer-tm-threshold` | Global complex-level alignment quality. |
| `--chain-tm-threshold` | Per-chain geometric compatibility within assignments. |
| `--interface-lddt-threshold` | Interface preservation quality across assigned complexes. |

#### Easy Multimer Wrappers {#fs-multimer-easy}

- [easy-multimersearch](#fs-easy-multimersearch): raw structure input to complex search output.
- [easy-multimercluster](#fs-easy-multimercluster): raw structure input to complex clusters.

These wrappers are convenient for direct file-based workflows but use the same core multimer stages.
