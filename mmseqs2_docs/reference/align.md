### `align` {#refcmd-align}

Optimal gapped local alignment.

Execution role: core compute module typically called by workflows and advanced custom pipelines.

This command family computes pair quality and coordinates and usually dominates per-pair compute cost after prefiltering. The current dependency map records 5 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-align); functional module: [`alignment`](#mod-alignment).

**Usage**

`usage: mmseqs align <i:queryDB> <i:targetDB> <i:resultDB> <o:alignmentDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `--alignment-mode` | How to compute the alignment: |
| `--alignment-output-mode` | How to compute the alignment: |
| `--wrapped-scoring` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `--min-aln-len` | Minimum alignment length (range 0-INT_MAX) |
| `--seq-id-mode` | 0: alignment length 1: shorter, 2: longer sequence |
| `--alt-ali` | Show up to this many alternative alignments |

**Full CLI Help Snapshot**

```text
usage: mmseqs align <i:queryDB> <i:targetDB> <i:resultDB> <o:alignmentDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr> & Maria Hauser
options: prefilter:                   
 --comp-bias-corr INT          Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT  Correct for locally biased amino acid composition (range 0-1) [1.000]
 --add-self-matches BOOL       Artificially add entries of queries with themselves (for clustering) [0]
align:                       
 -a BOOL                       Add backtrace string (convert to alignments with mmseqs convertalis module) [0]
 --alignment-mode INT          How to compute the alignment:
                               0: automatic
                               1: only score and end_pos
                               2: also start_pos and cov
                               3: also seq.id [0]
 --alignment-output-mode INT   How to compute the alignment:
                               0: automatic
                               1: only score and end_pos
                               2: also start_pos and cov
                               3: also seq.id
                               4: only ungapped alignment
                               5: score only (output) cluster format [0]
 --wrapped-scoring BOOL        Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start [0]
 -e DOUBLE                     List matches below this E-value (range 0.0-inf) [1.000E-03]
 --min-seq-id FLOAT            List matches above this sequence identity (for clustering) (range 0.0-1.0) [0.000]
 --min-aln-len INT             Minimum alignment length (range 0-INT_MAX) [0]
 --seq-id-mode INT             0: alignment length 1: shorter, 2: longer sequence [0]
 --alt-ali INT                 Show up to this many alternative alignments [0]
 -c FLOAT                      List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
 --cov-mode INT                0: coverage of query and target
                               1: coverage of target
                               2: coverage of query
                               3: target seq. length has to be at least x% of query length
                               4: query seq. length has to be at least x% of target length
                               5: short seq. needs to be at least x% of the other seq. length [0]
 --max-rejected INT            Maximum rejected alignments before alignment calculation for a query is stopped [2147483647]
 --max-accept INT              Maximum accepted alignments before alignment calculation for a query is stopped [2147483647]
 --score-bias FLOAT            Score bias when computing SW alignment (in bits) [0.000]
 --realign BOOL                Compute more conservative, shorter alignments (scores and E-values not changed) [0]
 --realign-score-bias FLOAT    Additional bias when computing realignment [-0.200]
 --realign-max-seqs INT        Maximum number of results to return in realignment [2147483647]
 --corr-score-weight FLOAT     Weight of backtrace correlation score that is added to the alignment score [0.000]
 --gap-open TWIN               Gap open cost [aa:11,nucl:5]
 --gap-extend TWIN             Gap extension cost [aa:1,nucl:2]
 --zdrop INT                   Maximal allowed difference between score values before alignment is truncated  (nucleotide alignment only) [40]
profile:                     
 --pca                         Pseudo count admixture strength []
 --pcb                         Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) []
common:                      
 --sub-mat TWIN                Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --max-seq-len INT             Maximum sequence length [65535]
 --db-load-mode INT            Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT                 Number of CPU-cores used (all by default) [10]
 --compressed INT              Write compressed output [0]
 -v INT                        Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
