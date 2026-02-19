# MMseqs2 Documentation Overview

MMseqs2 is a cascaded system for large-scale sequence analysis. User-facing workflows are orchestration layers that route data through lower-level modules with strict database contracts, resource tradeoffs, and mode-specific semantics. This manual follows the same architecture so readers can move from intent to execution detail without switching mental models.

At a high level, MMseqs2 gains speed by combining three design choices: compact internal databases, staged candidate reduction before expensive alignment, and parallel execution across cores and servers. Accuracy, runtime, and resource usage are therefore not independent concerns. They are coupled through the pipeline path, indexing strategy, and split policy selected for a run.

## Reading Path

| Stage | Goal | Entry Point |
| :--- | :--- | :--- |
| Overall idea | Understand how MMseqs2 turns large search spaces into tractable stages | `introduction.md` |
| Sharp bits | Avoid expensive correctness and performance mistakes | `sharp_bits.md` |
| System view | See API layers and dependency topology | `system_map.md` |
| Performance foundations | Understand storage, indexing, memory-split tradeoffs, and parallel execution model | `foundations.md` |
| Functional modules | Navigate by task domain and submodule relationships | `manual.md`, `submodules/*.md` |
| Expert behavior | Compose robust custom pipelines and maintain doc quality | `expert_manual.md` |

## Cascade Model

A typical MMseqs2 pipeline starts with database preparation, narrows candidates through prefiltering, computes alignment or rescoring on the reduced candidate set, and then applies downstream transforms such as clustering, taxonomy assignment, or export. This staged execution is the core scaling mechanism: expensive operations are deferred until cheap filters reduce the search space.

For practical work, this means that most large performance wins come from upstream decisions, not late-stage tweaking. Index reuse, split strategy, and load behavior can dominate total wall time before sensitivity or filtering changes even become visible.

## Navigation Axes

The documentation exposes two orthogonal views of the same commands. The functional view answers what to run for a task; the API-layer view answers where that command sits in the cascade and what it depends on.

| View | Question It Answers | Main Files |
| :--- | :--- | :--- |
| Functional modules | Which commands solve this workflow goal? | `manual.md`, `submodules/*.md` |
| Dependency and API layer | Which modules call this command, and which modules it calls | `system_map.md`, `reference/dependency_map.md`, `reference/index.md` |

```{=typst}
#doc_note[
When narrative text and command defaults disagree, treat local help snapshots in `mmseqs_help_output` as canonical for CLI behavior. Treat `foundations.md` as the canonical summary of storage and parallel mechanics in this manual.
]
```

## How to Use This Manual Efficiently

If you are selecting commands for a known task, start with `manual.md` and then open the linked submodule page. If you are diagnosing runtime, memory, or output interpretation problems, read `system_map.md` and `foundations.md` first, then inspect dependency links in `reference/dependency_map.md`. If you are composing custom pipelines, finish with `expert_manual.md` for contract and reproducibility discipline.

## Source of Truth

| Topic | Canonical Source |
| :--- | :--- |
| Visible command set and one-line intent | `MMseqs2/src/MMseqsBase.cpp` |
| Workflow orchestration logic | `MMseqs2/src/workflow/*.cpp`, `MMseqs2/data/workflow/*.sh` |
| Exact options and defaults | `mmseqs_help_output/*.txt` |
| Crosslinked command/module references | `mmseqs2_docs/reference/`, `mmseqs2_docs/submodules/` |
| Legacy long-form historical material | `mmseqs2_docs/wiki.md` |
