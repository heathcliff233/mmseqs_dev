## Prefiltering {#mod-prefiltering}

Candidate-generation modules that prune comparison space before expensive alignment kernels.

```{=typst}
#doc_note[
This page is task-oriented. Detailed call topology is centralized in the Dependency Map to avoid repeating large edge lists.
]
```

### `countkmer` {#modcmd-countkmer}

Count k-mers.

Low-level DB or utility command used for composition and contract enforcement. Design priority is minimizing expensive downstream alignments by aggressively pruning unlikely sequence pairs. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs countkmer <DB> [args] [options]` (source-derived synopsis; run `mmseqs countkmer` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-countkmer) · [Dependency entry](#depcmd-countkmer) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `gappedprefilter` {#modcmd-gappedprefilter}

Optimal Smith-Waterman-based prefiltering (slow).

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is minimizing expensive downstream alignments by aggressively pruning unlikely sequence pairs. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs gappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-gappedprefilter) · [Dependency entry](#depcmd-gappedprefilter) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--min-ungapped-score` | Accept only matches with ungapped alignment score above threshold |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |

### `kmermatcher` {#modcmd-kmermatcher}

Find bottom-m-hashed k-mer matches within sequence DB.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is minimizing expensive downstream alignments by aggressively pruning unlikely sequence pairs. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs kmermatcher <i:sequenceDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering) |
| References | [Full CLI](#refcmd-kmermatcher) · [Dependency entry](#depcmd-kmermatcher) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--alph-size` | Alphabet size (range 2-21) |
| `--spaced-kmer-mode` | 0: use consecutive positions in k-mers; 1: use spaced k-mers |
| `--spaced-kmer-pattern` | User-specified spaced k-mer pattern |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |
| `-k` | k-mer length (0: automatically set to optimum) |

### `kmersearch` {#modcmd-kmersearch}

Find bottom-m-hashed k-mer matches between target and query DB.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is minimizing expensive downstream alignments by aggressively pruning unlikely sequence pairs. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs kmersearch <i:queryDB> <i:kmerIndexDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-kmersearch) · [Dependency entry](#depcmd-kmersearch) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--cov-mode` | 0: coverage of query and target |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |

### `prefilter` {#modcmd-prefilter}

Double consecutive diagonal k-mer search.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is minimizing expensive downstream alignments by aggressively pruning unlikely sequence pairs. Current coupling is 3 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs prefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Upstream command count | `3` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| References | [Full CLI](#refcmd-prefilter) · [Dependency entry](#depcmd-prefilter) |

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

### `ungappedprefilter` {#modcmd-ungappedprefilter}

Optimal diagonal score search.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is minimizing expensive downstream alignments by aggressively pruning unlikely sequence pairs. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs ungappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-ungappedprefilter) · [Dependency entry](#depcmd-ungappedprefilter) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--min-ungapped-score` | Accept only matches with ungapped alignment score above threshold |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--cov-mode` | 0: coverage of query and target |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |

