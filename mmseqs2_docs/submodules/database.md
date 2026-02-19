## Database Management {#mod-database}

Modules for creating, indexing, splitting, merging, and maintaining MMseqs2 database artifacts.

```{=typst}
#doc_note[
This page emphasizes module relationships and practical options. For complete CLI details, open the linked command reference pages. In connection tables, `n/a` means no direct static edge was resolved.
]
```

### `aliasdb` {#modcmd-aliasdb}

Create relative symlink of DB to another name in the same folder.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs aliasdb <i:srcDB> <o:dstDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | [`tsv2exprofiledb`](#modcmd-tsv2exprofiledb) |
| Calls modules | `n/a` |
| Related functional groups | [`profiles`](#mod-profiles) |
| Workflow script usage | `tsv2exprofiledb.sh` |

Reference links: [Full CLI](#refcmd-aliasdb), [Dependency entry](#depcmd-aliasdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `concatdbs` {#modcmd-concatdbs}

Concatenate two DBs, giving new IDs to entries from 2nd DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs concatdbs <i:DB> <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Called by modules | [`cluster`](#modcmd-cluster), [`clusterupdate`](#modcmd-clusterupdate), [`linsearch`](#modcmd-linsearch) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows) |
| Workflow script usage | `linsearch.sh`, `nucleotide_clustering.sh`, `update_clustering.sh` |

Reference links: [Full CLI](#refcmd-concatdbs), [Dependency entry](#depcmd-concatdbs).

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

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs cpdb <i:srcDB> <o:dstDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-cpdb), [Dependency entry](#depcmd-cpdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `createdb` {#modcmd-createdb}

Convert FASTA/Q file(s) to a sequence DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createdb <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]>|<i:stdin> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Called by modules | [`databases`](#modcmd-databases), [`easy-cluster`](#modcmd-easy-cluster), [`easy-linclust`](#modcmd-easy-linclust), [`easy-linsearch`](#modcmd-easy-linsearch), [`easy-rbh`](#modcmd-easy-rbh), [`easy-search`](#modcmd-easy-search), [`easy-taxonomy`](#modcmd-easy-taxonomy), [`multihitdb`](#modcmd-multihitdb) |
| Calls modules | `n/a` |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows), [`multi_hit`](#mod-multi-hit) |
| Workflow script usage | `databases.sh`, `easycluster.sh`, `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh`, `multihitdb.sh` |

Reference links: [Full CLI](#refcmd-createdb), [Dependency entry](#depcmd-createdb).

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

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createindex <i:sequenceDB> <tmpDir> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Called by modules | `n/a` |
| Calls modules | [`extractframes`](#modcmd-extractframes), [`extractorfs`](#modcmd-extractorfs), [`rmdb`](#modcmd-rmdb), [`splitsequence`](#modcmd-splitsequence) |
| Related functional groups | [`sequence_manipulation`](#mod-sequence-manipulation) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-createindex), [Dependency entry](#depcmd-createindex).

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

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createlinindex <i:sequenceDB> <tmpDir> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Called by modules | [`easy-linsearch`](#modcmd-easy-linsearch), [`easy-search`](#modcmd-easy-search) |
| Calls modules | [`extractframes`](#modcmd-extractframes), [`extractorfs`](#modcmd-extractorfs), [`rmdb`](#modcmd-rmdb), [`splitsequence`](#modcmd-splitsequence) |
| Related functional groups | [`easy_workflows`](#mod-easy-workflows), [`sequence_manipulation`](#mod-sequence-manipulation) |
| Workflow script usage | `easysearch.sh` |

Reference links: [Full CLI](#refcmd-createlinindex), [Dependency entry](#depcmd-createlinindex).

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

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs createsubdb <i:subsetFile|DB> <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Called by modules | [`cluster`](#modcmd-cluster), [`clusterupdate`](#modcmd-clusterupdate), [`linclust`](#modcmd-linclust), [`search`](#modcmd-search), [`taxonomy`](#modcmd-taxonomy) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| Workflow script usage | `blastp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh`, `taxpercontig.sh`, `translated_search.sh`, `update_clustering.sh` |

Reference links: [Full CLI](#refcmd-createsubdb), [Dependency entry](#depcmd-createsubdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--id-mode` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `databases` {#modcmd-databases}

List and download databases.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Called by modules | `n/a` |
| Calls modules | [`convertmsa`](#modcmd-convertmsa), [`createdb`](#modcmd-createdb), [`createtaxdb`](#modcmd-createtaxdb), [`msa2profile`](#modcmd-msa2profile), [`nrtotaxmapping`](#modcmd-nrtotaxmapping), [`prefixid`](#modcmd-prefixid), [`rmdb`](#modcmd-rmdb), [`tar2db`](#modcmd-tar2db) |
| Related functional groups | [`profiles`](#mod-profiles), [`taxonomy`](#mod-taxonomy), [`utilities`](#mod-utilities) |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-databases), [Dependency entry](#depcmd-databases).

### `db2tar` {#modcmd-db2tar}

Archive contents of a DB to a tar archive.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs db2tar <i:DB> <o:tar[.gz]> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-db2tar), [Dependency entry](#depcmd-db2tar).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `lndb` {#modcmd-lndb}

Symlink a DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs lndb <i:srcDB> <o:dstDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-lndb), [Dependency entry](#depcmd-lndb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `mergedbs` {#modcmd-mergedbs}

Merge entries from multiple DBs.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs mergedbs <i:DB> <o:DB> <i:DB1> ... <i:DBn> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Called by modules | [`cluster`](#modcmd-cluster), [`clusterupdate`](#modcmd-clusterupdate), [`rbh`](#modcmd-rbh), [`search`](#modcmd-search) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows) |
| Workflow script usage | `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `enrich.sh`, `iterativepp.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `update_clustering.sh` |

Reference links: [Full CLI](#refcmd-mergedbs), [Dependency entry](#depcmd-mergedbs).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--prefixes` | Comma separated list of prefixes for each entry |
| `--merge-stop-empty` | Don't continue merging entries after an empty entry |

### `mvdb` {#modcmd-mvdb}

Move a DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs mvdb <i:srcDB> <o:dstDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | [`cluster`](#modcmd-cluster), [`clusterupdate`](#modcmd-clusterupdate), [`search`](#modcmd-search), [`taxonomy`](#modcmd-taxonomy), [`tsv2exprofiledb`](#modcmd-tsv2exprofiledb) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering), [`profiles`](#mod-profiles), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| Workflow script usage | `blastp.sh`, `cascaded_clustering.sh`, `searchslicedtargetprofile.sh`, `taxonomy.sh`, `tsv2exprofiledb.sh`, `update_clustering.sh` |

Reference links: [Full CLI](#refcmd-mvdb), [Dependency entry](#depcmd-mvdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `renamedbkeys` {#modcmd-renamedbkeys}

Create a new DB with original keys renamed.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs renamedbkeys <i:idMapFile|stdin> <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Called by modules | [`clusterupdate`](#modcmd-clusterupdate), [`pickconsensusrep`](#modcmd-pickconsensusrep) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering) |
| Workflow script usage | `update_clustering.sh` |

Reference links: [Full CLI](#refcmd-renamedbkeys), [Dependency entry](#depcmd-renamedbkeys).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `rmdb` {#modcmd-rmdb}

Remove a DB.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Called by modules | [`cluster`](#modcmd-cluster), [`clusterupdate`](#modcmd-clusterupdate), [`createindex`](#modcmd-createindex), [`createlinindex`](#modcmd-createlinindex), [`databases`](#modcmd-databases), [`easy-cluster`](#modcmd-easy-cluster), [`easy-linclust`](#modcmd-easy-linclust), [`easy-linsearch`](#modcmd-easy-linsearch), [`easy-rbh`](#modcmd-easy-rbh), [`easy-search`](#modcmd-easy-search), [`easy-taxonomy`](#modcmd-easy-taxonomy), [`linclust`](#modcmd-linclust), [`linsearch`](#modcmd-linsearch), [`multihitsearch`](#modcmd-multihitsearch), [`pickconsensusrep`](#modcmd-pickconsensusrep), [`rbh`](#modcmd-rbh), [`search`](#modcmd-search), [`taxonomy`](#modcmd-taxonomy), [`tsv2exprofiledb`](#modcmd-tsv2exprofiledb) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering), [`easy_workflows`](#mod-easy-workflows), [`multi_hit`](#mod-multi-hit), [`profiles`](#mod-profiles), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| Workflow script usage | `blastn.sh`, `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `createindex.sh`, `databases.sh`, `easycluster.sh`, `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh`, `iterativepp.sh`, `linclust.sh`, `linsearch.sh`, `multihitsearch.sh`, `nucleotide_clustering.sh`, `pickconsensusrep.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh`, `taxonomy.sh`, `taxpercontig.sh`, `translated_search.sh`, `tsv2exprofiledb.sh`, `update_clustering.sh` |

Reference links: [Full CLI](#refcmd-rmdb), [Dependency entry](#depcmd-rmdb).

### `splitdb` {#modcmd-splitdb}

Split DB into subsets.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs splitdb <i:DB> <o:DB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](#refcmd-splitdb), [Dependency entry](#depcmd-splitdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--split` | Split input into N equally distributed chunks |
| `--split-aa` | Try to find the best split boundaries by entry lengths |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `splitsequence` {#modcmd-splitsequence}

Split sequences by length.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs splitsequence <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | [`createindex`](#modcmd-createindex), [`createlinindex`](#modcmd-createlinindex), [`search`](#modcmd-search) |
| Calls modules | `n/a` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |
| Workflow script usage | `blastn.sh`, `createindex.sh` |

Reference links: [Full CLI](#refcmd-splitsequence), [Dependency entry](#depcmd-splitsequence).

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

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs subtractdbs <i:resultDBLeft> <i:resultDBRight> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Called by modules | [`cluster`](#modcmd-cluster), [`search`](#modcmd-search) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows) |
| Workflow script usage | `blastpgp.sh`, `cascaded_clustering.sh`, `enrich.sh`, `iterativepp.sh`, `nucleotide_clustering.sh` |

Reference links: [Full CLI](#refcmd-subtractdbs), [Dependency entry](#depcmd-subtractdbs).

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

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs swapdb <i:resultDB> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Called by modules | [`cluster`](#modcmd-cluster), [`clusterupdate`](#modcmd-clusterupdate), [`multihitdb`](#modcmd-multihitdb), [`taxonomy`](#modcmd-taxonomy) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering), [`multi_hit`](#mod-multi-hit), [`taxonomy`](#mod-taxonomy) |
| Workflow script usage | `cascaded_clustering.sh`, `multihitdb.sh`, `taxpercontig.sh`, `update_clustering.sh` |

Reference links: [Full CLI](#refcmd-swapdb), [Dependency entry](#depcmd-swapdb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `tar2db` {#modcmd-tar2db}

Convert content of tar archives to any DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs tar2db <i:tar[.gz]> ... <i:tar[.gz]> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Called by modules | [`databases`](#modcmd-databases) |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `databases.sh` |

Reference links: [Full CLI](#refcmd-tar2db), [Dependency entry](#depcmd-tar2db).

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

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs tsv2db <i:tsvFile> <o:resultDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Called by modules | [`cluster`](#modcmd-cluster), [`multihitdb`](#modcmd-multihitdb), [`pickconsensusrep`](#modcmd-pickconsensusrep), [`tsv2exprofiledb`](#modcmd-tsv2exprofiledb) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](#mod-clustering), [`multi_hit`](#mod-multi-hit), [`profiles`](#mod-profiles) |
| Workflow script usage | `cascaded_clustering.sh`, `multihitdb.sh`, `pickconsensusrep.sh`, `tsv2exprofiledb.sh` |

Reference links: [Full CLI](#refcmd-tsv2db), [Dependency entry](#depcmd-tsv2db).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--output-dbtype` | Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

