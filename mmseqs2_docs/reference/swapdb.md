# `swapdb`

Transpose DB with integer values in first column.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](../submodules/database.md) |
| Category flags | `COMMAND_DB` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`multihitdb`](./multihitdb.md), [`taxonomy`](./taxonomy.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `cascaded_clustering.sh`, `multihitdb.sh`, `taxpercontig.sh`, `update_clustering.sh` |

## Usage

`usage: mmseqs swapdb <i:resultDB> <o:resultDB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs swapdb <i:resultDB> <o:resultDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>, Clovis Galiez & Eli Levy Karin
options: prefilter:                
 --split-memory-limit BYTE  Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory [0]
common:                   
 --threads INT              Number of CPU-cores used (all by default) [10]
 --compressed INT           Write compressed output [0]
 -v INT                     Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/database.md).

