# `db2tar`

Archive contents of a DB to a tar archive.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](../submodules/database.md) |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Seen in workflow scripts | `n/a` |

## Usage

`usage: mmseqs db2tar <i:DB> <o:tar[.gz]> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs db2tar <i:DB> <o:tar[.gz]> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common: 
 -v INT   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Create a tar from a MSA DB
 mmseqs db2tar msaDB archive.tar.gz
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/database.md).

