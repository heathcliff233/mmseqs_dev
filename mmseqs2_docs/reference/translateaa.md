### `translateaa` {#refcmd-translateaa}

Translate proteins to lexicographically lowest codons.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family transforms sequence space before or after major compute stages. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-translateaa); functional module: [`sequence_manipulation`](#mod-sequence-manipulation).

**Usage**

`usage: mmseqs translateaa <i:sequenceDB> <o:sequenceDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs translateaa <i:sequenceDB> <o:sequenceDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
