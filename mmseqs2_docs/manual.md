# Functional Modules Manual {#sec-functional-modules-manual}

This section is the task-oriented entry point to MMseqs2 modules. Each functional page groups commands by workflow intent, then links each command into API-layer and dependency context so you can trace from practical usage to implementation topology.

For production-scale work, read [Performance Foundations](#sec-performance-foundations) before tuning command-level options. That chapter explains the algorithmic and infrastructure assumptions that dominate runtime and output behavior.

## Functional Groups

[Easy Workflows](#mod-easy-workflows) covers shortcut workflows over FASTA/FASTQ inputs for common tasks with minimal setup. [Search Workflows](#mod-search-workflows) covers homology search and mapping entrypoints. [Clustering](#mod-clustering) covers cascaded and linear clustering paths plus update operations.

[Prefiltering](#mod-prefiltering) and [Alignment](#mod-alignment) cover core compute kernels used inside search and clustering workflows. [Profiles](#mod-profiles) covers profile/MSA creation and conversion paths. [Database Management](#mod-database) covers creation, indexing, splitting, and storage operations required to keep DB contracts valid.

[Result Handling](#mod-result-handling), [Sequence Manipulation](#mod-sequence-manipulation), [Taxonomy](#mod-taxonomy), [Multi-hit](#mod-multi-hit), and [Utilities](#mod-utilities) cover downstream transforms, specialized analytics, and composition helpers for advanced pipelines. Functional pages answer what to run; generated maps answer how commands connect and where behavior is inherited from upstream orchestration. Use [System Map](#sec-system-map) for layered architecture framing, [Command Reference Index](#sec-command-reference) for per-command CLI pages, and [Dependency Map](#sec-dependency-map) for complete upstream/downstream topology.
