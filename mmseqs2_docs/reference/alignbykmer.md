## `alignbykmer` {#refcmd-alignbykmer}

Heuristic gapped local k-mer based alignment.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`alignment`](#mod-alignment) |
| Category flags | `COMMAND_ALIGNMENT` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Seen in workflow scripts | `n/a` |

### Usage

`usage: mmseqs alignbykmer <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `-k` | k-mer length (0: automatically set to optimum) |
| `--spaced-kmer-mode` | 0: use consecutive positions in k-mers; 1: use spaced k-mers |
| `--spaced-kmer-pattern` | User-specified spaced k-mer pattern |
| `--alph-size` | Alphabet size (range 2-21) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--cov-mode` | 0: coverage of query and target |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `--min-aln-len` | Minimum alignment length (range 0-INT_MAX) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |

### Full CLI Help Snapshot

```text
Rescore diagonals.
usage: mmseqs alignbykmer <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                 
 -k INT                      k-mer length (0: automatically set to optimum) [0]
 --spaced-kmer-mode INT      0: use consecutive positions in k-mers; 1: use spaced k-mers [1]
 --spaced-kmer-pattern STR   User-specified spaced k-mer pattern []
 --alph-size TWIN            Alphabet size (range 2-21) [aa:21,nucl:5]
 --add-self-matches BOOL     Artificially add entries of queries with themselves (for clustering) [0]
align:                     
 -c FLOAT                    List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
 -e DOUBLE                   List matches below this E-value (range 0.0-inf) [1.000E-03]
 --cov-mode INT              0: coverage of query and target
                             1: coverage of target
                             2: coverage of query
                             3: target seq. length has to be at least x% of query length
                             4: query seq. length has to be at least x% of target length
                             5: short seq. needs to be at least x% of the other seq. length [0]
 --min-seq-id FLOAT          List matches above this sequence identity (for clustering) (range 0.0-1.0) [0.000]
 --min-aln-len INT           Minimum alignment length (range 0-INT_MAX) [0]
 --gap-open TWIN             Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN           Gap extension cost [aa:1,nucl:2]
common:                    
 --sub-mat TWIN              Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --threads INT               Number of CPU-cores used (all by default) [10]
 --compressed INT            Write compressed output [0]
 -v INT                      Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                    
 --filter-hits BOOL          Filter hits by seq.id. and coverage [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-alignbykmer), [command reference index](#sec-command-reference), and [functional module page](#mod-alignment).

