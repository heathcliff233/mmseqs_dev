### `recoverlongestorf` {#refcmd-recoverlongestorf}

Recover longest ORF for taxonomy annotation after elimination.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family transforms sequence space before or after major compute stages. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-recoverlongestorf); functional module: [`sequence_manipulation`](#mod-sequence-manipulation).

**Usage**

`usage: mmseqs recoverlongestorf <i:orfDB> <i:resultDB> <o:tsvFile> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs recoverlongestorf <i:orfDB> <i:resultDB> <o:tsvFile> [options]
 By Sung-eun Jang
options: common:        
 --threads INT   Number of CPU-cores used (all by default) [10]
 -v INT          Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
