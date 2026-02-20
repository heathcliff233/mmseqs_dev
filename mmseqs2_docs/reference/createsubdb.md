### `createsubdb` {#refcmd-createsubdb}

Create a subset of a DB from list of DB keys.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 5 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-createsubdb); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs createsubdb <i:subsetFile|DB> <i:DB> <o:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--id-mode` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs createsubdb <i:subsetFile|DB> <i:DB> <o:DB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:             
 --subdb-mode INT   Subdb mode 0: copy data 1: soft link data and write index [0]
 --id-mode INT      Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) [0]
common:           
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Create a new sequenceDB from sequenceDB entries with keys 1, 2 and 3
 mmseqs createsubdb <(printf '1
 2
 3
 ') sequenceDB oneTwoThreeDB
 
 # Create a new sequence database with representatives of clusterDB
 mmseqs cluster sequenceDB clusterDB tmp
 mmseqs createsubdb clusterDB sequenceDB representativesDB
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
