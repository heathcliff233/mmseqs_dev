# `mergedbs`

Merge entries from multiple DBs.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](../submodules/database.md) |
| Category flags | `COMMAND_SET` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`rbh`](./rbh.md), [`search`](./search.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `enrich.sh`, `iterativepp.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `update_clustering.sh` |

## Usage

`usage: mmseqs mergedbs <i:DB> <o:DB> <i:DB1> ... <i:DBn> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--prefixes` | Comma separated list of prefixes for each entry |
| `--merge-stop-empty` | Don't continue merging entries after an empty entry |

## Full CLI Help Snapshot

```text
usage: mmseqs mergedbs <i:DB> <o:DB> <i:DB1> ... <i:DBn> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: common:                 
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                 
 --prefixes STR           Comma separated list of prefixes for each entry []
 --merge-stop-empty BOOL  Don't continue merging entries after an empty entry [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/database.md).

