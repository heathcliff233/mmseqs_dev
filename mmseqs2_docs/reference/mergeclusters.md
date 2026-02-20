### `mergeclusters` {#refcmd-mergeclusters}

Merge multiple cascaded clustering steps.

Execution role: core compute module typically called by workflows and advanced custom pipelines.

This command family controls graph construction and cluster assignment behavior, so early filter decisions strongly affect downstream structure. The current dependency map records 2 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when constructing, refining, or updating cluster assignments while preserving explicit coverage/identity criteria.

Dependency entry: [Open in map](#depcmd-mergeclusters); functional module: [`clustering`](#mod-clustering).

**Usage**

`usage: mmseqs mergeclusters <i:sequenceDB> <o:clusterDB> <i:clusterDB1> ... <i:clusterDBn> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs mergeclusters <i:sequenceDB> <o:clusterDB> <i:clusterDB1> ... <i:clusterDBn> [options]
 By Maria Hauser & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
