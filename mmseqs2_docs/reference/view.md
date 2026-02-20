## `view` {#refcmd-view}

Print DB entries given in --id-list to stdout.

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
| Detailed dependency entry | [Open in map](#depcmd-view) |

### Usage

`usage: mmseqs view <i:DB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--id-list` | Entries to be printed separated by ',' |
| `--id-mode` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) |
| `--idx-entry-type` | 0: sequence, 1: src sequence, 2: header, 3: src header |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs view <i:DB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                 
 --id-list STR          Entries to be printed separated by ',' []
 --id-mode INT          Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) [0]
 --idx-entry-type INT   0: sequence, 1: src sequence, 2: header, 3: src header [0]
common:               
 -v INT                 Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Print entries with keys 1, 2 and 3 from a sequence DB to stdout
 mmseqs view sequenecDB --id-list 1,2,3
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-view), [command reference index](#sec-command-reference), and [functional module page](#mod-utilities).

