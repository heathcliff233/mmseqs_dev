# Performance Foundations: Algorithmic and Systems Acceleration in MMseqs2 {#sec-performance-foundations}

MMseqs2 performance is a coupled system. Algorithmic pruning, kernel implementation, storage layout, indexing strategy, split policy, and execution topology all interact. This chapter unifies those layers so tuning decisions are made in the right order and interpreted with the correct assumptions.

## Performance Model

MMseqs2 does not rely on one fast algorithm. It applies a cascade that removes expensive comparisons early, computes detailed alignment only for survivors, and keeps data movement predictable through explicit database contracts.

In practical terms, runtime and output behavior are jointly determined by three levers:

| Lever | What It Changes | Typical Mechanisms |
| :--- | :--- | :--- |
| Candidate reduction | Number of sequence pairs that reach expensive stages | prefiltering, k-mer matching, diagonal filtering, clustering prefilters |
| Per-pair cost | Compute cost of each surviving pair | ungapped rescoring, SIMD alignment modes, backtrace settings |
| Data-movement cost | Startup and merge overhead around kernels | index reuse, preload mode, split policy, temporary I/O topology |

The highest gains usually come from ordering these levers correctly: stabilize contracts and data movement first, then tune candidate volume, then tune expensive alignment settings.

## Shared Comparison Backbone {#sec-sharp-backbone}

Search and clustering workflows share a common execution shape. Workflows select paths, prefiltering reduces candidate pairs, alignment or rescoring computes pair quality, and downstream modules convert those results into task artifacts.

For CPU search paths, the orchestration is explicit in `MMseqs2/data/workflow/blastp.sh`: prefilter then align, with optional iterative merge logic. Clustering orchestration (`MMseqs2/src/workflow/Cluster.cpp` and `MMseqs2/data/workflow/*.sh`) reuses the same primitives and then adds graph construction and cluster assignment.

Because this backbone is shared, upstream prefilter/index decisions usually have larger global impact than late-stage alignment-format tweaks.

## Candidate Generation: K-mer Indexing and Expansion {#sec-sharp-kmer}

The prefilter core (`MMseqs2/src/prefiltering/Prefiltering.cpp`, `QueryMatcher.cpp`, `IndexBuilder.cpp`) controls candidate growth through index-driven k-mer retrieval and thresholded similar-k-mer expansion.

For amino-acid searches, similar k-mers are generated from precomputed score matrices (`ExtendedSubstitutionMatrix`, `KmerGenerator`) rather than brute-force enumeration. In the main query loop (`QueryMatcher::match`), MMseqs2 either looks up one exact k-mer index entry or expands into many score-qualified similar k-mers. This branch alone can change candidate fan-out by orders of magnitude and is often the largest runtime lever before alignment.

Composition-bias correction in `QueryMatcher::matchQuery` shifts effective k-mer thresholds per position before k-mer list generation. This means sensitivity and bias controls are coupled in practice: `-s`, `--k-score`, bias correction settings, and k-mer mode selections jointly determine lookup volume and therefore prefilter cost.

## Reduced Alphabets and Information-Preserving Coupling {#sec-sharp-reduced-alphabet}

Reduced alphabets are a first-class acceleration path in MMseqs2. When amino-acid `--alph-size` is set below 21, prefiltering and linear-k-mer modules build a `ReducedMatrix` instead of the full substitution matrix (`Prefiltering::getSubstitutionMatrix`, `kmermatcher`, `kmerindexdb`, `kmersearch`, `alignbykmer`, `clusthash`).

The reduction is not a fixed hardcoded mapping. `ReducedMatrix` iteratively couples amino-acid states by maximizing retained mutual information in the substitution model, then rewrites residue-to-index mappings and the derived score matrix for the reduced state space. Operationally, this shrinks the k-mer combinatorial space (`a^k` term) used in index structures and similar-k-mer generation, which directly reduces memory and candidate-generation cost.

Workflow defaults use this intentionally. General search defaults keep full amino-acid alphabet size (`aa:21`), but linear clustering/search-oriented paths use smaller defaults (`aa:13` in linclust family), and `clusthash` forces an even smaller amino-acid alphabet (`aa:3`) for fast redundancy pruning.

