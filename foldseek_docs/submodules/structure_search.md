# Structure Search Modules

Foldseek provides several modules for performing structural similarity searches, from high-level workflows to low-level alignment algorithms.

## Core Search Modules

### `search`

**Description**: Main structural search module combining prefiltering and alignment.

**Usage**:
```bash
foldseek search queryDB targetDB resultDB tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `-s <float>` | Sensitivity (1.0-9.5, higher = more sensitive) | 9.5 |
| `--alignment-type <int>` | 0=3Di only, 1=TMalign, 2=3Di+AA | 2 |
| `--max-seqs <int>` | Maximum sequences per query | 1000 |
| `-e <float>` | E-value threshold | 10.0 |
| `--max-accept <int>` | Maximum accepted alignments per query | 2147483647 |
| `--max-rejected <int>` | Maximum consecutive rejections before stopping | 2147483647 |
| `--prefilter-mode <int>` | 0=3Di k-mer, 1=ungapped alignment | 0 |
| `--diag-score <bool>` | Enable diagonal score computation | true |
| `--min-ungapped-score <int>` | Minimum ungapped alignment score | 30 |
| `--comp-bias-corr <int>` | Compositional bias correction | 1 |
| `--mask <int>` | Low complexity masking | 0 |
| `--mask-prob <float>` | Masking probability threshold | 1.0 |
| `--gpu <int>` | Enable GPU acceleration | 0 |

**Examples**:

```bash
# Basic structural search
foldseek search queryDB targetDB results tmp

# High sensitivity search
foldseek search queryDB targetDB results tmp -s 9.5 --alignment-type 1

# Fast search with lower sensitivity
foldseek search queryDB targetDB results tmp -s 7.5 --max-seqs 300

# GPU-accelerated search
foldseek search queryDB targetDB results tmp --gpu 1 --prefilter-mode 1
```

### `structurealign`

**Description**: Direct structural alignment between two structure sets.

**Usage**:
```bash
foldseek structurealign queryDB targetDB resultDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--alignment-type <int>` | 0=3Di only, 1=TMalign, 2=3Di+AA | 2 |
| `--tmscore-threshold <float>` | TM-score threshold | 0.0 |
| `--lddt-threshold <float>` | LDDT threshold | 0.0 |
| `--max-seqs <int>` | Maximum sequences per query | 1000 |
| `-e <float>` | E-value threshold | 0.001 |
| `--comp-bias-corr <int>` | Compositional bias correction | 1 |
| `--mask <int>` | Low complexity masking | 1 |

**Examples**:

```bash
# Direct structural alignment
foldseek structurealign queryDB targetDB alignments

# TM-align based alignment
foldseek structurealign queryDB targetDB alignments --alignment-type 1 --tmscore-threshold 0.5

# High-quality alignments only
foldseek structurealign queryDB targetDB alignments --lddt-threshold 0.7
```

### `tmalign`

**Description**: TM-align based structural alignment.

**Usage**:
```bash
foldseek tmalign queryDB targetDB resultDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--tmscore-threshold <float>` | TM-score threshold | 0.0 |
| `--tmscore-threshold-mode <int>` | 0=alignment, 1=query, 2=target | 0 |
| `--max-seqs <int>` | Maximum sequences per query | 1000 |
| `-e <float>` | E-value threshold | 0.001 |

**Examples**:

```bash
# TM-align with default settings
foldseek tmalign queryDB targetDB tm_results

# Strict TM-score threshold
foldseek tmalign queryDB targetDB tm_results --tmscore-threshold 0.6

# Query-normalized TM-scores
foldseek tmalign queryDB targetDB tm_results --tmscore-threshold-mode 1
```

<!-- Moved `aln2tmscore` to structure_manipulation.md to avoid duplication. -->

### `structurerescorediagonal`

**Description**: Structure-based rescoring of diagonals from prefiltering.

**Usage**:
```bash
foldseek structurerescorediagonal queryDB targetDB prefilterDB resultDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--alignment-type <int>` | 0=3Di only, 1=TMalign, 2=3Di+AA | 2 |
| `--tmscore-threshold <float>` | TM-score threshold | 0.0 |
| `--lddt-threshold <float>` | LDDT threshold | 0.0 |
| `-e <float>` | E-value threshold | 10.0 |
| `-c <float>` | Coverage threshold | 0.0 |
| `--cov-mode <int>` | 0=bidirectional, 1=target, 2=query | 0 |
| `--exact-tmscore <int>` | Use exact TM-score calculation | 0 |

**Examples**:

```bash
# Rescore diagonals with structural alignment
foldseek structurerescorediagonal queryDB targetDB prefilterDB rescored_results

# TM-align based rescoring
foldseek structurerescorediagonal queryDB targetDB prefilterDB rescored_results --alignment-type 1

# Filter by TM-score during rescoring
foldseek structurerescorediagonal queryDB targetDB prefilterDB rescored_results --tmscore-threshold 0.5
```



<!-- Moved `convert2pdb` to structure_manipulation.md to avoid duplication. -->

## Advanced Search Features

### Iterative Search

**Description**: Perform iterative structural search for improved sensitivity.

**Usage**:
```bash
foldseek structuresearch queryDB targetDB iter1 tmp -s 9.5 --num-iterations 1
foldseek result2structprofile queryDB targetDB iter1 profileDB
foldseek structuresearch profileDB targetDB iter2 tmp --profile-search
```

### Profile-Based Search

**Description**: Search using structural profiles for improved sensitivity.

**Usage**:
```bash
# Create structural profiles
foldseek result2structprofile queryDB targetDB search_results profileDB

# Search with profiles
foldseek structuresearch profileDB targetDB profile_results tmp --profile-search
```

### GPU-Accelerated Search

**Description**: Use GPU acceleration for faster searches.

**Usage**:
```bash
# Prepare database for GPU
foldseek makepaddeddb targetDB targetDB_gpu

# GPU-accelerated search
foldseek structuresearch queryDB targetDB_gpu results tmp --gpu 1 --prefilter-mode 1
```

## Search Output Formats

### Tab-Separated Format (Default)
```
query target fident alnlen mismatch gapopen qstart qend tstart tend evalue bits
```

### Custom Output with Structural Information
```
query target alntmscore qtmscore ttmscore lddt u t
```

### SAM Format
```sam
@SQ	SN:target1	LN:150
query1	0	target1	1	255	50M	*	0	0	*	*	AS:i:100	NM:i:0
```

### BLAST Format
```blast
# BLASTP 2.2.26+
# Query: query1
# Database: targetDB
query1	target1	95.67	150	6	2	1	150	1	150	0.0	300
```

## Performance Optimization

### Search Speed Optimization
- Use lower `-s` values for faster searches
- Enable GPU acceleration with `--gpu 1 --prefilter-mode 1`
- Use `--max-seqs` to limit results per query
- Use `--max-rejected` to stop early when no good hits are found

### Search Sensitivity Optimization
- Use higher `-s` values for distant homology detection
- Enable `--num-iterations` for iterative refinement
- Use `--alignment-type 1` for TM-align based scoring
- Adjust `-e` threshold based on requirements

### Memory Optimization
- Use `--sort-by-structure-bits 0` to reduce memory usage
- Split large searches into smaller batches
- Use precomputed indexes for repeated searches
- Monitor memory usage with `-v 2`

These structure search modules provide comprehensive functionality for structural similarity analysis, from basic searches to advanced GPU-accelerated and profile-based methods.
