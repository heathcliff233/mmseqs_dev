## `besthitperset` {#refcmd-besthitperset}

For each set of sequences compute the best element and update p-value.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `high_level_api` |
| Primary functional group | [`multi_hit`](#mod-multi-hit) |
| Category flags | `COMMAND_MULTIHIT` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`multihitsearch`](#refcmd-multihitsearch) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `multihitsearch.sh` |

### Usage

`usage: mmseqs besthitperset  <i:targetSetDB> <i:resultDB> <o:resultDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--simple-best-hit` | Update the p-value by a single best hit, or by best and second best hits |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs besthitperset  <i:targetSetDB> <i:resultDB> <o:resultDB> [options]
 By Ruoshi Zhang, Clovis Norroy & Milot Mirdita <milot@mirdita.de>
options: misc:                  
 --simple-best-hit BOOL  Update the p-value by a single best hit, or by best and second best hits [1]
common:                
 --threads INT           Number of CPU-cores used (all by default) [10]
 --compressed INT        Write compressed output [0]
 -v INT                  Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-besthitperset), [command reference index](#sec-command-reference), and [functional module page](#mod-multi-hit).

