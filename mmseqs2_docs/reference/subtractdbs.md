## `subtractdbs` {#refcmd-subtractdbs}

Remove all entries from first DB occurring in second DB by key.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](#mod-database) |
| Category flags | `COMMAND_SET` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Workflow script count | `5` |
| Detailed dependency entry | [Open in map](#depcmd-subtractdbs) |

### Usage

`usage: mmseqs subtractdbs <i:resultDBLeft> <i:resultDBRight> <o:resultDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--e-profile` | Include sequences matches with < E-value thr. into the profile (>=0.0) |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

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
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-subtractdbs), [command reference index](#sec-command-reference), and [functional module page](#mod-database).

