### `result2dnamsa` {#refcmd-result2dnamsa}

Compute MSA DB with out insertions in the query for DNA sequences.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream.

Dependency entry: [Open in map](#depcmd-result2dnamsa); functional module: [`result_handling`](#mod-result-handling).

**Usage**

`usage: mmseqs result2dnamsa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--skip-query` | Skip the query sequence |

**Full CLI Help Snapshot**

```text
usage: mmseqs result2dnamsa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]
 By Martin Steinegger (martin.steinegger@snu.ac.kr)
options: common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:           
 --skip-query BOOL  Skip the query sequence [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
