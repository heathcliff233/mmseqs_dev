# Result Handling Modules

This document describes the result handling submodules of MMseqs2.

## `convertalis`

**Description:**

> Convert alignment DB to BLAST-tab, SAM or custom format

**Usage:**
```bash
mmseqs convertalis <i:queryDb> <i:targetDb> <i:alignmentDB> <o:alignmentFile> [options]
```

**Parameters:**

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--format-mode <INT>` | Output format: 0: BLAST-TAB, 1: SAM, 2: BLAST-TAB + query/db length, 3: Pretty HTML, 4: BLAST-TAB + column headers, BLAST-TAB (0) and BLAST-TAB + column headers (4) support custom output formats (--format-output) | `0` |
| `--format-output <STR>` | Choose comma separated list of output columns from: query,target,evalue,gapopen,pident,fident,nident,qstart,qend,qlen tstart,tend,tlen,alnlen,raw,bits,cigar,qseq,tseq,qheader,theader,qaln,taln,qframe,tframe,mismatch,qcov,tcov qset,qsetid,tset,tsetid,taxid,taxname,taxlineage,qorfstart,qorfend,torfstart,torfend,ppos | `query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits` |
| `--translation-table <INT>` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE 9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL 15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL 23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA 29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA | `1` |
| `--search-type <INT>` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--db-output <BOOL>` | Return a result DB instead of a text file | `0` |

**Examples:**
```bash

# Create output in BLAST M8 format (12 columns):

#  (1,2) identifiers for query and target sequences/profiles,

#  (3) sequence identity, (4) alignment length, (5) number of mismatches,

#  (6) number of gap openings, (7-8, 9-10) alignment start and end-position in query and in target,

#  (11) E-value, and (12) bit score
mmseqs convertalis queryDB targetDB result.m8

# Create a TSV containing pairwise alignments
mmseqs convertalis queryDB targetDB result.tsv --format-output query,target,qaln,taln

# Annotate a alignment result with taxonomy information from targetDB
mmseqs convertalis queryDB targetDB result.tsv --format-output query,target,taxid,taxname,taxlineage

 Create SAM output
mmseqs convertalis queryDB targetDB result.sam --format-mode 1

# Create a TSV containing which query file a result comes from
mmseqs createdb euk_queries.fasta bac_queries.fasta queryDB
mmseqs convertalis queryDB targetDB result.tsv --format-output qset,query,target
```

## `createtsv`

**Description:**

> Convert result DB to tab-separated flat file

**Usage:**
```bash
mmseqs createtsv <i:queryDB> [<i:targetDB>] <i:resultDB> <o:tsvFile> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--first-seq-as-repr <BOOL>` | Use the first sequence of the clustering result as representative sequence | `0` |
| `--target-column <INT>` | Select a target column (default 1), 0 if no target id exists | `1` |
| `--full-header <BOOL>` | Replace DB ID by its corresponding Full Header | `0` |
| `--idx-seq-src <INT>` | 0: auto, 1: split/translated sequences, 2: input sequences | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
| `--db-output <BOOL>` | Return a result DB instead of a text file | `0` |

## `result2flat`

**Description:**

> Create flat file by adding FASTA headers to DB entries

**Usage:**
```bash
mmseqs result2flat <i:queryDB> <i:targetDB> <i:resultDB> <o:fastaDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--use-fasta-header <BOOL>` | Use the id parsed from the fasta header as the index key instead of using incrementing numeric identifiers | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `createseqfiledb`

**Description:**

> Create a DB of unaligned FASTA entries

**Usage:**
```bash
mmseqs createseqfiledb <i:sequenceDB> <i:resultDB> <o:fastaDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--min-sequences <INT>` | Minimum number of sequences a cluster may contain | `1` |
| `--max-sequences <INT>` | Maximum number of sequences a cluster may contain | `2147483647` |
| `--hh-format <BOOL>` | Format entries to use with hhsuite (for singleton clusters) | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

**Examples:**
```bash

# Gather all sequences from a cluster DB
mmseqs createseqfiledb sequenceDB clusterDB unalignedDB --min-sequences 2

# Build MSAs with Clustal-Omega
mmseqs apply unalignedDB msaDB -- clustalo -i - -o stdout --threads=1
```

