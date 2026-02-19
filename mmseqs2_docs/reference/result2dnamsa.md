## `result2dnamsa` {#refcmd-result2dnamsa}

Compute MSA DB with out insertions in the query for DNA sequences.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](#mod-result-handling) |
| Category flags | `COMMAND_RESULT` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Seen in workflow scripts | `n/a` |

### Usage

`usage: mmseqs result2dnamsa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--skip-query` | Skip the query sequence |

### Full CLI Help Snapshot

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
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-result2dnamsa), [command reference index](#sec-command-reference), and [functional module page](#mod-result-handling).

