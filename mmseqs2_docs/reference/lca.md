# `lca`

Compute the lowest common ancestor.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`taxonomy`](../submodules/taxonomy.md) |
| Category flags | `COMMAND_TAXONOMY` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`easy-taxonomy`](./easy-taxonomy.md), [`taxonomy`](./taxonomy.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `taxonomy.sh` |

## Usage

`usage: mmseqs lca <i:targetDB> <i:resultDB> <o:taxaDB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--lca-ranks` | Add column with specified ranks (',' separated) |
| `--blacklist` | Comma separated list of ignored taxa in LCA computation |
| `--tax-lineage` | 0: don't show, 1: add all lineage names, 2: add all lineage taxids |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs lca <i:targetDB> <i:resultDB> <o:taxaDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:              
 --lca-ranks STR     Add column with specified ranks (',' separated) []
 --blacklist STR     Comma separated list of ignored taxa in LCA computation [12908:unclassified sequences,28384:other sequences]
 --tax-lineage INT   0: don't show, 1: add all lineage names, 2: add all lineage taxids [0]
common:            
 --compressed INT    Write compressed output [0]
 --threads INT       Number of CPU-cores used (all by default) [10]
 -v INT              Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Mirdita M, Steinegger M, Breitwieser F, Soding J, Levy Karin E: Fast and sensitive taxonomic assignment to metagenomic contigs. Bioinformatics, btab184 (2021)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/taxonomy.md).

