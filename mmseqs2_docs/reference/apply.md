# `apply`

Execute given program on each DB entry.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`utilities`](../submodules/utilities.md) |
| Category flags | `COMMAND_DB` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Seen in workflow scripts | `n/a` |

## Usage

`usage: mmseqs apply <i:DB> <o:DB> -- program [args...] [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## Full CLI Help Snapshot

```text
usage: mmseqs apply <i:DB> <o:DB> -- program [args...] [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Gather all sequences from a cluster DB
 mmseqs createseqfiledb sequenceDB clusterDB unalignedDB --min-sequences 2
 # Build MSAs with Clustal-Omega
 mmseqs apply unalignedDB msaDB -- clustalo -i - -o stdout --threads=1
 
 # Count lines in each DB entry inefficiently (result2stats is way faster)
 mmseqs apply DB wcDB -- awk '{ counter++; } END { print counter; }'
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/utilities.md).

