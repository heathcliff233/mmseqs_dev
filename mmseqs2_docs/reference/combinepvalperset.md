## `combinepvalperset` {#refcmd-combinepvalperset}

For each set compute the combined p-value.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `high_level_api` |
| Primary functional group | [`multi_hit`](#mod-multi-hit) |
| Category flags | `COMMAND_MULTIHIT` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Workflow script count | `0` |
| Detailed dependency entry | [Open in map](#depcmd-combinepvalperset) |

### Usage

`usage: mmseqs combinepvalperset <i:querySetDB> <i:targetSetDB> <i:resultDB> <o:pvalDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--alpha` | Set alpha for combining p-values during aggregation |
| `--aggregation-mode` | Combined P-values computed from 0: multi-hit, 1: minimum of all P-values, 2: product-of-P-values, 3: truncated product |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs combinepvalperset <i:querySetDB> <i:targetSetDB> <i:resultDB> <o:pvalDB> [options]
 By Ruoshi Zhang, Clovis Norroy & Milot Mirdita <milot@mirdita.de>
options: misc:                   
 --alpha FLOAT            Set alpha for combining p-values during aggregation [1.000]
 --aggregation-mode INT   Combined P-values computed from 0: multi-hit, 1: minimum of all P-values, 2: product-of-P-values, 3: truncated product [0]
common:                 
 --threads INT            Number of CPU-cores used (all by default) [10]
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-combinepvalperset), [command reference index](#sec-command-reference), and [functional module page](#mod-multi-hit).

