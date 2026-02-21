### Structure Search Modules {#fs-search-root}

This chapter covers the core single-chain search stack. The key distinction is orchestration versus execution: `search` is a workflow driver, while `structurealign`, `structurerescorediagonal`, and `tmalign` are lower-level alignment/rescoring modules.

In source terms, orchestration is in `foldseek/src/workflow/StructureSearch.cpp`, and alignment kernels are in `foldseek/src/strucclustutils/` plus `foldseek/src/commons/`.

#### Pipeline Model {#fs-search-pipeline}

The standard path is prefilter -> optional diagonal rescoring -> alignment. `--prefilter-mode` governs which prefilter stages run, and `--alignment-type` chooses the final alignment kernel. The workflow can change behavior under GPU mode; for example, the code path in `StructureSearch.cpp` forces ungapped prefilter defaults when needed.

`--sort-by-structure-bits` changes ranking from plain bit score to a structure-aware term. Because that ranking depends on TM/LDDT information, disabling structure-bit sorting changes how threshold options interact with final ordering.

#### `search` {#fs-search-command}

**Usage**

```bash
foldseek search <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
```

`search` is the canonical entry point for DB-to-DB structural search. Important controls:

| Option | Effect |
| :--- | :--- |
| `-s` | Primary sensitivity/speed tradeoff in candidate generation. |
| `--prefilter-mode` | `0`: k-mer+ungapped, `1`: ungapped only, `2`: nofilter, `3`: ungapped+gapped. |
| `--alignment-type` | `0`: 3Di, `1`: TM-align, `2`: 3Di+AA. |
| `--sort-by-structure-bits` | Enables structure-aware ranking. |
| `--tmscore-threshold`, `--lddt-threshold` | Structural quality filtering. |
| `--cluster-search` | Representative-first search for clustered targets. |
| `--gpu` | CUDA search path when supported by the current build. |

`search` should be preferred over direct low-level modules unless you intentionally control intermediate artifacts.

#### `structurealign` {#fs-search-structurealign}

**Usage**

```bash
foldseek structurealign <i:queryDB> <i:targetDB> <i:prefilterDB> <o:resultDB> [options]
```

`structurealign` consumes a candidate list (`prefilterDB`) and performs full structural alignment on those pairs. It is the right tool when you already own candidate generation, or when you need to re-align candidate pairs under different thresholds without rerunning prefilter.

Notable behavior from `structurealign.cpp`:

- TM/LDDT thresholding is enforced during alignment output.
- Some option combinations are normalized with warnings, especially around `--sort-by-structure-bits` versus lightweight alignment-output modes.

#### `structurerescorediagonal` {#fs-search-rescorediagonal}

**Usage**

```bash
foldseek structurerescorediagonal <i:queryDB> <i:targetDB> <i:prefilterDB> <o:resultDB> [options]
```

This module rescales candidate diagonals using structural scoring and can apply TM/LDDT gating earlier than full workflow composition. It is useful when you want to refine candidate quality in a modular pipeline before deciding on final alignment/reporting stages.

#### `tmalign` {#fs-search-tmalign}

**Usage**

```bash
foldseek tmalign <i:queryDB> <i:targetDB> <i:prefilterDB> <o:resultDB> [options]
```

`tmalign` runs TM-align directly on candidate pairs. Use it when global structural superposition quality is the primary objective and you already have candidate pairs prepared.

Important options are `--tmscore-threshold`, `--tmscore-threshold-mode`, `--tmalign-hit-order`, and `--tmalign-fast`.

#### `rbh` {#fs-search-rbh}

**Usage**

```bash
foldseek rbh <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
```

`rbh` runs reciprocal best-hit filtering on top of the structural search stack. It is the low-level counterpart to `easy-rbh`, with full DB-based workflow control.

#### Practical Composition Patterns {#fs-search-patterns}

A common advanced pattern is to keep stages explicit:

```bash
foldseek search queryDB targetDB alnDB tmp
foldseek convertalis queryDB targetDB alnDB result.tsv --format-output query,target,alntmscore,lddt,evalue,bits
```

For explicit candidate reuse:

```bash
foldseek structurerescorediagonal queryDB targetDB prefilterDB rescoredDB
foldseek structurealign queryDB targetDB rescoredDB alnDB
```

This separation is especially useful for benchmarking alternative scoring thresholds or alignment modes on the same candidate set.
