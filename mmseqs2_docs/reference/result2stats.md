## `result2stats` {#refcmd-result2stats}

Compute statistics for each entry in a DB.

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
| Called by modules | [`multihitdb`](#refcmd-multihitdb), [`search`](#refcmd-search) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `multihitdb.sh`, `searchslicedtargetprofile.sh` |

### Usage

`usage: mmseqs result2stats <i:queryDB> <i:targetDB> <i:resultDB> <o:statsDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--stat` | One of: linecount, mean, min, max, doolittle, charges, seqlen, firstline |
| `--tsv` | Return output in TSV format |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

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
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-result2stats), [command reference index](#sec-command-reference), and [functional module page](#mod-result-handling).

