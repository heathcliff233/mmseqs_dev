
# Easy Workflows

This document describes the "easy" workflows in MMseqs2, which are high-level commands for common tasks.

## `easy-cluster`

**Description:**

> Clustering workflow using cascaded clustering

**Usage:**
```bash
mmseqs easy-cluster <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]>|<i:stdin> <o:clusterPrefix> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `-s <FLOAT>` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive | `5.700` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--target-search-mode <INT>` | target search mode (0: regular k-mer, 1: similar k-mer) | `0` |
| `--k-score <TWIN>` | k-mer threshold for generating similar k-mer lists | `seq:2147483647,prof:2147483647` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |
| `--split <INT>` | Split input into N equally distributed chunks. 0: set the best split automatically | `0` |
| `--split-mode <INT>` | 0: split target db; 1: split query db; 2: auto, depending on main memory | `2` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |
| `--diag-score <BOOL>` | Use ungapped diagonal scoring during prefilter | `1` |
| `--exact-kmer-matching <INT>` | Extract only exact k-mers for matching (range 0-1) | `0` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--min-ungapped-score <INT>` | Accept only matches with ungapped alignment score above threshold | `15` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `1` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `--local-tmp <STR>` | Path where some of the temporary files will be created | `[]` |
| `--disk-space-limit <BYTE>` | Set max disk space to use for reverse profile searches. E.g. 800B, 5K, 10M, 1G. Default (0) to all available disk space in the temp folder | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id | `2` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.800` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `--realign <BOOL>` | Compute more conservative, shorter alignments (scores and E-values not changed) | `0` |
| `--realign-score-bias <FLOAT>` | Additional bias when computing realignment | `-0.200` |
| `--realign-max-seqs <INT>` | Maximum number of results to return in realignment | `2147483647` |
| `--corr-score-weight <FLOAT>` | Weight of backtrace correlation score that is added to the alignment score | `0.000` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--zdrop <INT>` | Maximal allowed difference between score values before alignment is truncated (nucleotide alignment only) | `40` |
| `--exhaustive-search-filter <INT>` | Filter result during search: 0: do not filter, 1: filter | `0` |

### Cluster Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--cluster-mode <INT>` | 0: Set-Cover (greedy), 1: Connected component, 2: Greedy clustering by sequence length, 3: Greedy clustering by sequence length (low mem) | `0` |
| `--cluster-steps <INT>` | Maximum depth of cascaded clustering | `3` |
| `--cluster-reassignment <INT>` | 0: no reassignment, 1: reassignment with maximum 25% increase of sequences per cluster | `1` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `0` |
| `--single-step-clustering <BOOL>` | Switch from cascaded to single step clustering | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `easy-search`

**Description:**

> Sensitive homology search

