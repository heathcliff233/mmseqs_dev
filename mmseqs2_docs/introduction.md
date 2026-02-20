# MMseqs2 Documentation Overview {#sec-overview}

MMseqs2 is designed for a difficult constraint set: very large sequence collections, sensitivity targets close to established alignment tools, and runtime envelopes that still fit production workflows. The project solves this by treating performance as a systems property instead of a single-kernel optimization problem. Workflows, core compute modules, storage format, and split policy are all part of one execution model.

This manual follows that same model. It starts from the big picture, then moves to algorithmic and systems acceleration details, then to functional modules and command-level references. The goal is that a reader can move from a task question ("what should I run?") to a design question ("why does this run behave this way?") without switching mental frameworks.

## What This Manual Assumes

The documentation assumes that you will run MMseqs2 as a cascade of stages, not as isolated commands. In practice, prefiltering and indexing choices set the candidate volume and memory behavior, alignment settings control the quality-cost boundary, and result-handling choices decide how downstream interpretation is constrained. If one stage is misconfigured, later stages may still produce outputs, but those outputs may no longer be comparable across runs.

For that reason, this manual repeatedly emphasizes contract stability: database type compatibility, sidecar availability, mode consistency, and reproducible parameter sets. These are not housekeeping details; they are part of algorithmic correctness at scale.

## Reading Strategy

Start with the conceptual chapters before diving into command pages:

1. Read [Performance Foundations](#sec-performance-foundations) for algorithmic acceleration, storage/indexing behavior, split policy, and parallel execution tradeoffs.
2. Read [System Map](#sec-system-map) to understand the layered API model and command cascade.
3. Use [Functional Modules Manual](#sec-functional-modules-manual) for task-oriented command discovery.
4. Use [Command Reference Index](#sec-command-reference) and [Dependency Map](#sec-dependency-map) for exact command topology and CLI details.

If you already know your task and only need command selection, you can jump directly to [Functional Modules Manual](#sec-functional-modules-manual). If you are diagnosing runtime or output drift, read the conceptual chapters first; they explain the cross-stage couplings that usually cause expensive surprises.

## Why the Cascade Matters

A typical MMseqs2 workflow performs database preparation, candidate generation, alignment or rescoring on surviving pairs, and downstream transformation such as clustering, taxonomy assignment, or export. This order is the primary scaling mechanism. Expensive operations are delayed until fast filters shrink the search space.

The practical consequence is that late-stage tuning often has less impact than early-stage tuning. Raising sensitivity or adding richer alignment outputs can be useful, but only after index strategy, load behavior, and split policy are stable. In large production runs, infrastructure misalignment can dominate wall time long before algorithmic thresholds are the true bottleneck.

## Source-of-Truth Policy

Narrative chapters explain design and usage strategy. Command snapshots in `mmseqs_help_output` define concrete CLI behavior for this repository state. Source code under `MMseqs2/src/` and workflow scripts under `MMseqs2/data/workflow/` remain the final authority when you need implementation-level confirmation.

Use [Expert Manual](#sec-expert-manual) and [MMseqs2 Source Development Guide](#sec-expert-dev-guide) when you need strict reproducibility discipline or source-level debugging and extension guidance.

```{=typst}
#doc_note[
When narrative guidance and local command snapshots diverge, treat local snapshots and source code as canonical for exact behavior.
]
```
