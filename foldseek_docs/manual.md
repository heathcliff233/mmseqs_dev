# Foldseek Manual {#fs-manual}

This chapter is the operational map for Foldseek. It does not duplicate command pages; it explains which command family to choose, how stages connect, and which options govern behavior across modules.

## Workflow Selection {#fs-workflow-selection}

| Goal | Primary entry point | Next chapter |
| :--- | :--- | :--- |
| Single-chain structure search from raw files | `easy-search` | [Easy Workflows](#fs-easy-root) |
| Single-chain search from existing DBs | `search` | [Structure Search](#fs-search-root) |
| Reciprocal best-hit screening | `easy-rbh` or `rbh` | [Easy Workflows](#fs-easy-rbh) / [Structure Search](#fs-search-rbh) |
| Single-chain structural clustering | `easy-cluster` or `cluster` | [Easy Workflows](#fs-easy-cluster) / [Structure Clustering](#fs-cluster-root) |
| Complex-level (multimer) search | `easy-multimersearch` or `multimersearch` | [Multimer Modules](#fs-multimer-root) |
| Complex-level clustering | `easy-multimercluster` or `multimercluster` | [Multimer Modules](#fs-multimer-root) |
| Build/maintain databases and indexes | `createdb`, `createindex`, `databases` | [Structure Manipulation](#fs-manip-root), [Database Management](#fs-db-modules) |

The easy workflows are wrappers around lower-level commands. They are best for starting quickly from PDB/mmCIF inputs, while low-level commands are better for controlled pipelines, reproducibility, and performance tuning.

## Shared Execution Model {#fs-shared-exec-model}

Most workflows pass through the same stages: database preparation, candidate generation, alignment, and conversion/reporting. This is why options such as `-s`, `--prefilter-mode`, `--alignment-type`, and `--sort-by-structure-bits` are visible across many commands and have similar effects.

In `foldseek/src/workflow/StructureSearch.cpp`, the workflow selects prefilter and alignment subcommands dynamically. In multimer workflows (`foldseek/src/workflow/MultimerSearch.cpp`, `foldseek/src/workflow/MultimerCluster.cpp`), the same base stages are followed by chain expansion and complex-level scoring.

## High-Impact Global Options {#fs-global-options}

| Option | Where it matters most | Practical effect |
| :--- | :--- | :--- |
| `-s` | Search and cluster workflows | Higher sensitivity increases candidate volume and runtime. |
| `--prefilter-mode` | `search`, `multimersearch`, easy workflows | Controls whether the pipeline uses k-mer prefilter, ungapped-only, no prefilter, or mixed mode. |
| `--alignment-type` | Search, clustering, multimer | Chooses 3Di-only, TM-align, or 3Di+AA alignment engine. |
| `--sort-by-structure-bits` | Search/alignment workflows | Enables ranking that uses structural quality terms in addition to bit score. |
| `--tmscore-threshold`, `--lddt-threshold` | `structurealign`, `structurerescorediagonal`, clustered/multimer flows | Hard filters on structural quality; can change both recall and ranking. |
| `--gpu` | Search workflows, ProstT5-backed `createdb` | Enables CUDA paths where implemented; may impose prefilter constraints. |
| `--index-subset`, `--index-exclude` | `createindex` | Trade memory and build size against downstream feature availability. |

## Output and Reporting Path {#fs-output-path}

Most search and clustering commands produce internal result databases. Text, HTML, SAM, and superposed structure outputs are generated in later conversion steps, typically via `convertalis`, `createmultimerreport`, or `convert2pdb`. For reproducible pipelines, treat conversion as a separate stage instead of embedding output concerns into search parameter tuning.

## Advanced Reading {#fs-manual-next}

For algorithm details and performance behavior, continue with the [Expert Manual](#fs-expert-root). For source-code ownership, module boundaries, and extension points, continue with the [Developer Manual](#fs-dev-root).

## Module Manual {#fs-modules-root}

The following module chapters are the canonical command reference for Foldseek. They are organized by workflow role and intentionally share options where they share execution stages.

| Module | Focus |
| :--- | :--- |
| [Easy Workflows](#fs-easy-root) | High-level commands from raw structures to final outputs. |
| [Structure Search](#fs-search-root) | Core search/alignment commands and RBH. |
| [Structure Clustering](#fs-cluster-root) | Cascaded and graph-based structural clustering. |
| [Multimer Modules](#fs-multimer-root) | Complex-level search, scoring, expansion, and clustering. |
| [Structure Manipulation](#fs-manip-root) | Database creation, conversion, coordinate and output utilities. |
| [Database Management](#fs-db-modules) | Downloaded datasets, indexing, and cluster-search DB preparation. |
