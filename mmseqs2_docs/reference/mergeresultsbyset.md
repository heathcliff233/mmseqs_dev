### `mergeresultsbyset` {#refcmd-mergeresultsbyset}

Merge results from multiple ORFs back to their respective contig.

Execution role: high-level API command that exposes a complete task path over MMseqs2 databases.

This command family aggregates sequence-level hits into set-level statistics and decisions. The current dependency map records 2 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-mergeresultsbyset); functional module: [`multi_hit`](#mod-multi-hit).

**Usage**

`usage: mmseqs mergeresultsbyset <i:setDB> <i:DB> <o:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs mergeresultsbyset <i:setDB> <i:DB> <o:DB> [options]
 By Ruoshi Zhang, Clovis Norroy & Milot Mirdita <milot@mirdita.de>
options: common:             
 --db-load-mode INT   Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT        Number of CPU-cores used (all by default) [10]
 --compressed INT     Write compressed output [0]
 -v INT               Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
