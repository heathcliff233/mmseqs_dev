### `msa2profile` {#refcmd-msa2profile}

Convert a MSA DB to a profile DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family preserves profile semantics across conversion and search steps. The current dependency map records 2 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-msa2profile); functional module: [`profiles`](#mod-profiles).

**Usage**

`usage: mmseqs msa2profile <i:msaDB> <o:profileDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--match-mode` | 0: Columns that have a residue in the first sequence are kept, 1: columns that have a residue in --match-ratio of all sequences are kept |
| `--match-ratio` | Columns that have a residue in this ratio of all sequences are kept |
| `--pseudo-cnt-mode` | use 0: substitution-matrix or 1: context-specific pseudocounts |
| `--pca` | Pseudo count admixture strength |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) |
| `--wg` | Use global sequence weighting for profile calculation |
| `--filter-msa` | Filter msa: 0: do not filter, 1: filter |
| `--filter-min-enable` | Only filter MSAs with more than N sequences, 0 always filters |

**Full CLI Help Snapshot**

```text
usage: mmseqs msa2profile <i:msaDB> <o:profileDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: prefilter:                  
 --comp-bias-corr INT         Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT Correct for locally biased amino acid composition (range 0-1) [1.000]
align:                      
 --gap-open TWIN              Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN            Gap extension cost [aa:1,nucl:2]
profile:                    
 --match-mode INT             0: Columns that have a residue in the first sequence are kept, 1: columns that have a residue in --match-ratio of all sequences are kept [0]
 --match-ratio FLOAT          Columns that have a residue in this ratio of all sequences are kept [0.500]
 --pseudo-cnt-mode INT        use 0: substitution-matrix or 1: context-specific pseudocounts [0]
 --pca                        Pseudo count admixture strength []
 --pcb                        Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) []
 --wg BOOL                    Use global sequence weighting for profile calculation [0]
 --filter-msa INT             Filter msa: 0: do not filter, 1: filter [1]
 --filter-min-enable INT      Only filter MSAs with more than N sequences, 0 always filters [0]
 --cov FLOAT                  Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] [0.000]
 --qid STR                    Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0]
                              Alternatively, can be a list of multiple thresholds:
                              E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] [0.0]
 --qsc FLOAT                  Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] [-20.000]
 --max-seq-id FLOAT           Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] [0.900]
 --diff INT                   Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 [1000]
misc:                       
 --msa-type INT               MSA Type: 0: cA3M, 1: A3M, 2: FASTA [2]
common:                     
 --sub-mat TWIN               Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --threads INT                Number of CPU-cores used (all by default) [10]
 --compressed INT             Write compressed output [0]
 -v INT                       Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                     
 --skip-query BOOL            Skip the query sequence [0]

examples:
 # Convert globally aligned MSAs to profiles
 # Defines columns as match columns if more than 50% of residues are not gaps
 # Non-match columns are discarded
 mmseqs msa2profile msaDB profileDB --match-mode 1 --match-ratio 0.5
 
 # Assign match-columns through the first sequence
 # Gaps in query sequence define non-match columns and are discarded
 mmseqs msa2profile msaDB profileDB --match-mode 0
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Mirdita M, Steinegger M, Soding J: MMseqs2 desktop and local web server app for fast, interactive sequence searches. Bioinformatics, 35(16), 2856-2858 (2019)
```
