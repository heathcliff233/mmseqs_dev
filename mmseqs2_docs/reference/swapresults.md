# `swapresults`

Transpose prefilter/alignment DB.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](../submodules/result_handling.md) |
| Category flags | `COMMAND_RESULT` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`easy-taxonomy`](./easy-taxonomy.md), [`linsearch`](./linsearch.md), [`rbh`](./rbh.md), [`search`](./search.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `easytaxonomy.sh`, `linsearch.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh` |

## Usage

`usage: mmseqs swapresults <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--sub-mat` | Substitution matrix file |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs swapresults <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>, Clovis Galiez & Eli Levy Karin
options: prefilter:                
 --split-memory-limit BYTE  Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory [0]
align:                    
 -e DOUBLE                  List matches below this E-value (range 0.0-inf) [1.000E-03]
 --gap-open TWIN            Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN          Gap extension cost [aa:1,nucl:2]
common:                   
 --sub-mat TWIN             Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --threads INT              Number of CPU-cores used (all by default) [10]
 --compressed INT           Write compressed output [0]
 --db-load-mode INT         Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 -v INT                     Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/result_handling.md).

