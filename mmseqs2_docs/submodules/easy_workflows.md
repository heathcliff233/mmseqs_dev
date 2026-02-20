## Easy Workflows {#mod-easy-workflows}

High-level shortcuts that operate directly on FASTA/FASTQ inputs and orchestrate MMseqs2 modules with practical defaults.

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

### `easy-cluster` {#modcmd-easy-cluster}

Slower, sensitive clustering.

Workflow-level entrypoint that orchestrates downstream MMseqs2 modules. Design priority is fast onboarding with robust defaults; fine-grained behavior is inherited from downstream workflow modules. Current coupling is 0 upstream caller(s) and 7 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-cluster <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]> <o:clusterPrefix> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Upstream command count | `0` |
| Downstream command count | `7` |
| Related functional groups | [`clustering`](#mod-clustering), [`database`](#mod-database), [`result_handling`](#mod-result-handling) |
| References | [Full CLI](#refcmd-easy-cluster) · [Dependency entry](#depcmd-easy-cluster) |

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

### `easy-linclust` {#modcmd-easy-linclust}

Fast linear time cluster, less sensitive clustering.

Workflow-level entrypoint that orchestrates downstream MMseqs2 modules. Design priority is fast onboarding with robust defaults; fine-grained behavior is inherited from downstream workflow modules. Current coupling is 0 upstream caller(s) and 7 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-linclust <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]> <o:clusterPrefix> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Upstream command count | `0` |
| Downstream command count | `7` |
| Related functional groups | [`clustering`](#mod-clustering), [`database`](#mod-database), [`result_handling`](#mod-result-handling) |
| References | [Full CLI](#refcmd-easy-linclust) · [Dependency entry](#depcmd-easy-linclust) |

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

### `easy-linsearch` {#modcmd-easy-linsearch}

Fast, less sensitive homology search.

Workflow-level entrypoint that orchestrates downstream MMseqs2 modules. Design priority is fast onboarding with robust defaults; fine-grained behavior is inherited from downstream workflow modules. Current coupling is 0 upstream caller(s) and 7 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-linsearch <i:queryFastaFile1[.gz|.bz2]> ... <i:queryFastaFileN[.gz|.bz2]> <i:targetFastaFile[.gz|.bz2]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY | COMMAND_EXPERT` |
| Upstream command count | `0` |
| Downstream command count | `7` |
| Related functional groups | [`database`](#mod-database), [`result_handling`](#mod-result-handling), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-easy-linsearch) · [Dependency entry](#depcmd-easy-linsearch) |

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

### `easy-rbh` {#modcmd-easy-rbh}

Find reciprocal best hit.

Workflow-level entrypoint that orchestrates downstream MMseqs2 modules. Design priority is fast onboarding with robust defaults; fine-grained behavior is inherited from downstream workflow modules. Current coupling is 0 upstream caller(s) and 4 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-rbh <i:queryFastaFile1[.gz|.bz2]> <i:targetFastaFile[.gz|.bz2]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Upstream command count | `0` |
| Downstream command count | `4` |
| Related functional groups | [`database`](#mod-database), [`result_handling`](#mod-result-handling), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-easy-rbh) · [Dependency entry](#depcmd-easy-rbh) |

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

### `easy-search` {#modcmd-easy-search}

Sensitive homology search.

Workflow-level entrypoint that orchestrates downstream MMseqs2 modules. Design priority is fast onboarding with robust defaults; fine-grained behavior is inherited from downstream workflow modules. Current coupling is 0 upstream caller(s) and 7 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-search <i:queryFastaFile1[.gz|.bz2]> ... <i:queryFastaFileN[.gz|.bz2]>|<i:stdin> <i:targetFastaFile[.gz]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Upstream command count | `0` |
| Downstream command count | `7` |
| Related functional groups | [`database`](#mod-database), [`result_handling`](#mod-result-handling), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-easy-search) · [Dependency entry](#depcmd-easy-search) |

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

### `easy-taxonomy` {#modcmd-easy-taxonomy}

Taxonomic classification.

Workflow-level entrypoint that orchestrates downstream MMseqs2 modules. Design priority is fast onboarding with robust defaults; fine-grained behavior is inherited from downstream workflow modules. Current coupling is 0 upstream caller(s) and 11 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs easy-taxonomy <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]> <i:targetDB> <o:taxReports> <tmpDir> [options]` |
| API layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Upstream command count | `0` |
| Downstream command count | `11` |
| Related functional groups | [`database`](#mod-database), [`result_handling`](#mod-result-handling), [`taxonomy`](#mod-taxonomy), [`utilities`](#mod-utilities) |
| References | [Full CLI](#refcmd-easy-taxonomy) · [Dependency entry](#depcmd-easy-taxonomy) |

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

