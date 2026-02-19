# `mvdb`

Move a DB.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](../submodules/database.md) |
| Category flags | `COMMAND_STORAGE` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md), [`tsv2exprofiledb`](./tsv2exprofiledb.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `blastp.sh`, `cascaded_clustering.sh`, `searchslicedtargetprofile.sh`, `taxonomy.sh`, `tsv2exprofiledb.sh`, `update_clustering.sh` |

## Usage

`usage: mmseqs mvdb <i:srcDB> <o:dstDB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs mvdb <i:srcDB> <o:dstDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: common: 
 -v INT   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/database.md).

