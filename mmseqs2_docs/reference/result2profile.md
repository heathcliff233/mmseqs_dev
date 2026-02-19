# `result2profile`

Compute profile DB from a result DB.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`profiles`](../submodules/profiles.md) |
| Category flags | `COMMAND_PROFILE` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`search`](./search.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `blastpgp.sh`, `enrich.sh` |

## Usage

`usage: mmseqs result2profile <i:queryDB> <i:targetDB> <i:resultDB> <o:profileDB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--mask-profile` | Mask query sequence of profile using tantan [0,1] |
| `--e-profile` | Include sequences matches with < E-value thr. into the profile (>=0.0) |
| `--wg` | Use global sequence weighting for profile calculation |
| `--filter-msa` | Filter msa: 0: do not filter, 1: filter |
| `--filter-min-enable` | Only filter MSAs with more than N sequences, 0 always filters |
| `--max-seq-id` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] |
| `--qid` | Reduce diversity of output MSAs using min.seq. identity with query sequences |

## Full CLI Help Snapshot

```text
usage: mmseqs result2profile <i:queryDB> <i:targetDB> <i:resultDB> <o:profileDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                  
 --comp-bias-corr INT         Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT Correct for locally biased amino acid composition (range 0-1) [1.000]
align:                      
 -e DOUBLE                    List matches below this E-value (range 0.0-inf) [1.000E-03]
 --gap-open TWIN              Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN            Gap extension cost [aa:1,nucl:2]
profile:                    
 --mask-profile INT           Mask query sequence of profile using tantan [0,1] [1]
 --e-profile DOUBLE           Include sequences matches with < E-value thr. into the profile (>=0.0) [1.000E-03]
 --wg BOOL                    Use global sequence weighting for profile calculation [0]
 --filter-msa INT             Filter msa: 0: do not filter, 1: filter [1]
 --filter-min-enable INT      Only filter MSAs with more than N sequences, 0 always filters [0]
 --max-seq-id FLOAT           Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] [0.900]
 --qid STR                    Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0]
                              Alternatively, can be a list of multiple thresholds:
                              E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] [0.0]
 --qsc FLOAT                  Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] [-20.000]
 --cov FLOAT                  Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] [0.000]
 --diff INT                   Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 [1000]
 --pseudo-cnt-mode INT        use 0: substitution-matrix or 1: context-specific pseudocounts [0]
 --pca                        Pseudo count admixture strength []
 --pcb                        Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) []
 --profile-output-mode INT    Profile output mode: 0: binary log-odds 1: human-readable frequencies [0]
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
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/profiles.md).

