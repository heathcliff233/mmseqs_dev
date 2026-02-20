### `splitdb` {#refcmd-splitdb}

Split DB into subsets.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-splitdb); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs splitdb <i:DB> <o:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--split` | Split input into N equally distributed chunks |
| `--split-aa` | Try to find the best split boundaries by entry lengths |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs splitdb <i:DB> <o:DB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:           
 --split INT        Split input into N equally distributed chunks [0]
 --split-aa BOOL    Try to find the best split boundaries by entry lengths [0]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
