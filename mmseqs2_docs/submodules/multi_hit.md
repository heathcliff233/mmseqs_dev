## Multi-hit {#mod-multi-hit}

Modules for grouped-sequence (set-based) search and per-set aggregation pipelines.

```{=typst}
#doc_note[
This page emphasizes module relationships and practical options. For complete CLI details, open the linked command reference pages. In connection tables, `n/a` means no direct static edge was resolved.
]
```

### `besthitperset` {#modcmd-besthitperset}

For each set of sequences compute the best element and update p-value.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs besthitperset  <i:targetSetDB> <i:resultDB> <o:resultDB> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | [`multihitsearch`](#modcmd-multihitsearch) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `multihitsearch.sh` |

Reference links: [Full CLI](#refcmd-besthitperset), [Dependency entry](#depcmd-besthitperset).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--simple-best-hit` | Update the p-value by a single best hit, or by best and second best hits |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `combinepvalperset` {#modcmd-combinepvalperset}

For each set compute the combined p-value.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs combinepvalperset <i:querySetDB> <i:targetSetDB> <i:resultDB> <o:pvalDB> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-combinepvalperset), [Dependency entry](#depcmd-combinepvalperset).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--alpha` | Set alpha for combining p-values during aggregation |
| `--aggregation-mode` | Combined P-values computed from 0: multi-hit, 1: minimum of all P-values, 2: product-of-P-values, 3: truncated product |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `mergeresultsbyset` {#modcmd-mergeresultsbyset}

Merge results from multiple ORFs back to their respective contig.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs mergeresultsbyset <i:setDB> <i:DB> <o:DB> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | [`multihitsearch`](#modcmd-multihitsearch), [`taxonomy`](#modcmd-taxonomy) |
| Calls modules | `n/a` |
| Related functional groups | [`taxonomy`](#mod-taxonomy) |
| Workflow script usage | `multihitsearch.sh`, `taxpercontig.sh` |

Reference links: [Full CLI](#refcmd-mergeresultsbyset), [Dependency entry](#depcmd-mergeresultsbyset).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `multihitdb` {#modcmd-multihitdb}

Create sequence DB for multi hit searches.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs multihitdb <i:fastaFile1[.gz|bz2]> ... <i:fastaFileN[.gz|bz2]> <o:setDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | `n/a` |
| Calls modules | [`createdb`](#modcmd-createdb), [`extractorfs`](#modcmd-extractorfs), [`filterdb`](#modcmd-filterdb), [`orftocontig`](#modcmd-orftocontig), [`result2stats`](#modcmd-result2stats), [`swapdb`](#modcmd-swapdb), [`translatenucs`](#modcmd-translatenucs), [`tsv2db`](#modcmd-tsv2db) |
| Related functional groups | [`database`](#mod-database), [`result_handling`](#mod-result-handling), [`sequence_manipulation`](#mod-sequence-manipulation), [`utilities`](#mod-utilities) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-multihitdb), [Dependency entry](#depcmd-multihitdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--dbtype` | Database type 0: auto, 1: amino acid 2: nucleotides |
| `--shuffle` | Shuffle input database |
| `--createdb-mode` | Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) |
| `--id-offset` | Numeric ids in index file are offset by this value |
| `--min-length` | Minimum codon number in open reading frames |
| `--max-length` | Maximum codon number in open reading frames |
| `--max-gaps` | Maximum number of codons with gaps or unknown residues before an open reading frame is rejected |
| `--contig-start-mode` | Contig start can be 0: incomplete, 1: complete, 2: both |

### `multihitsearch` {#modcmd-multihitsearch}

Search with a grouped set of sequences against another grouped set.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs multihitsearch <i:querySetDB> <i:targetSetDB> <o:resultDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | `n/a` |
| Calls modules | [`besthitperset`](#modcmd-besthitperset), [`mergeresultsbyset`](#modcmd-mergeresultsbyset), [`rmdb`](#modcmd-rmdb), [`search`](#modcmd-search) |
| Related functional groups | [`database`](#mod-database), [`search_workflows`](#mod-search-workflows) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-multihitsearch), [Dependency entry](#depcmd-multihitsearch).

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

