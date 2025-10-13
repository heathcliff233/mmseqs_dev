
# Clustering Modules

This document describes the clustering submodules of MMseqs2.

## Common Clustering Arguments

The following are some of the most common command line arguments used across various clustering modules.

| Flag | Description | Default |
| :--- | :--- | :--- |
| `-c <float>` | Coverage threshold. | `0.8` |
| `--cov-mode <int>` | Coverage mode (0: cov of query and target, 1: cov of target, 2: cov of query). | `0` |
| `--min-seq-id <float>` | Minimum sequence identity. | `0.3` |

## `linclust`

**Description:**

> Fast, less sensitive clustering

**Usage:**
```bash
mmseqs linclust <i:sequenceDB> <o:clusterDB> <tmpDir> [options]
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
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `0` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment | `2` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.900` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
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

### Clust Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--cluster-mode <INT>` | 0: Set-Cover (greedy), 1: Connected component (BLASTclust), 2,3: Greedy clustering by sequence length (CDHIT) | `0` |
| `--max-iterations <INT>` | Maximum depth of breadth first search in connected component clustering | `1000` |
| `--similarity-type <INT>` | Type of score used for clustering. 1: alignment score 2: sequence identity | `2` |

### Kmermatcher Options
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

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `0` |
| `--force-reuse <BOOL>` | Reuse tmp files in tmp/latest folder ignoring parameters and version changes | `0` |
| `--mpi-runner <STR>` | Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") | `[]` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |

**Examples:**
```bash

# Linear-time clustering of FASTA file
mmseqs linclust sequenceDB clusterDB tmp

                     --cov-mode 

# Sequence         0    1    2

# Q: MAVGTACRPA  60%  IGN  60%

# T: -AVGTAC---  60% 100%  IGN

# Cutoff -c 0.7    -    +    -

#        -c 0.6    +    +    +

# Cluster nucleotide sequences 
mmseqs easy-linclust nucl.fasta result tmp --kmer-per-seq-scale 0.3
```

## `cluster`

**Description:**

> Slower, sensitive clustering

**Usage:**
```bash
mmseqs cluster <i:sequenceDB> <o:clusterDB> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `-s <FLOAT>` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive | `4.000` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--target-search-mode <INT>` | target search mode (0: regular k-mer, 1: similar k-mer) | `0` |
| `--k-score <TWIN>` | k-mer threshold for generating similar k-mer lists | `seq:2147483647,prof:2147483647` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `20` |
| `--split <INT>` | Split input into N equally distributed chunks. 0: set the best split automatically | `0` |
| `--split-mode <INT>` | 0: split target db; 1: split query db; 2: auto, depending on main memory | `2` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--diag-score <BOOL>` | Use ungapped diagonal scoring during prefilter | `1` |
| `--exact-kmer-matching <INT>` | Extract only exact k-mers for matching (range 0-1) | `0` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--min-ungapped-score <INT>` | Accept only matches with ungapped alignment score above threshold | `15` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `1` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `--local-tmp <STR>` | Path where some of the temporary files will be created | `[]` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.800` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment | `3` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
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

### Clust Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--cluster-mode <INT>` | 0: Set-Cover (greedy), 1: Connected component (BLASTclust), 2,3: Greedy clustering by sequence length (CDHIT) | `0` |
| `--max-iterations <INT>` | Maximum depth of breadth first search in connected component clustering | `1000` |
| `--similarity-type <INT>` | Type of score used for clustering. 1: alignment score 2: sequence identity | `2` |
| `--single-step-clustering <BOOL>` | Switch from cascaded to simple clustering workflow | `0` |
| `--cluster-steps <INT>` | Cascaded clustering steps from 1 to -s | `3` |
| `--cluster-reassign <BOOL>` | Cascaded clustering can cluster sequence that do not fulfill the clustering criteria. Cluster reassignment corrects these errors | `0` |

### Kmermatcher Options
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
| `--taxon-list <STR>` | Taxonomy ID, possibly multiple values separated by ',' | `[]` |
| `--rescore-mode <INT>` | Rescore diagonals with: 0: Hamming distance, 1: local alignment (score only), 2: local alignment, 3: global alignment, 4: longest alignment fulfilling window quality criterion | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `0` |
| `--force-reuse <BOOL>` | Reuse tmp files in tmp/latest folder ignoring parameters and version changes | `0` |
| `--mpi-runner <STR>` | Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") | `[]` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |

