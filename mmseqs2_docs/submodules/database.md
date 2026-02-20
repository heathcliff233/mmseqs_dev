## Database Management {#mod-database}

Database lifecycle modules for creation, indexing, splitting, merging, and contract-preserving transforms.

```{=typst}
#doc_note[
This page is task-oriented. Detailed call topology is centralized in the Dependency Map to avoid repeating large edge lists.
]
```

### `aliasdb` {#modcmd-aliasdb}

Create relative symlink of DB to another name in the same folder.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs aliasdb <i:srcDB> <o:dstDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`profiles`](#mod-profiles) |
| References | [Full CLI](#refcmd-aliasdb) · [Dependency entry](#depcmd-aliasdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `concatdbs` {#modcmd-concatdbs}

Concatenate two DBs, giving new IDs to entries from 2nd DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 3 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs concatdbs <i:DB> <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Upstream command count | `3` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-concatdbs) · [Dependency entry](#depcmd-concatdbs) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--preserve-keys` | The keys of the two DB should be distinct, and they will be preserved in the concatenation |
| `--take-larger-entry` | Only keep the larger entry (dataSize >) in the concatenation, both databases need the same keys in the index |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `cpdb` {#modcmd-cpdb}

Copy a DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs cpdb <i:srcDB> <o:dstDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-cpdb) · [Dependency entry](#depcmd-cpdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `createdb` {#modcmd-createdb}

Convert FASTA/Q file(s) to a sequence DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 8 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createdb <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]>|<i:stdin> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Upstream command count | `8` |
| Downstream command count | `0` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows), [`multi_hit`](#mod-multi-hit) |
| References | [Full CLI](#refcmd-createdb) · [Dependency entry](#depcmd-createdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--dbtype` | Database type 0: auto, 1: amino acid 2: nucleotides |
| `--shuffle` | Shuffle input database |
| `--createdb-mode` | Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) |
| `--id-offset` | Numeric ids in index file are offset by this value |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--write-lookup` | write .lookup file containing mapping from internal id, fasta id and file number |

### `createindex` {#modcmd-createindex}

Store precomputed index on disk to reduce search overhead.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 0 upstream caller(s) and 4 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createindex <i:sequenceDB> <tmpDir> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Upstream command count | `0` |
| Downstream command count | `4` |
| Related functional groups | [`sequence_manipulation`](#mod-sequence-manipulation) |
| References | [Full CLI](#refcmd-createindex) · [Dependency entry](#depcmd-createindex) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `-k` | k-mer length (0: automatically set to optimum) |
| `--alph-size` | Alphabet size (range 2-21) |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |

### `createlinindex` {#modcmd-createlinindex}

Create linsearch index.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 2 upstream caller(s) and 4 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createlinindex <i:sequenceDB> <tmpDir> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Upstream command count | `2` |
| Downstream command count | `4` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows), [`sequence_manipulation`](#mod-sequence-manipulation) |
| References | [Full CLI](#refcmd-createlinindex) · [Dependency entry](#depcmd-createlinindex) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `-k` | k-mer length (0: automatically set to optimum) |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--alph-size` | Alphabet size (range 2-21) |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |

### `createsubdb` {#modcmd-createsubdb}

Create a subset of a DB from list of DB keys.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 5 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createsubdb <i:subsetFile|DB> <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Upstream command count | `5` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| References | [Full CLI](#refcmd-createsubdb) · [Dependency entry](#depcmd-createsubdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--id-mode` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `databases` {#modcmd-databases}

List and download databases.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 0 upstream caller(s) and 8 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs databases <DB> [args] [options]` (source-derived synopsis; run `mmseqs databases` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Upstream command count | `0` |
| Downstream command count | `8` |
| Related functional groups | [`profiles`](#mod-profiles), [`taxonomy`](#mod-taxonomy), [`utilities`](#mod-utilities) |
| References | [Full CLI](#refcmd-databases) · [Dependency entry](#depcmd-databases) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `db2tar` {#modcmd-db2tar}

Archive contents of a DB to a tar archive.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs db2tar <i:DB> <o:tar[.gz]> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-db2tar) · [Dependency entry](#depcmd-db2tar) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `lndb` {#modcmd-lndb}

Symlink a DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs lndb <i:srcDB> <o:dstDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-lndb) · [Dependency entry](#depcmd-lndb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `mergedbs` {#modcmd-mergedbs}

Merge entries from multiple DBs.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 4 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs mergedbs <i:DB> <o:DB> <i:DB1> ... <i:DBn> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Upstream command count | `4` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-mergedbs) · [Dependency entry](#depcmd-mergedbs) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--prefixes` | Comma separated list of prefixes for each entry |
| `--merge-stop-empty` | Don't continue merging entries after an empty entry |

### `mvdb` {#modcmd-mvdb}

Move a DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 5 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs mvdb <i:srcDB> <o:dstDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `5` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`profiles`](#mod-profiles), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| References | [Full CLI](#refcmd-mvdb) · [Dependency entry](#depcmd-mvdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `renamedbkeys` {#modcmd-renamedbkeys}

Create a new DB with original keys renamed.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 2 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs renamedbkeys <i:idMapFile|stdin> <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering) |
| References | [Full CLI](#refcmd-renamedbkeys) · [Dependency entry](#depcmd-renamedbkeys) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `rmdb` {#modcmd-rmdb}

Remove a DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 19 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs rmdb <DB> [args] [options]` (source-derived synopsis; run `mmseqs rmdb` for exact syntax) |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Upstream command count | `19` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`easy_workflows`](#mod-easy-workflows), [`multi_hit`](#mod-multi-hit), [`profiles`](#mod-profiles), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| References | [Full CLI](#refcmd-rmdb) · [Dependency entry](#depcmd-rmdb) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `splitdb` {#modcmd-splitdb}

Split DB into subsets.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs splitdb <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-splitdb) · [Dependency entry](#depcmd-splitdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--split` | Split input into N equally distributed chunks |
| `--split-aa` | Try to find the best split boundaries by entry lengths |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `splitsequence` {#modcmd-splitsequence}

Split sequences by length.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 3 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs splitsequence <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `3` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-splitsequence) · [Dependency entry](#depcmd-splitsequence) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--sequence-overlap` | Overlap between sequences |
| `--sequence-split-mode` | Sequence split mode 0: copy data, 1: soft link data and write new index, |
| `--headers-split-mode` | Header split mode: 0: split position, 1: original header |
| `--max-seq-len` | Maximum sequence length |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--create-lookup` | Create database lookup file (can be very large) |

### `subtractdbs` {#modcmd-subtractdbs}

Remove all entries from first DB occurring in second DB by key.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 2 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs subtractdbs <i:resultDBLeft> <i:resultDBRight> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-subtractdbs) · [Dependency entry](#depcmd-subtractdbs) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--e-profile` | Include sequences matches with < E-value thr. into the profile (>=0.0) |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `swapdb` {#modcmd-swapdb}

Transpose DB with integer values in first column.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 4 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs swapdb <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Upstream command count | `4` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`multi_hit`](#mod-multi-hit), [`taxonomy`](#mod-taxonomy) |
| References | [Full CLI](#refcmd-swapdb) · [Dependency entry](#depcmd-swapdb) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `tar2db` {#modcmd-tar2db}

Convert content of tar archives to any DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs tar2db <i:tar[.gz]> ... <i:tar[.gz]> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-tar2db) · [Dependency entry](#depcmd-tar2db) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--output-dbtype` | Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 |
| `--tar-include` | Include file names based on this regex |
| `--tar-exclude` | Exclude file names based on this regex |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `tsv2db` {#modcmd-tsv2db}

Convert a TSV file to any DB.

Low-level DB or utility command used for composition and contract enforcement. Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation. Current coupling is 4 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs tsv2db <i:tsvFile> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Upstream command count | `4` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`multi_hit`](#mod-multi-hit), [`profiles`](#mod-profiles) |
| References | [Full CLI](#refcmd-tsv2db) · [Dependency entry](#depcmd-tsv2db) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--output-dbtype` | Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

