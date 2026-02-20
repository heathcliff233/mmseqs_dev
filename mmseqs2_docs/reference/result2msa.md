### `result2msa` {#refcmd-result2msa}

Compute MSA DB from a result DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream.

Dependency entry: [Open in map](#depcmd-result2msa); functional module: [`result_handling`](#mod-result-handling).

**Usage**

`usage: mmseqs result2msa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--filter-msa` | Filter msa: 0: do not filter, 1: filter |
| `--filter-min-enable` | Only filter MSAs with more than N sequences, 0 always filters |
| `--max-seq-id` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] |
| `--qid` | Reduce diversity of output MSAs using min.seq. identity with query sequences |
| `--qsc` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] |
| `--cov` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] |
| `--diff` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 |
| `--allow-deletion` | Allow deletions in a MSA |

**Full CLI Help Snapshot**

```text
usage: mmseqs result2msa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]
 By Martin Steinegger (martin.steinegger@snu.ac.kr) & Milot Mirdita <milot@mirdita.de> & Clovis Galiez
options: prefilter:                  
 --comp-bias-corr INT         Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT Correct for locally biased amino acid composition (range 0-1) [1.000]
align:                      
 --gap-open TWIN              Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN            Gap extension cost [aa:1,nucl:2]
profile:                    
 --filter-msa INT             Filter msa: 0: do not filter, 1: filter [0]
 --filter-min-enable INT      Only filter MSAs with more than N sequences, 0 always filters [0]
 --max-seq-id FLOAT           Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] [0.900]
 --qid STR                    Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0]
                              Alternatively, can be a list of multiple thresholds:
                              E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] [0.0]
 --qsc FLOAT                  Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] [-20.000]
 --cov FLOAT                  Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] [0.000]
 --diff INT                   Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 [1000]
misc:                       
 --allow-deletion BOOL        Allow deletions in a MSA [0]
 --msa-format-mode INT        Format MSA as: 0: binary cA3M DB
                              1: binary ca3m w. consensus DB
                              2: aligned FASTA DB
                              3: aligned FASTA w. header summary
                              4: STOCKHOLM flat file
                              5: A3M format
                              6: A3M format w. alignment info [2]
common:                     
 --sub-mat TWIN               Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --db-load-mode INT           Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT                Number of CPU-cores used (all by default) [10]
 --compressed INT             Write compressed output [0]
 -v INT                       Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                     
 --summary-prefix STR         Set the cluster summary prefix [cl]
 --skip-query BOOL            Skip the query sequence [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
