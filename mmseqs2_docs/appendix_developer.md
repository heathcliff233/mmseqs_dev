# Appendix B: MMseqs2 Developer Guide {#sec-appendix-developer}

This appendix is for MMseqs2 code development. For behavior and implementation questions, treat `MMseqs2/` source files as canonical. Documentation markdown is a derived view for users.

## Command-Level Trace Map

| Development Goal | Start Here | Then Inspect |
| :--- | :--- | :--- |
| Add/remove or reclassify a visible command | `MMseqs2/src/MMseqsBase.cpp` | `MMseqs2/src/CommandDeclarations.h`, command implementation in `MMseqs2/src/*/*.cpp` |
| Change workflow orchestration | `MMseqs2/src/workflow/*.cpp` | `MMseqs2/data/workflow/*.sh`, downstream called modules |
| Change prefilter/alignment/clustering behavior | `MMseqs2/src/prefiltering/`, `MMseqs2/src/alignment/`, `MMseqs2/src/clustering/`, `MMseqs2/src/linclust/` | `MMseqs2/src/workflow/*.cpp` call sites |
| Change taxonomy or multi-hit behavior | `MMseqs2/src/taxonomy/`, `MMseqs2/src/multihit/` | workflow integration in `MMseqs2/src/workflow/Taxonomy.cpp` and related scripts |
| Change DB contract or storage behavior | `MMseqs2/src/commons/DBReader.h`, `MMseqs2/src/commons/DBWriter.h`, `MMseqs2/src/commons/Parameters.{h,cpp}` | data conversion utilities under `MMseqs2/src/util/` |
| Change export/result formatting | `MMseqs2/src/util/convertalignments.cpp`, `MMseqs2/src/util/createtsv.cpp`, `MMseqs2/src/util/result2*.cpp` | consuming workflows and command docs |

## Source Tree Responsibilities

| Path | Primary Responsibility |
| :--- | :--- |
| `MMseqs2/src/workflow/` | High-level orchestration (`search`, `cluster`, `taxonomy`, `easy-*`) |
| `MMseqs2/src/prefiltering/` | Candidate generation and prefilter index/matching |
| `MMseqs2/src/alignment/` | Core alignment, rescoring, and matching engines |
| `MMseqs2/src/clustering/` | Cluster graph and clustering algorithms |
| `MMseqs2/src/linclust/` | Linear-time k-mer matching/indexing components |
| `MMseqs2/src/taxonomy/` | Taxonomy DB creation, assignment, and reporting |
| `MMseqs2/src/multihit/` | Set-based search and aggregation logic |
| `MMseqs2/src/util/` | Database transforms, exports, wrappers, and utility commands |
| `MMseqs2/src/commons/` | Shared infra: parameters, DB I/O, memory, utility abstractions |

## Source-First Debug Workflow

| Step | Purpose | Example Command |
| :--- | :--- | :--- |
| Locate command registration | Confirm visibility/category/description | `rg -n "\"<command>\"" MMseqs2/src/MMseqsBase.cpp` |
| Trace orchestration path | See which module chain is executed | `rg -n "createParameterString\\(par\\." MMseqs2/src/workflow/*.cpp` |
| Inspect compute kernel entry | Verify algorithm-level behavior | `rg -n "<function_or_class>" MMseqs2/src/{prefiltering,alignment,clustering,linclust,taxonomy,multihit}/*.cpp` |
| Validate DB I/O boundaries | Check type/sidecar assumptions | `rg -n "DBReader|DBWriter|DBTYPE" MMseqs2/src/{workflow,util,commons}/*.{h,cpp}` |
| Check workflow script plumbing | Confirm shell-level variable wiring | `rg -n "MMSEQS|RUNNER|\\$\\{.*_PAR\\}" MMseqs2/data/workflow/*.sh` |

Documentation updates should follow source validation, not drive it.
