# Clustering

Modules for cluster construction, updates, and representative handling across different clustering strategies.

```{=typst}
#doc_note[
This page emphasizes module relationships and practical options. For complete CLI details, open the linked command reference pages. In connection tables, `n/a` means no direct static edge was resolved.
]
```

```{=typst}
#doc_perf[
For repeated runs against stable targets, prioritize index reuse and split-memory tuning before increasing sensitivity.
]
```

## `clust`

Cluster result by Set-Cover/Connected-Component/Greedy-Incremental.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs clust <i:sequenceDB> <i:resultDB> <o:clusterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Called by modules | [`cluster`](../reference/cluster.md), [`linclust`](../reference/linclust.md) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh` |

Reference links: [Full CLI](../reference/clust.md), [Dependency map](../reference/dependency_map.md#cmd-clust).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--cluster-mode` | 0: Set-Cover (greedy) |
| `--max-iterations` | Maximum depth of breadth first search in connected component clustering |
| `--similarity-type` | Type of score used for clustering. 1: alignment score 2: sequence identity |
| `--weights` | Weights used for cluster priorization |
| `--cluster-weight-threshold` | Weight threshold used for cluster priorization |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `cluster`

Slower, sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs cluster <i:sequenceDB> <o:clusterDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | [`clusterupdate`](../reference/clusterupdate.md), [`easy-cluster`](../reference/easy-cluster.md) |
| Calls modules | [`align`](../reference/align.md), [`clust`](../reference/clust.md), [`clusthash`](../reference/clusthash.md), [`concatdbs`](../reference/concatdbs.md), [`createsubdb`](../reference/createsubdb.md), [`extractframes`](../reference/extractframes.md), [`filterdb`](../reference/filterdb.md), [`linclust`](../reference/linclust.md), [`mergeclusters`](../reference/mergeclusters.md), [`mergedbs`](../reference/mergedbs.md), [`mvdb`](../reference/mvdb.md), [`offsetalignment`](../reference/offsetalignment.md), [`prefilter`](../reference/prefilter.md), [`rescorediagonal`](../reference/rescorediagonal.md), [`rmdb`](../reference/rmdb.md), [`subtractdbs`](../reference/subtractdbs.md), [`swapdb`](../reference/swapdb.md), [`tsv2db`](../reference/tsv2db.md) |
| Related functional groups | [`alignment`](./alignment.md), [`database`](./database.md), [`easy_workflows`](./easy_workflows.md), [`prefiltering`](./prefiltering.md), [`sequence_manipulation`](./sequence_manipulation.md), [`utilities`](./utilities.md) |
| Workflow script usage | `update_clustering.sh` |

Reference links: [Full CLI](../reference/cluster.md), [Dependency map](../reference/dependency_map.md#cmd-cluster).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `-s` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive |
| `-k` | k-mer length (0: automatically set to optimum) |
| `--target-search-mode` | target search mode (0: regular k-mer, 1: similar k-mer) |
| `--k-score` | k-mer threshold for generating similar k-mer lists |
| `--alph-size` | Alphabet size (range 2-21) |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--split` | Split input into N equally distributed chunks. 0: set the best split automatically |

## `clusterupdate`

Update previous clustering with new sequences.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs clusterupdate <i:oldSequenceDB> <i:newSequenceDB> <i:oldClustResultDB> <o:newMappedSequenceDB> <o:newClustResultDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | `n/a` |
| Calls modules | [`cluster`](../reference/cluster.md), [`concatdbs`](../reference/concatdbs.md), [`createsubdb`](../reference/createsubdb.md), [`diffseqdbs`](../reference/diffseqdbs.md), [`filterdb`](../reference/filterdb.md), [`mergedbs`](../reference/mergedbs.md), [`mvdb`](../reference/mvdb.md), [`prefixid`](../reference/prefixid.md), [`renamedbkeys`](../reference/renamedbkeys.md), [`result2repseq`](../reference/result2repseq.md), [`rmdb`](../reference/rmdb.md), [`search`](../reference/search.md), [`swapdb`](../reference/swapdb.md) |
| Related functional groups | [`database`](./database.md), [`result_handling`](./result_handling.md), [`search_workflows`](./search.md), [`utilities`](./utilities.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/clusterupdate.md), [Dependency map](../reference/dependency_map.md#cmd-clusterupdate).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `-s` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive |
| `-k` | k-mer length (0: automatically set to optimum) |
| `--target-search-mode` | target search mode (0: regular k-mer, 1: similar k-mer) |
| `--k-score` | k-mer threshold for generating similar k-mer lists |

## `clusthash`

Hash-based clustering of equal length sequences.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs clusthash <i:sequenceDB> <o:alignmentDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Called by modules | [`cluster`](../reference/cluster.md) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `clustering.sh` |

Reference links: [Full CLI](../reference/clusthash.md), [Dependency map](../reference/dependency_map.md#cmd-clusthash).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--alph-size` | Alphabet size (range 2-21) |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `--sub-mat` | Substitution matrix file |
| `--max-seq-len` | Maximum sequence length |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `linclust`

Fast, less sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs linclust <i:sequenceDB> <o:clusterDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | [`cluster`](../reference/cluster.md), [`easy-linclust`](../reference/easy-linclust.md) |
| Calls modules | [`align`](../reference/align.md), [`clust`](../reference/clust.md), [`createsubdb`](../reference/createsubdb.md), [`filterdb`](../reference/filterdb.md), [`kmermatcher`](../reference/kmermatcher.md), [`mergeclusters`](../reference/mergeclusters.md), [`rescorediagonal`](../reference/rescorediagonal.md), [`rmdb`](../reference/rmdb.md) |
| Related functional groups | [`alignment`](./alignment.md), [`database`](./database.md), [`easy_workflows`](./easy_workflows.md), [`prefiltering`](./prefiltering.md), [`utilities`](./utilities.md) |
| Workflow script usage | `cascaded_clustering.sh`, `nucleotide_clustering.sh` |

Reference links: [Full CLI](../reference/linclust.md), [Dependency map](../reference/dependency_map.md#cmd-linclust).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--alph-size` | Alphabet size (range 2-21) |
| `--spaced-kmer-mode` | 0: use consecutive positions in k-mers; 1: use spaced k-mers |
| `--spaced-kmer-pattern` | User-specified spaced k-mer pattern |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |

## `mergeclusters`

Merge multiple cascaded clustering steps.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs mergeclusters <i:sequenceDB> <o:clusterDB> <i:clusterDB1> ... <i:clusterDBn> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Called by modules | [`cluster`](../reference/cluster.md), [`linclust`](../reference/linclust.md) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh` |

Reference links: [Full CLI](../reference/mergeclusters.md), [Dependency map](../reference/dependency_map.md#cmd-mergeclusters).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `pickconsensusrep`

Select new representatives for each cluster based on consensus.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Called by modules | `n/a` |
| Calls modules | [`align`](../reference/align.md), [`msa2profile`](../reference/msa2profile.md), [`prefixid`](../reference/prefixid.md), [`renamedbkeys`](../reference/renamedbkeys.md), [`result2msa`](../reference/result2msa.md), [`rmdb`](../reference/rmdb.md), [`tsv2db`](../reference/tsv2db.md) |
| Related functional groups | [`alignment`](./alignment.md), [`database`](./database.md), [`profiles`](./profiles.md), [`result_handling`](./result_handling.md), [`utilities`](./utilities.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/pickconsensusrep.md), [Dependency map](../reference/dependency_map.md#cmd-pickconsensusrep).

