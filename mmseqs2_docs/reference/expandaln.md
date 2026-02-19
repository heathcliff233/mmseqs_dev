# `expandaln`

Expand an alignment result based on another.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`alignment`](../submodules/alignment.md) |
| Category flags | `COMMAND_PROFILE_PROFILE` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`search`](./search.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `enrich.sh`, `iterativepp.sh` |

## Usage

`usage: mmseqs expandaln <i:queryDB> <i:targetDB> <i:resultDB> <i:resultDB|ca3mDB> <o:alignmentDB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--score-bias` | Score bias when computing SW alignment (in bits) |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `--cov-mode` | 0: coverage of query and target |
| `--pseudo-cnt-mode` | use 0: substitution-matrix or 1: context-specific pseudocounts |
| `--pca` | Pseudo count admixture strength |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) |

## Full CLI Help Snapshot

```text
usage: mmseqs expandaln <i:queryDB> <i:targetDB> <i:resultDB> <i:resultDB|ca3mDB> <o:alignmentDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: prefilter:                    
 --comp-bias-corr INT           Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT   Correct for locally biased amino acid composition (range 0-1) [1.000]
align:                        
 --gap-open TWIN                Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN              Gap extension cost [aa:1,nucl:2]
 --score-bias FLOAT             Score bias when computing SW alignment (in bits) [0.000]
 -e DOUBLE                      List matches below this E-value (range 0.0-inf) [1.000E-03]
 --min-seq-id FLOAT             List matches above this sequence identity (for clustering) (range 0.0-1.0) [0.000]
 -c FLOAT                       List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
 --cov-mode INT                 0: coverage of query and target
                                1: coverage of target
                                2: coverage of query
                                3: target seq. length has to be at least x% of query length
                                4: query seq. length has to be at least x% of target length
                                5: short seq. needs to be at least x% of the other seq. length [0]
profile:                      
 --pseudo-cnt-mode INT          use 0: substitution-matrix or 1: context-specific pseudocounts [0]
 --pca                          Pseudo count admixture strength []
 --pcb                          Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) []
 --filter-min-enable INT        Only filter MSAs with more than N sequences, 0 always filters [0]
 --max-seq-id FLOAT             Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] [0.900]
 --qid STR                      Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0]
                                Alternatively, can be a list of multiple thresholds:
                                E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] [0.0]
 --qsc FLOAT                    Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] [-20.000]
 --cov FLOAT                    Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] [0.000]
 --diff INT                     Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 [1000]
misc:                         
 --expansion-mode INT           Update score, E-value, and sequence identity by 0: input alignment 1: rescoring the inferred backtrace [0]
 --expand-filter-clusters INT   Filter each target cluster during expansion 0: no filter 1: filter [0]
common:                       
 --sub-mat TWIN                 Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --max-seq-len INT              Maximum sequence length [65535]
 --db-load-mode INT             Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --compressed INT               Write compressed output [0]
 --threads INT                  Number of CPU-cores used (all by default) [10]
 -v INT                         Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/alignment.md).

