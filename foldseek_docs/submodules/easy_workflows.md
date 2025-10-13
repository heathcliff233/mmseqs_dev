# Easy Workflows

Foldseek provides several easy-to-use workflows that combine multiple modules for common structural analysis tasks. These workflows are designed to be user-friendly while providing access to advanced structural comparison capabilities.

## Easy Search Workflows

### `easy-search`

**Description**: Fast and sensitive protein structure search against a target database.

**Usage**:
```bash
foldseek easy-search queryStructures targetDB resultDB tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `-s <float>` | Sensitivity (1.0-9.5, higher = more sensitive) | 9.5 |
| `--alignment-type <int>` | 0=3Di only, 1=TMalign, 2=3Di+AA | 2 |
| `--format-mode <int>` | Output format (0=tab, 3=HTML, 5=PDB) | 0 |
| `--format-output <string>` | Custom output columns | query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits |
| `-e <float>` | E-value threshold | 0.001 |
| `--max-seqs <int>` | Maximum sequences per query | 1000 |
| `--num-iterations <int>` | Number of search iterations | 0 |
| `--exhaustive-search` | Skip prefilter (slower but more sensitive) | false |
| `--cluster-search <int>` | For clustered DBs: 0=representatives only, 1=all members | 0 |
| `--gpu <int>` | Enable GPU acceleration | 0 |
| `--prefilter-mode <int>` | Prefilter mode (1=GPU-optimized) | 0 |

**Examples**:

```bash
# Basic structural search
foldseek easy-search query.pdb targetDB results tmp

# High sensitivity search with TM-align
foldseek easy-search query.pdb targetDB results tmp -s 9.5 --alignment-type 1

# GPU-accelerated search
foldseek easy-search query.pdb targetDB results tmp --gpu 1 --prefilter-mode 1

# Custom output format
foldseek easy-search query.pdb targetDB results tmp --format-output "query,target,alntmscore,u,t"

# HTML visualization output
foldseek easy-search query.pdb targetDB results.html tmp --format-mode 3
```

### `easy-multimersearch`

**Description**: Search protein complexes (multimers) against a target database.

**Usage**:
```bash
foldseek easy-multimersearch queryComplexes targetDB resultDB tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--multimer-tm-threshold <float>` | Complex TM-score threshold | 0.0 |
| `--chain-tm-threshold <float>` | Individual chain TM-score threshold | 0.0 |
| `--interface-lddt-threshold <float>` | Interface LDDT threshold | 0.0 |
| `--alignment-type <int>` | Alignment algorithm | 2 |
| `-e <float>` | E-value threshold | 0.001 |
| `--format-output <string>` | Custom output columns | query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,complexassignid |

**Examples**:

```bash
# Basic multimer search
foldseek easy-multimersearch complex.pdb targetDB results tmp

# Strict complex matching
foldseek easy-multimersearch complex.pdb targetDB results tmp \
  --multimer-tm-threshold 0.8 --chain-tm-threshold 0.6 --interface-lddt-threshold 0.7

# Custom output with complex scores
foldseek easy-multimersearch complex.pdb targetDB results tmp \
  --format-output "query,target,complexqtmscore,complexttmscore,complexassignid"
```

## Easy Clustering Workflows

### `easy-cluster`

**Description**: Fast protein structure clustering using structural similarity.

**Usage**:
```bash
foldseek easy-cluster inputStructures resultDB tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `-c <float>` | Coverage threshold | 0.0 |
| `--min-seq-id <float>` | Minimum sequence identity | 0.0 |
| `--alignment-type <int>` | 0=3Di only, 1=TMalign, 2=3Di+AA | 2 |
| `--tmscore-threshold <float>` | TM-score threshold | 0.0 |
| `--lddt-threshold <float>` | LDDT threshold | 0.0 |
| `--cov-mode <int>` | 0=bidirectional, 1=target, 2=query | 0 |
| `--cluster-mode <int>` | 0=set cover, 1=connected component, 2=greedy | 0 |
| `-e <float>` | E-value threshold | 0.001 |

**Examples**:

```bash
# Basic structural clustering
foldseek easy-cluster structures/ cluster_results tmp

# High-quality clustering with TM-align
foldseek easy-cluster structures/ cluster_results tmp --alignment-type 1 --tmscore-threshold 0.5

# Clustering with specific coverage requirements
foldseek easy-cluster structures/ cluster_results tmp -c 0.8 --cov-mode 0
```

