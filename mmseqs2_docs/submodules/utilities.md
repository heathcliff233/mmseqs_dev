## Utilities {#mod-utilities}

General-purpose helpers and special-purpose composition commands used in advanced pipelines.

```{=typst}
#doc_note[
This page is task-oriented. Detailed call topology is centralized in the Dependency Map to avoid repeating large edge lists.
]
```

### `apply` {#modcmd-apply}

Execute given program on each DB entry.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs apply <i:DB> <o:DB> -- program [args...] [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-apply) · [Dependency entry](#depcmd-apply) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `compress` {#modcmd-compress}

Compress DB entries.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs compress <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`profiles`](#mod-profiles) |
| References | [Full CLI](#refcmd-compress) · [Dependency entry](#depcmd-compress) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `convertkb` {#modcmd-convertkb}

Convert UniProtKB data to a DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs convertkb <DB> [args] [options]` (source-derived synopsis; run `mmseqs convertkb` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-convertkb) · [Dependency entry](#depcmd-convertkb) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `decompress` {#modcmd-decompress}

Decompress DB entries.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs decompress <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-decompress) · [Dependency entry](#depcmd-decompress) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `diffseqdbs` {#modcmd-diffseqdbs}

Compute diff of two sequence DBs.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs diffseqdbs <DB> [args] [options]` (source-derived synopsis; run `mmseqs diffseqdbs` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering) |
| References | [Full CLI](#refcmd-diffseqdbs) · [Dependency entry](#depcmd-diffseqdbs) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `filterdb` {#modcmd-filterdb}

DB filtering by given conditions.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 8 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs filterdb <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Upstream command count | `8` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`easy_workflows`](#mod-easy-workflows), [`multi_hit`](#mod-multi-hit), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| References | [Full CLI](#refcmd-filterdb) · [Dependency entry](#depcmd-filterdb) |

#### Key Options

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

### `gff2db` {#modcmd-gff2db}

Extract regions from a sequence database based on a GFF3 file.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs gff2db <DB> [args] [options]` (source-derived synopsis; run `mmseqs gff2db` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-gff2db) · [Dependency entry](#depcmd-gff2db) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `gpuserver` {#modcmd-gpuserver}

Start a GPU server.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs gpuserver <i:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-gpuserver) · [Dependency entry](#depcmd-gpuserver) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--prefilter-mode` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped |
| `--gpu` | Use GPU (CUDA) if possible |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |

### `maskbygff` {#modcmd-maskbygff}

Mask out sequence regions in a sequence DB by features selected from a GFF3 file.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs maskbygff <DB> [args] [options]` (source-derived synopsis; run `mmseqs maskbygff` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-maskbygff) · [Dependency entry](#depcmd-maskbygff) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `prefixid` {#modcmd-prefixid}

For each entry in a DB prepend the entry key to the entry itself.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 3 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs prefixid <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Upstream command count | `3` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`database`](#mod-database) |
| References | [Full CLI](#refcmd-prefixid) · [Dependency entry](#depcmd-prefixid) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--prefix` | Use this prefix for all entries |
| `--mapping-file` | Specify a file that translates the keys of a DB to new keys, TSV format |
| `--tsv` | Return output in TSV format |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `setextendeddbtype` {#modcmd-setextendeddbtype}

Write an extended DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs setextendeddbtype <i:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-setextendeddbtype) · [Dependency entry](#depcmd-setextendeddbtype) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--extended-dbtype` | Set extended dbtype 1: compressed, 2: need src, 4: context pseudoe cnts |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `suffixid` {#modcmd-suffixid}

For each entry in a DB append the entry key to the entry itself.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs suffixid <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-suffixid) · [Dependency entry](#depcmd-suffixid) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--prefix` | Use this prefix for all entries |
| `--mapping-file` | Specify a file that translates the keys of a DB to new keys, TSV format |
| `--tsv` | Return output in TSV format |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `summarizetabs` {#modcmd-summarizetabs}

Extract annotations from HHblits BLAST-tab-formatted results.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs summarizetabs <DB> [args] [options]` (source-derived synopsis; run `mmseqs summarizetabs` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-summarizetabs) · [Dependency entry](#depcmd-summarizetabs) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `touchdb` {#modcmd-touchdb}

Preload DB into memory (page cache).

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs touchdb <i:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-touchdb) · [Dependency entry](#depcmd-touchdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `unpackdb` {#modcmd-unpackdb}

Unpack a DB into separate files.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs unpackdb <i:DB> <o:outDir> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-unpackdb) · [Dependency entry](#depcmd-unpackdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--unpack-name-mode` | Name unpacked files by 0: DB key, 1: accession (through .lookup) |
| `--unpack-suffix` | File suffix for unpacked files. |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `view` {#modcmd-view}

Print DB entries given in --id-list to stdout.

Low-level DB or utility command used for composition and contract enforcement. Design priority is composability and operational control for custom pipelines and debugging workflows. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs view <i:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-view) · [Dependency entry](#depcmd-view) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--id-list` | Entries to be printed separated by ',' |
| `--id-mode` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) |
| `--idx-entry-type` | 0: sequence, 1: src sequence, 2: header, 3: src header |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

