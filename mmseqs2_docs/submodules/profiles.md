# Profiles Modules

This document describes the profiles submodules of MMseqs2.

## `msa2profile`

**Description:**

> Convert a MSA DB to a profile DB

**Usage:**
```bash
mmseqs msa2profile <i:msaDB> <o:profileDB> [options]
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
| `--match-mode <INT>` | 0: Columns that have a residue in the first sequence are kept, 1: columns that have a residue in --match-ratio of all sequences are kept | `0` |
| `--match-ratio <FLOAT>` | Columns that have a residue in this ratio of all sequences are kept | `0.500` |
| `--pseudo-cnt-mode <INT>` | use 0: substitution-matrix or 1: context-specific pseudocounts | `0` |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |
| `--wg <BOOL>` | Use global sequence weighting for profile calculation | `0` |
| `--filter-msa <INT>` | Filter msa: 0: do not filter, 1: filter | `1` |
| `--filter-min-enable <INT>` | Only filter MSAs with more than N sequences, 0 always filters | `0` |
| `--cov <FLOAT>` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] | `0.000` |
| `--qid <STR>` | Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0] Alternatively, can be a list of multiple thresholds: E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] | `0.0` |
| `--qsc <FLOAT>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] | `-20.000` |
| `--max-seq-id <FLOAT>` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] | `0.900` |
| `--diff <INT>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | `1000` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--msa-type <INT>` | MSA Type: 0: cA3M, 1: A3M, 2: FASTA | `2` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--skip-query <BOOL>` | Skip the query sequence | `0` |

**Examples:**
```bash

# Convert globally aligned MSAs to profiles

# Defines columns as match columns if more than 50% of residues are not gaps

# Non-match columns are discarded
mmseqs msa2profile msaDB profileDB --match-mode 1 --match-ratio 0.5

# Assign match-columns through the first sequence

# Gaps in query sequence define non-match columns and are discarded
mmseqs msa2profile msaDB profileDB --match-mode 0
```

## `msa2result`

**Description:**

> Convert a MSA DB to a profile DB

**Usage:**
```bash
mmseqs msa2result <i:msaDB> <o:seqDB> <o:profileDB> [options]
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
| `--match-mode <INT>` | 0: Columns that have a residue in the first sequence are kept, 1: columns that have a residue in --match-ratio of all sequences are kept | `0` |
| `--match-ratio <FLOAT>` | Columns that have a residue in this ratio of all sequences are kept | `0.500` |
| `--pseudo-cnt-mode <INT>` | use 0: substitution-matrix or 1: context-specific pseudocounts | `0` |
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |
| `--wg <BOOL>` | Use global sequence weighting for profile calculation | `0` |
| `--filter-msa <INT>` | Filter msa: 0: do not filter, 1: filter | `1` |
| `--filter-min-enable <INT>` | Only filter MSAs with more than N sequences, 0 always filters | `0` |
| `--cov <FLOAT>` | Filter output MSAs using min. fraction of query residues covered by matched sequences [0.0,1.0] | `0.000` |
| `--qid <STR>` | Reduce diversity of output MSAs using min.seq. identity with query sequences [0.0,1.0] Alternatively, can be a list of multiple thresholds: E.g.: 0.15,0.30,0.50 to defines filter buckets of ]0.15-0.30] and ]0.30-0.50] | `0.0` |
| `--qsc <FLOAT>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences [-50.0,100.0] | `-20.000` |
| `--max-seq-id <FLOAT>` | Reduce redundancy of output MSA using max. pairwise sequence identity [0.0,1.0] | `0.900` |
| `--diff <INT>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | `1000` |

### Misc Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--msa-type <INT>` | MSA Type: 0: cA3M, 1: A3M, 2: FASTA | `2` |

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--sub-mat <TWIN>` | Substitution matrix file | `aa:blosum62.out,nucl:nucleotide.out` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

### Expert Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--skip-query <BOOL>` | Skip the query sequence | `0` |

## `result2profile`

**Description:**

> Compute profile DB from a result DB

**Usage:**
```bash
mmseqs result2profile <i:queryDB> <i:targetDB> <i:resultDB> <o:profileDB> [options]
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
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--gap-open <TWIN>` | Gap open cost | `aa:11,nucl:5` |
| `--gap-extend <TWIN>` | Gap extension cost | `aa:1,nucl:2` |

### Profile Options
| Flag | Description | Default |
| :--- | :--- | :--- |
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
| `--pca` | Pseudo count admixture strength | `[]` |
| `--pcb` | Pseudo counts: Neff at half of maximum admixture (range 0.0-inf) | `[]` |
| `--profile-output-mode <INT>` | Profile output mode: 0: binary log-odds 1: human-readable frequencies | `0` |

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

## `convertmsa`

**Description:**

> Convert STOCKHOLM file to MSA DB

**Usage:**
```bash
mmseqs convertmsa <i:msaFile.sto[.gz]> <o:msaDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--identifier-field <INT>` | Field from STOCKHOLM comments for choosing the MSA identifier: 0: ID, 1: AC. If the respective comment does not exist, the name of the first sequence will become the identifier | `1` |
| `--compressed <INT>` | Write compressed output | `0` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |

- Mirdita M, Steinegger M, Soding J: MMseqs2 desktop and local web server app for fast, interactive sequence searches. Bioinformatics, 35(16), 2856-2858 (2019)

## `tsv2exprofiledb`

**Description:**

> Convert TSV files to extended profile DB

**Usage:**
```bash
mmseqs tsv2exprofiledb <i:tsvFilesBase> <o:exprofileDB> [options]
```

**Parameters:**

### Common Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--gpu <INT>` | Use GPU (CUDA) if possible | `0` |
| `--threads <INT>` | Number of CPU-cores used (all by default) | `10` |
| `--compressed <INT>` | Write compressed output | `1` |
| `-v <INT>` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info | `3` |
