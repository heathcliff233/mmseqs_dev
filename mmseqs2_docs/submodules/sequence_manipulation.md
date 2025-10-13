
# Sequence Manipulation Modules

This document describes the sequence manipulation submodules of MMseqs2.

## `extractorfs`

**Description:**

> Six-frame extraction of open reading frames

**Usage:**
```bash
mmseqs extractorfs <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

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

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |

## `extractframes`

**Description:**

> Extract frames from a nucleotide sequence DB

**Usage:**
```bash
mmseqs extractframes <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--forward-frames <STR>` | Comma-separated list of frames on the forward strand to be extracted | `1,2,3` |
| `--reverse-frames <STR>` | Comma-separated list

| `--translation-table <INT>` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE 9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL 15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL 23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA 29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA | `1` |
| `--translate <INT>` | Translate ORF to amino acid | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |

## `reverseseq`

**Description:**

> Reverse sequences

**Usage:**
```bash
mmseqs reverseseq <i:sequenceDB> <o:revSequenceDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `translateaa`

**Description:**

> Translate amino acid sequences

**Usage:**
```bash
mmseqs translateaa <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `translatenucs`

**Description:**

> Translate nucleotide sequences

**Usage:**
```bash
mmseqs translatenucs <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--translation-table <INT>` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE 9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL 15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL 23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA 29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA | `1` |
| `--translate <INT>` | Translate ORF to amino acid | `0` |
| `--use-all-table-starts <BOOL>` | Use all alternatives for a start codon in the genetic table, if false - only ATG (AUG) | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `recoverlongestorf`

**Description:**

> Recover longest open reading frame

**Usage:**
```bash
mmseqs recoverlongestorf <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

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

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |

## `orftocontig`

**Description:**

> ORF to contig

**Usage:**
```bash
mmseqs orftocontig <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

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

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |

## `makepaddedseqdb`

**Description:**

> Make padded sequence DB

**Usage:**
```bash
mmseqs makepaddedseqdb <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

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

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--create-lookup <INT>` | Create database lookup file (can be very large) | `0` |

## `masksequence`

**Description:**

> Mask sequences

**Usage:**
```bash
mmseqs masksequence <i:sequenceDB> <o:sequenceDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `extractalignedregion`

**Description:**

> Extract aligned regions from sequences

**Usage:**
```bash
mmseqs extractalignedregion <i:queryDB> <i:targetDB> <i:resultDB> <o:sequenceDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--extract-mode <INT>` | Extract from 1: Query, 2: Target | `2` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
