# System Map: Cascaded APIs and Module Connections {#sec-system-map}

MMseqs2 commands are intentionally layered. Easy workflows and high-level entrypoints decide orchestration, while lower-level modules enforce data contracts and execute the expensive kernels. Understanding this layering is essential for both correctness and performance debugging: the command you invoke is often only the visible front of a deeper module chain.

The generated topology views, [Command Reference Index](#sec-command-reference) and [Dependency Map](#sec-dependency-map), provide the complete command-level map. This chapter explains how to interpret that map.

## Layered API Model

At the top, workflow commands prioritize usability and sensible defaults. They hide many internal steps but still inherit all low-level behavior from their called modules. High-level API commands expose full DB-to-DB task execution and are typically the right interface for reproducible production pipelines.

Mid-level API commands are where core algorithmic work happens: prefiltering, alignment, clustering kernels, and related computational modules. Low-level API commands perform DB creation, conversion, indexing, filtering, and utility operations. These lower layers are frequently used in custom pipelines and debugging workflows where explicit control matters more than convenience.

## Cascade Pattern in Practice

Most workflows follow a common shape: first reduce the candidate space, then score surviving pairs with progressively more expensive methods, then transform outputs into task-specific artifacts. Search and clustering differ in final objectives, but they share this backbone.

That shared backbone creates an important operational rule: changing a high-level command can silently switch lower-level modules and therefore change output semantics, runtime profile, or both. Dependency edges should therefore be read as behavior links, not merely as call graph arrows.

```{=typst}
#doc_note[
Functional group and API layer are orthogonal. A command can belong to one functional group but live in a different API layer than neighboring commands in that group.
]
```

## How Submodule Pages Encode This Map

Each entry in `submodules/*.md` now combines prose and compact metadata. The prose explains what a command does, how it participates in the cascade, and when to use it. The compact metadata table records API layer, category flags, and coupling counts so readers can quickly assess execution context.

To avoid duplication, full upstream/downstream edge lists and script evidence are centralized in [Dependency Map](#sec-dependency-map).

## Choosing Your Entry View

Start from [Functional Modules Manual](#sec-functional-modules-manual) when your task intent is clear and you need command candidates quickly. Start from [Dependency Map](#sec-dependency-map) when behavior is surprising, performance is unstable, or you are composing a custom low-level pipeline and need exact topology evidence.

Use [Performance Foundations](#sec-performance-foundations) with this chapter to connect architecture placement with storage, index, split, and parallel execution consequences.
