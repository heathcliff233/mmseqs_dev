## Search Workflows {#mod-search-workflows}

Search and mapping workflows that compose prefiltering, alignment, and result conversion paths under different sensitivity and runtime envelopes.

```{=typst}
#doc_note[
This page is task-oriented. Detailed call topology is centralized in the Dependency Map to avoid repeating large edge lists.
]
```

```{=typst}
#doc_perf[
In production, tune index/load and split-memory policy before increasing sensitivity. Infrastructure choices usually dominate runtime swings.
]
```

### `linsearch` {#modcmd-linsearch}

Fast, less sensitive homology search.

High-level API command for end-to-end DB workflows with explicit controls. Design priority is balancing sensitivity, candidate pruning, and alignment cost under explicit memory and split constraints. Current coupling is 2 upstream caller(s) and 9 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs linsearch <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN|COMMAND_EXPERT` |
| Upstream command count | `2` |
| Downstream command count | `9` |
| Related functional groups | [`alignment`](#mod-alignment), [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`prefiltering`](#mod-prefiltering), [`result_handling`](#mod-result-handling), [`sequence_manipulation`](#mod-sequence-manipulation), [`utilities`](#mod-utilities) |
| References | [Full CLI](#refcmd-linsearch) · [Dependency entry](#depcmd-linsearch) |

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

High-level API command for end-to-end DB workflows with explicit controls. Design priority is balancing sensitivity, candidate pruning, and alignment cost under explicit memory and split constraints. Current coupling is 0 upstream caller(s) and 1 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs map <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Upstream command count | `0` |
| Downstream command count | `1` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-map) · [Dependency entry](#depcmd-map) |

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

High-level API command for end-to-end DB workflows with explicit controls. Design priority is balancing sensitivity, candidate pruning, and alignment cost under explicit memory and split constraints. Current coupling is 1 upstream caller(s) and 6 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs rbh <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Upstream command count | `1` |
| Downstream command count | `6` |
| Related functional groups | [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`result_handling`](#mod-result-handling), [`utilities`](#mod-utilities) |
| References | [Full CLI](#refcmd-rbh) · [Dependency entry](#depcmd-rbh) |

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

High-level API command for end-to-end DB workflows with explicit controls. Design priority is balancing sensitivity, candidate pruning, and alignment cost under explicit memory and split constraints. Current coupling is 8 upstream caller(s) and 22 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs search <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Upstream command count | `8` |
| Downstream command count | `22` |
| Related functional groups | [`alignment`](#mod-alignment), [`clustering`](#mod-clustering), [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`multi_hit`](#mod-multi-hit), [`prefiltering`](#mod-prefiltering), [`profiles`](#mod-profiles), [`result_handling`](#mod-result-handling), [`sequence_manipulation`](#mod-sequence-manipulation), [`taxonomy`](#mod-taxonomy) |
| References | [Full CLI](#refcmd-search) · [Dependency entry](#depcmd-search) |

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

