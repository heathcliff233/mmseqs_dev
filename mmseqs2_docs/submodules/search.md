# Search Workflows

Workflow-level search and mapping modules that orchestrate prefiltering and alignment under different modes.

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

## `linsearch`

Fast, less sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs linsearch <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN|COMMAND_EXPERT` |
| Called by modules | [`easy-linsearch`](../reference/easy-linsearch.md), [`easy-search`](../reference/easy-search.md) |
| Calls modules | [`align`](../reference/align.md), [`concatdbs`](../reference/concatdbs.md), [`extractorfs`](../reference/extractorfs.md), [`filterdb`](../reference/filterdb.md), [`kmersearch`](../reference/kmersearch.md), [`offsetalignment`](../reference/offsetalignment.md), [`rescorediagonal`](../reference/rescorediagonal.md), [`rmdb`](../reference/rmdb.md), [`swapresults`](../reference/swapresults.md) |
| Related functional groups | [`alignment`](./alignment.md), [`database`](./database.md), [`easy_workflows`](./easy_workflows.md), [`prefiltering`](./prefiltering.md), [`result_handling`](./result_handling.md), [`sequence_manipulation`](./sequence_manipulation.md), [`utilities`](./utilities.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/linsearch.md), [Dependency map](../reference/dependency_map.md#cmd-linsearch).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |

## `map`

Map nearly identical sequences.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs map <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | `n/a` |
| Calls modules | [`search`](../reference/search.md) |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/map.md), [Dependency map](../reference/dependency_map.md#cmd-map).

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

## `rbh`

Reciprocal best hit search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs rbh <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | [`easy-rbh`](../reference/easy-rbh.md) |
| Calls modules | [`filterdb`](../reference/filterdb.md), [`mergedbs`](../reference/mergedbs.md), [`result2rbh`](../reference/result2rbh.md), [`rmdb`](../reference/rmdb.md), [`search`](../reference/search.md), [`swapresults`](../reference/swapresults.md) |
| Related functional groups | [`database`](./database.md), [`easy_workflows`](./easy_workflows.md), [`result_handling`](./result_handling.md), [`utilities`](./utilities.md) |
| Workflow script usage | `easyrbh.sh` |

Reference links: [Full CLI](../reference/rbh.md), [Dependency map](../reference/dependency_map.md#cmd-rbh).

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

## `search`

Sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs search <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | [`clusterupdate`](../reference/clusterupdate.md), [`easy-linsearch`](../reference/easy-linsearch.md), [`easy-search`](../reference/easy-search.md), [`map`](../reference/map.md), [`multihitsearch`](../reference/multihitsearch.md), [`rbh`](../reference/rbh.md), [`search`](../reference/search.md), [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | [`align`](../reference/align.md), [`createsubdb`](../reference/createsubdb.md), [`expand2profile`](../reference/expand2profile.md), [`expandaln`](../reference/expandaln.md), [`extractframes`](../reference/extractframes.md), [`extractorfs`](../reference/extractorfs.md), [`filterresult`](../reference/filterresult.md), [`lcaalign`](../reference/lcaalign.md), [`mergedbs`](../reference/mergedbs.md), [`mvdb`](../reference/mvdb.md), [`offsetalignment`](../reference/offsetalignment.md), [`prefilter`](../reference/prefilter.md), [`profile2consensus`](../reference/profile2consensus.md), [`rescorediagonal`](../reference/rescorediagonal.md), [`result2profile`](../reference/result2profile.md), [`result2stats`](../reference/result2stats.md), [`rmdb`](../reference/rmdb.md), [`search`](../reference/search.md), [`splitsequence`](../reference/splitsequence.md), [`subtractdbs`](../reference/subtractdbs.md), [`swapresults`](../reference/swapresults.md), [`ungappedprefilter`](../reference/ungappedprefilter.md) |
| Related functional groups | [`alignment`](./alignment.md), [`clustering`](./clustering.md), [`database`](./database.md), [`easy_workflows`](./easy_workflows.md), [`multi_hit`](./multi_hit.md), [`prefiltering`](./prefiltering.md), [`profiles`](./profiles.md), [`result_handling`](./result_handling.md), [`sequence_manipulation`](./sequence_manipulation.md), [`taxonomy`](./taxonomy.md) |
| Workflow script usage | `enrich.sh`, `iterativepp.sh`, `map.sh`, `multihitsearch.sh`, `rbh.sh`, `taxonomy.sh`, `update_clustering.sh` |

Reference links: [Full CLI](../reference/search.md), [Dependency map](../reference/dependency_map.md#cmd-search).

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