## Exact, Similar, and Spaced K-mer Modes {#sec-sharp-kmer-modes}

MMseqs2 exposes both exact and non-exact k-mer matching. In prefilter/search CLI, `--exact-kmer-matching` forces exact lookup, while the default path expands similar k-mers under `--k-score` thresholding. In the current prefilter implementation, the same exact-only branch (`takeOnlyBestKmer`) is also activated for nucleotide-vs-nucleotide search, amino-acid query against profile target, and `--target-search-mode 1`.

Spaced k-mers are an additional speed/sensitivity control (`--spaced-kmer-mode`, `--spaced-kmer-pattern`). In linear modules, MMseqs2 also adapts k-mer behavior through automatic k-mer length/alphabet heuristics and nucleotide-specific adaptive k-mer length logic (`--adjust-kmer-len`) so the candidate generator stays tractable across identity regimes and sequence lengths.

When an index DB is reused, compatibility metadata checks (k-mer size, alphabet size, spaced-kmer mode/pattern, split assumptions) become part of performance correctness. A mismatch is not only a reproducibility risk; it also changes candidate-generation complexity and therefore runtime behavior.

## Diagonal and Ungapped Filters {#sec-sharp-ungapped}

After raw seed hits are collected, MMseqs2 aggregates by target and diagonal and keeps strongest evidence per target (`QueryMatcher`). This compresses large hit lists into a tractable candidate set.

With diagonal scoring enabled, `UngappedAlignment` computes local ungapped scores on diagonals using SIMD paths (AVX2/SSE fallback in `MMseqs2/src/prefiltering/UngappedAlignment.cpp`). This stage is much cheaper than full Smith-Waterman and often removes weak candidates early enough to dominate total runtime savings.

```{=typst}
#doc_perf[
If runtime is high, reduce candidate volume and tune ungapped gates before tuning full alignment output richness.
]
```

## SIMD Gapped Alignment and Output-Cost Economics {#sec-sharp-gapped}

Full alignment (`MMseqs2/src/alignment/Alignment.cpp`) dispatches through `Matcher` to vectorized Striped Smith-Waterman (`StripedSmithWaterman.cpp`) for amino-acid/profile paths and banded nucleotide alignment for nucleotide paths.

The dynamic programming score is only part of cost. Coverage/identity calculations, alternative alignment handling, and backtrace generation can substantially increase per-pair cost and output size. Alignment mode is therefore both a semantic choice and a throughput choice.

Use richer alignment outputs only when downstream interpretation explicitly needs them.

## Clustering-Specific Accelerators {#sec-sharp-clustering}

Clustering workflows add graph-level acceleration on top of search-like filtering. Cascaded clustering intentionally starts with cheaper passes and increases sensitivity later (`MMseqs2/src/workflow/Cluster.cpp`). Early passes shrink graph density before expensive stages.

This staged design also changes k-mer representation on purpose. Cascaded clustering temporarily switches to linclust-oriented defaults (including reduced amino-acid alphabet) for early low-cost filtering, then restores broader settings for later steps. In single-step clustering, a dedicated `clusthash` redundancy pass uses an even smaller alphabet to remove near-duplicates cheaply before full prefilter/alignment work.

Single-step clustering scripts use redundancy shortcuts such as `clusthash` before full prefilter+alignment. Linclust (`MMseqs2/src/workflow/Linclust.cpp`) applies bounded-k-mer selection plus cheap filters (Hamming and ungapped rescoring) before full local alignment, which is why it scales near-linearly for very large sequence sets.

## Masking and Composition-Bias Tradeoffs {#sec-sharp-bias}

Low-complexity masking and composition-bias correction are both speed and quality controls. Masking reduces repetitive false seed growth during indexing and matching. Composition-bias correction reduces spurious composition-driven matches in prefilter and alignment scoring.

Disabling these controls can improve throughput in some data regimes, but it can also destabilize precision and make run-to-run comparisons less interpretable if mode envelopes are not fixed.

## GPU Comparison Backend {#sec-sharp-gpu}

GPU acceleration is implemented in `ungappedprefilter` (`MMseqs2/src/prefiltering/ungappedprefilter.cpp`) with optional persistent server mode in `gpuserver` (`MMseqs2/src/util/gpuserver.cpp`).

