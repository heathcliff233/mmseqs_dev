## `aliasdb` {#refcmd-aliasdb}

Create relative symlink of DB to another name in the same folder.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](#mod-database) |
| Category flags | `COMMAND_STORAGE` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Workflow script count | `1` |
| Detailed dependency entry | [Open in map](#depcmd-aliasdb) |

### Usage

`usage: mmseqs aliasdb <i:srcDB> <o:dstDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs aliasdb <i:srcDB> <o:dstDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common: 
 -v INT   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-aliasdb), [command reference index](#sec-command-reference), and [functional module page](#mod-database).

