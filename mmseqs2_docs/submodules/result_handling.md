## Result Handling {#mod-result-handling}

Modules that filter, summarize, reshape, and export result databases for downstream analysis.

```{=typst}
#doc_note[
This page is task-oriented. Detailed call topology is centralized in the Dependency Map to avoid repeating large edge lists.
]
```

```{=typst}
#doc_warning[
Validate DB-type and sidecar contracts before chaining modules. Most pipeline failures are contract mismatches, not algorithmic defects.
]
```

### `convert2fasta` {#modcmd-convert2fasta}

Convert sequence DB to FASTA format.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs convert2fasta <DB> [args] [options]` (source-derived synopsis; run `mmseqs convert2fasta` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-convert2fasta) · [Dependency entry](#depcmd-convert2fasta) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `convertalis` {#modcmd-convertalis}

Convert alignment DB to BLAST-tab, SAM or custom format.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 4 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs convertalis <i:queryDb> <i:targetDb> <i:alignmentDB> <o:alignmentFile> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Upstream command count | `4` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |
| References | [Full CLI](#refcmd-convertalis) · [Dependency entry](#depcmd-convertalis) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--format-mode` | Output format: |
| `--format-output` | Choose comma separated list of output columns from: query,target,evalue,gapopen,pident,fident,nident,qstart,qend,qlen |
| `--translation-table` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE |
| `--search-type` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment |
| `--sub-mat` | Substitution matrix file |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |

### `createseqfiledb` {#modcmd-createseqfiledb}

Create a DB of unaligned FASTA entries.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 2 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createseqfiledb <i:sequenceDB> <i:resultDB> <o:fastaDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION | COMMAND_EXPERT` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |
| References | [Full CLI](#refcmd-createseqfiledb) · [Dependency entry](#depcmd-createseqfiledb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--min-sequences` | Minimum number of sequences a cluster may contain |
| `--max-sequences` | Maximum number of sequences a cluster may contain |
| `--hh-format` | Format entries to use with hhsuite (for singleton clusters) |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `createtsv` {#modcmd-createtsv}

Convert result DB to tab-separated flat file.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 3 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createtsv <i:queryDB> [<i:targetDB>] <i:resultDB> <o:tsvFile> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Upstream command count | `3` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |
| References | [Full CLI](#refcmd-createtsv) · [Dependency entry](#depcmd-createtsv) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--first-seq-as-repr` | Use the first sequence of the clustering result as representative sequence |
| `--target-column` | Select a target column (default 1), 0 if no target id exists |
| `--full-header` | Replace DB ID by its corresponding Full Header |
| `--idx-seq-src` | 0: auto, 1: split/translated sequences, 2: input sequences |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--db-output` | Return a result DB instead of a text file |

### `extractdomains` {#modcmd-extractdomains}

Extract highest scoring alignment regions for each sequence from BLAST-tab file.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs extractdomains <DB> [args] [options]` (source-derived synopsis; run `mmseqs extractdomains` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-extractdomains) · [Dependency entry](#depcmd-extractdomains) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `filterresult` {#modcmd-filterresult}

Pairwise alignment result filter.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs filterresult <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-filterresult) · [Dependency entry](#depcmd-filterresult) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | keep the query (representative) sequence |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--filter-min-enable` | Only filter MSAs with more than N sequences, 0 always filters |
| `--max-seq-id` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] |
| `--qid` | Reduce diversity of output MSAs using min.seq. identity with query sequences |

### `result2dnamsa` {#modcmd-result2dnamsa}

Compute MSA DB with out insertions in the query for DNA sequences.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs result2dnamsa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-result2dnamsa) · [Dependency entry](#depcmd-result2dnamsa) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--skip-query` | Skip the query sequence |

### `result2flat` {#modcmd-result2flat}

Create flat file by adding FASTA headers to DB entries.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 2 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs result2flat <i:queryDB> <i:targetDB> <i:resultDB> <o:fastaDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION | COMMAND_EXPERT` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |
| References | [Full CLI](#refcmd-result2flat) · [Dependency entry](#depcmd-result2flat) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--use-fasta-header` | Use the id parsed from the fasta header as the index key instead of using incrementing numeric identifiers |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `result2msa` {#modcmd-result2msa}

Compute MSA DB from a result DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs result2msa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering) |
| References | [Full CLI](#refcmd-result2msa) · [Dependency entry](#depcmd-result2msa) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--filter-msa` | Filter msa: 0: do not filter, 1: filter |
| `--filter-min-enable` | Only filter MSAs with more than N sequences, 0 always filters |
| `--max-seq-id` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] |
| `--qid` | Reduce diversity of output MSAs using min.seq. identity with query sequences |

### `result2rbh` {#modcmd-result2rbh}

Filter a merged result DB to retain only reciprocal best hits.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs result2rbh <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-result2rbh) · [Dependency entry](#depcmd-result2rbh) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `result2repseq` {#modcmd-result2repseq}

Get representative sequences from result DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 3 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs result2repseq <i:sequenceDB> <i:resultDB> <o:sequenceDb> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `3` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`easy_workflows`](#mod-easy-workflows) |
| References | [Full CLI](#refcmd-result2repseq) · [Dependency entry](#depcmd-result2repseq) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `result2stats` {#modcmd-result2stats}

Compute statistics for each entry in a DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 2 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs result2stats <i:queryDB> <i:targetDB> <i:resultDB> <o:statsDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | [`multi_hit`](#mod-multi-hit), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-result2stats) · [Dependency entry](#depcmd-result2stats) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--stat` | One of: linecount, mean, min, max, doolittle, charges, seqlen, firstline |
| `--tsv` | Return output in TSV format |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `sortresult` {#modcmd-sortresult}

Sort a result DB in the same order as the prefilter or align module.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs sortresult <i:resultbDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-sortresult) · [Dependency entry](#depcmd-sortresult) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `summarizealis` {#modcmd-summarizealis}

Summarize alignment result to one row (uniq. cov., cov., avg. seq. id.).

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs summarizealis <i:alignmentDB> <o:summerizedDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |
| References | [Full CLI](#refcmd-summarizealis) · [Dependency entry](#depcmd-summarizealis) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `summarizeheaders` {#modcmd-summarizeheaders}

Summarize FASTA headers of result DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs summarizeheaders <DB> [args] [options]` (source-derived synopsis; run `mmseqs summarizeheaders` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-summarizeheaders) · [Dependency entry](#depcmd-summarizeheaders) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `summarizeresult` {#modcmd-summarizeresult}

Extract annotations from alignment DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 2 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs summarizeresult <i:alignmentDB> <o:alignmentDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |
| References | [Full CLI](#refcmd-summarizeresult) · [Dependency entry](#depcmd-summarizeresult) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `--overlap` | Maximum overlap of covered regions |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `swapresults` {#modcmd-swapresults}

Transpose prefilter/alignment DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules. Current coupling is 4 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs swapresults <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `4` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-swapresults) · [Dependency entry](#depcmd-swapresults) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--sub-mat` | Substitution matrix file |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |

