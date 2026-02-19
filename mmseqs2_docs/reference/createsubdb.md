# `createsubdb`

Create a subset of a DB from list of DB keys.

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
| Called by modules | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`linclust`](./linclust.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `blastp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh`, `taxpercontig.sh`, `translated_search.sh`, `update_clustering.sh` |

## Usage

`usage: mmseqs createsubdb <i:subsetFile|DB> <i:DB> <o:DB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--id-mode` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs createsubdb <i:subsetFile|DB> <i:DB> <o:DB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:             
 --subdb-mode INT   Subdb mode 0: copy data 1: soft link data and write index [0]
 --id-mode INT      Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) [0]
common:           
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Create a new sequenceDB from sequenceDB entries with keys 1, 2 and 3
 mmseqs createsubdb <(printf '1
 2
 3
 ') sequenceDB oneTwoThreeDB
 
 # Create a new sequence database with representatives of clusterDB
 mmseqs cluster sequenceDB clusterDB tmp
 mmseqs createsubdb clusterDB sequenceDB representativesDB
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/database.md).

