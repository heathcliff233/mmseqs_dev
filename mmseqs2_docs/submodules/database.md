
# Database Management Modules

This document describes the database management submodules of MMseqs2.

## `createdb`

**Description:**

> Convert FASTA/Q file(s) to a sequence DB

**Usage:**
```bash
mmseqs createdb <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]>|<i:stdin> <o:sequenceDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--dbtype <INT>` | Database type 0: auto, 1: amino acid 2: nucleotides | `0` |
| `--shuffle <BOOL>` | Shuffle input database | `1` |
| `--createdb-mode <INT>` | Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) | `0` |
| `--id-offset <INT>` | Numeric ids in index file are offset by this value | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--write-lookup <INT>` | write .lookup file containing mapping from internal id, fasta id and file number | `1` |

**Examples:**
```bash

# Create a sequence database from multiple FASTA files
mmseqs createdb file1.fa file2.fa.gz file3.fa sequenceDB

# Create a seqDB from stdin
cat seq.fasta | mmseqs createdb stdin sequenceDB

# Create a seqDB by indexing existing FASTA/Q (for single line fasta entries only)
mmseqs createdb seq.fasta sequenceDB --createdb-mode 1
```

## `createindex`

**Description:**

> Store precomputed index on disk to reduce search overhead

**Usage:**
```bash
mmseqs createindex <i:sequenceDB> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `1` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `-s <FLOAT>` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive | `7.500` |
| `--k-score <TWIN>` | k-mer threshold for generating similar k-mer lists | `seq:0,prof:0` |
| `--split <INT>` | Split input into N equally distributed chunks. 0: set the best split automatically | `0` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--check-compatible <INT>` | 0: Always recreate index, 1: Check if recreating index is needed, 2: Fail if index is incompatible | `0` |
| `--search-type <INT>` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment | `0` |
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
| `--translation-mode <INT>` | Translation AA seq from nucleotide by 0: ORFs, 1: full reading frames | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `0` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--index-subset <INT>` | Create specialized index with subset of entries 0: normal index, 1: index without headers, 2: index without prefiltering data, 4: index without aln (for cluster db) Flags can be combined bit wise | `0` |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |
| `--strand <INT>` | Strand selection only works for DNA/DNA search 0: reverse, 1: forward, 2: both | `1` |

**Examples:**
```bash

# Create protein sequence index
mmseqs createindex sequenceDB tmp

# Create TBLASTX/N index from nucleotide sequences
mmseqs createindex sequenceDB tmp --search-type 2

# Create BLASTN index from nucleotide sequences
mmseqs createindex sequenceDB tmp --search-type 3
```

## `createlinindex`

**Description:**

> Create linsearch index

**Usage:**
```bash
mmseqs createlinindex <i:sequenceDB> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:blosum62.out,nucl:nucleotide.out` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `0` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `0` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |

### Kmermatcher Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--hash-shift <INT>` | Shift k-mer hash initialization | `67` |
| `--kmer-per-seq <INT>` | k-mers per sequence | `21` |
| `--kmer-per-seq-scale <TWIN>` | Scale k-mer per sequence based on sequence length as kmer-per-seq val + scale x seqlen | `aa:0.000,nucl:0.200` |
| `--adjust-kmer-len <BOOL>` | Adjust k-mer length based on specificity (only for nucleotides) | `0` |
| `--ignore-multi-kmer <BOOL>` | Skip k-mers occurring multiple times (>=2) | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--check-compatible <INT>` | 0: Always recreate index, 1: Check if recreating index is needed, 2: Fail if index is incompatible | `0` |
| `--search-type <INT>` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment | `0` |
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

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--max-seq-len <INT>` | Maximum sequence length | `65535` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `--remove-tmp-files <BOOL>` | Delete temporary files | `0` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |

## `subtractdbs`

**Description:**

> Subtract databases

**Usage:**
```bash
mmseqs subtractdbs <i:resultDBLeft> <i:resultDBRight> <o:resultDB> [options]
```

**Parameters:**

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--e-profile <DOUBLE>` | Include sequences matches with < E-value thr. into the profile (>=0.0) | `1.000E-03` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `tar2db`

**Description:**

> Create database from tar archive

**Usage:**
```bash
mmseqs tar2db <i:tar[.gz]> ... <i:tar[.gz]> <o:resultDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--output-dbtype <INT>` | Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 | `12` |
| `--tar-include <STR>` | Include file names based on this regex | `.*` |
| `--tar-exclude <STR>` | Exclude file names based on this regex | `^$` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

**Examples:**
```bash

# Assuming tar archive containing three aligned FASTA files:

