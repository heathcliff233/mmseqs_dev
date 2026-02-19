## `tsv2exprofiledb` {#refcmd-tsv2exprofiledb}

Create a expandable profile db from TSV files.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`profiles`](#mod-profiles) |
| Category flags | `COMMAND_PROFILE_PROFILE` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | `n/a` |
| Calls modules | [`aliasdb`](#refcmd-aliasdb), [`compress`](#refcmd-compress), [`mvdb`](#refcmd-mvdb), [`rmdb`](#refcmd-rmdb), [`tsv2db`](#refcmd-tsv2db) |
| Seen in workflow scripts | `n/a` |

### Usage

`usage: mmseqs tsv2exprofiledb <i:tsvFilesBase> <o:exprofileDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--gpu` | Use GPU (CUDA) if possible |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs tsv2exprofiledb <i:tsvFilesBase> <o:exprofileDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:           
 --gpu INT          Use GPU (CUDA) if possible [0]
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [1]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-tsv2exprofiledb), [command reference index](#sec-command-reference), and [functional module page](#mod-profiles).

