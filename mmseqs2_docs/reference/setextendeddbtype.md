## `setextendeddbtype` {#refcmd-setextendeddbtype}

Write an extended DB.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`utilities`](#mod-utilities) |
| Category flags | `COMMAND_DB` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Workflow script count | `0` |
| Detailed dependency entry | [Open in map](#depcmd-setextendeddbtype) |

### Usage

`usage: mmseqs setextendeddbtype <i:DB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--extended-dbtype` | Set extended dbtype 1: compressed, 2: need src, 4: context pseudoe cnts |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs setextendeddbtype <i:DB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                  
 --extended-dbtype INT   Set extended dbtype 1: compressed, 2: need src, 4: context pseudoe cnts [0]
common:                
 -v INT                  Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Print entries with keys 1, 2 and 3 from a sequence DB to stdout
 mmseqs setextendedbtype db --extended-dbtype 2
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-setextendeddbtype), [command reference index](#sec-command-reference), and [functional module page](#mod-utilities).

