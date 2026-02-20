### `proteinaln2nucl` {#refcmd-proteinaln2nucl}

Transform protein alignments to nucleotide alignments.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family computes pair quality and coordinates and usually dominates per-pair compute cost after prefiltering. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-proteinaln2nucl); functional module: [`alignment`](#mod-alignment).

**Usage**

`usage: mmseqs proteinaln2nucl <i:nuclQueryDB> <i:nuclTargetDB> <i:aaQueryDB> <i:aaTargetDB> <i:alnDB> <o:alnDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--sub-mat` | Substitution matrix file |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

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
