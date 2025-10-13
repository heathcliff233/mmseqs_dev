# Utilities Modules

This document describes the utilities submodules of MMseqs2.

## `compress`

**Description:**

> Compress DB entries

**Usage:**
```bash
mmseqs compress <i:DB> <o:DB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `decompress`

**Description:**

> Decompress DB entries

**Usage:**
```bash
mmseqs decompress <i:DB> <o:DB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `gpuserver`

**Description:**

> Start a GPU server

**Usage:**
```bash
mmseqs gpuserver <i:DB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--prefilter-mode <INT>` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--gpu <INT>` | Use GPU (CUDA) if possible | `0` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |

- Kallenborn F, Chacon A, Hundt C, Sirelkhatim H, Didi K, Dallago C, Mirdita M, Schmidt B, Steinegger M: GPU-accelerated homology search with MMseqs2. bioRxiv, 2024.11.13.623350 (2024)

## `apply`

**Description:**

> Apply external program to each entry in a DB

**Usage:**
```bash
mmseqs apply <i:DB> <o:DB> -- program [args...] [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

**Examples:**
```bash

# Gather all sequences from a cluster DB
mmseqs createseqfiledb sequenceDB clusterDB unalignedDB --min-sequences 2

# Build MSAs with Clustal-Omega
mmseqs apply unalignedDB msaDB -- clustalo -i - -o stdout --threads=1

# Count lines in each DB entry inefficiently (result2stats is way faster)
mmseqs apply DB wcDB -- awk '{ counter++; } END { print counter; }'
```

## `compress`

**Description:**

> Compress DB entries

**Usage:**
```bash
mmseqs compress <i:DB> <o:DB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `decompress`

**Description:**

> Decompress DB entries

**Usage:**
```bash
mmseqs decompress <i:DB> <o:DB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `prefixid`

**Description:**

> Prefix database keys

**Usage:**
```bash
mmseqs prefixid <i:DB> <o:DB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--prefix <STR>` | Use this prefix for all entries | `[]` |
| `--mapping-file <STR>` | Specify a file that translates the keys of a DB to new keys, TSV format | `[]` |
| `--tsv <BOOL>` | Return output in TSV format | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `suffixid`

**Description:**

> Suffix database keys

**Usage:**
```bash
mmseqs suffixid <i:resultDB> <o:resultDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--prefix <STR>` | Use this prefix for all entries | `[]` |
| `--mapping-file <STR>` | Specify a file that translates the keys of a DB to new keys, TSV format | `[]` |
| `--tsv <BOOL>` | Return output in TSV format | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `touchdb`

**Description:**

> Touch database

**Usage:**
```bash
mmseqs touchdb <i:DB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `unpackdb`

**Description:**

> Unpack database entries to flat files

**Usage:**
```bash
mmseqs unpackdb <i:DB> <o:outDir> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--unpack-name-mode <INT>` | Name unpacked files by 0: DB key, 1: accession (through .lookup) | `1` |
| `--unpack-suffix <STR>` | File suffix for unpacked files. Add .gz suffix to write compressed files. | `[]` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `view`

**Description:**

> View database entries

**Usage:**
```bash
mmseqs view <i:DB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--id-list <STR>` | Entries to be printed separated by ',' | `[]` |
| `--id-mode <INT>` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) | `0` |
| `--idx-entry-type <INT>` | 0: sequence, 1: src sequence, 2: header, 3: src header | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

**Examples:**
```bash

# Print entries with keys 1, 2 and 3 from a sequence DB to stdout
mmseqs view sequenecDB --id-list 1,2,3
```

## `filterdb`

**Description:**

> Filter database entries

**Usage:**
```bash
mmseqs filterdb <i:resultDB> <o:resultDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-expression <STR>` | Specify a mathematical expression to filter lines | `[]` |
| `--filter-column <INT>` | column | `1` |
| `--column-to-take <INT>` | column to take in join mode. If -1, the whole line is taken | `-1` |
| `--filter-regex <STR>` | Regex to select column (example float: [0-9]*(.[0-9]+)? int:[1-9]{1}[0-9]) | `^.*$` |
| `--positive-filter <BOOL>` | Used in conjunction with --filter-file. If true, out  = in \intersect filter ; if false, out = in - filter | `1` |
| `--filter-file <STR>` | Specify a file that contains the filtering elements | `[]` |
| `--beats-first <BOOL>` | Filter by comparing each entry to the first entry | `0` |
| `--mapping-file <STR>` | Specify a file that translates the keys of a DB to new keys, TSV format | `[]` |
| `--weights <STR>` | Weights used for cluster priorization | `[]` |
| `--trim-to-one-column <BOOL>` | Output only the column specified by --filter-column | `0` |
| `--extract-lines <INT>` | Extract n lines of each entry | `0` |
| `--comparison-operator <STR>` | Filter by comparing each entry row numerically by using the le) less-than-equal, ge) greater-than-equal or e) equal operator | `[]` |
| `--comparison-value <DOUBLE>` | Filter by comparing each entry to this value | `0.000E+00` |
| `--sort-entries <INT>` | Sort column set by --filter-column, by 0: no sorting, 1: increasing, 2: decreasing, 3: random shuffle, 4: priority | `0` |
| `--join-db <STR>` | Join another database entry with respect to the database identifier in the chosen column | `[]` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

**Examples:**
```bash

# Retain top alignment for each query (alignment DBs are sorted by E-value)
mmseqs filterdb alignmentDB topHitAlignmentDB --extract-lines 1

# Extract alignments with Seq.id. greater than 90%
mmseqs filterdb alignmentDB scoreGreater35AlignmentDB --comparison-operator ge --comparison-value 0.9 --filter-column 2

# Retain all hits matching a regular expression
mmseqs filterdb alignmentDB regexFilteredDB --filter-regex '^[1-9].$' --filter-column 2

# Remove all hits to target keys contained in file db.index
mmseqs filterdb --filter-file db.index --positive-filter false

# Retain all hits matching any boolean expression
mmseqs filterdb --filter-expression '$1 * $2 >= 200'
```

## `setextendeddbtype`

**Description:**

> Set extended database type

**Usage:**
```bash
mmseqs setextendeddbtype <i:DB> <o:DB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--extended-dbtype <INT>` | Set extended database type: 0: no extended type, 1: MSA DB, 2: Profile DB, 3: Consensus DB | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `map`

**Description:**

> Map sequences

**Usage:**
```bash
mmseqs map <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0.0-1.0) | `1.000` |
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
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id | `2` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
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
| `--use-seq-id <BOOL>` | Sequence ID (Uniprot, GenBank, ...) is used for identifying matches between the old and the new DB | `0` |
| `--recover-deleted <BOOL>` | Find and recover deleted sequences during updating of clustering | `0` |

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
| `--remove-tmp-files <BOOL>` | Delete temporary files | `0` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |
| `--chain-alignments <INT>` | Chain overlapping alignments | `0` |
| `--merge-query <INT>` | Combine ORFs/split sequences to a single entry | `1` |
| `--strand <INT>` | Strand selection only works for DNA/DNA search 0: reverse, 1: forward, 2: both | `1` |

