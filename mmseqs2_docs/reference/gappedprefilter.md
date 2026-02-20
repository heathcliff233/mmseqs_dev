## `gappedprefilter` {#refcmd-gappedprefilter}

Optimal Smith-Waterman-based prefiltering (slow).

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`prefiltering`](#mod-prefiltering) |
| Category flags | `COMMAND_PREFILTER` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Workflow script count | `0` |
| Detailed dependency entry | [Open in map](#depcmd-gappedprefilter) |

### Usage

`usage: mmseqs gappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--min-ungapped-score` | Accept only matches with ungapped alignment score above threshold |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `--cov-mode` | 0: coverage of query and target |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |
| `--sub-mat` | Substitution matrix file |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |

### Full CLI Help Snapshot

```text
usage: mmseqs gappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]
 By Milot Mirdita <milot@mirdita.de> & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                  
 --comp-bias-corr INT         Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT Correct for locally biased amino acid composition (range 0-1) [1.000]
 --min-ungapped-score INT     Accept only matches with ungapped alignment score above threshold [15]
 --max-seqs INT               Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) [300]
align:                      
 --gap-open TWIN              Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN            Gap extension cost [aa:1,nucl:2]
 -e DOUBLE                    List matches below this E-value (range 0.0-inf) [1.000E-03]
 -c FLOAT                     List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
 --cov-mode INT               0: coverage of query and target
                              1: coverage of target
                              2: coverage of query
                              3: target seq. length has to be at least x% of query length
                              4: query seq. length has to be at least x% of target length
                              5: short seq. needs to be at least x% of the other seq. length [0]
misc:                       
 --taxon-list STR             Taxonomy ID, possibly multiple values separated by ',' []
common:                     
 --sub-mat TWIN               Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --db-load-mode INT           Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT                Number of CPU-cores used (all by default) [10]
 --compressed INT             Write compressed output [0]
 -v INT                       Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Kallenborn F, Chacon A, Hundt C, Sirelkhatim H, Didi K, Dallago C, Mirdita M, Schmidt B, Steinegger M: GPU-accelerated homology search with MMseqs2. bioRxiv, 2024.11.13.623350 (2024)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-gappedprefilter), [command reference index](#sec-command-reference), and [functional module page](#mod-prefiltering).

