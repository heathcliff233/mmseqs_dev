## `extractalignedregion` {#refcmd-extractalignedregion}

Extract aligned sequence region from query.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`sequence_manipulation`](#mod-sequence-manipulation) |
| Category flags | `COMMAND_SEQUENCE` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Workflow script count | `0` |
| Detailed dependency entry | [Open in map](#depcmd-extractalignedregion) |

### Usage

`usage: mmseqs extractalignedregion <i:queryDB> <i:targetDB> <i:resultDB> <o:sequenceDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--extract-mode` | Extract from 1: Query, 2: Target |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs extractalignedregion <i:queryDB> <i:targetDB> <i:resultDB> <o:sequenceDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:               
 --extract-mode INT   Extract from 1: Query, 2: Target [2]
common:             
 --compressed INT     Write compressed output [0]
 --db-load-mode INT   Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT        Number of CPU-cores used (all by default) [10]
 -v INT               Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-extractalignedregion), [command reference index](#sec-command-reference), and [functional module page](#mod-sequence-manipulation).