**Examples:**
```bash

# Cascaded clustering of FASTA file
mmseqs cluster sequenceDB clusterDB tmp

#                  --cov-mode

# Sequence         0    1    2

# Q: MAVGTACRPA  60%  IGN  60%

# T: -AVGTAC---  60% 100%  IGN

# Cutoff -c 0.7    -    +    -

#        -c 0.6    +    +    +

# Cascaded clustering with reassignment

# - Corrects criteria-violations of cascaded merging

# - Produces more clusters and is a bit slower
mmseqs cluster sequenceDB clusterDB tmp --cluster-reassign
```

- Hauser M, Steinegger M, Soding J: MMseqs software suite for fast and deep clustering and searching of large protein sequence sets. Bioinformatics, 32(9), 1323-1330 (2016)
- Steinegger M, Soding J: Clustering huge protein sequence sets in linear time. Nature Communications, 9(1), 2542 (2018)

## `clust`

**Description:**

> Set-cover clustering

**Usage:**
```bash
mmseqs clust <i:sequenceDB> <i:resultDB> <o:clusterDB> [options]
```

**Parameters:**

### Clust Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--cluster-mode <INT>` | 0: Set-Cover (greedy), 1: Connected component (BLASTclust), 2,3: Greedy clustering by sequence length (CDHIT) | `0` |
| `--max-iterations <INT>` | Maximum depth of breadth first search in connected component clustering | `1000` |
| `--similarity-type <INT>` | Type of score used for clustering. 1: alignment score 2: sequence identity | `2` |

### Kmermatcher Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--weights <STR>` | Weights used for cluster priorization | `[]` |
| `--cluster-weight-threshold <FLOAT>` | Weight threshold used for cluster priorization | `0.900` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `clusthash`

**Description:**

> Hash clustering

**Usage:**
```bash
mmseqs clusthash <i:sequenceDB> <o:alignmentDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:3,nucl:5` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.990` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `clusterupdate`

**Description:**

> Update clustering

**Usage:**
```bash
mmseqs clusterupdate <i:oldSequenceDB> <i:newSequenceDB> <i:oldClustResultDB> <o:newClustResultDB> <tmpDir> [options]
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

### Clust Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--cluster-mode <INT>` | 0: Set-Cover (greedy), 1: Connected component (BLASTclust), 2,3: Greedy clustering by sequence length (CDHIT) | `0` |
| `--max-iterations <INT>` | Maximum depth of breadth first search in connected component clustering | `1000` |
| `--similarity-type <INT>` | Type of score used for clustering. 1: alignment score 2: sequence identity | `2` |
| `--single-step-clustering <BOOL>` | Switch from cascaded to simple clustering workflow | `0` |
| `--cluster-steps <INT>` | Cascaded clustering steps from 1 to -s | `3` |
| `--cluster-reassign <BOOL>` | Cascaded clustering can cluster sequence that do not fulfill the clustering criteria. Cluster reassignment corrects these errors | `0` |

### Kmermatcher Options
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
| `--taxon-list <STR>` | Taxonomy ID, possibly multiple values separated by ',' | `[]` |
| `--rescore-mode <INT>` | Rescore diagonals with: 0: Hamming distance, 1: local alignment (score only), 2: local alignment, 3: global alignment, 4: longest alignment fulfilling window quality criterion | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `0` |
| `--force-reuse <BOOL>` | Reuse tmp files in tmp/latest folder ignoring parameters and version changes | `0` |
| `--mpi-runner <STR>` | Use MPI on compute cluster with this MPI command (e.g. "mpirun -np 42") | `[]` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |

**Examples:**
```bash

# Update clustering workflow

# Perform initial clustering of 5000 sequences
mmseqs createdb <(head -n 10000 examples/DB.fasta) sequenceDB
mmseqs cluster sequenceDB clusterDB tmp

# Use-case 1: Update by only adding sequences
mmseqs createdb examples/QUERY.fasta addedSequenceDB
mmseqs concatdbs sequenceDB addedSequenceDB allSequenceDB
mmseqs concatdbs sequenceDB_h addedSequenceDB_h allSequenceDB_h
mmseqs clusterupdate sequenceDB allSequenceDB clusterDB newSequenceDB newClusterDB tmp

# Use-case 2: Update clustering with deletions)

# Create a FASTA file missing 500 of the original sequences and 2500 new ones
mmseqs createdb <(tail -n +1001 examples/DB.fasta | head -n 15000) updateSequenceDB
mmseqs clusterupdate sequenceDB updateSequenceDB clusterDB newSequenceDB newClusterDB tmp
```

- Hauser M, Steinegger M, Soding J: MMseqs software suite for fast and deep clustering and searching of large protein sequence sets. Bioinformatics, 32(9), 1323-1330 (2016)

## `mergeclusters`

**Description:**

> Merge multiple cluster databases

**Usage:**
```bash
mmseqs mergeclusters <i:sequenceDB> <o:clusterDB> <i:clusterDB1> ... <i:clusterDBn> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
