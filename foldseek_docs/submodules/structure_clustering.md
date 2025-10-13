# Structure Clustering Modules

Foldseek provides specialized modules for clustering protein structures based on structural similarity, supporting both single-chain and multi-chain (multimer) clustering.


### `cluster`

**Description**: Core clustering algorithm for structural data.

**Usage**:
```bash
foldseek cluster sequenceDB alignmentDB resultDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--cluster-mode <int>` | 0=set cover, 1=connected component, 2=greedy | 0 |
| `-c <float>` | Coverage threshold | 0.8 |
| `--min-seq-id <float>` | Minimum sequence identity | 0.3 |
| `--max-seqs <int>` | Maximum sequences per query | 1000 |
| `--cluster-reassign <bool>` | Reassign sequences after clustering | false |

**Examples**:

```bash
# Set cover clustering (default)
foldseek cluster structuresDB alignments cluster_results

# Connected component clustering
foldseek cluster structuresDB alignments cluster_results --cluster-mode 1

# Greedy incremental clustering
foldseek cluster structuresDB alignments cluster_results --cluster-mode 2
```

### `clust`

**Description**: Core clustering algorithm for structural data with advanced options.

**Usage**:
```bash
foldseek clust sequenceDB resultDB clusterDB [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--cluster-mode <int>` | 0=Set-Cover (greedy), 1=Connected component, 2=Greedy by length | 0 |
| `--max-iterations <int>` | Maximum depth for connected component clustering | 1000 |
| `--similarity-type <int>` | 1=alignment score, 2=sequence identity | 2 |
| `--weights <string>` | Weights for cluster prioritization | "" |
| `--cluster-weight-threshold <float>` | Weight threshold for cluster prioritization | 0.9 |

**Examples**:

```bash
# Set cover clustering (default)
foldseek clust structuresDB alignments cluster_results

# Connected component clustering
foldseek clust structuresDB alignments cluster_results --cluster-mode 1

# Greedy clustering by length
foldseek clust structuresDB alignments cluster_results --cluster-mode 2

# Custom cluster weights
foldseek clust structuresDB alignments cluster_results --weights "0.5,0.3,0.2"
```

## Clustering Algorithms

### Set Cover Clustering (Mode 0)

**Description**: Approximates the NP-complete set cover problem using a greedy algorithm.

**Algorithm**:
1. Iteratively selects the structure with most connections
2. Forms cluster with all connected structures
3. Removes clustered structures from consideration
4. Repeats until all structures are clustered

**Use Case**: Optimal for finding representative structures with minimal redundancy.

### Connected Component Clustering (Mode 1)

**Description**: Uses transitive connections to form larger clusters.

**Algorithm**:
1. Starts with structure having most connections
2. Performs breadth-first search to find all reachable structures
3. Forms cluster with all connected structures
4. Repeats with remaining structures

**Use Case**: Good for finding all related structures in a similarity graph.

### Greedy Incremental Clustering (Mode 2)

**Description**: Similar to CD-HIT algorithm, sorts by length and clusters incrementally.

**Algorithm**:
1. Sorts structures by length (longest first)
2. For each structure, finds all similar structures
3. Forms cluster with representative and similar structures
4. Removes clustered structures from consideration

**Use Case**: Good for length-biased clustering where longer structures are preferred as representatives.

## Clustering Output

### Cluster Database Format

The clustering result database contains cluster assignments:

```
# Cluster 0 (representative: structure_0)
structure_0
structure_1
structure_2

# Cluster 1 (representative: structure_5)
structure_5
structure_3
structure_4
```

### Tab-Separated Format

Convert to tab-separated format for analysis:

```bash
foldseek createtsv structuresDB structuresDB clusterDB cluster_results.tsv
```

Output format:
```
#cluster-representative	cluster-member
structure_0	structure_0
structure_0	structure_1
structure_0	structure_2
structure_5	structure_5
structure_5	structure_3
structure_5	structure_4
```

### Representative Sequences

Extract representative sequences:

```bash
foldseek createsubdb clusterDB structuresDB representativesDB
foldseek convert2fasta representativesDB representatives.fasta
```

### All Member Sequences

Extract all sequences with cluster markers:

