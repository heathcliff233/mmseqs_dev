## `linsearch` {#refcmd-linsearch}

Fast, less sensitive homology search.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `high_level_api` |
| Primary functional group | [`search_workflows`](#mod-search-workflows) |
| Category flags | `COMMAND_MAIN|COMMAND_EXPERT` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `2` |
| Downstream command count | `9` |
| Workflow script count | `0` |
| Detailed dependency entry | [Open in map](#depcmd-linsearch) |

### Usage

`usage: mmseqs linsearch <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `--alignment-mode` | How to compute the alignment: |
| `--alignment-output-mode` | How to compute the alignment: |

### Full CLI Help Snapshot

```text
usage: mmseqs linsearch <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                   
 --comp-bias-corr INT          Correct for locally biased amino acid composition (range 0-1) [1]
 --comp-bias-corr-scale FLOAT  Correct for locally biased amino acid composition (range 0-1) [1.000]
 --add-self-matches BOOL       Artificially add entries of queries with themselves (for clustering) [0]
 --seed-sub-mat TWIN           Substitution matrix file for k-mer generation [aa:blosum62.out,nucl:nucleotide.out]
 --mask INT                    Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking [0]
 --mask-prob FLOAT             Mask sequences is probablity is above threshold [0.900]
 --mask-lower-case INT         Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region [0]
 --mask-n-repeat INT           Repeat letters that occure > threshold in a rwo [0]
 --split-memory-limit BYTE     Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory [0]
align:                       
 -a BOOL                       Add backtrace string (convert to alignments with mmseqs convertalis module) [0]
 --alignment-mode INT          How to compute the alignment:
                               0: automatic
                               1: only score and end_pos
                               2: also start_pos and cov
                               3: also seq.id
                               4: only ungapped alignment [2]
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
kmermatcher:                 
 --kmer-per-seq INT            k-mers per sequence [21]
 --kmer-per-seq-scale TWIN     Scale k-mer per sequence based on sequence length as kmer-per-seq val + scale x seqlen [aa:0.000,nucl:0.200]
 --pick-n-sim-kmer INT         Add N similar k-mers to search [1]
 --result-direction INT        result is 0: query, 1: target centric [1]
profile:                     
 --pca                         Pseudo count admixture strength []
 --pcb                         Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) []
misc:                        
 --min-length INT              Minimum codon number in open reading frames [30]
 --max-length INT              Maximum codon number in open reading frames [32734]
 --max-gaps INT                Maximum number of codons with gaps or unknown residues before an open reading frame is rejected [2147483647]
 --contig-start-mode INT       Contig start can be 0: incomplete, 1: complete, 2: both [2]
 --contig-end-mode INT         Contig end can be 0: incomplete, 1: complete, 2: both [2]
 --orf-start-mode INT          Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) [1]
 --forward-frames STR          Comma-separated list of frames on the forward strand to be extracted [1,2,3]
 --reverse-frames STR          Comma-separated list of frames on the reverse strand to be extracted [1,2,3]
 --translation-table INT       1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE
                               9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL
                               15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL
                               23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA
                                29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA [1]
 --translate INT               Translate ORF to amino acid [0]
 --use-all-table-starts BOOL   Use all alternatives for a start codon in the genetic table, if false - only ATG (AUG) [0]
 --id-offset INT               Numeric ids in index file are offset by this value [0]
 --search-type INT             Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment [0]
common:                      
 --sub-mat TWIN                Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --max-seq-len INT             Maximum sequence length [65535]
 --db-load-mode INT            Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT                 Number of CPU-cores used (all by default) [10]
 --compressed INT              Write compressed output [0]
 -v INT                        Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
 --mpi-runner STR              Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") []
 --force-reuse BOOL            Reuse tmp filse in tmp/latest folder ignoring parameters and version changes [0]
 --remove-tmp-files BOOL       Delete temporary files [0]
expert:                      
 --create-lookup INT           Create database lookup file (can be very large) [0]
 --chain-alignments INT        Chain overlapping alignments [0]
 --merge-query INT             Combine ORFs/split sequences to a single entry [1]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-linsearch), [command reference index](#sec-command-reference), and [functional module page](#mod-search-workflows).

