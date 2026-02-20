### `filterresult` {#refcmd-filterresult}

Pairwise alignment result filter.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream.

Dependency entry: [Open in map](#depcmd-filterresult); functional module: [`result_handling`](#mod-result-handling).

**Usage**

`usage: mmseqs filterresult <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | keep the query (representative) sequence |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--filter-min-enable` | Only filter MSAs with more than N sequences, 0 always filters |
| `--max-seq-id` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] |
| `--qid` | Reduce diversity of output MSAs using min.seq. identity with query sequences |
| `--qsc` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] |
| `--cov` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] |
| `--diff` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 |
| `--allow-deletion` | Allow deletions in a MSA |

**Full CLI Help Snapshot**

```text
usage: mmseqs filterresult <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: prefilter:                  
 --comp-bias-corr INT         Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT Correct for locally biased amino acid composition (range 0-1) [1.000]
 --add-self-matches BOOL      keep the query (representative) sequence [0]
align:                      
 --gap-open TWIN              Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN            Gap extension cost [aa:1,nucl:2]
profile:                    
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
common:                     
 --sub-mat TWIN               Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --db-load-mode INT           Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT                Number of CPU-cores used (all by default) [10]
 --compressed INT             Write compressed output [0]
 -v INT                       Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
