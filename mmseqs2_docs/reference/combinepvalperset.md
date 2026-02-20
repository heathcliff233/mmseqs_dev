### `combinepvalperset` {#refcmd-combinepvalperset}

For each set compute the combined p-value.

Execution role: high-level API command that exposes a complete task path over MMseqs2 databases.

This command family aggregates sequence-level hits into set-level statistics and decisions. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-combinepvalperset); functional module: [`multi_hit`](#mod-multi-hit).

**Usage**

`usage: mmseqs combinepvalperset <i:querySetDB> <i:targetSetDB> <i:resultDB> <o:pvalDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--alpha` | Set alpha for combining p-values during aggregation |
| `--aggregation-mode` | Combined P-values computed from 0: multi-hit, 1: minimum of all P-values, 2: product-of-P-values, 3: truncated product |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs combinepvalperset <i:querySetDB> <i:targetSetDB> <i:resultDB> <o:pvalDB> [options]
 By Ruoshi Zhang, Clovis Norroy & Milot Mirdita <milot@mirdita.de>
options: misc:                   
 --alpha FLOAT            Set alpha for combining p-values during aggregation [1.000]
 --aggregation-mode INT   Combined P-values computed from 0: multi-hit, 1: minimum of all P-values, 2: product-of-P-values, 3: truncated product [0]
common:                 
 --threads INT            Number of CPU-cores used (all by default) [10]
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
