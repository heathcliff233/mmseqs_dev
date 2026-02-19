# Taxonomy

Modules for taxonomy DB preparation, assignment, filtering, and reporting workflows.

```{=typst}
#doc_note[
This page emphasizes module relationships and practical options. For complete CLI details, open the linked command reference pages. In connection tables, `n/a` means no direct static edge was resolved.
]
```

```{=typst}
#doc_warning[
Validate database-type and sidecar compatibility before chaining modules. Most pipeline failures come from DB contract mismatches.
]
```

## `addtaxonomy`

Add taxonomic labels to result DB.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Called by modules | [`easy-taxonomy`](../reference/easy-taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | [`easy_workflows`](./easy_workflows.md) |
| Workflow script usage | `easytaxonomy.sh` |

Reference links: [Full CLI](../reference/addtaxonomy.md), [Dependency map](../reference/dependency_map.md#cmd-addtaxonomy).

## `aggregatetax`

Aggregate multiple taxon labels to a single label.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Called by modules | [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/aggregatetax.md), [Dependency map](../reference/dependency_map.md#cmd-aggregatetax).

## `aggregatetaxweights`

Aggregate multiple taxon labels to a single label.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Called by modules | [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `taxpercontig.sh` |

Reference links: [Full CLI](../reference/aggregatetaxweights.md), [Dependency map](../reference/dependency_map.md#cmd-aggregatetaxweights).

## `createbintaxmapping`

Create binary taxonomy mapping from tabular taxonomy mapping.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/createbintaxmapping.md), [Dependency map](../reference/dependency_map.md#cmd-createbintaxmapping).

## `createbintaxonomy`

Create binary taxonomy from NCBI input.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Called by modules | [`createtaxdb`](../reference/createtaxdb.md) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `createtaxdb.sh` |

Reference links: [Full CLI](../reference/createbintaxonomy.md), [Dependency map](../reference/dependency_map.md#cmd-createbintaxonomy).

## `createdmptaxonomy`

Create dmp files from binary taxonomy.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/createdmptaxonomy.md), [Dependency map](../reference/dependency_map.md#cmd-createdmptaxonomy).

## `createtaxdb`

Add taxonomic labels to sequence DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createtaxdb <i:sequenceDB> <tmpDir> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Called by modules | [`databases`](../reference/databases.md) |
| Calls modules | [`createbintaxonomy`](../reference/createbintaxonomy.md) |
| Related functional groups | [`database`](./database.md) |
| Workflow script usage | `databases.sh` |

Reference links: [Full CLI](../reference/createtaxdb.md), [Dependency map](../reference/dependency_map.md#cmd-createtaxdb).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--ncbi-tax-dump` | tax dump directory. The tax dump can be downloaded here "ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz" |
| `--tax-mapping-file` | File to map sequence identifier to taxonomical identifier |
| `--tax-mapping-mode` | Map taxonomy based on sequence database 0: .lookup file 1: .source file |
| `--tax-db-mode` | Create taxonomy database as: 0: .dmp flat files (human readable) 1: binary dump (faster readin) |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `filtertaxdb`

Filter taxonomy result database.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs filtertaxdb <i:targetDB> <i:taxDB> <o:taxDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/filtertaxdb.md), [Dependency map](../reference/dependency_map.md#cmd-filtertaxdb).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `filtertaxseqdb`

Filter taxonomy sequence database.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs filtertaxseqdb <i:taxSeqDB> <o:taxSeqDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/filtertaxseqdb.md), [Dependency map](../reference/dependency_map.md#cmd-filtertaxseqdb).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `lca`

Compute the lowest common ancestor.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs lca <i:targetDB> <i:resultDB> <o:taxaDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Called by modules | [`easy-taxonomy`](../reference/easy-taxonomy.md), [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | [`easy_workflows`](./easy_workflows.md) |
| Workflow script usage | `taxonomy.sh` |

Reference links: [Full CLI](../reference/lca.md), [Dependency map](../reference/dependency_map.md#cmd-lca).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--lca-ranks` | Add column with specified ranks (',' separated) |
| `--blacklist` | Comma separated list of ignored taxa in LCA computation |
| `--tax-lineage` | 0: don't show, 1: add all lineage names, 2: add all lineage taxids |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `lcaalign`

Efficient gapped alignment for lca computation.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs lcaalign <i:queryDB> <i:targetDB> <i:resultDB> <o:alignmentDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Called by modules | [`search`](../reference/search.md) |
| Calls modules | `n/a` |
| Related functional groups | [`search_workflows`](./search.md) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/lcaalign.md), [Dependency map](../reference/dependency_map.md#cmd-lcaalign).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `--alignment-mode` | How to compute the alignment: |
| `--alignment-output-mode` | How to compute the alignment: |
| `--wrapped-scoring` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start |
| `-e` | List matches below this E-value (range 0.0-inf) |

## `majoritylca`

Compute the lowest common ancestor using majority voting.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/majoritylca.md), [Dependency map](../reference/dependency_map.md#cmd-majoritylca).

## `nrtotaxmapping`

Create taxonomy mapping for NR database.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Called by modules | [`databases`](../reference/databases.md) |
| Calls modules | `n/a` |
| Related functional groups | [`database`](./database.md) |
| Workflow script usage | `databases.sh` |

Reference links: [Full CLI](../reference/nrtotaxmapping.md), [Dependency map](../reference/dependency_map.md#cmd-nrtotaxmapping).

## `taxonomy`

Taxonomic classification.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs taxonomy <i:queryDB> <i:targetDB> <o:taxaDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Called by modules | [`easy-taxonomy`](../reference/easy-taxonomy.md), [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | [`aggregatetax`](../reference/aggregatetax.md), [`aggregatetaxweights`](../reference/aggregatetaxweights.md), [`createsubdb`](../reference/createsubdb.md), [`extractorfs`](../reference/extractorfs.md), [`filterdb`](../reference/filterdb.md), [`lca`](../reference/lca.md), [`mergeresultsbyset`](../reference/mergeresultsbyset.md), [`mvdb`](../reference/mvdb.md), [`prefilter`](../reference/prefilter.md), [`recoverlongestorf`](../reference/recoverlongestorf.md), [`rescorediagonal`](../reference/rescorediagonal.md), [`rmdb`](../reference/rmdb.md), [`search`](../reference/search.md), [`swapdb`](../reference/swapdb.md), [`taxonomy`](../reference/taxonomy.md) |
| Related functional groups | [`alignment`](./alignment.md), [`database`](./database.md), [`easy_workflows`](./easy_workflows.md), [`multi_hit`](./multi_hit.md), [`prefiltering`](./prefiltering.md), [`search_workflows`](./search.md), [`sequence_manipulation`](./sequence_manipulation.md), [`utilities`](./utilities.md) |
| Workflow script usage | `easytaxonomy.sh`, `taxpercontig.sh` |

Reference links: [Full CLI](../reference/taxonomy.md), [Dependency map](../reference/dependency_map.md#cmd-taxonomy).

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

## `taxonomyreport`

Create a taxonomy report in Kraken or Krona format.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs taxonomyreport <i:seqTaxDB> <i:taxResultDB/resultDB/sequenceDB> <o:taxonomyReport> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_FORMAT_CONVERSION` |
| Called by modules | [`easy-taxonomy`](../reference/easy-taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | [`easy_workflows`](./easy_workflows.md) |
| Workflow script usage | `easytaxonomy.sh` |

Reference links: [Full CLI](../reference/taxonomyreport.md), [Dependency map](../reference/dependency_map.md#cmd-taxonomyreport).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--report-mode` | Taxonomy report mode 0: Kraken 1: Krona |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

