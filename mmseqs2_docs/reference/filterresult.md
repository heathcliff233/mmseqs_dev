## `filterresult` {#refcmd-filterresult}

Pairwise alignment result filter.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](#mod-result-handling) |
| Category flags | `COMMAND_RESULT` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`search`](#refcmd-search) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `searchslicedtargetprofile.sh` |

### Usage

`usage: mmseqs filterresult <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]`

### Key Options

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

### Full CLI Help Snapshot

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
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-filterresult), [command reference index](#sec-command-reference), and [functional module page](#mod-result-handling).

