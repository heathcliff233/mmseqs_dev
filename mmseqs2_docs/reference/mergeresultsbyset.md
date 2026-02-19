# `mergeresultsbyset`

Merge results from multiple ORFs back to their respective contig.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `high_level_api` |
| Primary functional group | [`multi_hit`](../submodules/multi_hit.md) |
| Category flags | `COMMAND_MULTIHIT` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`multihitsearch`](./multihitsearch.md), [`taxonomy`](./taxonomy.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `multihitsearch.sh`, `taxpercontig.sh` |

## Usage

`usage: mmseqs mergeresultsbyset <i:setDB> <i:DB> <o:DB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs mergeresultsbyset <i:setDB> <i:DB> <o:DB> [options]
 By Ruoshi Zhang, Clovis Norroy & Milot Mirdita <milot@mirdita.de>
options: common:             
 --db-load-mode INT   Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT        Number of CPU-cores used (all by default) [10]
 --compressed INT     Write compressed output [0]
 -v INT               Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/multi_hit.md).

