# Database Management Modules

Foldseek provides comprehensive database management capabilities, from downloading pre-built databases to creating custom indexes and managing large-scale structural data collections.

## Database Download and Setup

### `databases`

**Description**: Download and set up pre-built structural databases.

**Usage**:
```bash
foldseek databases <name> <o:sequenceDB> <tmpDir> [options]
```

**Available Databases**:

| Database | Type | Taxonomy | URL |
|----------|------|-----|-----------|
| Alphafold/UniProt | Aminoacid | yes | https://alphafold.ebi.ac.uk/ |
| Alphafold/UniProt50-minimal | Aminoacid | yes | https://alphafold.ebi.ac.uk/ |
| Alphafold/UniProt50 | Aminoacid | yes | https://alphafold.ebi.ac.uk/ |
| Alphafold/Proteome | Aminoacid | yes | https://alphafold.ebi.ac.uk/ |
| Alphafold/Swiss-Prot | Aminoacid | yes | https://alphafold.ebi.ac.uk/ |
| ESMAtlas30 | Aminoacid | - | https://esmatlas.com |
| PDB | Aminoacid | yes | https://www.rcsb.org |
| CATH50 | Aminoacid | yes | https://www.cath.info |
| BFMD | Aminoacid | yes | https://foldseek.steineggerlab.workers.dev/bfmd.version |
| BFVD | Aminoacid | yes | https://bfvd.steineggerlab.workers.dev |
| ProstT5 | Aminoacid | - | https://huggingface.co/Rostlab/ProstT5 |

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--tsv <bool>` | Return output in TSV format | 0 |
| `--force-reuse <bool>` | Reuse tmp files in tmp/latest folder ignoring parameters and version changes | 0 |
| `--remove-tmp-files <bool>` | Delete temporary files | 0 |
| `--compressed <int>` | Write compressed output | 0 |
| `--threads <int>` | Number of CPU-cores used (all by default) | 10 |

**Examples**:

```bash
# Download AlphaFold database for Swiss-Prot
foldseek databases Alphafold/Swiss-Prot afdb_swissprot tmp

# Download PDB database
foldseek databases PDB pdb tmp

# Download with multiple threads
foldseek databases Alphafold/UniProt afdb_uniprot tmp --threads 8

