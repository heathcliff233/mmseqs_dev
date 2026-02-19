## `renamedbkeys` {#refcmd-renamedbkeys}

Create a new DB with original keys renamed.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](#mod-database) |
| Category flags | `COMMAND_DB` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`clusterupdate`](#refcmd-clusterupdate), [`pickconsensusrep`](#refcmd-pickconsensusrep) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `update_clustering.sh` |

### Usage

`usage: mmseqs renamedbkeys <i:idMapFile|stdin> <i:DB> <o:DB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs renamedbkeys <i:idMapFile|stdin> <i:DB> <o:DB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:             
 --subdb-mode INT   Subdb mode 0: copy data 1: soft link data and write index [0]
common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-renamedbkeys), [command reference index](#sec-command-reference), and [functional module page](#mod-database).

