# Sharp Bits {#sec-sharp-bits}

Most expensive MMseqs2 failures are not algorithmic bugs. They come from contract mismatches, mode drift across runs, and late detection of pipeline issues. The goal of this section is to front-load the mistakes that cost the most time in large-scale runs.

The recurring pattern is simple: workflows appear similar, but runtime and output behavior are shaped by earlier infrastructure choices such as indexing, load mode, split policy, and sidecar completeness. A small mismatch upstream can invalidate interpretation downstream.

| Risk Surface | Why It Matters | Guardrail |
| :--- | :--- | :--- |
| Rebuilding indexes every run | Repeated setup work dominates runtime on stable targets | Reuse `createindex` or `createlinindex` artifacts |
| Raising sensitivity too early | Runtime and intermediate volume increase quickly | Tune indexing and split policy before raising `-s` |
| Split-memory-temp mismatch | Reduced RAM can increase I/O and wall time | Tune `--split*` with both memory and temporary disk budgets |
| Mixed alignment/rescore modes | Output fields become semantically incomparable | Lock mode flags when comparing experiments |
| DB sidecar mismatches | Downstream modules silently lose required metadata | Validate `_h`, taxonomy, and lookup sidecars before chaining |
| Taxonomy and ORF preprocessing drift | Classification quality changes with preprocessing choices | Fix frame, ORF, and aggregation policy per dataset type |
| Duplicate conversion steps | Unnecessary transforms add cost and interpretation noise | Keep a minimal transform chain with explicit rationale |

## Diagnostics Sequence

When something looks wrong, inspect in this order: database contracts, mode consistency, resource policy, then threshold tuning. This order prevents expensive false debugging loops where parameter changes mask an infrastructure mismatch.

```{=typst}
#doc_perf[
Treat performance tuning as a sequence: index reuse first, split-memory policy second, sensitivity increase last.
]
```

```{=typst}
#doc_warning[
Treat exported tables as pipeline artifacts, not standalone truth. Interpretation depends on upstream search mode, alignment mode, and filters.
]
```

```{=typst}
#doc_tip[
Validate pipelines on a small representative subset before scaling to full datasets. Early contract checks prevent full reruns.
]
```
