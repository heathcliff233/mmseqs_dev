# Foldseek Developer Manual {#fs-dev-root}

This chapter documents Foldseek source architecture and extension points. It is for contributors modifying Foldseek behavior, not for user-level command tutorials.

## Command Registration and Ownership {#fs-dev-command-registry}

Public command registration is centralized in `foldseek/src/FoldseekBase.cpp`. This file is the first source of truth for:

- command visibility (main/easy/hidden categories),
- usage signatures,
- command descriptions and examples,
- command-to-function entrypoint mapping.

When behavior changes but docs are stale, check `FoldseekBase.cpp` first, then the target implementation.

## Parameter System {#fs-dev-parameters}

Foldseek-specific parameters and workflow parameter bundles are defined in `foldseek/src/commons/LocalParameters.cpp` and declared in `LocalParameters.h`.

This layer controls:

- option defaults and validation regexes,
- semantic groupings (prefilter, align, clust, misc, expert),
- workflow parameter composition (`structuresearchworkflow`, `multimersearchworkflow`, easy workflow bundles),
- output-column dependency flags used by converters.

If an option appears in help but not in expected workflow behavior, inspect the workflow’s parameter bundle composition in `LocalParameters.cpp`.

## Workflow Layer {#fs-dev-workflow-layer}

Workflow commands live in `foldseek/src/workflow/` and primarily orchestrate stage composition rather than numerical kernels.

| File | Responsibility |
| :--- | :--- |
| `StructureSearch.cpp` | Main search workflow composition and mode switching. |
| `StructureCluster.cpp` | Structural clustering workflow orchestration. |
| `StructureRbh.cpp` | Reciprocal-best-hit workflow. |
| `MultimerSearch.cpp` | Complex-level search orchestration. |
| `MultimerCluster.cpp` | Complex clustering orchestration. |
| `Easy*.cpp` | Raw-input wrappers that call `createdb` + workflow stages + conversion. |
| `StructureIndex.cpp` | Index workflow wrapper for Foldseek DBs. |

Most “why did this pipeline run this module” questions are answered in these files and their generated shell templates under `foldseek/data/`.

## Algorithm and Utility Layer {#fs-dev-algo-layer}

Structural kernels and transformations are in `foldseek/src/strucclustutils/`.

| Area | Key files |
| :--- | :--- |
| Structure DB creation | `structcreatedb.cpp`, `structureto3didescriptor.cpp`, `GemmiWrapper.*`, `PulchraWrapper.*` |
| Search alignment kernels | `structurealign.cpp`, `structurerescorediagonal.cpp`, `tmalign.cpp` |
| Conversion/reporting | `structureconvertalis.cpp`, `convert2pdb.cpp`, `createmultimerreport.cpp` |
| Multimer internals | `expandmultimer.cpp`, `scoremultimer.cpp`, `MultimerUtil.h` |
| Utility transforms | `compressca.cpp`, `aln2tmscore.cpp`, `result2structprofile.cpp` |

When changing scoring semantics, always check both runtime modules and conversion modules; output columns may recompute or reinterpret metrics.

## Core Libraries and Shared Engines {#fs-dev-core-libs}

Foldseek reuses MMseqs infrastructure but adds structural engines in dedicated components:

| Component | Files |
| :--- | :--- |
| 3Di encoder | `foldseek/lib/3di/structureto3di.*` |
| TM-align backend | `foldseek/lib/tmalign/*`, `foldseek/src/commons/TMaligner.*` |
| LDDT scoring | `foldseek/src/commons/LDDT.*` |
| Structure-aware SW | `foldseek/src/commons/StructureSmithWaterman.*` |
| Shared command/DB infra | MMseqs-derived `DBReader`, `DBWriter`, `IndexReader`, `Parameters` |

The 3Di encoder is isolated from workflow code, which allows algorithm updates without rewriting orchestration paths.

## End-to-End Data Flow (Developer View) {#fs-dev-data-flow}

1. `createdb` builds synchronized DB channels from structures or ProstT5 inference output.
2. Workflow module (`search`, `cluster`, `multimersearch`, etc.) composes prefilter/alignment stages.
3. Alignment/result DBs are written in internal formats.
4. Conversion/report modules derive user-facing outputs.

Because multiple commands share the same DB channels, schema changes in `createdb` impact almost every downstream module.

## Editing Guidelines {#fs-dev-guidelines}

1. For command behavior changes, update all three layers together:
- `FoldseekBase.cpp` command declaration,
- `LocalParameters.cpp` option bundles/defaults,
- implementation file(s).

2. For score or ranking changes, validate:
- runtime filtering paths (`structurealign`, `structurerescorediagonal`, multimer filters),
- conversion paths (`structureconvertalis`, reports),
- sorting/threshold side effects.

3. For DB/index changes, test both:
- non-indexed and indexed targets,
- coordinate-dependent and coordinate-light modes (`--sort-by-structure-bits`, TM/LDDT outputs).

## Debugging Map {#fs-dev-debugging-map}

| Symptom | First files to inspect |
| :--- | :--- |
| Wrong command usage/help | `foldseek/src/FoldseekBase.cpp`, regenerated `foldseek_help_output/*.txt` |
| Option accepted but ignored | `foldseek/src/commons/LocalParameters.cpp`, workflow bundle composition |
| Unexpected stage order | `foldseek/src/workflow/*.cpp`, generated workflow shell templates |
| Score/ranking mismatch | `structurealign.cpp`, `structurerescorediagonal.cpp`, `StructureSmithWaterman.*`, `TMaligner.*`, `LDDT.*` |
| Multimer assignment anomalies | `scoremultimer.cpp`, `expandmultimer.cpp`, `MultimerUtil.h` |
| Output field inconsistency | `structureconvertalis.cpp`, `createmultimerreport.cpp` |

## Documentation Sync Rule {#fs-dev-doc-sync}

Whenever command interfaces or defaults change, refresh help snapshots with `generate_foldseek_docs.sh` and reconcile the module chapters before generating `foldseek_doc.pdf`.