#  * folder/msa1.fa.gz  * folder/msa2.fa  * folder/msa3.fa

# Create a msaDB with three DB entries each containing a separate MSA
mmseqs tar2db archive.tar.gz msaDB --output-dbtype 11
```

## `swapdb`

**Description:**

> Swap query and target in result database

**Usage:**
```bash
mmseqs swapdb <i:resultDB> <o:resultDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

- Mirdita M, Steinegger M, Soding J: MMseqs2 desktop and local web server app for fast, interactive sequence searches. Bioinformatics, 35(16), 2856-2858 (2019)

## `aliasdb`

**Description:**

> Alias database

**Usage:**
```bash
mmseqs aliasdb <i:srcDB> <o:dstDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `cpdb`

**Description:**

> Copy database

**Usage:**
```bash
mmseqs cpdb <i:srcDB> <o:dstDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `concatdbs`

**Description:**

> Concatenate databases

**Usage:**
```bash
mmseqs concatdbs <i:DB> <i:DB> <o:DB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--preserve-keys <BOOL>` | The keys of the two DB should be distinct, and they will be preserved in the concatenation | `0` |
| `--take-larger-entry <BOOL>` | Only keep the larger entry (dataSize >) in the concatenation, both databases need the same keys in the index | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `1` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

**Examples:**
```bash

# Download two sequences databases and concat them
mmseqs databases PDB pdbDB tmp
mmseqs UniProtKB/Swiss-Prot swissprotDB tmp

# Works only single threaded since seq. and header DB need the same ordering
mmseqs concatdbs pdbDB swissprotDB pdbAndSwissprotDB --threads 1
mmseqs concatdbs pdbDB_h swissprotDB_h pdbAndSwissprotDB_h --threads 1
```

## `createsubdb`

**Description:**

> Create sub database

**Usage:**
```bash
mmseqs createsubdb <i:subsetFile|DB> <i:DB> <o:DB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--subdb-mode <INT>` | Subdb mode 0: copy data 1: soft link data and write index | `0` |
| `--id-mode <INT>` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

**Examples:**
```bash

# Create a new sequenceDB from sequenceDB entries with keys 1, 2 and 3
mmseqs createsubdb <(printf '1
2
3
') sequenceDB oneTwoThreeDB

# Create a new sequence database with representatives of clusterDB
mmseqs cluster sequenceDB clusterDB tmp
mmseqs createsubdb clusterDB sequenceDB representativesDB
```

## `db2tar`

**Description:**

> Create tar from database

**Usage:**
```bash
mmseqs db2tar <i:DB> <o:tar[.gz]> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

**Examples:**
```bash

# Create a tar from a MSA DB
mmseqs db2tar msaDB archive.tar.gz
```

## `lndb`

**Description:**

> Hard link database

**Usage:**
```bash
mmseqs lndb <i:srcDB> <o:dstDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `mergedbs`

**Description:**

> Merge multiple databases

**Usage:**
```bash
mmseqs mergedbs <i:DB> <o:DB> <i:DB1> ... <i:DBn> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `splitsequence`

**Description:**

> Split sequences into smaller chunks

**Usage:**
```bash
mmseqs splitsequence <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sequence-overlap <INT>` | Overlap between sequences | `300` |
| `--sequence-split-mode <INT>` | Sequence split mode 0: copy data, 1: soft link data and write new index, | `1` |
| `--headers-split-mode <INT>` | Header split mode: 0: split position, 1: original header | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--max-seq-len <INT>` | Maximum sequence length | `10000` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--prefixes <STR>` | Comma separated list of prefixes for each entry | `[]` |
| `--merge-stop-empty <BOOL>` | Don't continue merging entries after an empty entry | `0` |

## `mvdb`

**Description:**

> Move database

**Usage:**
```bash
mmseqs mvdb <i:srcDB> <o:dstDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `renamedbkeys`

**Description:**

> Rename database keys

**Usage:**
```bash
mmseqs renamedbkeys <i:idMapFile|stdin> <i:DB> <o:DB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--subdb-mode <INT>` | Subdb mode 0: copy data 1: soft link data and write index | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `splitdb`

**Description:**

> Split database into chunks

**Usage:**
```bash
mmseqs splitdb <i:DB> <o:DB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--split <INT>` | Split input into N equally distributed chunks | `0` |
| `--split-aa <BOOL>` | Try to find the best split boundaries by entry lengths | `0` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `tsv2db`

**Description:**

> Convert TSV file to a database

**Usage:**
```bash
mmseqs tsv2db <i:tsvFile> <o:resultDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--output-dbtype <INT>` | Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 | `12` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
