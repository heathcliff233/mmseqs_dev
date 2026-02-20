### `besthitperset` {#refcmd-besthitperset}

For each set of sequences compute the best element and update p-value.

Execution role: high-level API command that exposes a complete task path over MMseqs2 databases.

This command family aggregates sequence-level hits into set-level statistics and decisions. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-besthitperset); functional module: [`multi_hit`](#mod-multi-hit).

**Usage**

`usage: mmseqs besthitperset  <i:targetSetDB> <i:resultDB> <o:resultDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--simple-best-hit` | Update the p-value by a single best hit, or by best and second best hits |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs besthitperset  <i:targetSetDB> <i:resultDB> <o:resultDB> [options]
 By Ruoshi Zhang, Clovis Norroy & Milot Mirdita <milot@mirdita.de>
options: misc:                  
 --simple-best-hit BOOL  Update the p-value by a single best hit, or by best and second best hits [1]
common:                
 --threads INT           Number of CPU-cores used (all by default) [10]
 --compressed INT        Write compressed output [0]
 -v INT                  Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
