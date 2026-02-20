## Clustering {#mod-clustering}

Modules for cluster construction, updates, and representative handling across different clustering strategies.

```{=typst}
#doc_note[
This page focuses on task-oriented usage and practical options. Detailed call topology is centralized in the Dependency Map to reduce duplicated edge listings.
]
```

```{=typst}
#doc_perf[
For repeated runs against stable targets, prioritize index reuse and split-memory tuning before increasing sensitivity.
]
```

### `clust` {#modcmd-clust}

Cluster result by Set-Cover/Connected-Component/Greedy-Incremental.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs clust <i:sequenceDB> <i:resultDB> <o:clusterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-clust), [Dependency entry](#depcmd-clust).

#### Key Options

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

### `cluster` {#modcmd-cluster}

Slower, sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs cluster <i:sequenceDB> <o:clusterDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Upstream command count | `2` |
| Downstream command count | `18` |
| Related functional groups | [`alignment`](#mod-alignment), [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`prefiltering`](#mod-prefiltering), [`sequence_manipulation`](#mod-sequence-manipulation), [`utilities`](#mod-utilities) |

Reference links: [Full CLI](#refcmd-cluster), [Dependency entry](#depcmd-cluster).

#### Key Options

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

### `clusterupdate` {#modcmd-clusterupdate}

Update previous clustering with new sequences.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs clusterupdate <i:oldSequenceDB> <i:newSequenceDB> <i:oldClustResultDB> <o:newMappedSequenceDB> <o:newClustResultDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Upstream command count | `0` |
| Downstream command count | `13` |
| Related functional groups | [`database`](#mod-database), [`result_handling`](#mod-result-handling), [`search_workflows`](#mod-search-workflows), [`utilities`](#mod-utilities) |

Reference links: [Full CLI](#refcmd-clusterupdate), [Dependency entry](#depcmd-clusterupdate).

#### Key Options

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

### `clusthash` {#modcmd-clusthash}

Hash-based clustering of equal length sequences.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs clusthash <i:sequenceDB> <o:alignmentDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-clusthash), [Dependency entry](#depcmd-clusthash).

#### Key Options

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

### `linclust` {#modcmd-linclust}

Fast, less sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs linclust <i:sequenceDB> <o:clusterDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Upstream command count | `2` |
| Downstream command count | `8` |
| Related functional groups | [`alignment`](#mod-alignment), [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`prefiltering`](#mod-prefiltering), [`utilities`](#mod-utilities) |

Reference links: [Full CLI](#refcmd-linclust), [Dependency entry](#depcmd-linclust).

#### Key Options

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

### `mergeclusters` {#modcmd-mergeclusters}

Merge multiple cascaded clustering steps.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs mergeclusters <i:sequenceDB> <o:clusterDB> <i:clusterDB1> ... <i:clusterDBn> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-mergeclusters), [Dependency entry](#depcmd-mergeclusters).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `pickconsensusrep` {#modcmd-pickconsensusrep}

Select new representatives for each cluster based on consensus.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Upstream command count | `0` |
| Downstream command count | `7` |
| Related functional groups | [`alignment`](#mod-alignment), [`database`](#mod-database), [`profiles`](#mod-profiles), [`result_handling`](#mod-result-handling), [`utilities`](#mod-utilities) |

Reference links: [Full CLI](#refcmd-pickconsensusrep), [Dependency entry](#depcmd-pickconsensusrep).

