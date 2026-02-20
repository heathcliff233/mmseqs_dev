### `swapdb` {#refcmd-swapdb}

Transpose DB with integer values in first column.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 4 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-swapdb); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs swapdb <i:resultDB> <o:resultDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs swapdb <i:resultDB> <o:resultDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>, Clovis Galiez & Eli Levy Karin
options: prefilter:                
 --split-memory-limit BYTE  Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory [0]
common:                   
 --threads INT              Number of CPU-cores used (all by default) [10]
 --compressed INT           Write compressed output [0]
 -v INT                     Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
