# Expert Manual {#sec-expert-manual}

This chapter focuses on advanced pipeline composition, reproducibility controls, and documentation maintenance. Foundational storage and parallel mechanics are summarized in [Performance Foundations](#sec-performance-foundations); this chapter assumes that baseline model.

## Expert Operating Discipline

Custom MMseqs2 pipelines fail most often from implicit assumptions, not syntax errors. Advanced users should lock assumptions explicitly before scaling.

| Discipline | Practical Rule |
| :--- | :--- |
| Contract discipline | Validate DB type and sidecar completeness at each boundary |
| Mode discipline | Keep alignment, rescoring, and filter modes fixed across comparisons |
| Topology discipline | Confirm real call path with dependency map before debugging behavior |
| Scale discipline | Validate on representative subsets before full runs |

## Contract Enforcement in Custom Pipelines

Module chains should be reviewed as explicit contracts:

| Contract Surface | What to Verify |
| :--- | :--- |
| Structural contract | `.dbtype` and index compatibility with downstream module requirements |
| Metadata contract | Header, lookup, taxonomy, and mapping sidecars required by downstream exports |
| Semantic contract | Output fields remain meaningful under selected mode and filter policy |

A common anti-pattern is tuning thresholds while the contract itself is broken. In practice, contract validation should happen before parameter optimization.

```{=typst}
#doc_warning[
If a downstream result looks wrong, verify contract and mode assumptions first. Parameter tuning should be the last step.
]
```

## Reproducibility Controls

Reproducible comparisons need a stable run envelope, not only stable command names.

| Reproducibility Domain | Controls to Pin |
| :--- | :--- |
| Core scoring semantics | `--alignment-mode`, `--alignment-output-mode`, `--rescore-mode` |
| Selection semantics | `-e`, `-c`, `--cov-mode`, `--max-accept`, `--max-rejected` |
| Profile behavior | Pseudocount, weighting, and MSA filtering settings |
| Taxonomy behavior | ORF/frame extraction policy and aggregation/report mode |
| Runtime envelope | Split policy, load mode, thread/MPI strategy, temporary-storage topology |

When benchmarking, record these controls as part of run metadata. Without this context, result deltas are difficult to interpret.

## Performance Triage for Advanced Workloads

For slow or unstable large runs, triage in this order:

| Step | Question |
| :--- | :--- |
| 1 | Is startup dominated by index read-in or shared-storage contention? |
| 2 | Is split policy over-reducing memory at the cost of merge and I/O overhead? |
| 3 | Is the distributed mode aligned with actual storage topology? |
| 4 | Are mode and filter choices inflating downstream data volume unexpectedly? |

This sequence is intentionally infrastructure-first. It reflects how MMseqs2 runtime is typically determined at scale.

```{=typst}
#doc_perf[
In most production pipelines, index/load/split decisions create larger runtime swings than final threshold adjustments.
]
```

## Documentation Maintenance Workflow

Use this workflow when MMseqs2 source, options, or dependencies evolve:

| Step | Purpose | Command |
| :--- | :--- | :--- |
| Refresh help snapshots | Sync CLI defaults with active binary | `./generate_mmseqs_docs.sh /path/to/mmseqs` |
| Rebuild dependency artifacts | Refresh command topology from source and workflow scripts | `mmseqs2_docs/scripts/build_dependency_graph.py` |
| Regenerate command reference | Rebuild per-command pages and reference index | `mmseqs2_docs/scripts/generate_command_reference.py` |
| Regenerate module pages | Rebuild `submodules/*.md` with dependency crosslinks | `mmseqs2_docs/scripts/generate_module_docs.py` |
| Validate structure | Detect missing pages, duplicate command sections, broken links | `mmseqs2_docs/scripts/validate_docs.py` |
| Build deliverable PDF | Produce final manual | `./mmseqs2_docs/build_pdf.sh` |

## Cross References

Use these chapters together:

| Need | Chapter |
| :--- | :--- |
| Storage/index/split/parallel mechanics | [Performance Foundations](#sec-performance-foundations) |
| Architecture and dependency navigation | [System Map](#sec-system-map), [Dependency Map](#sec-dependency-map) |
| Task-oriented command selection | [Functional Modules Manual](#sec-functional-modules-manual), functional module pages |
| Full command-level option detail | [Command Reference Index](#sec-command-reference), command reference entries |
