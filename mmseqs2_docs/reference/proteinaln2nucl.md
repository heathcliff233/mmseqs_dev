## `proteinaln2nucl` {#refcmd-proteinaln2nucl}

Transform protein alignments to nucleotide alignments.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`alignment`](#mod-alignment) |
| Category flags | `COMMAND_RESULT` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Workflow script count | `0` |
| Detailed dependency entry | [Open in map](#depcmd-proteinaln2nucl) |

### Usage

`usage: mmseqs proteinaln2nucl <i:nuclQueryDB> <i:nuclTargetDB> <i:aaQueryDB> <i:aaTargetDB> <i:alnDB> <o:alnDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--sub-mat` | Substitution matrix file |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs proteinaln2nucl <i:nuclQueryDB> <i:nuclTargetDB> <i:aaQueryDB> <i:aaTargetDB> <i:alnDB> <o:alnDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr> 
options: align:            
 --gap-open TWIN    Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN  Gap extension cost [aa:1,nucl:2]
common:           
 --sub-mat TWIN     Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-proteinaln2nucl), [command reference index](#sec-command-reference), and [functional module page](#mod-alignment).

