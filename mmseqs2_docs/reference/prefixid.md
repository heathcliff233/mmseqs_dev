### `prefixid` {#refcmd-prefixid}

For each entry in a DB prepend the entry key to the entry itself.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family provides compositional utilities for custom pipelines, migration tasks, and diagnostics. The current dependency map records 3 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-prefixid); functional module: [`utilities`](#mod-utilities).

**Usage**

`usage: mmseqs prefixid <i:DB> <o:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--prefix` | Use this prefix for all entries |
| `--mapping-file` | Specify a file that translates the keys of a DB to new keys, TSV format |
| `--tsv` | Return output in TSV format |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs prefixid <i:DB> <o:DB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:               
 --prefix STR         Use this prefix for all entries []
 --mapping-file STR   Specify a file that translates the keys of a DB to new keys, TSV format []
 --tsv BOOL           Return output in TSV format [0]
common:             
 --threads INT        Number of CPU-cores used (all by default) [10]
 --compressed INT     Write compressed output [0]
 -v INT               Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
