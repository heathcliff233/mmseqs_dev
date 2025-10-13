# Multimer Analysis Modules

Foldseek provides specialized modules for analyzing protein complexes (multimers), including search, clustering, and evaluation of multi-chain protein structures.

## Core Multimer Modules

### `multimersearch`

**Description**: Core multimer search functionality for protein complexes.

**Usage**:
```bash
foldseek multimersearch queryDB targetDB resultDB tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--multimer-tm-threshold <float>` | Complex TM-score threshold | 0.65 |
| `--chain-tm-threshold <float>` | Individual chain TM-score threshold | 0.5 |
| `--interface-lddt-threshold <float>` | Interface LDDT threshold | 0.65 |
| `--alignment-type <int>` | 0=3Di only, 1=TMalign, 2=3Di+AA | 2 |
| `-e <float>` | E-value threshold | 0.001 |
| `--max-seqs <int>` | Maximum sequences per query | 1000 |
| `--comp-bias-corr <int>` | Compositional bias correction | 1 |
| `--mask <int>` | Low complexity masking | 1 |
| `--cov-mode <int>` | 0=bidirectional, 1=target, 2=query | 0 |

**Examples**:

```bash
# Basic multimer search
foldseek multimersearch query_complexes.pdb targetDB multimer_results tmp

# Strict complex matching
foldseek multimersearch query_complexes.pdb targetDB multimer_results tmp \
  --multimer-tm-threshold 0.8 --chain-tm-threshold 0.6 --interface-lddt-threshold 0.7

# Custom alignment type
foldseek multimersearch query_complexes.pdb targetDB multimer_results tmp --alignment-type 1
```

### `multimercluster`

**Description**: Core multimer clustering functionality.

**Usage**:
```bash
foldseek multimercluster inputDB resultDB tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--multimer-tm-threshold <float>` | Complex TM-score threshold | 0.65 |
| `--chain-tm-threshold <float>` | Individual chain TM-score threshold | 0.5 |
| `--interface-lddt-threshold <float>` | Interface LDDT threshold | 0.65 |
| `--cov-mode <int>` | Coverage mode | 0 |
| `--cluster-mode <int>` | Clustering algorithm | 0 |
| `-e <float>` | E-value threshold | 0.001 |
| `--max-seqs <int>` | Maximum sequences per query | 1000 |

**Examples**:

```bash
# Basic multimer clustering
foldseek multimercluster complexesDB multimer_clusters tmp

# Strict multimer clustering
foldseek multimercluster complexesDB multimer_clusters tmp \
  --multimer-tm-threshold 0.8 --chain-tm-threshold 0.7 --interface-lddt-threshold 0.8
```

## Multimer Scoring and Filtering

### `scoremultimer`

**Description**: Score multimer alignments with detailed metrics.

**Usage**:
```bash
foldseek scoremultimer queryDB targetDB alignmentDB scoreDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--multimer-tm-threshold <float>` | Complex TM-score threshold | 0.0 |
| `--chain-tm-threshold <float>` | Chain TM-score threshold | 0.0 |
| `--interface-lddt-threshold <float>` | Interface LDDT threshold | 0.0 |

**Examples**:

```bash
# Score multimer alignments
foldseek scoremultimer queryDB targetDB alignments scored_alignments

# Filter by complex score
foldseek scoremultimer queryDB targetDB alignments scored_alignments --multimer-tm-threshold 0.7
```

### `filtermultimer`

**Description**: Filter multimer results based on complex-specific criteria.

**Usage**:
```bash
foldseek filtermultimer inputDB filterDB outputDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--multimer-tm-threshold <float>` | Complex TM-score threshold | 0.0 |
| `--chain-tm-threshold <float>` | Chain TM-score threshold | 0.0 |
| `--interface-lddt-threshold <float>` | Interface LDDT threshold | 0.0 |
| `--filter-expression <string>` | Custom filter expression | "" |

**Examples**:

```bash
# Filter by complex TM-score
foldseek filtermultimer alignments filtered_alignments outputDB --multimer-tm-threshold 0.7

# Filter by interface LDDT
foldseek filtermultimer alignments filtered_alignments outputDB --interface-lddt-threshold 0.8

# Custom filter expression
foldseek filtermultimer alignments filtered_alignments outputDB \
  --filter-expression '$3 > 0.7 && $5 > 0.8'
```

## Multimer Result Processing

### `createmultimerreport`

**Description**: Generate detailed reports for multimer alignments.

**Usage**:
```bash
foldseek createmultimerreport queryDB targetDB alignmentDB reportDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--format-mode <int>` | Output format | 0 |
| `--db-output <bool>` | Output as database | false |

**Examples**:

```bash
# Create multimer report
foldseek createmultimerreport queryDB targetDB alignments multimer_report

# Convert to TSV
foldseek createtsv queryDB targetDB multimer_report multimer_report.tsv
```

### `expandmultimer`

**Description**: Expand multimer search results with additional information.

**Usage**:
```bash
foldseek expandmultimer queryDB targetDB resultDB expandedDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--max-seqs <int>` | Maximum sequences per query | 1000 |

**Examples**:

```bash
# Expand multimer results
foldseek expandmultimer queryDB targetDB results expanded_results

# Convert to detailed TSV
foldseek createtsv queryDB targetDB expanded_results expanded_results.tsv
```

## Easy Multimer Workflows

### `easy-multimersearch`

**Description**: User-friendly multimer search workflow.

**Usage**:
```bash
foldseek easy-multimersearch queryComplexes targetDB resultDB tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--multimer-tm-threshold <float>` | Complex TM-score threshold | 0.65 |
| `--chain-tm-threshold <float>` | Chain TM-score threshold | 0.5 |
| `--interface-lddt-threshold <float>` | Interface LDDT threshold | 0.65 |
| `--format-mode <int>` | Output format | 0 |
| `--format-output <string>` | Custom output columns | query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,complexassignid |

