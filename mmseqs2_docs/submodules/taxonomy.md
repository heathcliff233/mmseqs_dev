## Taxonomy {#mod-taxonomy}

Modules for taxonomy DB preparation, assignment, filtering, and reporting workflows.

```{=typst}
#doc_note[
This page focuses on task-oriented usage and practical options. Detailed call topology is centralized in the Dependency Map to reduce duplicated edge listings.
]
```

```{=typst}
#doc_warning[
Validate database-type and sidecar compatibility before chaining modules. Most pipeline failures come from DB contract mismatches.
]
```

### `addtaxonomy` {#modcmd-addtaxonomy}

Add taxonomic labels to result DB.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |

Reference links: [Full CLI](#refcmd-addtaxonomy), [Dependency entry](#depcmd-addtaxonomy).

### `aggregatetax` {#modcmd-aggregatetax}

Aggregate multiple taxon labels to a single label.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-aggregatetax), [Dependency entry](#depcmd-aggregatetax).

### `aggregatetaxweights` {#modcmd-aggregatetaxweights}

Aggregate multiple taxon labels to a single label.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-aggregatetaxweights), [Dependency entry](#depcmd-aggregatetaxweights).

### `createbintaxmapping` {#modcmd-createbintaxmapping}

Create binary taxonomy mapping from tabular taxonomy mapping.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-createbintaxmapping), [Dependency entry](#depcmd-createbintaxmapping).

### `createbintaxonomy` {#modcmd-createbintaxonomy}

Create binary taxonomy from NCBI input.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-createbintaxonomy), [Dependency entry](#depcmd-createbintaxonomy).

### `createdmptaxonomy` {#modcmd-createdmptaxonomy}

Create dmp files from binary taxonomy.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-createdmptaxonomy), [Dependency entry](#depcmd-createdmptaxonomy).

### `createtaxdb` {#modcmd-createtaxdb}

Add taxonomic labels to sequence DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createtaxdb <i:sequenceDB> <tmpDir> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Upstream command count | `1` |
| Downstream command count | `1` |
| Related functional groups | [`database`](#mod-database) |

Reference links: [Full CLI](#refcmd-createtaxdb), [Dependency entry](#depcmd-createtaxdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--ncbi-tax-dump` | tax dump directory. The tax dump can be downloaded here "ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz" |
| `--tax-mapping-file` | File to map sequence identifier to taxonomical identifier |
| `--tax-mapping-mode` | Map taxonomy based on sequence database 0: .lookup file 1: .source file |
| `--tax-db-mode` | Create taxonomy database as: 0: .dmp flat files (human readable) 1: binary dump (faster readin) |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `filtertaxdb` {#modcmd-filtertaxdb}

Filter taxonomy result database.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs filtertaxdb <i:targetDB> <i:taxDB> <o:taxDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-filtertaxdb), [Dependency entry](#depcmd-filtertaxdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `filtertaxseqdb` {#modcmd-filtertaxseqdb}

Filter taxonomy sequence database.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs filtertaxseqdb <i:taxSeqDB> <o:taxSeqDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-filtertaxseqdb), [Dependency entry](#depcmd-filtertaxseqdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `lca` {#modcmd-lca}

Compute the lowest common ancestor.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs lca <i:targetDB> <i:resultDB> <o:taxaDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |

Reference links: [Full CLI](#refcmd-lca), [Dependency entry](#depcmd-lca).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--lca-ranks` | Add column with specified ranks (',' separated) |
| `--blacklist` | Comma separated list of ignored taxa in LCA computation |
| `--tax-lineage` | 0: don't show, 1: add all lineage names, 2: add all lineage taxids |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `lcaalign` {#modcmd-lcaalign}

Efficient gapped alignment for lca computation.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs lcaalign <i:queryDB> <i:targetDB> <i:resultDB> <o:alignmentDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |

Reference links: [Full CLI](#refcmd-lcaalign), [Dependency entry](#depcmd-lcaalign).

#### Key Options

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

### `majoritylca` {#modcmd-majoritylca}

Compute the lowest common ancestor using majority voting.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-majoritylca), [Dependency entry](#depcmd-majoritylca).

### `nrtotaxmapping` {#modcmd-nrtotaxmapping}

Create taxonomy mapping for NR database.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`database`](#mod-database) |

Reference links: [Full CLI](#refcmd-nrtotaxmapping), [Dependency entry](#depcmd-nrtotaxmapping).

### `taxonomy` {#modcmd-taxonomy}

Taxonomic classification.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs taxonomy <i:queryDB> <i:targetDB> <o:taxaDB> <tmpDir> [options]` |
| API layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Upstream command count | `2` |
| Downstream command count | `15` |
| Related functional groups | [`alignment`](#mod-alignment), [`database`](#mod-database), [`easy_workflows`](#mod-easy-workflows), [`multi_hit`](#mod-multi-hit), [`prefiltering`](#mod-prefiltering), [`search_workflows`](#mod-search-workflows), [`sequence_manipulation`](#mod-sequence-manipulation), [`utilities`](#mod-utilities) |

Reference links: [Full CLI](#refcmd-taxonomy), [Dependency entry](#depcmd-taxonomy).

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

### `taxonomyreport` {#modcmd-taxonomyreport}

Create a taxonomy report in Kraken or Krona format.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs taxonomyreport <i:seqTaxDB> <i:taxResultDB/resultDB/sequenceDB> <o:taxonomyReport> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_FORMAT_CONVERSION` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows) |

Reference links: [Full CLI](#refcmd-taxonomyreport), [Dependency entry](#depcmd-taxonomyreport).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--report-mode` | Taxonomy report mode 0: Kraken 1: Krona |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

