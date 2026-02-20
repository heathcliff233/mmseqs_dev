### `ungappedprefilter` {#refcmd-ungappedprefilter}

Optimal diagonal score search.

Execution role: core compute module typically called by workflows and advanced custom pipelines.

This command family is the main acceleration gate that prunes candidate pairs before expensive alignment. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command in custom pipelines that must expose candidate-generation behavior before alignment stages.

Dependency entry: [Open in map](#depcmd-ungappedprefilter); functional module: [`prefiltering`](#mod-prefiltering).

**Usage**

`usage: mmseqs ungappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--min-ungapped-score` | Accept only matches with ungapped alignment score above threshold |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--cov-mode` | 0: coverage of query and target |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |
| `--prefilter-mode` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped |
| `--sub-mat` | Substitution matrix file |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--gpu` | Use GPU (CUDA) if possible |

**Full CLI Help Snapshot**

```text
usage: mmseqs ungappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]
 By Milot Mirdita <milot@mirdita.de> & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                     
 --comp-bias-corr INT            Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT    Correct for locally biased amino acid composition (range 0-1) [1.000]
 --min-ungapped-score INT        Accept only matches with ungapped alignment score above threshold [15]
 --max-seqs INT                  Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) [300]
align:                         
 -c FLOAT                        List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
 -e DOUBLE                       List matches below this E-value (range 0.0-inf) [1.000E-03]
 --cov-mode INT                  0: coverage of query and target
                                 1: coverage of target
                                 2: coverage of query
                                 3: target seq. length has to be at least x% of query length
                                 4: query seq. length has to be at least x% of target length
                                 5: short seq. needs to be at least x% of the other seq. length [0]
misc:                          
 --taxon-list STR                Taxonomy ID, possibly multiple values separated by ',' []
 --prefilter-mode INT            prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped [0]
common:                        
 --sub-mat TWIN                  Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --db-load-mode INT              Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --gpu INT                       Use GPU (CUDA) if possible [0]
 --gpu-server INT                Use GPU server [0]
 --gpu-server-wait-timeout INT   Wait for GPU server for 0: don't wait -1: no wait limit: >0 this many seconds [600]
 --threads INT                   Number of CPU-cores used (all by default) [10]
 --compressed INT                Write compressed output [0]
 -v INT                          Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Kallenborn F, Chacon A, Hundt C, Sirelkhatim H, Didi K, Dallago C, Mirdita M, Schmidt B, Steinegger M: GPU-accelerated homology search with MMseqs2. bioRxiv, 2024.11.13.623350 (2024)
```
