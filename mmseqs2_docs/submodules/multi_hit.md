# Multi-hit

Modules for grouped-sequence (set-based) search and per-set aggregation pipelines.

```{=typst}
#doc_note[
This page emphasizes module relationships and practical options. For complete CLI details, open the linked command reference pages. In connection tables, `n/a` means no direct static edge was resolved.
]
```

## `besthitperset`

For each set of sequences compute the best element and update p-value.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs besthitperset  <i:targetSetDB> <i:resultDB> <o:resultDB> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | [`multihitsearch`](../reference/multihitsearch.md) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `multihitsearch.sh` |

Reference links: [Full CLI](../reference/besthitperset.md), [Dependency map](../reference/dependency_map.md#cmd-besthitperset).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--simple-best-hit` | Update the p-value by a single best hit, or by best and second best hits |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `combinepvalperset`

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

Reference links: [Full CLI](../reference/combinepvalperset.md), [Dependency map](../reference/dependency_map.md#cmd-combinepvalperset).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--alpha` | Set alpha for combining p-values during aggregation |
| `--aggregation-mode` | Combined P-values computed from 0: multi-hit, 1: minimum of all P-values, 2: product-of-P-values, 3: truncated product |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `mergeresultsbyset`

Merge results from multiple ORFs back to their respective contig.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs mergeresultsbyset <i:setDB> <i:DB> <o:DB> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | [`multihitsearch`](../reference/multihitsearch.md), [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | [`taxonomy`](./taxonomy.md) |
| Workflow script usage | `multihitsearch.sh`, `taxpercontig.sh` |

Reference links: [Full CLI](../reference/mergeresultsbyset.md), [Dependency map](../reference/dependency_map.md#cmd-mergeresultsbyset).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `multihitdb`

Create sequence DB for multi hit searches.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs multihitdb <i:fastaFile1[.gz|bz2]> ... <i:fastaFileN[.gz|bz2]> <o:setDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | `n/a` |
| Calls modules | [`createdb`](../reference/createdb.md), [`extractorfs`](../reference/extractorfs.md), [`filterdb`](../reference/filterdb.md), [`orftocontig`](../reference/orftocontig.md), [`result2stats`](../reference/result2stats.md), [`swapdb`](../reference/swapdb.md), [`translatenucs`](../reference/translatenucs.md), [`tsv2db`](../reference/tsv2db.md) |
| Related functional groups | [`database`](./database.md), [`result_handling`](./result_handling.md), [`sequence_manipulation`](./sequence_manipulation.md), [`utilities`](./utilities.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/multihitdb.md), [Dependency map](../reference/dependency_map.md#cmd-multihitdb).

### Key Options

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

## `multihitsearch`

Search with a grouped set of sequences against another grouped set.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs multihitsearch <i:querySetDB> <i:targetSetDB> <o:resultDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Called by modules | `n/a` |
| Calls modules | [`besthitperset`](../reference/besthitperset.md), [`mergeresultsbyset`](../reference/mergeresultsbyset.md), [`rmdb`](../reference/rmdb.md), [`search`](../reference/search.md) |
| Related functional groups | [`database`](./database.md), [`search_workflows`](./search.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/multihitsearch.md), [Dependency map](../reference/dependency_map.md#cmd-multihitsearch).

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

