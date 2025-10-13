
# Prefiltering Modules

This document describes the prefiltering submodules of MMseqs2.

## `prefilter`

**Description:**

> Double consecutive diagonal k-mer search

**Usage:**
```bash
mmseqs prefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]
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
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |
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
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--taxon-list <STR>` | Taxonomy ID, possibly multiple values separated by ',' | `[]` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `ungappedprefilter`

**Description:**

> Optimal diagonal score search

**Usage:**
```bash
mmseqs ungappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--min-ungapped-score <INT>` | Accept only matches with ungapped alignment score above threshold | `15` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--taxon-list <STR>` | Taxonomy ID, possibly multiple values separated by ',' | `[]` |
| `--prefilter-mode <INT>` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--gpu <INT>` | Use GPU (CUDA) if possible | `0` |
| `--gpu-server <INT>` | Use GPU server | `0` |
| `--gpu-server-wait-timeout <INT>` | Wait for GPU server for 0: don't wait -1: no wait limit: >0 this many seconds | `600` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `gappedprefilter`

**Description:**

> Optimal Smith-Waterman-based prefiltering (slow)

**Usage:**
```bash
mmseqs gappedprefilter <i:queryDB> <i:targetDB> <o:prefilterDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--min-ungapped-score <INT>` | Accept only matches with ungapped alignment score above threshold | `15` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--taxon-list <STR>` | Taxonomy ID, possibly multiple values separated by ',' | `[]` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `kmermatcher`

**Description:**

> Find bottom-m-hashed k-mer matches within sequence DB

**Usage:**
```bash
mmseqs kmermatcher <i:sequenceDB> <o:prefilterDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:13,nucl:5` |
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
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.800` |

### Kmermatcher Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--kmer-per-seq <INT>` | k-mers per sequence | `0` |
| `--kmer-per-seq-scale <TWIN>` | Scale k-mer per sequence based on sequence length as kmer-per-seq val + scale x seqlen | `aa:0.000,nucl:0.200` |
| `--adjust-kmer-len <BOOL>` | Adjust k-mer length based on specificity (only for nucleotides) | `0` |
| `--ignore-multi-kmer <BOOL>` | Skip k-mers occurring multiple times (>=2) | `0` |
| `--hash-shift <INT>` | Shift k-mer hash initialization | `67` |
| `--include-only-extendable <BOOL>` | Include only extendable | `0` |

## `kmersearch`

**Description:**

> k-mer search using index

**Usage:**
```bash
mmseqs kmersearch <i:queryDB> <i:kmerIndexDB> <o:prefilterDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `0` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.800` |

### Kmermatcher Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--kmer-per-seq <INT>` | k-mers per sequence | `0` |
| `--kmer-per-seq-scale <TWIN>` | Scale k-mer per sequence based on sequence length as kmer-per-seq val + scale x seqlen | `aa:0.000,nucl:0.200` |
| `--pick-n-sim-kmer <INT>` | Add N similar k-mers to search | `1` |
| `--result-direction <INT>` | result is 0: query, 1: target centric | `1` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
