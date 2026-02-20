## `rescorediagonal` {#refcmd-rescorediagonal}

Compute sequence identity for diagonal.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`alignment`](#mod-alignment) |
| Category flags | `COMMAND_ALIGNMENT` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `5` |
| Downstream command count | `0` |
| Workflow script count | `4` |
| Detailed dependency entry | [Open in map](#depcmd-rescorediagonal) |

### Usage

`usage: mmseqs rescorediagonal <i:queryDB> <i:targetDB> <i:prefilterDB> <o:resultDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--wrapped-scoring` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `--cov-mode` | 0: coverage of query and target |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `--min-aln-len` | Minimum alignment length (range 0-INT_MAX) |
| `--seq-id-mode` | 0: alignment length 1: shorter, 2: longer sequence |
| `--rescore-mode` | Rescore diagonals with: |
| `--sub-mat` | Substitution matrix file |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |

### Full CLI Help Snapshot

```text
usage: mmseqs rescorediagonal <i:queryDB> <i:targetDB> <i:prefilterDB> <o:resultDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:              
 --add-self-matches BOOL  Artificially add entries of queries with themselves (for clustering) [0]
align:                  
 --wrapped-scoring BOOL   Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start [0]
 -e DOUBLE                List matches below this E-value (range 0.0-inf) [1.000E-03]
 -c FLOAT                 List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
 -a BOOL                  Add backtrace string (convert to alignments with mmseqs convertalis module) [0]
 --cov-mode INT           0: coverage of query and target
                          1: coverage of target
                          2: coverage of query
                          3: target seq. length has to be at least x% of query length
                          4: query seq. length has to be at least x% of target length
                          5: short seq. needs to be at least x% of the other seq. length [0]
 --min-seq-id FLOAT       List matches above this sequence identity (for clustering) (range 0.0-1.0) [0.000]
 --min-aln-len INT        Minimum alignment length (range 0-INT_MAX) [0]
 --seq-id-mode INT        0: alignment length 1: shorter, 2: longer sequence [0]
misc:                   
 --rescore-mode INT       Rescore diagonals with:
                          0: Hamming distance
                          1: local alignment (score only)
                          2: local alignment
                          3: global alignment
                          4: longest alignment fulfilling window quality criterion [0]
common:                 
 --sub-mat TWIN           Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --db-load-mode INT       Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT            Number of CPU-cores used (all by default) [10]
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                 
 --filter-hits BOOL       Filter hits by seq.id. and coverage [0]
 --sort-results INT       Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-rescorediagonal), [command reference index](#sec-command-reference), and [functional module page](#mod-alignment).

