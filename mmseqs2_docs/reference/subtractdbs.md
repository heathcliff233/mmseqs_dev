### `subtractdbs` {#refcmd-subtractdbs}

Remove all entries from first DB occurring in second DB by key.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 2 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-subtractdbs); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs subtractdbs <i:resultDBLeft> <i:resultDBRight> <o:resultDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--e-profile` | Include sequences matches with < E-value thr. into the profile (>=0.0) |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs subtractdbs <i:resultDBLeft> <i:resultDBRight> <o:resultDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: align:            
 -e DOUBLE          List matches below this E-value (range 0.0-inf) [1.000E-03]
profile:          
 --e-profile DOUBLE Include sequences matches with < E-value thr. into the profile (>=0.0) [1.000E-03]
common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
