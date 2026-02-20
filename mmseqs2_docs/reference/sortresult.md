### `sortresult` {#refcmd-sortresult}

Sort a result DB in the same order as the prefilter or align module.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream.

Dependency entry: [Open in map](#depcmd-sortresult); functional module: [`result_handling`](#mod-result-handling).

**Usage**

`usage: mmseqs sortresult <i:resultbDB> <o:resultDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs sortresult <i:resultbDB> <o:resultDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:           
 --compressed INT   Write compressed output [0]
 --threads INT      Number of CPU-cores used (all by default) [10]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
