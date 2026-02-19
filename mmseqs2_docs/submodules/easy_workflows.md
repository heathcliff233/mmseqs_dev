# Easy Workflows

High-level shortcuts that operate directly on FASTA/FASTQ and produce user-facing outputs with minimal setup.

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

## `easy-cluster`

Slower, sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-cluster <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]> <o:clusterPrefix> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Called by modules | `n/a` |
| Calls modules | [`cluster`](../reference/cluster.md), [`createdb`](../reference/createdb.md), [`createseqfiledb`](../reference/createseqfiledb.md), [`createtsv`](../reference/createtsv.md), [`result2flat`](../reference/result2flat.md), [`result2repseq`](../reference/result2repseq.md), [`rmdb`](../reference/rmdb.md) |
| Related functional groups | [`clustering`](./clustering.md), [`database`](./database.md), [`result_handling`](./result_handling.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/easy-cluster.md), [Dependency map](../reference/dependency_map.md#cmd-easycluster).

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

## `easy-linclust`

Fast linear time cluster, less sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-linclust <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]> <o:clusterPrefix> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Called by modules | `n/a` |
| Calls modules | [`createdb`](../reference/createdb.md), [`createseqfiledb`](../reference/createseqfiledb.md), [`createtsv`](../reference/createtsv.md), [`linclust`](../reference/linclust.md), [`result2flat`](../reference/result2flat.md), [`result2repseq`](../reference/result2repseq.md), [`rmdb`](../reference/rmdb.md) |
| Related functional groups | [`clustering`](./clustering.md), [`database`](./database.md), [`result_handling`](./result_handling.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/easy-linclust.md), [Dependency map](../reference/dependency_map.md#cmd-easylinclust).

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

## `easy-linsearch`

Fast, less sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-linsearch <i:queryFastaFile1[.gz|.bz2]> ... <i:queryFastaFileN[.gz|.bz2]> <i:targetFastaFile[.gz|.bz2]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY | COMMAND_EXPERT` |
| Called by modules | `n/a` |
| Calls modules | [`convertalis`](../reference/convertalis.md), [`createdb`](../reference/createdb.md), [`createlinindex`](../reference/createlinindex.md), [`linsearch`](../reference/linsearch.md), [`rmdb`](../reference/rmdb.md), [`search`](../reference/search.md), [`summarizeresult`](../reference/summarizeresult.md) |
| Related functional groups | [`database`](./database.md), [`result_handling`](./result_handling.md), [`search_workflows`](./search.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/easy-linsearch.md), [Dependency map](../reference/dependency_map.md#cmd-easylinsearch).

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

## `easy-rbh`

Find reciprocal best hit.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-rbh <i:queryFastaFile1[.gz|.bz2]> <i:targetFastaFile[.gz|.bz2]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Called by modules | `n/a` |
| Calls modules | [`convertalis`](../reference/convertalis.md), [`createdb`](../reference/createdb.md), [`rbh`](../reference/rbh.md), [`rmdb`](../reference/rmdb.md) |
| Related functional groups | [`database`](./database.md), [`result_handling`](./result_handling.md), [`search_workflows`](./search.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/easy-rbh.md), [Dependency map](../reference/dependency_map.md#cmd-easyrbh).

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

## `easy-search`

Sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-search <i:queryFastaFile1[.gz|.bz2]> ... <i:queryFastaFileN[.gz|.bz2]>|<i:stdin> <i:targetFastaFile[.gz]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Called by modules | `n/a` |
| Calls modules | [`convertalis`](../reference/convertalis.md), [`createdb`](../reference/createdb.md), [`createlinindex`](../reference/createlinindex.md), [`linsearch`](../reference/linsearch.md), [`rmdb`](../reference/rmdb.md), [`search`](../reference/search.md), [`summarizeresult`](../reference/summarizeresult.md) |
| Related functional groups | [`database`](./database.md), [`result_handling`](./result_handling.md), [`search_workflows`](./search.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/easy-search.md), [Dependency map](../reference/dependency_map.md#cmd-easysearch).

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

## `easy-taxonomy`

Taxonomic classification.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-taxonomy <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]> <i:targetDB> <o:taxReports> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Called by modules | `n/a` |
| Calls modules | [`addtaxonomy`](../reference/addtaxonomy.md), [`convertalis`](../reference/convertalis.md), [`createdb`](../reference/createdb.md), [`createtsv`](../reference/createtsv.md), [`filterdb`](../reference/filterdb.md), [`lca`](../reference/lca.md), [`rmdb`](../reference/rmdb.md), [`summarizealis`](../reference/summarizealis.md), [`swapresults`](../reference/swapresults.md), [`taxonomy`](../reference/taxonomy.md), [`taxonomyreport`](../reference/taxonomyreport.md) |
| Related functional groups | [`database`](./database.md), [`result_handling`](./result_handling.md), [`taxonomy`](./taxonomy.md), [`utilities`](./utilities.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/easy-taxonomy.md), [Dependency map](../reference/dependency_map.md#cmd-easytaxonomy).

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