**Examples**:

```bash
# Basic easy multimer search
foldseek easy-multimersearch complex.pdb targetDB results tmp

# Custom output format
foldseek easy-multimersearch complex.pdb targetDB results tmp \
  --format-output "query,target,complexqtmscore,complexttmscore,complexassignid"

# HTML output
foldseek easy-multimersearch complex.pdb targetDB results.html tmp --format-mode 3
```

### `easy-multimercluster`

**Description**: User-friendly multimer clustering workflow.

**Usage**:
```bash
foldseek easy-multimercluster inputComplexes resultDB tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--multimer-tm-threshold <float>` | Complex TM-score threshold | 0.65 |
| `--chain-tm-threshold <float>` | Chain TM-score threshold | 0.5 |
| `--interface-lddt-threshold <float>` | Interface LDDT threshold | 0.65 |
| `--cov-mode <int>` | Coverage mode | 0 |
| `--cluster-mode <int>` | Clustering algorithm | 0 |

**Examples**:

```bash
# Basic multimer clustering
foldseek easy-multimercluster complexes/ multimer_clusters tmp

# Strict clustering criteria
foldseek easy-multimercluster complexes/ multimer_clusters tmp \
  --multimer-tm-threshold 0.8 --chain-tm-threshold 0.7 --interface-lddt-threshold 0.8
```

## Multimer Output Formats

### Tab-Separated Format (Default)
```
query target fident alnlen mismatch gapopen qstart qend tstart tend evalue bits complexassignid
```

### Custom Complex Output
```
query target complexqtmscore complexttmscore complexu complext complexassignid
```

### Complex Report Format
```
query_complex target_complex matched_chains_q matched_chains_t qTM tTM U_matrix T_vector assignment_id
```

### Multimer Cluster Format
```
# Representative complex
representative_1
member_1
member_2

# Representative complex
representative_2
member_3
member_4
```

## Multimer Analysis Concepts

### Complex TM-Score

**Description**: TM-score calculated for the entire complex after optimal chain assignment.

**Formula**:
```
complexTM = Σ(chainTM_i * chainLength_i) / totalComplexLength
```

### Chain Assignment

**Description**: Optimal assignment of query chains to target chains using Hungarian algorithm.

**Algorithm**:
1. Calculate similarity matrix between all query and target chains
2. Apply Hungarian algorithm for optimal assignment
3. Maximize total similarity score across all chains

### Interface LDDT

**Description**: Local Distance Difference Test for protein-protein interfaces.

**Calculation**:
- Identifies contacting residue pairs between chains
- Calculates LDDT for interface residues
- Provides measure of interface conservation

## Advanced Multimer Features

### Iterative Multimer Search

**Description**: Perform iterative search for improved multimer detection.

**Usage**:
```bash
# First iteration
foldseek multimersearch query_complexes.pdb targetDB iter1 tmp --multimer-tm-threshold 0.8

# Create multimer profiles
foldseek result2structprofile query_complexes.pdb targetDB iter1 multimer_profiles

# Second iteration with profiles
foldseek multimersearch multimer_profiles targetDB iter2 tmp --profile-search
```

### Multimer Quality Assessment

**Description**: Assess quality of multimer alignments.

**Usage**:
```bash
# Score multimer alignments
foldseek scoremultimer queryDB targetDB alignments scored_alignments

# Filter high-quality multimers
foldseek filtermultimer scored_alignments high_quality_multimers outputDB \
  --multimer-tm-threshold 0.7 --interface-lddt-threshold 0.8
```

### Multimer Visualization

**Description**: Generate visualizations of multimer alignments.

**Usage**:
```bash
# Create superimposed structures
foldseek convert2pdb queryDB targetDB multimer_alignments superimposed_complexes/

# Generate HTML report
foldseek createmultimerreport queryDB targetDB multimer_alignments multimer_report
```

## Performance Optimization

### Speed Optimization
- Use appropriate thresholds to reduce search space
- Enable GPU acceleration when available
- Use `--max-seqs` to limit results per query
- Consider using precomputed indexes for large databases

### Memory Optimization
- Use `--sort-by-structure-bits 0` to reduce memory usage
- Split large multimer searches into smaller batches
- Monitor memory usage with `-v 2`

### Sensitivity Optimization
- Adjust TM-score and LDDT thresholds based on requirements
- Use higher thresholds for stricter matching
- Use lower thresholds for broader similarity detection

## Integration Examples

### With Structure Prediction
```bash
# Predict multimer structures
colabfold_batch --num-recycle 3 multimer_sequences.fasta predicted_multimers/

# Search predicted multimers
foldseek easy-multimersearch predicted_multimers/ reference_multimers/ multimer_results tmp
```

### With Experimental Structures
```bash
# Compare predicted vs experimental multimers
foldseek easy-multimersearch predicted_multimers/ experimental_multimers/ comparison_results tmp

# Filter high-confidence matches
foldseek filtermultimer comparison_results high_confidence outputDB \
  --multimer-tm-threshold 0.8 --interface-lddt-threshold 0.7
```

### Large-Scale Analysis
```bash
# Process large multimer datasets
for i in {1..100}; do
    foldseek easy-multimersearch batch_${i}.pdb large_multimer_db results_${i} tmp_${i}
done

# Merge and analyze results
foldseek mergedbs all_multimer_results results_* tmp
foldseek createmultimerreport queryDB targetDB all_multimer_results multimer_analysis
```

These multimer modules provide comprehensive functionality for protein complex analysis, from basic search and clustering to advanced evaluation and visualization.