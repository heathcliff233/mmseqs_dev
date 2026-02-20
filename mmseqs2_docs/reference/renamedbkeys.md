### `renamedbkeys` {#refcmd-renamedbkeys}

Create a new DB with original keys renamed.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 2 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-renamedbkeys); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs renamedbkeys <i:idMapFile|stdin> <i:DB> <o:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs renamedbkeys <i:idMapFile|stdin> <i:DB> <o:DB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:             
 --subdb-mode INT   Subdb mode 0: copy data 1: soft link data and write index [0]
common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
