## `prefilter` {#refcmd-prefilter}

Double consecutive diagonal k-mer search.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`prefiltering`](#mod-prefiltering) |
| Category flags | `COMMAND_PREFILTER` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `3` |
| Downstream command count | `0` |
| Workflow script count | `11` |
| Detailed dependency entry | [Open in map](#depcmd-prefilter) |

### Usage

`usage: mmseqs prefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `-s` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive |
| `-k` | k-mer length (0: automatically set to optimum) |
| `--target-search-mode` | target search mode (0: regular k-mer, 1: similar k-mer) |
| `--k-score` | k-mer threshold for generating similar k-mer lists |
| `--alph-size` | Alphabet size (range 2-21) |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--split` | Split input into N equally distributed chunks. 0: set the best split automatically |
| `--split-mode` | 0: split target db; 1: split query db; 2: auto, depending on main memory |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |

### Full CLI Help Snapshot

```text
usage: mmseqs prefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr> & Maria Hauser
options: prefilter:                  
 --seed-sub-mat TWIN          Substitution matrix file for k-mer generation [aa:VTML80.out,nucl:nucleotide.out]
 -s FLOAT                     Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive [4.000]
 -k INT                       k-mer length (0: automatically set to optimum) [0]
 --target-search-mode INT     target search mode (0: regular k-mer, 1: similar k-mer) [0]
 --k-score TWIN               k-mer threshold for generating similar k-mer lists [seq:2147483647,prof:2147483647]
 --alph-size TWIN             Alphabet size (range 2-21) [aa:21,nucl:5]
 --max-seqs INT               Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) [300]
 --split INT                  Split input into N equally distributed chunks. 0: set the best split automatically [0]
 --split-mode INT             0: split target db; 1: split query db; 2: auto, depending on main memory [2]
 --split-memory-limit BYTE    Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory [0]
 --comp-bias-corr INT         Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT Correct for locally biased amino acid composition (range 0-1) [1.000]
 --diag-score BOOL            Use ungapped diagonal scoring during prefilter [1]
 --exact-kmer-matching INT    Extract only exact k-mers for matching (range 0-1) [0]
 --mask INT                   Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking [1]
 --mask-prob FLOAT            Mask sequences is probablity is above threshold [0.900]
 --mask-lower-case INT        Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region [0]
 --mask-n-repeat INT          Repeat letters that occure > threshold in a rwo [0]
 --min-ungapped-score INT     Accept only matches with ungapped alignment score above threshold [15]
 --add-self-matches BOOL      Artificially add entries of queries with themselves (for clustering) [0]
 --spaced-kmer-mode INT       0: use consecutive positions in k-mers; 1: use spaced k-mers [1]
 --spaced-kmer-pattern STR    User-specified spaced k-mer pattern []
 --local-tmp STR              Path where some of the temporary files will be created []
align:                      
 -c FLOAT                     List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
 --cov-mode INT               0: coverage of query and target
                              1: coverage of target
                              2: coverage of query
                              3: target seq. length has to be at least x% of query length
                              4: query seq. length has to be at least x% of target length
                              5: short seq. needs to be at least x% of the other seq. length [0]
profile:                    
 --pca                        Pseudo count admixture strength []
 --pcb                        Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) []
misc:                       
 --taxon-list STR             Taxonomy ID, possibly multiple values separated by ',' []
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

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-prefilter), [command reference index](#sec-command-reference), and [functional module page](#mod-prefiltering).