### `easy-multimercluster`

**Description**: Cluster protein complexes based on structural similarity.

**Usage**:
```bash
foldseek easy-multimercluster inputComplexes resultDB tmpDir [options]
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

**Examples**:

```bash
# Basic multimer clustering
foldseek easy-multimercluster complexes/ multimer_clusters tmp

# Strict multimer clustering
foldseek easy-multimercluster complexes/ multimer_clusters tmp \
  --multimer-tm-threshold 0.8 --chain-tm-threshold 0.7 --interface-lddt-threshold 0.8
```

## Easy RBH Workflow

### `easy-rbh`

**Description**: Reciprocal best hit analysis for structural data.

**Usage**:
```bash
foldseek easy-rbh queryFastaFile1 targetFastaFile|targetDB alignmentFile tmpDir [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `-s <float>` | Sensitivity (1.0-9.5, higher = more sensitive) | 4.0 |
| `--alignment-type <int>` | 0=3Di only, 1=TMalign, 2=3Di+AA | 2 |
| `-e <float>` | E-value threshold | 10.0 |
| `--max-seqs <int>` | Maximum sequences per query | 300 |
| `--format-mode <int>` | Output format (0=tab, 3=HTML, 5=PDB) | 0 |
| `--format-output <string>` | Custom output columns | query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits |

**Examples**:

```bash
# Basic reciprocal best hit analysis
foldseek easy-rbh query.fasta target.fasta rbh_results tmp

# High sensitivity RBH analysis
foldseek easy-rbh query.fasta target.fasta rbh_results tmp -s 9.5 --alignment-type 1

# Custom output format
foldseek easy-rbh query.fasta target.fasta rbh_results tmp --format-output "query,target,alntmscore,u,t"

# HTML visualization output
foldseek easy-rbh query.fasta target.fasta rbh_results.html tmp --format-mode 3
```

## Output Files

Easy workflows generate multiple output files:

### Search Results
- `resultDB`: Main result database
- `resultDB.index`: Result index
- `resultDB_report`: Search report (if applicable)

### Clustering Results
- `resultDB_clu`: Cluster assignments
- `resultDB_clu.index`: Cluster index
- `resultDB_rep_seq.fasta`: Representative sequences
- `resultDB_all_seq.fasta`: All sequences with cluster markers
- `resultDB_cluster.tsv`: Tab-separated cluster assignments

### Multimer Results
- `resultDB`: Complex alignment results
- `resultDB_report`: Complex matching report
- `resultDB_cluster.tsv`: Multimer cluster assignments

## Performance Tips

### Speed Optimization
- Use lower `-s` values for faster searches (e.g., `-s 7.5`)
- Enable GPU acceleration with `--gpu 1 --prefilter-mode 1`
- Use `--max-seqs` to limit results per query
- Use `--exhaustive-search` only when maximum sensitivity is required

### Sensitivity Optimization
- Use higher `-s` values for distant homology detection
- Enable `--num-iterations` for iterative refinement
- Use `--alignment-type 1` for TM-align based scoring
- Adjust `-e` threshold based on your requirements

### Memory Optimization
- Use `--sort-by-structure-bits 0` to reduce memory usage
- Split large searches into smaller batches
- Use precomputed indexes for repeated searches
- Monitor memory usage with `-v 2`

## Integration Examples

### With Structure Prediction
```bash
# Predict structures with ColabFold
colabfold_batch sequences.fasta predicted_structures/

# Search predicted structures
foldseek easy-search predicted_structures/ reference_db results tmp
```

### With Experimental Validation
```bash
# Search against experimental structures
foldseek easy-search predicted_model.pdb experimental_db validation_results tmp

# Filter high-confidence matches
foldseek filterdb validation_results high_confidence --filter-expression '$11 < 1e-10'
```

### Large-Scale Analysis
```bash
# Process large datasets in batches
for i in {1..100}; do
    foldseek easy-search batch_${i}.pdb large_db results_${i} tmp_${i} --max-seqs 100
done

# Merge results
foldseek mergedbs all_results results_* tmp
```

These easy workflows provide a user-friendly interface to Foldseek's powerful structural analysis capabilities while maintaining access to advanced parameters for fine-tuning performance and sensitivity.