# `convertmsa`

Convert Stockholm/PFAM MSA file to a MSA DB.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`profiles`](../submodules/profiles.md) |
| Category flags | `COMMAND_DATABASE_CREATION` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`databases`](./databases.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `databases.sh` |

## Usage

`usage: mmseqs convertmsa <i:msaFile.sto[.gz]> <o:msaDB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--identifier-field` | Field from STOCKHOLM comments for choosing the MSA identifier: 0: ID, 1: AC. If the respective comment does not exist, the name of the first sequence will become the identifier |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs convertmsa <i:msaFile.sto[.gz]> <o:msaDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:                 
 --identifier-field INT   Field from STOCKHOLM comments for choosing the MSA identifier: 0: ID, 1: AC. If the respective comment does not exist, the name of the first sequence will become the identifier [1]
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Mirdita M, Steinegger M, Soding J: MMseqs2 desktop and local web server app for fast, interactive sequence searches. Bioinformatics, 35(16), 2856-2858 (2019)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/profiles.md).

