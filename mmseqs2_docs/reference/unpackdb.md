### `unpackdb` {#refcmd-unpackdb}

Unpack a DB into separate files.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family provides compositional utilities for custom pipelines, migration tasks, and diagnostics. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-unpackdb); functional module: [`utilities`](#mod-utilities).

**Usage**

`usage: mmseqs unpackdb <i:DB> <o:outDir> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--unpack-name-mode` | Name unpacked files by 0: DB key, 1: accession (through .lookup) |
| `--unpack-suffix` | File suffix for unpacked files. |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs unpackdb <i:DB> <o:outDir> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:                   
 --unpack-name-mode INT   Name unpacked files by 0: DB key, 1: accession (through .lookup) [1]
 --unpack-suffix STR      File suffix for unpacked files.
                          Add .gz suffix to write compressed files. []
common:                 
 --threads INT            Number of CPU-cores used (all by default) [10]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
