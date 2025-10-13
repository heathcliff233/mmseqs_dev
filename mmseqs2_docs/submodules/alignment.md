
# Alignment Modules

This document describes the alignment submodules of MMseqs2.

## `align`

**Description:**

> Optimal gapped local alignment

**Usage:**
```bash
mmseqs align <i:queryDB> <i:targetDB> <i:resultDB> <o:alignmentDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id | `0` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--zdrop <INT>` | Maximal allowed difference between score values before alignment is truncated (nucleotide alignment only) | `40` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

- Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)

## `alignall`

**Description:**

> Align all-vs-all

**Usage:**
```bash
mmseqs alignall <i:sequenceDB> <i:resultDB> <o:alignmentDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--zdrop <INT>` | Maximal allowed difference between score values before alignment is truncated (nucleotide alignment only) | `40` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `alignbykmer`

**Description:**

> Rescore diagonals.

**Usage:**
```bash
mmseqs alignbykmer <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `1` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length 1: shorter, 2: longer sequence | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |

## `expandaln`

**Description:**

> Expand alignment

**Usage:**
```bash
mmseqs expandaln <i:queryDB> <i:targetDB> <i:resultDB> <i:resultDB|ca3mDB> <o:alignmentDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--pseudo-cnt-mode <INT>` | use 0: substitution-matrix or 1: context-specific pseudocounts | `0` |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |
| `--filter-min-enable <INT>` | Only filter MSAs with more than N sequences, 0 always filters | `0` |
| `--max-seq-id <FLOAT>` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] | `0.900` |
| `--qid <STR>` | Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0] Alternatively, can be a list of multiple thresholds: E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] | `0.0` |
| `--qsc <FLOAT>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] | `-20.000` |
| `--cov <FLOAT>` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] | `0.000` |
| `--diff <INT>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | `1000` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--expansion-mode <INT>` | Update score, E-value, and sequence identity by 0: input alignment 1: rescoring the inferred backtrace | `0` |
| `--expand-filter-clusters <INT>` | Filter each target cluster during expansion 0: no filter 1: filter | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--compressed <INT>` | Write compressed output | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `offsetalignment`

**Description:**

> Offset alignment

**Usage:**
```bash
mmseqs offsetalignment <i:queryDB> <i:queryOrfDB> <i:targetDB> <i:targetOrfDB> <i:alnDB> <o:alnDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--search-type <INT>` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--chain-alignments <INT>` | Chain overlapping alignments | `0` |
| `--merge-query <INT>` | Combine ORFs/split sequences to a single entry | `1` |

## `proteinaln2nucl`

**Description:**

> Protein alignment to nucleotide alignment

**Usage:**
```bash
mmseqs proteinaln2nucl <i:nuclQueryDB> <i:nuclTargetDB> <i:aaQueryDB> <i:aaTargetDB> <i:alnDB> <o:alnDB> [options]
```

**Parameters:**

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `rescorediagonal`

**Description:**

> Rescore diagonals

**Usage:**
```bash
mmseqs rescorediagonal <i:queryDB> <i:targetDB> <i:prefilterDB> <o:resultDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length 1: shorter, 2: longer sequence | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--rescore-mode <INT>` | Rescore diagonals with: 0: Hamming distance, 1: local alignment (score only), 2: local alignment, 3: global alignment, 4: longest alignment fulfilling window quality criterion | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |
