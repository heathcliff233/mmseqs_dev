# `result2repseq`

Get representative sequences from result DB.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](../submodules/result_handling.md) |
| Category flags | `COMMAND_RESULT` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`clusterupdate`](./clusterupdate.md), [`easy-cluster`](./easy-cluster.md), [`easy-linclust`](./easy-linclust.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `easycluster.sh`, `update_clustering.sh` |

## Usage

`usage: mmseqs result2repseq <i:sequenceDB> <i:resultDB> <o:sequenceDb> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs result2repseq <i:sequenceDB> <i:resultDB> <o:sequenceDb> [options]
 By Milot Mirdita <milot@mirdita.de> & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: common:             
 --db-load-mode INT   Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --compressed INT     Write compressed output [0]
 --threads INT        Number of CPU-cores used (all by default) [10]
 -v INT               Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/result_handling.md).