## `swapresults`

**Description:**

> Transpose prefilter/alignment DB

**Usage:**
```bash
mmseqs swapresults <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `result2rbh`

**Description:**

> Filter a merged result DB to retain only reciprocal best hits

**Usage:**
```bash
mmseqs result2rbh <i:resultDB> <o:resultDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `result2msa`

**Description:**

> Compute MSA DB from a result DB

**Usage:**
```bash
mmseqs result2msa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]
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

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-msa <INT>` | Filter msa: 0: do not filter, 1: filter | `0` |
| `--filter-min-enable <INT>` | Only filter MSAs with more than N sequences, 0 always filters | `0` |
| `--max-seq-id <FLOAT>` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] | `0.900` |
| `--qid <STR>` | Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0] Alternatively, can be a list of multiple thresholds: E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] | `0.0` |
| `--qsc <FLOAT>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] | `-20.000` |
| `--cov <FLOAT>` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] | `0.000` |
| `--diff <INT>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | `1000` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--allow-deletion <BOOL>` | Allow deletions in a MSA | `0` |
| `--msa-format-mode <INT>` | Format MSA as: 0: binary cA3M DB, 1: binary ca3m w. consensus DB, 2: aligned FASTA DB, 3: aligned FASTA w. header summary, 4: STOCKHOLM flat file, 5: A3M format, 6: A3M format w. alignment info | `2` |

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
| `--summary-prefix <STR>` | Set the cluster summary prefix | `cl` |
| `--skip-query <BOOL>` | Skip the query sequence | `0` |

## `result2dnamsa`

**Description:**

> Compute MSA DB with out insertions in the query for DNA sequences

**Usage:**
```bash
mmseqs result2dnamsa <i:queryDB> <i:targetDB> <i:resultDB> <o:msaDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--skip-query <BOOL>` | Skip the query sequence | `0` |

## `result2stats`

**Description:**

> Compute statistics for each entry in a DB

**Usage:**
```bash
mmseqs result2stats <i:queryDB> <i:targetDB> <i:resultDB> <o:statsDB> [options]
```

**Parameters:**

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--stat <STR>` | One of: linecount, mean, min, max, doolittle, charges, seqlen, firstline | `[]` |
| `--tsv <BOOL>` | Return output in TSV format | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `filterresult`

**Description:**

> Pairwise alignment result filter

**Usage:**
```bash
mmseqs filterresult <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | keep the query (representative) sequence | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--filter-min-enable <INT>` | Only filter MSAs with more than N sequences, 0 always filters | `0` |
| `--max-seq-id <FLOAT>` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] | `0.900` |
| `--qid <STR>` | Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0] Alternatively, can be a list of multiple thresholds: E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] | `0.0` |
| `--qsc <FLOAT>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] | `-20.000` |
| `--cov <FLOAT>` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] | `0.000` |
| `--diff <INT>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | `1000` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--allow-deletion <BOOL>` | Allow deletions in a MSA | `0` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `result2repseq`

**Description:**

> Get representative sequences from result DB

**Usage:**
```bash
mmseqs result2repseq <i:sequenceDB> <i:resultDB> <o:sequenceDb> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--db-load-mode <INT>` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch | `0` |
| `--compressed <INT>` | Write compressed output | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `sortresult`

**Description:**

> Sort a result DB in the same order as the prefilter or align module

**Usage:**
```bash
mmseqs sortresult <i:resultbDB> <o:resultDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--compressed <INT>` | Write compressed output | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `summarizealis`

**Description:**

> Summarize alignment result to one row (uniq. cov., cov., avg. seq. id.)

**Usage:**
```bash
mmseqs summarizealis <i:alignmentDB> <o:summerizedDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

## `summarizeresult`

**Description:**

> Extract annotations from alignment DB

**Usage:**
```bash
mmseqs summarizeresult <i:alignmentDB> <o:alignmentDB> [options]
```

**Parameters:**

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--overlap <FLOAT>` | Maximum overlap of covered regions | `0.000` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
