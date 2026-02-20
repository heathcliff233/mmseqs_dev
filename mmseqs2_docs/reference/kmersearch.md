## `kmersearch` {#refcmd-kmersearch}

Find bottom-m-hashed k-mer matches between target and query DB.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`prefiltering`](#mod-prefiltering) |
| Category flags | `COMMAND_PREFILTER` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Workflow script count | `1` |
| Detailed dependency entry | [Open in map](#depcmd-kmersearch) |

### Usage

`usage: mmseqs kmersearch <i:queryDB> <i:kmerIndexDB> <o:prefilterDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--cov-mode` | 0: coverage of query and target |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `--kmer-per-seq` | k-mers per sequence |
| `--kmer-per-seq-scale` | Scale k-mer per sequence based on sequence length as kmer-per-seq val + scale x seqlen |
| `--pick-n-sim-kmer` | Add N similar k-mers to search |
| `--result-direction` | result is 0: query, 1: target centric |

### Full CLI Help Snapshot

```text
usage: mmseqs kmersearch <i:queryDB> <i:kmerIndexDB> <o:prefilterDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                
 --seed-sub-mat TWIN        Substitution matrix file for k-mer generation [aa:VTML80.out,nucl:nucleotide.out]
 --mask INT                 Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking [0]
 --mask-prob FLOAT          Mask sequences is probablity is above threshold [0.900]
 --mask-lower-case INT      Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region [0]
 --mask-n-repeat INT        Repeat letters that occure > threshold in a rwo [0]
 --split-memory-limit BYTE  Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory [0]
align:                    
 --cov-mode INT             0: coverage of query and target
                            1: coverage of target
                            2: coverage of query
                            3: target seq. length has to be at least x% of query length
                            4: query seq. length has to be at least x% of target length
                            5: short seq. needs to be at least x% of the other seq. length [0]
 -c FLOAT                   List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.800]
kmermatcher:              
 --kmer-per-seq INT         k-mers per sequence [0]
 --kmer-per-seq-scale TWIN  Scale k-mer per sequence based on sequence length as kmer-per-seq val + scale x seqlen [aa:0.000,nucl:0.200]
 --pick-n-sim-kmer INT      Add N similar k-mers to search [1]
 --result-direction INT     result is 0: query, 1: target centric [1]
common:                   
 --max-seq-len INT          Maximum sequence length [65535]
 --threads INT              Number of CPU-cores used (all by default) [10]
 --compressed INT           Write compressed output [0]
 -v INT                     Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-kmersearch), [command reference index](#sec-command-reference), and [functional module page](#mod-prefiltering).