In GPU mode, query profiles are prepared on CPU and scanned against GPU-resident target layouts. In server mode, target data remains resident and query exchange uses shared memory, reducing repeated startup overhead for low-latency repeated searches.

This backend targets search workflows; clustering workflows are not GPU-accelerated in the current architecture.

## Internal Database and Storage Model

Most MMseqs2 modules exchange MMseqs2 DB artifacts rather than plain FASTA. Contiguous record files plus explicit index offsets reduce filesystem overhead and enable direct key-based access.

Core file roles are stable: `<db>` stores records, `<db>.index` maps IDs to offsets/lengths, and `<db>.dbtype` encodes contract type. Header and lookup sidecars (`<db>_h`, `<db>.lookup`, taxonomy sidecars) separate sequence-heavy compute paths from annotation-heavy export paths.

This design is why MMseqs2 favors writing new DBs over in-place edits. Offsets are positional contracts; mutating payload layout in place would invalidate index semantics.

```{=typst}
#doc_note[
Header and sequence separation is intentional. Compute-heavy kernels can avoid header I/O, while export and annotation stages opt in to sidecar reads.
]
```

## Indexing and Data-Access Strategy

Precomputed indexes move cost from repeated startup into reusable artifacts. They pay off most when targets are stable across many runs. For short-lived targets, on-the-fly indexing can be cheaper than index management overhead.

Storage topology determines whether index reuse helps or hurts. On slower shared storage, startup can become I/O-bound even if compute kernels are fast. In those environments, local caching, preload controls, and resident-memory behavior may produce larger gains than threshold retuning.

`--db-load-mode` changes startup/throughput tradeoffs and should be selected as part of infrastructure design, not as an afterthought.

## Memory Model and Split Tradeoffs

Prefilter structures are typically the largest memory consumers. Legacy MMseqs2 guidance models major prefilter terms as:

`M = (7 * N * L + 8 * a^k) bytes`

with `N` sequence count, `L` mean length, `a` alphabet size, and `k` k-mer length. Operationally, memory grows with database scale plus alphabet/k-mer pointer terms.

When memory is constrained, MMseqs2 splits query or target space. Splitting lowers peak RAM but introduces extra merge and temporary I/O overhead. The penalty is often smaller at high sensitivity (compute-dominated runs) and larger at low sensitivity (I/O-dominated runs).

Set split policy as a resource-envelope decision first. Tune thresholds after split behavior is stable.

## Parallel Execution Model

MMseqs2 parallelism is layered. Intra-node OpenMP paths accelerate kernels inside one process. Inter-node execution (MPI or scheduler partitioning) distributes chunks across machines.

Distributed throughput is constrained by I/O topology as much as CPU count. Target splitting may reduce per-node RAM but can increase merge overhead. Query splitting can simplify scheduling but may duplicate target-side work. Temporary directory placement can become the dominant bottleneck at high split counts.

```{=typst}
#doc_warning[
Before attributing distributed slowdowns to compute, check shared-disk contention, split count, and merge pressure.
]
```

## Practical Tuning Order

A robust tuning order for large runs is:

1. Validate DB contracts and sidecars.
2. Stabilize index and load strategy for your storage topology.
3. Set split-memory and temp-disk policy for resource limits.
4. Align parallel mode with hardware and scheduler realities.
5. Tune sensitivity and filtering thresholds last.

This sequence matches real production bottlenecks: contract and infrastructure instability usually dominates before score-threshold tuning becomes the true limiter.

## Practical Playbooks {#sec-sharp-playbooks}

For repeated searches against a stable large target, prioritize index reuse and stable preload behavior before changing sensitivity. For memory-bound runs, tune split policy and merge overhead first. For near-identity mapping pipelines, favor ungapped/diagonal-centric paths and avoid expensive output modes that do not change decision quality.

For architecture and layer placement, use [System Map](#sec-system-map); for task-oriented command selection, use [Functional Modules Manual](#sec-functional-modules-manual); for full topology evidence, use [Dependency Map](#sec-dependency-map); and for advanced composition and reproducibility discipline, use [Expert Manual](#sec-expert-manual).
