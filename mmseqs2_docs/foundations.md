# Performance Foundations: Why MMseqs2 Is Fast

This chapter summarizes the low-level mechanics that make MMseqs2 fast at scale. It is the canonical overview for storage format, indexing behavior, memory-split tradeoffs, and parallel execution strategy in this manual.

## 1. Internal Database and Storage Model

Most MMseqs2 modules consume and produce MMseqs2 database files rather than plain FASTA. The design avoids creating millions of small files and instead stores records in contiguous files with explicit indexing.

| Component | Role | Performance Implication |
| :--- | :--- | :--- |
| `<db>` data file | Concatenated records separated by `\0` | Sequential storage keeps filesystem overhead low |
| `<db>.index` | ID, byte offset, and record size per entry | Enables direct random access by key |
| `<db>.dbtype` | Binary type marker (protein, nucleotide, profile, generic, etc.) | Enforces module input contracts early |
| `<db>_h` and `<db>_h.index` | Header sidecar database | Separates sequence-heavy and header-heavy access paths |
| `<db>.lookup` and taxonomy sidecars | External ID and annotation mapping | Required for complete downstream annotation workflows |

Because offsets in `.index` point into immutable byte positions, in-place editing is avoided. MMseqs2 generally writes new databases for transformations. This design preserves indexing correctness and enables predictable high-throughput I/O.

```{=typst}
#doc_note[
Header and sequence separation is a deliberate performance choice. Sequence-heavy stages can avoid header I/O, while export and annotation stages can load both paths explicitly.
]
```

## 2. Indexing and Data-Access Strategy

Precomputed indexes improve repeated searches against stable targets by shifting cost from repeated startup to reusable artifacts. The gain is strongest when targets are reused many times or iterative workflows are run.

The placement of index data matters. If index files are accessed through slower shared storage, read-in can become a bottleneck. In those cases, a strategy that keeps index data resident in memory, or in local fast storage, can outperform repeated shared-storage reads.

MMseqs2 load behavior also matters:

| Access Pattern | Typical Effect |
| :--- | :--- |
| Precomputed index with efficient local access | Fast startup across repeated runs |
| Shared-storage index read bottleneck | Startup overhead dominates short queries |
| Memory-resident index path | Reduces repeated transfer overhead |
| Alternative load modes (`--db-load-mode`) | Trade off startup copy behavior and runtime access pattern |

For small query sets, memory-mapped access can minimize startup latency if target index data is already resident. For large query sets, alternative copy behavior can improve throughput by reducing translation-lookaside-buffer pressure in prefilter-heavy phases.

## 3. Memory Model and Split Tradeoffs

Prefiltering is usually the largest memory consumer. Legacy MMseqs2 guidance models prefilter index memory approximately as:

`M = (7 * N * L + 8 * a^k) bytes`

where `N` is sequence count, `L` is average sequence length, `a` is alphabet size, and `k` is k-mer length. The key operational takeaway is linear growth with database size plus an exponential alphabet-and-k-mer term for pointer structures.

When memory is insufficient, MMseqs2 splits databases and processes chunks. Splitting lowers peak memory but introduces additional merge and I/O overhead.

| Split Choice | Benefit | Cost |
| :--- | :--- | :--- |
| Fewer/larger chunks | Better runtime efficiency | Higher peak memory requirement |
| More/smaller chunks | Lower peak memory footprint | More merge and temporary I/O overhead |
| `--split-memory-limit` cap | Predictable memory envelope | Usually slower wall time than unsplit runs |

The slowdown from splitting is often less visible at high sensitivity, where core compute dominates, and more visible at low sensitivity, where merge and I/O overhead are a larger share of total runtime.

## 4. Parallel Execution Model

MMseqs2 parallelism is layered:

| Layer | Mechanism | Main Idea |
| :--- | :--- | :--- |
| Intra-node | Multi-core execution (OpenMP-based stages) | Parallelize computational kernels within each process |
| Inter-node | MPI runner model | Distribute chunks across servers, then execute local multi-core work |
| Scheduler-based | Batch-system splitting | Partition query DB and submit independent jobs when MPI is not used |

In MPI mode, workloads can be distributed by splitting targets or queries. Target splitting usually reduces per-node memory pressure but can be less time-efficient because merging is I/O-heavy. Query splitting can be easier to distribute in batch environments but may duplicate some target-side work.

Temporary storage placement is also part of parallel performance. Shared temporary storage simplifies coordination but can create contention at high split counts. Local temporary storage can reduce shared-disk bottlenecks in large distributed runs.

```{=typst}
#doc_warning[
Distributed performance is constrained by I/O topology as much as by CPU count. Evaluate shared-disk behavior before attributing slowdowns to compute.
]
```

## 5. Practical Tuning Order

A stable tuning sequence avoids expensive trial-and-error:

| Step | Question |
| :--- | :--- |
| 1. Contract check | Are DB types and sidecars compatible across the pipeline? |
| 2. Index strategy | Are stable targets indexed and loaded in a way that matches storage topology? |
| 3. Split and temp policy | Is memory capped appropriately without overpaying in merge and I/O overhead? |
| 4. Parallel model | Is the run mode aligned with hardware and storage architecture? |
| 5. Sensitivity and filters | Only after infrastructure choices are stable, are scoring thresholds tuned |

This ordering reflects how MMseqs2 runtime is usually determined in practice: infrastructure first, algorithmic strictness second.

## 6. Cross References

Use `manual.md` and `submodules/*.md` for task-oriented command selection, `reference/dependency_map.md` for call-topology debugging, and `expert_manual.md` for advanced composition and reproducibility discipline. Use `wiki.md` for historical long-form detail and extended examples beyond this condensed chapter.
