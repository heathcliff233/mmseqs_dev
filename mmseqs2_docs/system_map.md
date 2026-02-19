# System Map: Cascaded APIs and Module Connections {#sec-system-map}

MMseqs2 commands are layered. Workflow and high-level commands orchestrate lower-level modules, and those modules enforce the actual data contracts. This layering is both an architecture map and a performance map: most runtime and correctness characteristics are inherited from the lower levels each workflow chooses.

Primary generated maps are [Command Reference Index](#sec-command-reference) and [Dependency Map](#sec-dependency-map).

## API Layers

| Layer | Typical Role | Representative Commands |
| :--- | :--- | :--- |
| `workflow` | Easy entry points over FASTA/FASTQ with default orchestration | `easy-search`, `easy-cluster`, `easy-taxonomy` |
| `high_level_api` | End-to-end MMseqs DB workflows for search, clustering, taxonomy, or set workflows | `search`, `cluster`, `taxonomy`, `linsearch`, `multihitsearch` |
| `mid_level_api` | Core compute modules used inside workflows | `prefilter`, `align`, `clust`, `kmermatcher` |
| `low_level_api` | DB operations, conversion, utilities, and composition helpers | `createdb`, `convertalis`, `filterdb`, `createtsv` |

## Cascade Pattern

Most pipelines follow the same execution shape: an orchestration command selects a path, prefiltering narrows candidate pairs, alignment or rescoring computes pair quality, and downstream modules transform or aggregate outputs. Not every command uses every stage, but this pattern explains most runtime and output behavior.

The important operational consequence is that changing a high-level workflow can silently switch lower-level modules and therefore change both output semantics and resource profile. Dependency links should be read as behavior links, not only call graph links.

```{=typst}
#doc_note[
Functional grouping and API layer are orthogonal. A command can be in the taxonomy group and still be low-level API.
]
```

## Crosslink Model Used in Submodule Pages

Each command entry in `submodules/*.md` includes a structured metadata table with:

| Field | Purpose |
| :--- | :--- |
| API layer and category | Places command in the execution stack |
| Called-by and calls | Exposes upstream and downstream dependencies |
| Related functional groups | Shows cross-domain coupling |
| Workflow script usage | Shows script-level evidence from extracted workflows |
| Reference links | Links to full CLI help and dependency-map anchor |

## When to Start from the Dependency View

Start with [Dependency Map](#sec-dependency-map) when tuning runtime at workflow level, debugging unexpected output semantics, or composing custom pipelines from low-level modules. Start with [Functional Modules Manual](#sec-functional-modules-manual) and submodule pages when task intent is clear and you need command selection guidance first.

## Transition to Performance Foundations

This chapter explains where commands sit in the cascade. The next chapter, [Performance Foundations](#sec-performance-foundations), explains why that cascade is fast in practice: internal storage format, index and load mechanics, memory and split tradeoffs, and parallel execution strategies.
