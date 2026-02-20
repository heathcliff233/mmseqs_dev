## `result2flat` {#refcmd-result2flat}

Create flat file by adding FASTA headers to DB entries.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](#mod-result-handling) |
| Category flags | `COMMAND_FORMAT_CONVERSION | COMMAND_EXPERT` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Workflow script count | `1` |
| Detailed dependency entry | [Open in map](#depcmd-result2flat) |

### Usage

`usage: mmseqs result2flat <i:queryDB> <i:targetDB> <i:resultDB> <o:fastaDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--use-fasta-header` | Use the id parsed from the fasta header as the index key instead of using incrementing numeric identifiers |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs result2flat <i:queryDB> <i:targetDB> <i:resultDB> <o:fastaDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                   
 --use-fasta-header BOOL  Use the id parsed from the fasta header as the index key instead of using incrementing numeric identifiers [0]
common:                 
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-result2flat), [command reference index](#sec-command-reference), and [functional module page](#mod-result-handling).

