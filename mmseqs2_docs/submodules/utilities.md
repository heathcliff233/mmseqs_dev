# Utilities

General-purpose helpers and special-purpose modules that support advanced workflow composition.

```{=typst}
#doc_note[
This page emphasizes module relationships and practical options. For complete CLI details, open the linked command reference pages. In connection tables, `n/a` means no direct static edge was resolved.
]
```

## `apply`

Execute given program on each DB entry.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs apply <i:DB> <o:DB> -- program [args...] [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/apply.md), [Dependency map](../reference/dependency_map.md#cmd-apply).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `compress`

Compress DB entries.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs compress <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | [`tsv2exprofiledb`](../reference/tsv2exprofiledb.md) |
| Calls modules | `n/a` |
| Related functional groups | [`profiles`](./profiles.md) |
| Workflow script usage | `tsv2exprofiledb.sh` |

Reference links: [Full CLI](../reference/compress.md), [Dependency map](../reference/dependency_map.md#cmd-compress).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `convertkb`

Convert UniProtKB data to a DB.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/convertkb.md), [Dependency map](../reference/dependency_map.md#cmd-convertkb).

## `decompress`

Decompress DB entries.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs decompress <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/decompress.md), [Dependency map](../reference/dependency_map.md#cmd-decompress).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `diffseqdbs`

Compute diff of two sequence DBs.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Called by modules | [`clusterupdate`](../reference/clusterupdate.md) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](./clustering.md) |
| Workflow script usage | `update_clustering.sh` |

Reference links: [Full CLI](../reference/diffseqdbs.md), [Dependency map](../reference/dependency_map.md#cmd-diffseqdbs).

## `filterdb`

DB filtering by given conditions.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs filterdb <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Called by modules | [`cluster`](../reference/cluster.md), [`clusterupdate`](../reference/clusterupdate.md), [`easy-taxonomy`](../reference/easy-taxonomy.md), [`linclust`](../reference/linclust.md), [`linsearch`](../reference/linsearch.md), [`multihitdb`](../reference/multihitdb.md), [`rbh`](../reference/rbh.md), [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](./clustering.md), [`easy_workflows`](./easy_workflows.md), [`multi_hit`](./multi_hit.md), [`search_workflows`](./search.md), [`taxonomy`](./taxonomy.md) |
| Workflow script usage | `cascaded_clustering.sh`, `easytaxonomy.sh`, `linclust.sh`, `linsearch.sh`, `multihitdb.sh`, `rbh.sh`, `taxonomy.sh`, `taxpercontig.sh`, `update_clustering.sh` |

Reference links: [Full CLI](../reference/filterdb.md), [Dependency map](../reference/dependency_map.md#cmd-filterdb).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--filter-expression` | Specify a mathematical expression to filter lines |
| `--filter-column` | column |
| `--column-to-take` | column to take in join mode. If -1, the whole line is taken |
| `--filter-regex` | Regex to select column (example float: [0-9]*(.[0-9]+)? int:[1-9]{1}[0-9]) |
| `--positive-filter` | Used in conjunction with --filter-file. If true, out  = in \intersect filter ; if false, out = in - filter |
| `--filter-file` | Specify a file that contains the filtering elements |
| `--beats-first` | Filter by comparing each entry to the first entry |

## `gff2db`

Extract regions from a sequence database based on a GFF3 file.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/gff2db.md), [Dependency map](../reference/dependency_map.md#cmd-gff2db).

## `gpuserver`

Start a GPU server.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs gpuserver <i:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/gpuserver.md), [Dependency map](../reference/dependency_map.md#cmd-gpuserver).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--prefilter-mode` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped |
| `--gpu` | Use GPU (CUDA) if possible |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |

## `maskbygff`

Mask out sequence regions in a sequence DB by features selected from a GFF3 file.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/maskbygff.md), [Dependency map](../reference/dependency_map.md#cmd-maskbygff).

## `prefixid`

For each entry in a DB prepend the entry key to the entry itself.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs prefixid <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Called by modules | [`clusterupdate`](../reference/clusterupdate.md), [`databases`](../reference/databases.md), [`pickconsensusrep`](../reference/pickconsensusrep.md) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](./clustering.md), [`database`](./database.md) |
| Workflow script usage | `databases.sh`, `pickconsensusrep.sh`, `update_clustering.sh` |

Reference links: [Full CLI](../reference/prefixid.md), [Dependency map](../reference/dependency_map.md#cmd-prefixid).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--prefix` | Use this prefix for all entries |
| `--mapping-file` | Specify a file that translates the keys of a DB to new keys, TSV format |
| `--tsv` | Return output in TSV format |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `setextendeddbtype`

Write an extended DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs setextendeddbtype <i:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/setextendeddbtype.md), [Dependency map](../reference/dependency_map.md#cmd-setextendeddbtype).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--extended-dbtype` | Set extended dbtype 1: compressed, 2: need src, 4: context pseudoe cnts |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `suffixid`

For each entry in a DB append the entry key to the entry itself.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs suffixid <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/suffixid.md), [Dependency map](../reference/dependency_map.md#cmd-suffixid).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--prefix` | Use this prefix for all entries |
| `--mapping-file` | Specify a file that translates the keys of a DB to new keys, TSV format |
| `--tsv` | Return output in TSV format |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `summarizetabs`

Extract annotations from HHblits BLAST-tab-formatted results.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/summarizetabs.md), [Dependency map](../reference/dependency_map.md#cmd-summarizetabs).

## `touchdb`

Preload DB into memory (page cache).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs touchdb <i:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/touchdb.md), [Dependency map](../reference/dependency_map.md#cmd-touchdb).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `unpackdb`

Unpack a DB into separate files.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs unpackdb <i:DB> <o:outDir> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/unpackdb.md), [Dependency map](../reference/dependency_map.md#cmd-unpackdb).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--unpack-name-mode` | Name unpacked files by 0: DB key, 1: accession (through .lookup) |
| `--unpack-suffix` | File suffix for unpacked files. |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `view`

Print DB entries given in --id-list to stdout.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs view <i:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/view.md), [Dependency map](../reference/dependency_map.md#cmd-view).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--id-list` | Entries to be printed separated by ',' |
| `--id-mode` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) |
| `--idx-entry-type` | 0: sequence, 1: src sequence, 2: header, 3: src header |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

