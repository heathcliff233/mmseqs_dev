# Functional Modules Manual

This section is the task-oriented navigation hub. Each functional page groups related commands, then links every command to API layer and dependency context so you can move directly to execution details.

Before diving into module pages for large production runs, read `foundations.md`. That chapter explains storage, indexing, split policy, and parallel model assumptions that shape runtime and output behavior across all modules.

## Functional Groups

| Functional Group | Scope | Module Page |
| :--- | :--- | :--- |
| Easy Workflows | Shortcut workflows over FASTA/FASTQ with standard outputs | [Easy Workflows](./submodules/easy_workflows.md) |
| Search Workflows | Homology search and mapping workflows | [Search Workflows](./submodules/search.md) |
| Clustering | Cascaded and linear clustering workflows and cluster transforms | [Clustering](./submodules/clustering.md) |
| Prefiltering | Candidate-generation modules before expensive alignment | [Prefiltering](./submodules/prefiltering.md) |
| Alignment | Alignment and rescoring modules | [Alignment](./submodules/alignment.md) |
| Profiles | Profile and MSA creation, conversion, and profile-search helpers | [Profiles](./submodules/profiles.md) |
| Database Management | DB creation, indexing, merging, splitting, and storage operations | [Database Management](./submodules/database.md) |
| Result Handling | Result filtering, summarization, and export transforms | [Result Handling](./submodules/result_handling.md) |
| Sequence Manipulation | ORF, frame, masking, and sequence-level transforms | [Sequence Manipulation](./submodules/sequence_manipulation.md) |
| Taxonomy | Taxonomy DB preparation, assignment, filtering, and reports | [Taxonomy](./submodules/taxonomy.md) |
| Multi-hit | Set-based search and aggregation workflows | [Multi-hit](./submodules/multi_hit.md) |
| Utilities | General and special-purpose helpers used in custom pipelines | [Utilities](./submodules/utilities.md) |

## Complementary Maps

Functional pages answer what to run. Generated maps answer how commands connect.

| Need | Open |
| :--- | :--- |
| Layered architecture and navigation rules | [System Map](./system_map.md) |
| Storage, indexing, memory-split, and parallel execution model | [Performance Foundations](./foundations.md) |
| Complete command catalog with CLI pages | [Command Reference Index](./reference/index.md) |
| Command dependency topology | [Dependency Map](./reference/dependency_map.md) |
