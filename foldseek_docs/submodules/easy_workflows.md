### Easy Workflows {#fs-easy-root}

The easy workflows are front doors that accept structure files directly and orchestrate database creation, search/alignment, and output conversion. They trade fine-grained control for speed of setup and are ideal when you want reliable defaults with minimal command composition.

Internally, these workflows are orchestrated in `foldseek/src/workflow/Easy*.cpp` and shell templates in `foldseek/data/`. If you need strict stage control, use the low-level commands in [Structure Search](#fs-search-root), [Structure Clustering](#fs-cluster-root), and [Multimer Modules](#fs-multimer-root).

#### `easy-search` {#fs-easy-search}

`easy-search` runs end-to-end single-chain structural search from raw structure input to text output.

**Usage**

```bash
foldseek easy-search <i:PDB|mmCIF[.gz]> ... <i:PDB|mmCIF[.gz]>|<i:stdin> <i:targetFastaFile[.gz]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]
```

High-impact options are `-s`, `--prefilter-mode`, `--alignment-type`, `--tmscore-threshold`, `--lddt-threshold`, `--format-mode`, `--format-output`, and `--gpu`.

`--alignment-type` controls whether hits are finalized by 3Di local alignment (`0`), TM-align (`1`), or combined 3Di+AA (`2`). `--prefilter-mode` determines how aggressively candidates are pruned before alignment. `--format-mode 3` produces HTML output and `--format-mode 5` writes superposed C-alpha PDB views.

#### `easy-cluster` {#fs-easy-cluster}

`easy-cluster` performs structure clustering from raw files and produces representative/member outputs.

**Usage**

```bash
foldseek easy-cluster <i:PDB|mmCIF[.gz]> ... <i:PDB|mmCIF[.gz]> <o:clusterPrefix> <tmpDir> [options]
```

This workflow wraps search, alignment filtering, and `clust`. The most important controls are `-c`, `--cov-mode`, `--cluster-mode`, `--alignment-type`, and quality thresholds (`--tmscore-threshold`, `--lddt-threshold`).

#### `easy-rbh` {#fs-easy-rbh}

`easy-rbh` computes reciprocal best hits through a bidirectional structure-search workflow.

**Usage**

```bash
foldseek easy-rbh <i:queryFastaFile1[.gz|.bz2]> <i:targetFastaFile[.gz|.bz2]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]
```

This is appropriate when orthology-style reciprocal filtering is required but you still want the structural scoring stack available through `--alignment-type`, TM-score, and LDDT settings.

#### `easy-multimersearch` {#fs-easy-multimersearch}

`easy-multimersearch` is the multimer counterpart of `easy-search`: it accepts raw complex files and runs complex-aware expansion, assignment, and reporting.

**Usage**

```bash
foldseek easy-multimersearch <i:PDB|mmCIF[.gz]> ... <i:PDB|mmCIF[.gz]>|<i:stdin> <i:targetFastaFile[.gz]>|<i:targetDB> <o:outputFileName> <tmpDir> [options]
```

In addition to standard search controls, multimer workflows expose `--min-assigned-chains-ratio`, `--monomer-include-mode`, `--expand-multimer-evalue`, and `--multimer-report-mode`.

#### `easy-multimercluster` {#fs-easy-multimercluster}

`easy-multimercluster` performs clustering at complex level.

**Usage**

```bash
foldseek easy-multimercluster <i:PDB|mmCIF[.gz]> ... <i:PDB|mmCIF[.gz]> <o:clusterPrefix> <tmpDir> [options]
```

Compared with `easy-cluster`, this workflow adds complex-aware filters such as `--multimer-tm-threshold`, `--chain-tm-threshold`, and `--interface-lddt-threshold`.

#### When to Drop to Low-Level Commands {#fs-easy-when-lowlevel}

Use easy workflows when you need rapid execution from raw inputs. Switch to low-level commands when you need to reuse intermediate DBs, enforce exact prefilter/alignment stages, tune memory/index compatibility, or insert custom conversion/scoring steps between stages.
