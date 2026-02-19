# `concatdbs`

Concatenate two DBs, giving new IDs to entries from 2nd DB.

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
| Called by modules | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`linsearch`](./linsearch.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `linsearch.sh`, `nucleotide_clustering.sh`, `update_clustering.sh` |

## Usage

`usage: mmseqs concatdbs <i:DB> <i:DB> <o:DB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--preserve-keys` | The keys of the two DB should be distinct, and they will be preserved in the concatenation |
| `--take-larger-entry` | Only keep the larger entry (dataSize >) in the concatenation, both databases need the same keys in the index |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs concatdbs <i:DB> <i:DB> <o:DB> [options]
 By Clovis Galiez, Eli Levy Karin & Martin Steinegger (martin.steinegger@snu.ac.kr)
options: misc:                    
 --preserve-keys BOOL      The keys of the two DB should be distinct, and they will be preserved in the concatenation [0]
 --take-larger-entry BOOL  Only keep the larger entry (dataSize >) in the concatenation, both databases need the same keys in the index [0]
common:                  
 --compressed INT          Write compressed output [0]
 --threads INT             Number of CPU-cores used (all by default) [1]
 -v INT                    Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Download two sequences databases and concat them
 mmseqs databases PDB pdbDB tmp
 mmseqs UniProtKB/Swiss-Prot swissprotDB tmp
 # Works only single threaded since seq. and header DB need the same ordering
 mmseqs concatdbs pdbDB swissprotDB pdbAndSwissprotDB --threads 1
 mmseqs concatdbs pdbDB_h swissprotDB_h pdbAndSwissprotDB_h --threads 1
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/database.md).

