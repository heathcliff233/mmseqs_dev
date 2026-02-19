# Prefiltering

Core candidate-generation modules used to reduce search space before expensive alignment stages.

```{=typst}
#doc_note[
This page emphasizes module relationships and practical options. For complete CLI details, open the linked command reference pages. In connection tables, `n/a` means no direct static edge was resolved.
]
```

## `countkmer`

Count k-mers.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/countkmer.md), [Dependency map](../reference/dependency_map.md#cmd-countkmer).

## `gappedprefilter`

Optimal Smith-Waterman-based prefiltering (slow).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs gappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/gappedprefilter.md), [Dependency map](../reference/dependency_map.md#cmd-gappedprefilter).

### Key Options

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

## `kmermatcher`

Find bottom-m-hashed k-mer matches within sequence DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs kmermatcher <i:sequenceDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Called by modules | [`linclust`](../reference/linclust.md) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](./clustering.md) |
| Workflow script usage | `linclust.sh` |

Reference links: [Full CLI](../reference/kmermatcher.md), [Dependency map](../reference/dependency_map.md#cmd-kmermatcher).

### Key Options

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

## `kmersearch`

Find bottom-m-hashed k-mer matches between target and query DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs kmersearch <i:queryDB> <i:kmerIndexDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Called by modules | [`linsearch`](../reference/linsearch.md) |
| Calls modules | `n/a` |
| Related functional groups | [`search_workflows`](./search.md) |
| Workflow script usage | `linsearch.sh` |

Reference links: [Full CLI](../reference/kmersearch.md), [Dependency map](../reference/dependency_map.md#cmd-kmersearch).

### Key Options

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

## `prefilter`

Double consecutive diagonal k-mer search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs prefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Called by modules | [`cluster`](../reference/cluster.md), [`search`](../reference/search.md), [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](./clustering.md), [`search_workflows`](./search.md), [`taxonomy`](./taxonomy.md) |
| Workflow script usage | `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `enrich.sh`, `iterativepp.sh`, `nucleotide_clustering.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh`, `taxpercontig.sh`, `translated_search.sh` |

Reference links: [Full CLI](../reference/prefilter.md), [Dependency map](../reference/dependency_map.md#cmd-prefilter).

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

## `ungappedprefilter`

Optimal diagonal score search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs ungappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Called by modules | [`search`](../reference/search.md) |
| Calls modules | `n/a` |
| Related functional groups | [`search_workflows`](./search.md) |
| Workflow script usage | `blastp.sh`, `blastpgp.sh` |

Reference links: [Full CLI](../reference/ungappedprefilter.md), [Dependency map](../reference/dependency_map.md#cmd-ungappedprefilter).

### Key Options

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

