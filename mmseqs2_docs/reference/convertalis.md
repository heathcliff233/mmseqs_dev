# `convertalis`

Convert alignment DB to BLAST-tab, SAM or custom format.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](../submodules/result_handling.md) |
| Category flags | `COMMAND_FORMAT_CONVERSION` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`easy-linsearch`](./easy-linsearch.md), [`easy-rbh`](./easy-rbh.md), [`easy-search`](./easy-search.md), [`easy-taxonomy`](./easy-taxonomy.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh` |

## Usage

`usage: mmseqs convertalis <i:queryDb> <i:targetDb> <i:alignmentDB> <o:alignmentFile> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--format-mode` | Output format: |
| `--format-output` | Choose comma separated list of output columns from: query,target,evalue,gapopen,pident,fident,nident,qstart,qend,qlen |
| `--translation-table` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE |
| `--search-type` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment |
| `--sub-mat` | Substitution matrix file |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--db-output` | Return a result DB instead of a text file |

## Full CLI Help Snapshot

```text
usage: mmseqs convertalis <i:queryDb> <i:targetDb> <i:alignmentDB> <o:alignmentFile> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: align:                   
 --gap-open TWIN           Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN         Gap extension cost [aa:1,nucl:2]
misc:                    
 --format-mode INT         Output format:
                           0: BLAST-TAB
                           1: SAM
                           2: BLAST-TAB + query/db length
                           3: Pretty HTML
                           4: BLAST-TAB + column headers
                           BLAST-TAB (0) and BLAST-TAB + column headers (4) support custom output formats (--format-output) [0]
 --format-output STR       Choose comma separated list of output columns from: query,target,evalue,gapopen,pident,fident,nident,qstart,qend,qlen
                           tstart,tend,tlen,alnlen,raw,bits,cigar,qseq,tseq,qheader,theader,qaln,taln,qframe,tframe,mismatch,qcov,tcov
                           qset,qsetid,tset,tsetid,taxid,taxname,taxlineage,qorfstart,qorfend,torfstart,torfend,ppos [query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits]
 --translation-table INT   1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE
                           9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL
                           15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL
                           23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA
                            29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA [1]
 --search-type INT         Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment [0]
common:                  
 --sub-mat TWIN            Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --db-load-mode INT        Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT             Number of CPU-cores used (all by default) [10]
 --compressed INT          Write compressed output [0]
 -v INT                    Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                  
 --db-output BOOL          Return a result DB instead of a text file [0]

examples:
 # Create output in BLAST M8 format (12 columns):
 #  (1,2) identifiers for query and target sequences/profiles,
 #  (3) sequence identity, (4) alignment length, (5) number of mismatches,
 #  (6) number of gap openings, (7-8, 9-10) alignment start and end-position in query and in target,
 #  (11) E-value, and (12) bit score
 mmseqs convertalis queryDB targetDB result.m8
 
 # Create a TSV containing pairwise alignments
 mmseqs convertalis queryDB targetDB result.tsv --format-output query,target,qaln,taln
 
 # Annotate a alignment result with taxonomy information from targetDB
 mmseqs convertalis queryDB targetDB result.tsv --format-output query,target,taxid,taxname,taxlineage
 
  Create SAM output
 mmseqs convertalis queryDB targetDB result.sam --format-mode 1
 
 # Create a TSV containing which query file a result comes from
 mmseqs createdb euk_queries.fasta bac_queries.fasta queryDB
 mmseqs convertalis queryDB targetDB result.tsv --format-output qset,query,target
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/result_handling.md).

