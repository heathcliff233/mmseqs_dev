### `result2stats` {#refcmd-result2stats}

Compute statistics for each entry in a DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes. The current dependency map records 2 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream.

Dependency entry: [Open in map](#depcmd-result2stats); functional module: [`result_handling`](#mod-result-handling).

**Usage**

`usage: mmseqs result2stats <i:queryDB> <i:targetDB> <i:resultDB> <o:statsDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--stat` | One of: linecount, mean, min, max, doolittle, charges, seqlen, firstline |
| `--tsv` | Return output in TSV format |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs result2stats <i:queryDB> <i:targetDB> <i:resultDB> <o:statsDB> [options]
 By Clovis Galiez & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:             
 --stat STR         One of: linecount, mean, min, max, doolittle, charges, seqlen, firstline []
 --tsv BOOL         Return output in TSV format [0]
common:           
 --compressed INT   Write compressed output [0]
 --threads INT      Number of CPU-cores used (all by default) [10]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
