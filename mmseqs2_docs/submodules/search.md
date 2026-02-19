## Search Workflows {#mod-search-workflows}

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

### `linsearch` {#modcmd-linsearch}

Fast, less sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs linsearch <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN|COMMAND_EXPERT` |
| Called by modules | [`easy-linsearch`](#modcmd-easy-linsearch), [`easy-search`](#modcmd-easy-search) |
| Calls modules | [`align`](#modcmd-align), [`concatdbs`](#modcmd-concatdbs), [`extractorfs`](#modcmd-extractorfs), [`filterdb`](#modcmd-filterdb), [`kmersearch`](#modcmd-kmersearch), [`offsetalignment`](#modcmd-offsetalignment), [`rescorediagonal`](#modcmd-rescorediagonal), [`rmdb`](#modcmd-rmdb), [`swapresults`](#modcmd-swapresults) |
| Related functional groups | [`alignment`](#mod-alignment), [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`prefiltering`](#mod-prefiltering), [`result_handling`](#mod-result-handling), [`sequence_manipulation`](#mod-sequence-manipulation), [`utilities`](#mod-utilities) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-linsearch), [Dependency entry](#depcmd-linsearch).

#### Key Options

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

### `map` {#modcmd-map}

Map nearly identical sequences.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs map <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | `n/a` |
| Calls modules | [`search`](#modcmd-search) |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-map), [Dependency entry](#depcmd-map).

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

### `rbh` {#modcmd-rbh}

Reciprocal best hit search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs rbh <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | [`easy-rbh`](#modcmd-easy-rbh) |
| Calls modules | [`filterdb`](#modcmd-filterdb), [`mergedbs`](#modcmd-mergedbs), [`result2rbh`](#modcmd-result2rbh), [`rmdb`](#modcmd-rmdb), [`search`](#modcmd-search), [`swapresults`](#modcmd-swapresults) |
| Related functional groups | [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`result_handling`](#mod-result-handling), [`utilities`](#mod-utilities) |
| Workflow script usage | `easyrbh.sh` |

Reference links: [Full CLI](#refcmd-rbh), [Dependency entry](#depcmd-rbh).

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

### `search` {#modcmd-search}

Sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs search <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | [`clusterupdate`](#modcmd-clusterupdate), [`easy-linsearch`](#modcmd-easy-linsearch), [`easy-search`](#modcmd-easy-search), [`map`](#modcmd-map), [`multihitsearch`](#modcmd-multihitsearch), [`rbh`](#modcmd-rbh), [`search`](#modcmd-search), [`taxonomy`](#modcmd-taxonomy) |
| Calls modules | [`align`](#modcmd-align), [`createsubdb`](#modcmd-createsubdb), [`expand2profile`](#modcmd-expand2profile), [`expandaln`](#modcmd-expandaln), [`extractframes`](#modcmd-extractframes), [`extractorfs`](#modcmd-extractorfs), [`filterresult`](#modcmd-filterresult), [`lcaalign`](#modcmd-lcaalign), [`mergedbs`](#modcmd-mergedbs), [`mvdb`](#modcmd-mvdb), [`offsetalignment`](#modcmd-offsetalignment), [`prefilter`](#modcmd-prefilter), [`profile2consensus`](#modcmd-profile2consensus), [`rescorediagonal`](#modcmd-rescorediagonal), [`result2profile`](#modcmd-result2profile), [`result2stats`](#modcmd-result2stats), [`rmdb`](#modcmd-rmdb), [`search`](#modcmd-search), [`splitsequence`](#modcmd-splitsequence), [`subtractdbs`](#modcmd-subtractdbs), [`swapresults`](#modcmd-swapresults), [`ungappedprefilter`](#modcmd-ungappedprefilter) |
| Related functional groups | [`alignment`](#mod-alignment), [`clustering`](#mod-clustering), [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`multi_hit`](#mod-multi-hit), [`prefiltering`](#mod-prefiltering), [`profiles`](#mod-profiles), [`result_handling`](#mod-result-handling), [`sequence_manipulation`](#mod-sequence-manipulation), [`taxonomy`](#mod-taxonomy) |
| Workflow script usage | `enrich.sh`, `iterativepp.sh`, `map.sh`, `multihitsearch.sh`, `rbh.sh`, `taxonomy.sh`, `update_clustering.sh` |

Reference links: [Full CLI](#refcmd-search), [Dependency entry](#depcmd-search).

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