```bash
foldseek createseqfiledb structuresDB clusterDB all_membersDB
foldseek result2flat structuresDB structuresDB all_membersDB all_members.fasta
```

## Advanced Clustering Features

### Cascaded Clustering

**Description**: Multi-step clustering for improved sensitivity and speed.

**Process**:
1. **Step 1**: Fast clustering with low sensitivity to find initial clusters
2. **Step 2**: Cluster representatives from step 1 with higher sensitivity
3. **Step 3**: Final clustering with maximum sensitivity
4. **Merge**: Combine results from all steps

**Usage**:
```bash
foldseek structurecluster structuresDB cluster_results tmp --single-step-clustering false
```

### Cluster Reassignment

**Description**: Reassigns sequences to better clusters after initial clustering.

**Usage**:
```bash
foldseek structurecluster structuresDB cluster_results tmp --cluster-reassign
```

### Custom Clustering Criteria

**Description**: Use custom similarity thresholds for clustering.

**Usage**:
```bash
# High similarity clustering
foldseek structurecluster structuresDB cluster_results tmp \
  --tmscore-threshold 0.8 --lddt-threshold 0.9 -c 0.9

# Low similarity clustering (more clusters)
foldseek structurecluster structuresDB cluster_results tmp \
  --tmscore-threshold 0.3 --lddt-threshold 0.5 -c 0.5
```

## Multimer Clustering

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

**Examples**:

```bash
# Basic multimer clustering
foldseek multimercluster complexesDB multimer_clusters tmp

# Strict multimer clustering
foldseek multimercluster complexesDB multimer_clusters tmp \
  --multimer-tm-threshold 0.8 --chain-tm-threshold 0.7 --interface-lddt-threshold 0.8
```

## Clustering Evaluation

### Cluster Quality Assessment

**Description**: Evaluate clustering quality using various metrics.

**Usage**:
```bash
# Calculate cluster statistics
foldseek result2stats structuresDB clusterDB cluster_stats

# Convert to TSV for analysis
foldseek createtsv structuresDB clusterDB cluster_stats cluster_stats.tsv
```

### Cluster Size Distribution

**Description**: Analyze the distribution of cluster sizes.

**Usage**:
```bash
# Get cluster sizes
foldseek createtsv structuresDB structuresDB clusterDB cluster_sizes.tsv

# Analyze with standard tools
awk 'NR>1 {print $2}' cluster_sizes.tsv | sort | uniq -c | sort -nr
```

## Performance Optimization

### Speed Optimization
- Use `--single-step-clustering` for faster clustering
- Lower `-s` values for faster prefiltering
- Use `--max-seqs` to limit sequences per query
- Enable GPU acceleration when available

### Memory Optimization
- Use `--sort-by-structure-bits 0` to reduce memory usage
- Split large datasets into smaller chunks
- Use precomputed indexes for repeated clustering
- Monitor memory usage with `-v 2`

### Sensitivity Optimization
- Use higher `-s` values for distant homology detection
- Enable `--cluster-reassign` for better cluster assignments
- Use `--alignment-type 1` for TM-align based clustering
- Adjust coverage and identity thresholds based on requirements

## Integration Examples

### With Structure Prediction
```bash
# Predict structures
colabfold_batch sequences.fasta predicted_structures/

# Cluster predicted structures
foldseek structurecluster predicted_structures/ predicted_clusters tmp

# Extract representatives
foldseek createsubdb predicted_clusters predicted_structures/ representativesDB
foldseek convert2fasta representativesDB representatives.fasta
```

### With Experimental Validation
```bash
# Cluster experimental structures
foldseek structurecluster experimental_structures/ experimental_clusters tmp

# Compare with predicted structures
foldseek structuresearch predicted_structures/ experimental_structures/ comparison_results tmp
```

### Large-Scale Clustering
```bash
# Split large dataset
foldseek splitdb large_structuresDB large_structuresDB_split --split 10

# Cluster each split
for i in {0..9}; do
    foldseek structurecluster large_structuresDB_split_${i}_10 cluster_results_${i} tmp_${i}
done

# Merge cluster results
foldseek mergeclusters large_structuresDB final_clusters cluster_results_*
```

These clustering modules provide comprehensive functionality for structural similarity-based grouping, supporting various algorithms and evaluation methods for different use cases.