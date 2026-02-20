## `mergeclusters` {#refcmd-mergeclusters}

Merge multiple cascaded clustering steps.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`clustering`](#mod-clustering) |
| Category flags | `COMMAND_CLUSTER` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Workflow script count | `4` |
| Detailed dependency entry | [Open in map](#depcmd-mergeclusters) |

### Usage

`usage: mmseqs mergeclusters <i:sequenceDB> <o:clusterDB> <i:clusterDB1> ... <i:clusterDBn> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

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
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-mergeclusters), [command reference index](#sec-command-reference), and [functional module page](#mod-clustering).

