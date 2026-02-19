## `alignall` {#refcmd-alignall}

Within-result all-vs-all gapped local alignment.

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

`usage: mmseqs alignall <i:sequenceDB> <i:resultDB> <o:alignmentDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `--alignment-mode` | How to compute the alignment: |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `--min-aln-len` | Minimum alignment length (range 0-INT_MAX) |
| `--seq-id-mode` | 0: alignment length 1: shorter, 2: longer sequence |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `--cov-mode` | 0: coverage of query and target |
| `--score-bias` | Score bias when computing SW alignment (in bits) |

### Full CLI Help Snapshot

```text
usage: mmseqs alignall <i:sequenceDB> <i:resultDB> <o:alignmentDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                  
 --comp-bias-corr INT         Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT Correct for locally biased amino acid composition (range 0-1) [1.000]
 --add-self-matches BOOL      Artificially add entries of queries with themselves (for clustering) [0]
align:                      
 -a BOOL                      Add backtrace string (convert to alignments with mmseqs convertalis module) [0]
 --alignment-mode INT         How to compute the alignment:
                              0: automatic
                              1: only score and end_pos
                              2: also start_pos and cov
                              3: also seq.id [0]
 -e DOUBLE                    List matches below this E-value (range 0.0-inf) [1.000E-03]
 --min-seq-id FLOAT           List matches above this sequence identity (for clustering) (range 0.0-1.0) [0.000]
 --min-aln-len INT            Minimum alignment length (range 0-INT_MAX) [0]
 --seq-id-mode INT            0: alignment length 1: shorter, 2: longer sequence [0]
 -c FLOAT                     List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
 --cov-mode INT               0: coverage of query and target
                              1: coverage of target
                              2: coverage of query
                              3: target seq. length has to be at least x% of query length
                              4: query seq. length has to be at least x% of target length
                              5: short seq. needs to be at least x% of the other seq. length [0]
 --score-bias FLOAT           Score bias when computing SW alignment (in bits) [0.000]
 --gap-open TWIN              Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN            Gap extension cost [aa:1,nucl:2]
 --zdrop INT                  Maximal allowed difference between score values before alignment is truncated  (nucleotide alignment only) [40]
profile:                    
 --pca                        Pseudo count admixture strength []
 --pcb                        Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) []
common:                     
 --sub-mat TWIN               Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --max-seq-len INT            Maximum sequence length [65535]
 --db-load-mode INT           Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT                Number of CPU-cores used (all by default) [10]
 --compressed INT             Write compressed output [0]
 -v INT                       Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-alignall), [command reference index](#sec-command-reference), and [functional module page](#mod-alignment).

