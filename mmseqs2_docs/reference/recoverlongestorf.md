# `recoverlongestorf`

Recover longest ORF for taxonomy annotation after elimination.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`sequence_manipulation`](../submodules/sequence_manipulation.md) |
| Category flags | `COMMAND_EXPERT` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`taxonomy`](./taxonomy.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `taxpercontig.sh` |

## Usage

`usage: mmseqs recoverlongestorf <i:orfDB> <i:resultDB> <o:tsvFile> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs recoverlongestorf <i:orfDB> <i:resultDB> <o:tsvFile> [options]
 By Sung-eun Jang
options: common:        
 --threads INT   Number of CPU-cores used (all by default) [10]
 -v INT          Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/sequence_manipulation.md).