**Usage:**
```bash
mmseqs easy-search <i:queryFastaFile1[.gz|.bz2]> ... <i:queryFastaFileN[.gz|.bz2]>|<i:stdin> <i:targetFastaFile[.gz]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `-s <FLOAT>` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive | `5.700` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--target-search-mode <INT>` | target search mode (0: regular k-mer, 1: similar k-mer) | `0` |
| `--k-score <TWIN>` | k-mer threshold for generating similar k-mer lists | `seq:2147483647,prof:2147483647` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |
| `--split <INT>` | Split input into N equally distributed chunks. 0: set the best split automatically | `0` |
| `--split-mode <INT>` | 0: split target db; 1: split query db; 2: auto, depending on main memory | `2` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |
| `--diag-score <BOOL>` | Use ungapped diagonal scoring during prefilter | `1` |
| `--exact-kmer-matching <INT>` | Extract only exact k-mers for matching (range 0-1) | `0` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--min-ungapped-score <INT>` | Accept only matches with ungapped alignment score above threshold | `15` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `1` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `--local-tmp <STR>` | Path where some of the temporary files will be created | `[]` |
| `--disk-space-limit <BYTE>` | Set max disk space to use for reverse profile searches. E.g. 800B, 5K, 10M, 1G. Default (0) to all available disk space in the temp folder | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment | `3` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--max-rejected <INT>` | Maximum rejected alignments before alignment calculation for a query is stopped | `2147483647` |
| `--max-accept <INT>` | Maximum accepted alignments before alignment calculation for a query is stopped | `2147483647` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `--realign <BOOL>` | Compute more conservative, shorter alignments (scores and E-values not changed) | `0` |
| `--realign-score-bias <FLOAT>` | Additional bias when computing realignment | `-0.200` |
| `--realign-max-seqs <INT>` | Maximum number of results to return in realignment | `2147483647` |
| `--corr-score-weight <FLOAT>` | Weight of backtrace correlation score that is added to the alignment score | `0.000` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--zdrop <INT>` | Maximal allowed difference between score values before alignment is truncated (nucleotide alignment only) | `40` |
| `--exhaustive-search-filter <INT>` | Filter result during search: 0: do not filter, 1: filter | `0` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |
| `--mask-profile <INT>` | Mask query sequence of profile using tantan [0,1] | `1` |
| `--e-profile <DOUBLE>` | Include sequences matches with < E-value thr. into the profile (>=0.0) | `1.000E-03` |
| `--wg <BOOL>` | Use global sequence weighting for profile calculation | `0` |
| `--filter-msa <INT>` | Filter msa: 0: do not filter, 1: filter | `1` |
| `--filter-min-enable <INT>` | Only filter MSAs with more than N sequences, 0 always filters | `0` |
| `--max-seq-id <FLOAT>` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] | `0.900` |
| `--qid <STR>` | Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0] Alternatively, can be a list of multiple thresholds: E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] | `0.0` |
| `--qsc <FLOAT>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] | `-20.000` |
| `--cov <FLOAT>` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] | `0.000` |
| `--diff <INT>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | `1000` |
| `--pseudo-cnt-mode <INT>` | use 0: substitution-matrix or 1: context-specific pseudocounts | `0` |
| `--profile-output-mode <INT>` | Profile output mode: 0: binary log-odds 1: human-readable frequencies | `0` |
| `--num-iterations <INT>` | Number of iterative profile search iterations | `1` |
| `--exhaustive-search <BOOL>` | For bigger profile DB, run iteratively the search by greedily swapping the search results | `0` |
| `--lca-search <BOOL>` | Efficient search for LCA candidates | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--taxon-list <STR>` | Taxonomy ID, possibly multiple values separated by ',' | `[]` |
| `--prefilter-mode <INT>` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped | `0` |
| `--rescore-mode <INT>` | Rescore diagonals with: 0: Hamming distance, 1: local alignment (score only), 2: local alignment, 3: global alignment, 4: longest alignment fulfilling window quality criterion | `0` |
| `--allow-deletion <BOOL>` | Allow deletions in a MSA | `0` |
| `--min-length <INT>` | Minimum codon number in open reading frames | `30` |
| `--max-length <INT>` | Maximum codon number in open reading frames | `32734` |
| `--max-gaps <INT>` | Maximum number of codons with gaps or unknown residues before an open reading frame is rejected | `2147483647` |
| `--contig-start-mode <INT>` | Contig start can be 0: incomplete, 1: complete, 2: both | `2` |
| `--contig-end-mode <INT>` | Contig end can be 0: incomplete, 1: complete, 2: both | `2` |
| `--orf-start-mode <INT>` | Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) | `1` |
| `--forward-frames <STR>` | Comma-separated list of frames on the forward strand to be extracted | `1,2,3` |
| `--reverse-frames <STR>` | Comma-separated list of frames on the reverse strand to be extracted | `1,2,3` |
| `--translation-table <INT>` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE 9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL 15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL 23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28)

## `easy-linclust`

**Description:**

> Linear time clustering workflow

