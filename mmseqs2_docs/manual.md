# Functional Modules Manual {#sec-functional-modules-manual}

This section is the task-oriented navigation hub. Each functional page groups related commands, then links every command to API layer and dependency context so you can move directly to execution details.

Before diving into module pages for large production runs, read [Performance Foundations](#sec-performance-foundations). That chapter explains storage, indexing, split policy, and parallel model assumptions that shape runtime and output behavior across all modules.

## Functional Groups

| Functional Group | Scope | Module Page |
| :--- | :--- | :--- |
| Easy Workflows | Shortcut workflows over FASTA/FASTQ with standard outputs | [Easy Workflows](#mod-easy-workflows) |
| Search Workflows | Homology search and mapping workflows | [Search Workflows](#mod-search-workflows) |
| Clustering | Cascaded and linear clustering workflows and cluster transforms | [Clustering](#mod-clustering) |
| Prefiltering | Candidate-generation modules before expensive alignment | [Prefiltering](#mod-prefiltering) |
| Alignment | Alignment and rescoring modules | [Alignment](#mod-alignment) |
| Profiles | Profile and MSA creation, conversion, and profile-search helpers | [Profiles](#mod-profiles) |
| Database Management | DB creation, indexing, merging, splitting, and storage operations | [Database Management](#mod-database) |
| Result Handling | Result filtering, summarization, and export transforms | [Result Handling](#mod-result-handling) |
| Sequence Manipulation | ORF, frame, masking, and sequence-level transforms | [Sequence Manipulation](#mod-sequence-manipulation) |
| Taxonomy | Taxonomy DB preparation, assignment, filtering, and reports | [Taxonomy](#mod-taxonomy) |
| Multi-hit | Set-based search and aggregation workflows | [Multi-hit](#mod-multi-hit) |
| Utilities | General and special-purpose helpers used in custom pipelines | [Utilities](#mod-utilities) |

## Complementary Maps

Functional pages answer what to run. Generated maps answer how commands connect.

| Need | Open |
| :--- | :--- |
| Layered architecture and navigation rules | [System Map](#sec-system-map) |
| Storage, indexing, memory-split, and parallel execution model | [Performance Foundations](#sec-performance-foundations) |
| Complete command catalog with CLI pages | [Command Reference Index](#sec-command-reference) |
| Command dependency topology | [Dependency Map](#sec-dependency-map) |
