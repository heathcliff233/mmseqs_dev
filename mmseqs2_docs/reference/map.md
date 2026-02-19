## `map` {#refcmd-map}

Map nearly identical sequences.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `high_level_api` |
| Primary functional group | [`search_workflows`](#mod-search-workflows) |
| Category flags | `COMMAND_MAIN` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | `n/a` |
| Calls modules | [`search`](#refcmd-search) |
| Seen in workflow scripts | `n/a` |

### Usage

`usage: mmseqs map <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--seed-sub-mat` | Substitution matrix file for k-mer generation |
| `-s` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive |
| `-k` | k-mer length (0: automatically set to optimum) |
| `--target-search-mode` | target search mode (0: regular k-mer, 1: similar k-mer) |
| `--k-score` | k-mer threshold for generating similar k-mer lists |
| `--alph-size` | Alphabet size (range 2-21) |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--split` | Split input into N equally distributed chunks. 0: set the best split automatically |
| `--split-mode` | 0: split target db; 1: split query db; 2: auto, depending on main memory |
| `--split-memory-limit` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |

### Full CLI Help Snapshot

```text
usage: mmseqs map <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
 By Milot Mirdita <milot@mirdita.de> & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                  
 --seed-sub-mat TWIN          Substitution matrix file for k-mer generation [aa:VTML80.out,nucl:nucleotide.out]
 -s FLOAT                     Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive [2.000]
 -k INT                       k-mer length (0: automatically set to optimum) [0]
 --target-search-mode INT     target search mode (0: regular k-mer, 1: similar k-mer) [0]
 --k-score TWIN               k-mer threshold for generating similar k-mer lists [seq:2147483647,prof:2147483647]
 --alph-size TWIN             Alphabet size (range 2-21) [aa:21,nucl:5]
 --max-seqs INT               Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) [300]
 --split INT                  Split input into N equally distributed chunks. 0: set the best split automatically [0]
 --split-mode INT             0: split target db; 1: split query db; 2: auto, depending on main memory [2]
 --split-memory-limit BYTE    Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory [0]
 --comp-bias-corr INT         Correct for locally biased amino acid composition (range 0-1) [0]
 --comp-bias-corr-scale FLOAT Correct for locally biased amino acid composition (range 0-1) [1.000]
 --diag-score BOOL            Use ungapped diagonal scoring during prefilter [1]
 --exact-kmer-matching INT    Extract only exact k-mers for matching (range 0-1) [0]
 --mask INT                   Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking [0]
 --mask-prob FLOAT            Mask sequences is probablity is above threshold [0.900]
 --mask-lower-case INT        Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region [0]
 --mask-n-repeat INT          Repeat letters that occure > threshold in a rwo [0]
 --min-ungapped-score INT     Accept only matches with ungapped alignment score above threshold [15]
 --add-self-matches BOOL      Artificially add entries of queries with themselves (for clustering) [0]
 --spaced-kmer-mode INT       0: use consecutive positions in k-mers; 1: use spaced k-mers [1]
 --spaced-kmer-pattern STR    User-specified spaced k-mer pattern []
 --local-tmp STR              Path where some of the temporary files will be created []
align:                      
 -c FLOAT                     List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.950]
 --cov-mode INT               0: coverage of query and target
                              1: coverage of target
                              2: coverage of query
                              3: target seq. length has to be at least x% of query length
                              4: query seq. length has to be at least x% of target length
                              5: short seq. needs to be at least x% of the other seq. length [2]
 --wrapped-scoring BOOL       Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start [0]
 -e DOUBLE                    List matches below this E-value (range 0.0-inf) [1.000E-03]
 -a BOOL                      Add backtrace string (convert to alignments with mmseqs convertalis module) [0]
 --min-seq-id FLOAT           List matches above this sequence identity (for clustering) (range 0.0-1.0) [0.900]
 --min-aln-len INT            Minimum alignment length (range 0-INT_MAX) [0]
 --seq-id-mode INT            0: alignment length 1: shorter, 2: longer sequence [0]
profile:                    
 --pca                        Pseudo count admixture strength []
 --pcb                        Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) []
misc:                       
 --taxon-list STR             Taxonomy ID, possibly multiple values separated by ',' []
 --rescore-mode INT           Rescore diagonals with:
                              0: Hamming distance
                              1: local alignment (score only)
                              2: local alignment
                              3: global alignment
                              4: longest alignment fulfilling window quality criterion [2]
 --min-length INT             Minimum codon number in open reading frames [10]
 --max-length INT             Maximum codon number in open reading frames [32734]
 --max-gaps INT               Maximum number of codons with gaps or unknown residues before an open reading frame is rejected [2147483647]
 --contig-start-mode INT      Contig start can be 0: incomplete, 1: complete, 2: both [2]
 --contig-end-mode INT        Contig end can be 0: incomplete, 1: complete, 2: both [2]
 --orf-start-mode INT         Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) [1]
 --forward-frames STR         Comma-separated list of frames on the forward strand to be extracted [1,2,3]
 --reverse-frames STR         Comma-separated list of frames on the reverse strand to be extracted [1,2,3]
 --translation-table INT      1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE
                              9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL
                              15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL
                              23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA
                               29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA [1]
 --translate INT              Translate ORF to amino acid [0]
 --use-all-table-starts BOOL  Use all alternatives for a start codon in the genetic table, if false - only ATG (AUG) [0]
 --id-offset INT              Numeric ids in index file are offset by this value [0]
 --start-sens FLOAT           Start sensitivity [4.000]
 --sens-steps INT             Number of search steps performed from --start-sens to -s [1]
common:                     
 --sub-mat TWIN               Substitution matrix file [aa:blosum62.out,nucl:nucleotide.out]
 --max-seq-len INT            Maximum sequence length [65535]
 --db-load-mode INT           Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT                Number of CPU-cores used (all by default) [10]
 --compressed INT             Write compressed output [0]
 -v INT                       Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
 --mpi-runner STR             Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") []
 --force-reuse BOOL           Reuse tmp filse in tmp/latest folder ignoring parameters and version changes [0]
 --remove-tmp-files BOOL      Delete temporary files [0]
expert:                     
 --filter-hits BOOL           Filter hits by seq.id. and coverage [0]
 --sort-results INT           Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) [1]
 --create-lookup INT          Create database lookup file (can be very large) [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Steinegger M, Mirdita M, Soding J: Protein-level assembly increases protein sequence recovery from metagenomic samples manyfold. Nature Methods, 16(7), 603-606 (2019)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-map), [command reference index](#sec-command-reference), and [functional module page](#mod-search-workflows).