**Usage:**
```bash
mmseqs easy-linclust <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]> <o:clusterPrefix> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `0` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment | `0` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.800` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--max-rejected <INT>` | Maximum rejected alignments before alignment calculation for a query is stopped | `2147483647` |
| `--max-accept <INT>` | Maximum accepted alignments before alignment calculation for a query is stopped | `2147483647` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `--realign <BOOL>` | Compute more conservative, shorter alignments (scores and E-values not changed) | `0` |
| `--realign-score-bias <FLOAT>` | Additional bias when computing realignment | `-0.200` |
| `--realign-max-seqs <INT>` | Maximum number of results to return in realignment | `2147483647` |
| `--corr-score-weight <FLOAT>` | Weight of backtrace correlation score that is added to the alignment score | `0.000` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--zdrop <INT>` | Maximal allowed difference between score values before alignment is truncated (nucleotide alignment only) | `40` |

### Cluster Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--cluster-mode <INT>` | 0: Set-Cover (greedy), 1: Connected component (BLASTclust), 2,3: Greedy clustering by sequence length (CDHIT) | `0` |
| `--max-iterations <INT>` | Maximum depth of breadth first search in connected component clustering | `1000` |
| `--similarity-type <INT>` | Type of score used for clustering. 1: alignment score 2: sequence identity | `2` |

### Kmer Matcher Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--weights <STR>` | Weights used for cluster priorization | `[]` |
| `--cluster-weight-threshold <FLOAT>` | Weight threshold used for cluster priorization | `0.900` |
| `--kmer-per-seq <INT>` | k-mers per sequence | `21` |
| `--kmer-per-seq-scale <TWIN>` | Scale k-mer per sequence based on sequence length as kmer-per-seq val + scale x seqlen | `aa:0.000,nucl:0.200` |
| `--adjust-kmer-len <BOOL>` | Adjust k-mer length based on specificity (only for nucleotides) | `0` |
| `--hash-shift <INT>` | Shift k-mer hash initialization | `67` |
| `--include-only-extendable <BOOL>` | Include only extendable | `0` |
| `--ignore-multi-kmer <BOOL>` | Skip k-mers occurring multiple times (>=2) | `0` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--rescore-mode <INT>` | Rescore diagonals with: 0: Hamming distance, 1: local alignment (score only), 2: local alignment, 3: global alignment, 4: longest alignment fulfilling window quality criterion | `0` |
| `--dbtype <INT>` | Database type 0: auto, 1: amino acid 2: nucleotides | `0` |
| `--shuffle <BOOL>` | Shuffle input database | `1` |
| `--createdb-mode <INT>` | Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) | `1` |
| `--id-offset <INT>` | Numeric ids in index file are offset by this value | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `1` |
| `--force-reuse <BOOL>` | Reuse tmp filse in tmp/latest folder ignoring parameters and version changes | `0` |
| `--mpi-runner <STR>` | Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") | `[]` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |
| `--write-lookup <INT>` | write .lookup file containing mapping from internal id, fasta id and file number | `0` |

## `easy-linsearch`

**Description:**

> Linear time search workflow

**Usage:**
```bash
mmseqs easy-linsearch <i:queryFastaFile1[.gz|.bz2]> ... <i:queryFastaFileN[.gz|.bz2]> <i:targetFastaFile[.gz|.bz2]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment | `3` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--max-rejected <INT>` | Maximum rejected alignments before alignment calculation for a query is stopped | `2147483647` |
| `--max-accept <INT>` | Maximum accepted alignments before alignment calculation for a query is stopped | `2147483647` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `--realign <BOOL>` | Compute more conservative, shorter alignments (scores and E-values not changed) | `0` |
| `--realign-score-bias <FLOAT>` | Additional bias when computing realignment | `-0.200` |
| `--realign-max-seqs <INT>` | Maximum number of results to return in realignment | `2147483647` |
| `--corr-score-weight <FLOAT>` | Weight of backtrace correlation score that is added to the alignment score | `0.000` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--zdrop <INT>` | Maximal allowed difference between score values before alignment is truncated (nucleotide alignment only) | `40` |

