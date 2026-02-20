### `clusthash` {#refcmd-clusthash}

Hash-based clustering of equal length sequences.

Execution role: core compute module typically called by workflows and advanced custom pipelines.

This command family controls graph construction and cluster assignment behavior, so early filter decisions strongly affect downstream structure. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when constructing, refining, or updating cluster assignments while preserving explicit coverage/identity criteria.

Dependency entry: [Open in map](#depcmd-clusthash); functional module: [`clustering`](#mod-clustering).

**Usage**

`usage: mmseqs clusthash <i:sequenceDB> <o:alignmentDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--alph-size` | Alphabet size (range 2-21) |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `--sub-mat` | Substitution matrix file |
| `--max-seq-len` | Maximum sequence length |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs clusthash <i:sequenceDB> <o:alignmentDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr> 
options: prefilter:          
 --alph-size TWIN     Alphabet size (range 2-21) [aa:3,nucl:5]
align:              
 --min-seq-id FLOAT   List matches above this sequence identity (for clustering) (range 0.0-1.0) [0.990]
common:             
 --sub-mat TWIN       Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --max-seq-len INT    Maximum sequence length [65535]
 --db-load-mode INT   Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT        Number of CPU-cores used (all by default) [10]
 --compressed INT     Write compressed output [0]
 -v INT               Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