# Get database list in TSV format
foldseek databases --tsv
```

## Index Creation and Management

### `createindex`

**Description**: Create precomputed index for faster structural searches.

**Usage**:
```bash
foldseek createindex <i:sequenceDB> <tmpDir> [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--index-subset <int>` | Create specialized index with subset of entries: 0: normal index, 1: index without headers, 2: index without prefiltering data, 4: index without aln (for cluster db), Flags can be combined bit wise | 0 |
| `--check-compatible <int>` | 0: Always recreate index, 1: Check if recreating index is needed, 2: Fail if index is incompatible | 0 |
| `--split <int>` | Split input into N equally distributed chunks. 0: set the best split automatically | 0 |
| `--split-memory-limit <byte>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | 0 |
| `--kmer-size <int>` | k-mer length (0: automatically set to optimum) | 0 |
| `--seed-sub-mat <twin>` | Substitution matrix file for k-mer generation | "aa:3di.out,nucl:3di.out" |
| `--comp-bias-corr <int>` | Correct for locally biased amino acid composition (range 0-1) | 1 |
| `--comp-bias-corr-scale <float>` | Correct for locally biased amino acid composition (range 0-1) | 1.000 |
| `--max-seqs <int>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | 1000 |
| `--mask <int>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | 0 |
| `--mask-prob <float>` | Mask sequences is probablity is above threshold | 1.000 |
| `--mask-lower-case <int>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | 1 |
| `--mask-n-repeat <int>` | Repeat letters that occure > threshold in a rwo | 6 |
| `--spaced-kmer-mode <int>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | 1 |
| `--spaced-kmer-pattern <string>` | User-specified spaced k-mer pattern | "" |
| `-s <float>` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive | 9.500 |
| `--k-score <twin>` | k-mer threshold for generating similar k-mer lists | "seq:2147483647,prof:2147483647" |
| `--threads <int>` | Number of CPU-cores used (all by default) | 10 |
| `--compressed <int>` | Write compressed output | 0 |
| `--remove-tmp-files <bool>` | Delete temporary files | 1 |

**Examples**:

```bash
# Create protein sequence index
foldseek createindex sequenceDB tmp

# Create specialized index with subset of entries
foldseek createindex targetDB tmp --index-subset 2

# Create index with custom parameters
foldseek createindex targetDB tmp --kmer-size 6 --spaced-kmer-mode 1
```

### `createclusearchdb`

**Description**: Create searchable databases from clustered results.

**Usage**:
```bash
foldseek createclusearchdb <i:sequenceDB> <i:clusterDB> <o:sequenceDB> [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--db-suffix-list <string>` | Suffixes for database to be split in rep/seq | "_h,_ss,_ca" |
| `--threads <int>` | Number of CPU-cores used (all by default) | 10 |
| `--compressed <int>` | Write compressed output | 0 |

**Examples**:

```bash
# Cluster database and build a searchable db
foldseek cluster sequenceDB clusterDB tmp --min-seq-id 0.3
foldseek createclusearchdb sequenceDB clusterDB clusterSearchDb
foldseek search sequenceDB clusterSearchDb aln tmp --cluster-search 1
```

## Database Operations

### Database Information and Utilities

Database information can be obtained using standard system tools:

```bash
# List database files
ls -la structDB*

# Check database size
du -sh structDB*

# Verify database integrity
foldseek createindex structDB tmp --check-compatible 1
```

## Custom Database Creation

### From Structure Files

```bash
# 1. Create basic database
foldseek createdb structures/ customDB

# 2. Create index
foldseek createindex customDB tmp
```

### From Sequence Files with ProstT5

```bash
# 1. Download ProstT5 model
foldseek databases ProstT5 weights tmp

# 2. Create database with 3Di prediction
foldseek createdb sequences.fasta structDB --prostt5-model weights/

# 3. GPU-accelerated creation
foldseek createdb sequences.fasta structDB --prostt5-model weights/ --gpu 1

# 4. Create index
foldseek createindex structDB tmp
```

### From AlphaFold Results

```bash
# 1. Organize AlphaFold results
mkdir alphafold_results
# Copy AlphaFold PDB files to alphafold_results/

# 2. Create database
foldseek createdb alphafold_results/ afdb

# 3. Create index
foldseek createindex afdb tmp
```

## Database Maintenance

### Database Validation

```bash
# Check database integrity
foldseek createindex structDB tmp --check-compatible 1

# Validate against original files
foldseek convertalis structDB structDB structDB validation_results --format-output query
```

### Database Cleanup

```bash
# Remove temporary files
rm -f structDB.tmp*

# Compress database
foldseek createdb structDB structDB_compressed --compressed 1

# Remove original
rm -rf structDB*

# Rename compressed version
mv structDB_compressed* structDB
```

### Database Backup

```bash
# Create compressed backup
tar -czf structDB_backup.tar.gz structDB*

# Create index backup
tar -czf structDB_index_backup.tar.gz structDB.idx*

# Verify backup
foldseek createindex structDB tmp --check-compatible 1
```

## Performance Optimization

### Index Optimization

```bash
# Create optimal index for structural search
foldseek createindex structDB tmp --index-subset 2

# Create optimal index for sequence search
foldseek createindex structDB tmp --index-subset 1

# Create comprehensive index
foldseek createindex structDB tmp --index-subset 0
```

### Memory Optimization

```bash
# Use memory-efficient indexing
foldseek createindex structDB tmp --split 8

# Use compressed databases
foldseek createdb structDB structDB_compressed --compressed 1
```

### GPU Optimization

```bash
# Use GPU acceleration for database creation
foldseek createdb sequences.fasta structDB --prostt5-model weights/ --gpu 1

# Create index for GPU-optimized database
foldseek createindex structDB tmp
```

## Large-Scale Database Management

### Batch Processing

```bash
# Process large datasets in batches
for i in {1..100}; do
    foldseek createdb batch_${i}/ batch_${i}_db
    foldseek createindex batch_${i}_db tmp_${i}
done

# Create cluster search database
foldseek cluster largeDB clusterDB tmp
foldseek createclusearchdb largeDB clusterDB largeDB_search

# Create final index
foldseek createindex largeDB_search tmp
```

### Distributed Processing

```bash
# Process large datasets in parallel
for i in {1..100}; do
    foldseek createdb batch_${i}/ batch_${i}_db
    foldseek createindex batch_${i}_db tmp_${i} &
done
wait

# Create cluster search database
foldseek cluster largeDB clusterDB tmp
foldseek createclusearchdb largeDB clusterDB largeDB_search
```

### Creating Searchable Databases from New Structures

```bash
# Create new database with additional structures
foldseek createdb new_structures/ newDB

# Create cluster search database for efficient searching
foldseek cluster newDB clusterDB tmp
foldseek createclusearchdb newDB clusterDB newDB_search

# Create index for fast search operations
foldseek createindex newDB_search tmp
```

## Integration Examples

### With High-Performance Computing

```bash
# Use MPI for large database operations
mpirun -np 64 foldseek createindex largeDB tmp

# Use job scheduler
sbatch --nodes=4 --ntasks=128 create_index_job.sh
```

### With Cloud Storage

```bash
# Download from cloud storage
aws s3 cp s3://bucket/structures/ ./structures/ --recursive

# Create database
foldseek createdb structures/ structDB

# Upload to cloud storage
aws s3 cp structDB* s3://bucket/databases/ --recursive
```

### With Version Control

```bash
# Create versioned database
foldseek createdb structures/ structDB_v1.0

# Create index
foldseek createindex structDB_v1.0 tmp

# Tag version
git tag -a v1.0 -m "Initial database version"

# Create backup
tar -czf structDB_v1.0_backup.tar.gz structDB_v1.0*
```

These database management modules provide comprehensive functionality for handling large-scale structural databases, from initial creation and indexing to maintenance and optimization.

## Database Format Comparison with MMseqs2

### Structural vs Sequence Databases

| Feature | MMseqs2 Database | Foldseek Database | Key Difference |
|---------|------------------|-------------------|----------------|
| **Data Types** | Amino acid sequences<br>Nucleotide sequences<br>Profile databases | 3Di sequences<br>Amino acid sequences<br>Cα coordinates<br>Secondary structure | Foldseek adds structural data |
| **File Components** | `database`, `database.index`<br>`database_h`, `database_h.index`<br>`database.lookup`, `database.dbtype` | `database`, `database.index`<br>`database_h`, `database_h.index`<br>`database_ca`, `database_ss`<br>`database.lookup`, `database.dbtype` | Additional structural files |
| **Memory Usage** | ~7 bytes per residue (index)<br>~1 byte per residue (sequences) | ~1 byte per residue (3Di)<br>~8 bytes per residue (Cα coords)<br>~1 byte per residue (sequences) | More compact for structural data |
| **Index Structure** | K-mer index for sequences | 3Di k-mer index<br>Structural descriptors | Optimized for structural search |

### Database Creation Process

#### MMseqs2 Database Creation
```bash
# Convert FASTA sequences to MMseqs2 database
mmseqs createdb sequences.fasta seqDB

# Files created:
# - seqDB (amino acid sequences)
# - seqDB.index (sequence index)
# - seqDB_h (FASTA headers)
# - seqDB_h.index (header index)
# - seqDB.lookup (ID mapping)
# - seqDB.dbtype (database type)
```

#### Foldseek Database Creation
```bash
# Convert structures to Foldseek database
foldseek createdb structures/ structDB

# Files created:
# - structDB (3Di + AA sequences)
# - structDB.index (structural index)
# - structDB_h (structure headers)
# - structDB_h.index (header index)
# - structDB_ca (Cα coordinates)
# - structDB_ss (secondary structure)
# - structDB.lookup (ID mapping)
# - structDB.dbtype (database type)
```

### Index Structure Differences

#### MMseqs2 Index
- **K-mer size**: Variable (6-14 amino acids)
- **Alphabet**: 20 amino acids (or reduced alphabet)
- **Memory usage**: ~7 bytes per residue
- **Search type**: Sequence similarity
- **Substitution matrix**: BLOSUM62, VTML matrices

#### Foldseek Index
- **K-mer size**: Variable (3Di alphabet)
- **Alphabet**: 3-letter 3Di (H/E/C)
- **Memory usage**: ~1 byte per residue
- **Search type**: Structural similarity
- **Substitution matrix**: 3Di-specific matrix
- **Additional data**: Structural descriptors, Cα coordinates

### Database Type Specifications

| Database Type | MMseqs2 | Foldseek | Description |
|---------------|---------|----------|-------------|
| **Amino Acid** | 0 | 0 | Standard protein sequences |
| **Nucleotide** | 1 | 1 | DNA/RNA sequences |
| **Profiles** | 2 | 2 | Profile databases |
| **Structural** | N/A | 3 | 3Di + structural data |
| **Alignment Results** | 5 | 5 | Search results |
| **Clustering Results** | 6 | 6 | Cluster assignments |
| **Prefiltering Results** | 7 | 7 | Prefilter hits |
| **Taxonomy Results** | 8 | 8 | Taxonomic assignments |

### Performance Implications

#### Memory Efficiency
- **MMseqs2**: Requires ~7 bytes per residue for k-mer indexing
- **Foldseek**: Requires ~1 byte per residue for 3Di indexing
- **Advantage**: Foldseek uses ~7x less memory for indexing

#### I/O Efficiency
- **MMseqs2**: Memory-maps sequence data and k-mer indices
- **Foldseek**: Memory-maps 3Di data, Cα coordinates, and structural indices
- **Advantage**: Foldseek's smaller indices enable faster loading

#### Search Speed
- **MMseqs2**: Optimized for sequence similarity search
- **Foldseek**: Optimized for structural similarity search
- **Trade-off**: Different optimization targets for different data types

### Compatibility and Integration

#### Shared Database Operations
Both tools support:
- Memory-mapped I/O for efficient access
- Compressed database storage
- Index creation and management
- Database splitting for large datasets
- Sub-database creation

#### Unique Foldseek Operations
- 3Di sequence generation from structures
- Cα coordinate extraction and storage
- Secondary structure assignment
- Structural index creation
- GPU-optimized database creation

#### Cross-Compatibility
- Foldseek can read MMseqs2 sequence databases
- MMseqs2 cannot read Foldseek structural databases
- Both use compatible result formats
- Shared taxonomy and clustering modules