### Kmer Matcher Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--kmer-per-seq <INT>` | k-mers per sequence | `21` |
| `--kmer-per-seq-scale <TWIN>` | Scale k-mer per sequence based on sequence length as kmer-per-seq val + scale x seqlen | `aa:0.000,nucl:0.200` |
| `--pick-n-sim-kmer <INT>` | Add N similar k-mers to search | `1` |
| `--result-direction <INT>` | result is 0: query, 1: target centric | `1` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--min-length <INT>` | Minimum codon number in open reading frames | `30` |
| `--max-length <INT>` | Maximum codon number in open reading frames | `32734` |
| `--max-gaps <INT>` | Maximum number of codons with gaps or unknown residues before an open reading frame is rejected | `2147483647` |
| `--contig-start-mode <INT>` | Contig start can be 0: incomplete, 1: complete, 2: both | `2` |
| `--contig-end-mode <INT>` | Contig end can be 0: incomplete, 1: complete, 2: both | `2` |
| `--orf-start-mode <INT>` | Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) | `1` |
| `--forward-frames <STR>` | Comma-separated list of frames on the forward strand to be extracted | `1,2,3` |
| `--reverse-frames <STR>` | Comma-separated list of frames on the reverse strand to be extracted | `1,2,3` |
| `--translation-table <INT>` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE 9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL 15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL 23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA 29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA | `1` |
| `--translate <INT>` | Translate ORF to amino acid | `0` |
| `--use-all-table-starts <BOOL>` | Use all alternatives for a start codon in the genetic table, if false - only ATG (AUG) | `0` |
| `--id-offset <INT>` | Numeric ids in index file are offset by this value | `0` |
| `--search-type <INT>` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment | `0` |
| `--format-mode <INT>` | Output format: 0: BLAST-TAB, 1: SAM, 2: BLAST-TAB + query/db length, 3: Pretty HTML, 4: BLAST-TAB + column headers BLAST-TAB (0) and BLAST-TAB + column headers (4) support custom output formats (--format-output) | `0` |
| `--format-output <STR>` | Choose comma separated list of output columns from: query,target,evalue,gapopen,pident,fident,nident,qstart,qend,qlen tstart,tend,tlen,alnlen,raw,bits,cigar,qseq,tseq,qheader,theader,qaln,taln,qframe,tframe,mismatch,qcov,tcov qset,qsetid,tset,tsetid,taxid,taxname,taxlineage,qorfstart,qorfend,torfstart,torfend,ppos | `query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--mpi-runner <STR>` | Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") | `[]` |
| `--force-reuse <BOOL>` | Reuse tmp filse in tmp/latest folder ignoring parameters and version changes | `0` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `1` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |
| `--chain-alignments <INT>` | Chain overlapping alignments | `0` |
| `--merge-query <INT>` | Combine ORFs/split sequences to a single entry | `1` |
| `--db-output <BOOL>` | Return a result DB instead of a text file | `0` |

## `easy-rbh`

**Description:**

> Reciprocal best hit workflow

**Usage:**
```bash
mmseqs easy-rbh <i:queryFastaFile1[.gz|.bz2]> <i:targetFastaFile[.gz|.bz2]>|<i:targetDB> <o:alignmentFile> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `-s <FLOAT>` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive | `5.700` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--target-search-mode <INT>` | target search mode (0: regular k-mer, 1: similar k-mer) | `0` |
| `--k-score <TWIN>` | k-mer threshold for generating similar k-mer lists | `seq:2147483647,prof:2147483647` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |
| `--split <INT>` | Split input into N equally distributed chunks. 0: set the best split automatically | `0` |
| `--split-mode <INT>` | 0: split target db; 1: split query db; 2: auto, depending on main memory | `2` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |
| `--diag-score <BOOL>` | Use ungapped diagonal scoring during prefilter | `1` |
| `--exact-kmer-matching <INT>` | Extract only exact k-mers for matching (range 0-1) | `0` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--min-ungapped-score <INT>` | Accept only matches with ungapped alignment score above threshold | `15` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `1` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `--local-tmp <STR>` | Path where some of the temporary files will be created | `[]` |
| `--disk-space-limit <BYTE>` | Set max disk space to use for reverse profile searches. E.g. 800B, 5K, 10M, 1G. Default (0) to all available disk space in the temp folder | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment | `3` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--max-rejected <INT>` | Maximum rejected alignments before alignment calculation for a query is stopped | `2147483647` |
| `--max-accept <INT>` | Maximum accepted alignments before alignment calculation for a query is stopped | `2147483647` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `--realign <BOOL>` | Compute more conservative, shorter alignments (scores and E-values not changed) | `0` |
| `--realign-score-bias <FLOAT>` | Additional bias when computing realignment | `-0.200` |
| `--realign-max-seqs <INT>` | Maximum number of results to return in realignment | `2147483647` |
| `--corr-score-weight <FLOAT>` | Weight of backtrace correlation score that is added to the alignment score | `0.000` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--zdrop <INT>` | Maximal allowed difference between score values before alignment is truncated (nucleotide alignment only) | `40` |
| `--exhaustive-search-filter <INT>` | Filter result during search: 0: do not filter, 1: filter | `0` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |
| `--mask-profile <INT>` | Mask query sequence of profile using tantan [0,1] | `1` |
| `--e-profile <DOUBLE>` | Include sequences matches with < E-value thr. into the profile (>=0.0) | `1.000E-03` |
| `--wg <BOOL>` | Use global sequence weighting for profile calculation | `0` |
| `--filter-msa <INT>` | Filter msa: 0: do not filter, 1: filter | `1` |
| `--filter-min-enable <INT>` | Only filter MSAs with more than N sequences, 0 always filters | `0` |
| `--max-seq-id <FLOAT>` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] | `0.900` |
| `--qid <STR>` | Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0] Alternatively, can be a list of multiple thresholds: E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] | `0.0` |
| `--qsc <FLOAT>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] | `-20.000` |
| `--cov <FLOAT>` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] | `0.000` |
| `--diff <INT>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | `1000` |
| `--pseudo-cnt-mode <INT>` | use 0: substitution-matrix or 1: context-specific pseudocounts | `0` |
| `--profile-output-mode <INT>` | Profile output mode: 0: binary log-odds 1: human-readable frequencies | `0` |
| `--num-iterations <INT>` | Number of iterative profile search iterations | `1` |
| `--exhaustive-search <BOOL>` | For bigger profile DB, run iteratively the search by greedily swapping the search results | `0` |
| `--lca-search <BOOL>` | Efficient search for LCA candidates | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--taxon-list <STR>` | Taxonomy ID, possibly multiple values separated by ',' | `[]` |
| `--prefilter-mode <INT>` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped | `0` |
| `--rescore-mode <INT>` | Rescore diagonals with: 0: Hamming distance, 1: local alignment (score only), 2: local alignment, 3: global alignment, 4: longest alignment fulfilling window quality criterion | `0` |
| `--allow-deletion <BOOL>` | Allow deletions in a MSA | `0` |
| `--min-length <INT>` | Minimum codon number in open reading frames | `30` |
| `--max-length <INT>` | Maximum codon number in open reading frames | `32734` |
| `--max-gaps <INT>` | Maximum number of codons with gaps or unknown residues before an open reading frame is rejected | `2147483647` |
| `--contig-start-mode <INT>` | Contig start can be 0: incomplete, 1: complete, 2: both | `2` |
| `--contig-end-mode <INT>` | Contig end can be 0: incomplete, 1: complete, 2: both | `2` |
| `--orf-start-mode <INT>` | Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) | `1` |
| `--forward-frames <STR>` | Comma-separated list of frames on the forward strand to be extracted | `1,2,3` |
| `--reverse-frames <STR>` | Comma-separated list of frames on the reverse strand to be extracted | `1,2,3` |
| `--translation-table <INT>` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE 9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL 15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL 23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA 29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA | `1` |
| `--translate <INT>` | Translate ORF to amino acid | `0` |
| `--use-all-table-starts <BOOL>` | Use all alternatives for a start codon in the genetic table, if false - only ATG (AUG) | `0` |
| `--id-offset <INT>` | Numeric ids in index file are offset by this value | `0` |
| `--sequence-overlap <INT>` | Overlap between sequences | `0` |
| `--sequence-split-mode <INT>` | Sequence split mode 0: copy data, 1: soft link data and write new index, | `1` |
| `--headers-split-mode <INT>` | Header split mode: 0: split position, 1: original header | `0` |
| `--search-type <INT>` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment | `0` |
| `--start-sens <FLOAT>` | Start sensitivity | `4.000` |
| `--sens-steps <INT>` | Number of search steps performed from --start-sens to -s | `1` |
| `--translation-mode <INT>` | Translation AA seq from nucleotide by 0: ORFs, 1: full reading frames | `0` |
| `--format-mode <INT>` | Output format: 0: BLAST-TAB, 1: SAM, 2: BLAST-TAB + query/db length, 3: Pretty HTML, 4: BLAST-TAB + column headers BLAST-TAB (0) and BLAST-TAB + column headers (4) support custom output formats (--format-output) | `0` |
| `--format-output <STR>` | Choose comma separated list of output columns from: query,target,evalue,gapopen,pident,fident,nident,qstart,qend,qlen tstart,tend,tlen,alnlen,raw,bits,cigar,qseq,tseq,qheader,theader,qaln,taln,qframe,tframe,mismatch,qcov,tcov qset,qsetid,tset,tsetid,taxid,taxname,taxlineage,qorfstart,qorfend,torfstart,torfend,ppos | `query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits` |
| `--overlap <FLOAT>` | Maximum overlap of covered regions | `0.000` |
| `--dbtype <INT>` | Database type 0: auto, 1: amino acid 2: nucleotides | `0` |
| `--shuffle <BOOL>` | Shuffle input database | `1` |
| `--createdb-mode <INT>` | Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) | `1` |
| `--greedy-best-hits <BOOL>` | Choose the best hits greedily to cover the query | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--gpu <INT>` | Use GPU (CUDA) if possible | `0` |
| `--gpu-server <INT>` | Use GPU server | `0` |
| `--gpu-server-wait-timeout <INT>` | Wait for GPU server for 0: don't wait -1: no wait limit: >0 this many seconds | `600` |
| `--mpi-runner <STR>` | Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") | `[]` |
| `--force-reuse <BOOL>` | Reuse tmp filse in tmp/latest folder ignoring parameters and version changes | `0` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `1` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |
| `--chain-alignments <INT>` | Chain overlapping alignments | `0` |
| `--merge-query <INT>` | Combine ORFs/split sequences to a single entry | `1` |
| `--strand <INT>` | Strand selection only works for DNA/DNA search 0: reverse, 1: forward, 2: both | `1` |
| `--db-output <BOOL>` | Return a result DB instead of a text file | `0` |
| `--write-lookup <INT>` | write .lookup file containing mapping from internal id, fasta id and file number | `0` |

