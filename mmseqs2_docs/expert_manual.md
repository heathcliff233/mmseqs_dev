# Expert Manual {#sec-expert-manual}

This chapter covers advanced MMseqs2 operation for users who build custom pipelines, run large production workloads, or debug behavior across layered workflows. It assumes familiarity with [System Map](#sec-system-map) and [Performance Foundations](#sec-performance-foundations).

## Expert Operating Discipline

At expert scale, the common failure mode is not command syntax. It is uncontrolled assumptions. Pipelines drift when DB contracts change silently, when modes are mixed across experiments, or when topology changes are not tracked.

A disciplined workflow starts by fixing contracts and mode envelopes before threshold tuning. DB type compatibility, sidecar completeness, and mode stability should be treated as required preconditions for meaningful performance or quality comparison.

## Contract Enforcement in Custom Pipelines

Every module boundary should be treated as an explicit contract surface. Structural contracts define whether downstream modules can parse and trust the input DB type and index structures. Metadata contracts define whether required sidecars (headers, lookup maps, taxonomy files, mapping tables) are present. Semantic contracts define whether output fields still mean the same thing after mode and filter choices.

A frequent anti-pattern is adjusting scoring thresholds while one of these contracts is already broken. That often yields plausible-looking output with unstable interpretation.

```{=typst}
#doc_warning[
When a downstream result looks wrong, verify structural, metadata, and semantic contracts first. Threshold tuning should be the last step.
]
```

## Reproducibility Controls

Reproducibility requires pinning an execution envelope, not only command names. You should lock alignment and rescoring modes, filter gates, profile-construction controls, taxonomy extraction/aggregation policy, and runtime envelope settings such as split mode, load mode, and parallel topology.

In practice, most hard-to-explain result deltas come from one unpinned control in that envelope. Record these controls with every benchmark or production run so regression triage is possible.

## Performance Triage for Advanced Workloads

When large jobs become slow or unstable, triage in infrastructure-first order: startup/index behavior, split and merge overhead, distributed I/O topology, then mode/filter output inflation. This ordering matches how MMseqs2 workloads typically fail at scale.

```{=typst}
#doc_perf[
In production, index/load/split decisions usually produce larger runtime swings than late-stage threshold changes.
]
```

## MMseqs2 Source Development Guide {#sec-expert-dev-guide}

This section is for MMseqs2 source development. The authoritative behavior definition lives in `MMseqs2/` source files; documentation markdown is a derived layer for users.

### Source-First Trace Strategy

When you change a command, start from command registration in `MMseqs2/src/MMseqsBase.cpp` and confirm declarations in `MMseqs2/src/CommandDeclarations.h`. This tells you visibility, category flags, and baseline intent.

When you change workflow behavior, inspect `MMseqs2/src/workflow/*.cpp` and the corresponding script glue in `MMseqs2/data/workflow/*.sh`. Most user-visible behavior differences come from this orchestration boundary rather than isolated kernel changes.

When you change algorithmic behavior, move to the corresponding kernel directories: `prefiltering`, `alignment`, `clustering`, `linclust`, `taxonomy`, and `multihit`. Then verify where those kernels are invoked from workflow entrypoints so you can reason about downstream impact.

### Source Tree Responsibilities

`MMseqs2/src/workflow/` is the orchestration layer for end-to-end workflows. `MMseqs2/src/prefiltering/`, `MMseqs2/src/alignment/`, `MMseqs2/src/clustering/`, and `MMseqs2/src/linclust/` host core compute modules. `MMseqs2/src/taxonomy/` and `MMseqs2/src/multihit/` cover specialized assignment and set-aggregation logic.

`MMseqs2/src/util/` and `MMseqs2/src/commons/` provide DB transforms, exports, shared parameter logic, and low-level I/O abstractions. If behavior shifts unexpectedly across many commands, inspect `commons` first; it is often the shared root cause.

### Practical Debug Workflow

Use a repeatable debug loop:

1. Locate command registration and category metadata.
2. Trace workflow composition and parameter propagation.
3. Inspect the target kernel implementation.
4. Validate DB type and sidecar boundary assumptions.
5. Re-check output semantics in result/export transforms.

Representative commands for this loop:

- `rg -n '"<command>"' MMseqs2/src/MMseqsBase.cpp`
- `rg -n 'createParameterString\(par\.' MMseqs2/src/workflow/*.cpp`
- `rg -n '<symbol>' MMseqs2/src/{prefiltering,alignment,clustering,linclust,taxonomy,multihit}/*.cpp`
- `rg -n 'DBReader|DBWriter|DBTYPE' MMseqs2/src/{workflow,util,commons}/*.{h,cpp}`
- `rg -n 'MMSEQS|RUNNER|\$\{.*_PAR\}' MMseqs2/data/workflow/*.sh`

After source validation, regenerate documentation artifacts so command pages and module pages remain synchronized with implementation.

Use [Performance Foundations](#sec-performance-foundations) for storage/index/split/parallel mechanics, [System Map](#sec-system-map) and [Dependency Map](#sec-dependency-map) for architecture and topology debugging, [Functional Modules Manual](#sec-functional-modules-manual) for task-first command selection, and this section ([MMseqs2 Source Development Guide](#sec-expert-dev-guide)) for source-first tracing paths.
