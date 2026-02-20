# MMseqs2 Developer Manual: Submodule Classification

This document summarizes MMseqs2 command layers for contributors who need a quick mental model before tracing source code paths. It complements [System Map](#sec-system-map) and [MMseqs2 Source Development Guide](#sec-expert-dev-guide).

## Layer Model

MMseqs2 commands can be grouped into four abstraction levels. Workflow commands are user-facing shortcuts (`easy-*`) that compose deeper modules. High-level API commands expose complete DB workflows such as search, clustering, taxonomy, and multi-hit processing. Mid-level API commands implement core computational stages such as prefiltering, alignment, and clustering kernels. Low-level API commands provide DB lifecycle operations, sequence/result transforms, and utility operations used to compose custom pipelines.

These layers are conceptual boundaries, not strict package boundaries. A high-level command may directly reference low-level utilities in addition to mid-level kernels. Always verify the actual call path with dependency and workflow sources.

## Dependency Direction

The common flow is workflow -> high-level orchestration -> mid-level compute -> low-level DB/utilities. In practice, the most important transitions are:

- search-like workflows: prefiltering to alignment to export/filter stages;
- clustering workflows: fast redundancy reduction to alignment-filtered graph construction to cluster assignment;
- taxonomy workflows: search evidence to LCA/aggregation/report stages;
- update and conversion workflows: DB contract transforms that preserve compatibility for downstream modules.

Because these transitions are chained, parameter changes in earlier layers can alter both runtime and semantics in later layers. Use source and dependency maps together when debugging unexpected behavior.

## Source Anchors

For fast tracing, start in `MMseqs2/src/MMseqsBase.cpp` for command registration, then `MMseqs2/src/workflow/*.cpp` plus `MMseqs2/data/workflow/*.sh` for orchestration, then kernel directories (`prefiltering`, `alignment`, `clustering`, `linclust`, `taxonomy`, `multihit`) for algorithm behavior, and finally `commons`/`util` for shared DB and output infrastructure.