## `easy-taxonomy`

**Description:**

> Taxonomy assignment workflow

**Usage:**
```bash
mmseqs easy-taxonomy <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]> <i:targetDB> <o:taxReports> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `-s <FLOAT>` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive | `4.000` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--target-search-mode <INT>` | target search mode (0: regular k-mer, 1: similar k-mer) | `0` |
| `--k-score <TWIN>` | k-mer threshold for generating similar k-mer lists | `seq:2147483647,prof:2147483647` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |
| `--split <INT>` | Split input into N equally distributed chunks. 0: set the best split automatically | `0` |
| `--split-mode <INT>` | 0: split target db; 1: split query db; 2: auto, depending on main memory | `2` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |
| `--diag-score <BOOL>` | Use ungapped diagonal scoring during prefilter | `1` |
| `--exact-kmer-matching <INT>` | Extract only exact k-mers for matching (range 0-1) | `0` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--min-ungapped-score <INT>` | Accept only matches with ungapped alignment score above threshold | `15` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `1` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `--local-tmp <STR>` | Path where some of the temporary files will be created | `[]` |
| `--disk-space-limit <BYTE>` | Set max disk space to use for reverse profile searches. E.g. 800B, 5K, 10M, 1G. Default (0) to all available disk space in the temp folder | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment | `0` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--max-rejected <INT>` | Maximum rejected alignments before alignment calculation for a query is stopped | `2147483647` |
| `--max-accept <INT>` | Maximum accepted alignments before alignment calculation for a query is stopped | `2147483647` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `--realign <BOOL>` | Compute more conservative, shorter alignments (scores and E-values not changed) | `0` |
| `--realign-score-bias <FLOAT>` | Additional bias when computing realignment | `-0.200` |
| `--realign-max-seqs <INT>` | Maximum number of results to return in realignment | `2147483647` |
| `--corr-score-weight <FLOAT>` | Weight of backtrace correlation score that is added to the alignment score | `0.000` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--zdrop <INT>` | Maximal allowed difference between score values before alignment is truncated (nucleotide alignment only) | `40` |
| `--exhaustive-search-filter <INT>` | Filter result during search: 0: do not filter, 1: filter | `0` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |
| `--mask-profile <INT>` | Mask query sequence of profile using tantan [0,1] | `1` |
| `--e-profile <DOUBLE>` | Include sequences matches with < E-value thr. into the profile (>=0.0) | `1.000E-03` |
| `--wg <BOOL>` | Use global sequence weighting for profile calculation | `0` |
| `--filter-msa <INT>` | Filter msa: 0: do not filter, 1: filter | `1` |
| `--filter-min-enable <INT>` | Only filter MSAs with more than N sequences, 0 always filters | `0` |
| `--max-seq-id <FLOAT>` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] | `0.900` |
| `--qid <STR>` | Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0] Alternatively, can be a list of multiple thresholds: E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] | `0.0` |
| `--qsc <FLOAT>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] | `-20.000` |
| `--cov <FLOAT>` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] | `0.000` |
| `--diff <INT>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | `1000` |
| `--pseudo-cnt-mode <INT>` | use 0: substitution-matrix or 1: context-specific pseudocounts | `0` |
| `--profile-output-mode <INT>` | Profile output mode: 0: binary log-odds 1: human-readable frequencies | `0` |
| `--exhaustive-search <BOOL>` | For bigger profile DB, run iteratively the search by greedily swapping the search results | `0` |
| `--lca-search <BOOL>` | Efficient search for LCA candidates | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--orf-filter <INT>` | Prefilter query ORFs with non-selective search Only used during nucleotide-vs-protein classification NOTE: Consider disabling when classifying short reads | `0` |
| `--orf-filter-e <DOUBLE>` | E-value threshold used for query ORF prefiltering | `1.000E+02` |
| `--orf-filter-s <FLOAT>` | Sensitivity used for query ORF prefiltering | `2.000` |
| `--lca-mode <INT>` | LCA Mode 1: single search LCA , 2/3: approximate 2bLCA, 4: top hit | `3` |
| `--majority <FLOAT>` | minimal fraction of agreement among taxonomically assigned sequences of a set | `0.500` |
| `--vote-mode <INT>` | Mode of assigning weights to compute majority. 0: uniform, 1: minus log E-value, 2: score | `1` |
| `--lca-ranks <STR>` | Add column with specified ranks (',' separated) | `[]` |
| `--tax-lineage <INT>` | 0: don't show, 1: add all lineage names, 2: add all lineage taxids | `0` |
| `--blacklist <STR>` | Comma separated list of ignored taxa in LCA computation | `12908:unclassified sequences,28384:other sequences` |
| `--taxon-list <STR>` | Taxonomy ID, possibly multiple values separated by ',' | `[]` |
| `--prefilter-mode <INT>` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped | `0` |
| `--rescore-mode <INT>` | Rescore diagonals with: 0: Hamming distance, 1: local alignment (score only), 2: local alignment, 3: global alignment, 4: longest alignment fulfilling window quality criterion | `0` |
| `--allow-deletion <BOOL>` | Allow deletions in a MSA | `0` |
| `--min-length <INT>` | Minimum codon number in open reading frames | `30` |
| `--max-length <INT>` | Maximum codon number in open reading frames | `32734` |
| `--max-gaps <INT>` | Maximum number of codons with gaps or unknown residues before an open reading frame is rejected | `2147483647` |
| `--contig-start-mode <INT>` | Contig start can be 0: incomplete, 1: complete, 2: both | `2` |
| `--contig-end-mode <INT>` | Contig end can be 0: incomplete, 1: complete, 2: both | `2` |
| `--orf-start-mode <INT>` | Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) | `1` |
| `--forward-frames <STR>` | Comma-separated list of frames on the forward strand to be extracted | `1,2,3` |
| `--reverse-frames <STR>` | Comma-separated list of frames on the reverse strand to be extracted | `1,2,3` |
| `--translation-table <INT>` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE 9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL 15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL 23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA 29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA | `1` |
| `--translate <INT>` | Translate ORF to amino acid | `0` |
| `--use-all-table-starts <BOOL>` | Use all alternatives for a start codon in the genetic table, if false - only ATG (AUG) | `0` |
| `--id-offset <INT>` | Numeric ids in index file are offset by this value | `0` |
| `--sequence-overlap <INT>` | Overlap between sequences | `0` |
| `--sequence-split-mode <INT>` | Sequence split mode 0: copy data, 1: soft link data and write new index, | `1` |
| `--headers-split-mode <INT>` | Header split mode: 0: split position, 1: original header | `0` |
| `--search-type <INT>` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment | `0` |
| `--translation-mode <INT>` | Translation AA seq from nucleotide by 0: ORFs, 1: full reading frames | `0` |
| `--report-mode <INT>` | Taxonomy report mode 0: Kraken 1: Krona | `0` |
| `--format-mode <INT>` | Output format: 0: BLAST-TAB, 1: SAM, 2: BLAST-TAB + query/db length, 3: Pretty HTML, 4: BLAST-TAB + column headers BLAST-TAB (0) and BLAST-TAB + column headers (4) support custom output formats (--format-output) | `0` |
| `--format-output <STR>` | Choose comma separated list of output columns from: query,target,evalue,gapopen,pident,fident,nident,qstart,qend,qlen tstart,tend,tlen,alnlen,raw,bits,cigar,qseq,tseq,qheader,theader,qaln,taln,qframe,tframe,mismatch,qcov,tcov qset,qsetid,tset,tsetid,taxid,taxname,taxlineage,qorfstart,qorfend,torfstart,torfend,ppos | `query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits` |
| `--first-seq-as-repr <BOOL>` | Use the first sequence of the clustering result as representative sequence | `0` |
| `--target-column <INT>` | Select a target column (default 1), 0 if no target id exists | `1` |
| `--full-header <BOOL>` | Replace DB ID by its corresponding Full Header | `0` |
| `--idx-seq-src <INT>` | 0: auto, 1: split/translated sequences, 2: input sequences | `0` |
| `--dbtype <INT>` | Database type 0: auto, 1: amino acid 2: nucleotides | `0` |
| `--shuffle <BOOL>` | Shuffle input database | `1` |
| `--createdb-mode <INT>` | Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) | `1` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--gpu <INT>` | Use GPU (CUDA) if possible | `0` |
| `--gpu-server <INT>` | Use GPU server | `0` |
| `--gpu-server-wait-timeout <INT>` | Wait for GPU server for 0: don't wait -1: no wait limit: >0 this many seconds | `600` |
| `--mpi-runner <STR>` | Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") | `[]` |
| `--force-reuse <BOOL>` | Reuse tmp filse in tmp/latest folder ignoring parameters and version changes | `0` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `1` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |
| `--chain-alignments <INT>` | Chain overlapping alignments | `0` |
| `--merge-query <INT>` | Combine ORFs/split sequences to a single entry | `1` |
| `--strand <INT>` | Strand selection only works for DNA/DNA search 0: reverse, 1: forward, 2: both | `1` |
| `--db-output <BOOL>` | Return a result DB instead of a text file | `0` |
| `--write-lookup <INT>` | write .lookup file containing mapping from internal id, fasta id and file number | `0` |