## `rbh`

**Description:**

> Reciprocal best hit

**Usage:**
```bash
mmseqs rbh <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0.0-1.0) | `1.000` |
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
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id | `2` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of query and target, 1: coverage of target, 2: coverage of query, 3: target seq. length has to be at least x% of query length, 4: query seq. length has to be at least x% of target length, 5: short seq. needs to be at least x% of the other seq. length | `0` |
| `--score-bias <FLOAT>` | Score bias when computing SW alignment (in bits) | `0.000` |
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
| `--use-seq-id <BOOL>` | Sequence ID (Uniprot, GenBank, ...) is used for identifying matches between the old and the new DB | `0` |
| `--recover-deleted <BOOL>` | Find and recover deleted sequences during updating of clustering | `0` |

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
| `--remove-tmp-files <BOOL>` | Delete temporary files | `0` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-hits <BOOL>` | Filter hits by seq.id. and coverage | `0` |
| `--sort-results <INT>` | Sort results: 0: no sorting, 1: sort by E-value (Alignment) or seq.id. (Hamming) | `0` |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |
| `--chain-alignments <INT>` | Chain overlapping alignments | `0` |
| `--merge-query <INT>` | Combine ORFs/split sequences to a single entry | `1` |
| `--strand <INT>` | Strand selection only works for DNA/DNA search 0: reverse, 1: forward, 2: both | `1` |
