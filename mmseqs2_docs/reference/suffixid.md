## `suffixid` {#refcmd-suffixid}

For each entry in a DB append the entry key to the entry itself.

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
| Detailed dependency entry | [Open in map](#depcmd-suffixid) |

### Usage

`usage: mmseqs suffixid <i:resultDB> <o:resultDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--prefix` | Use this prefix for all entries |
| `--mapping-file` | Specify a file that translates the keys of a DB to new keys, TSV format |
| `--tsv` | Return output in TSV format |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs suffixid <i:resultDB> <o:resultDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:               
 --prefix STR         Use this prefix for all entries []
 --mapping-file STR   Specify a file that translates the keys of a DB to new keys, TSV format []
 --tsv BOOL           Return output in TSV format [0]
common:             
 --threads INT        Number of CPU-cores used (all by default) [10]
 --compressed INT     Write compressed output [0]
 -v INT               Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-suffixid), [command reference index](#sec-command-reference), and [functional module page](#mod-utilities).

