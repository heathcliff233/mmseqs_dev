### `extractalignedregion` {#refcmd-extractalignedregion}

Extract aligned sequence region from query.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family transforms sequence space before or after major compute stages. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-extractalignedregion); functional module: [`sequence_manipulation`](#mod-sequence-manipulation).

**Usage**

`usage: mmseqs extractalignedregion <i:queryDB> <i:targetDB> <i:resultDB> <o:sequenceDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--extract-mode` | Extract from 1: Query, 2: Target |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs extractalignedregion <i:queryDB> <i:targetDB> <i:resultDB> <o:sequenceDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:               
 --extract-mode INT   Extract from 1: Query, 2: Target [2]
common:             
 --compressed INT     Write compressed output [0]
 --db-load-mode INT   Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT        Number of CPU-cores used (all by default) [10]
 -v INT               Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
