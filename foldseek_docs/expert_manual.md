# Foldseek Expert Manual: Advanced Database Interactions and Structural Alignment

This document provides a detailed look into how various Foldseek modules interact with structural databases and perform advanced structural alignments. Understanding these interactions is key to building custom structural analysis workflows and troubleshooting complex pipelines.

## Core Concepts

This expert manual focuses on advanced usage and database/alignment behavior. For internals and formats, see:
- Developer Manual (`foldseek_docs/developer_manual.md`) for architecture, 3Di internals, and database file layout
- Databases (`foldseek_docs/submodules/databases.md`) for user-facing database operations and formats

### Header Database Handling Patterns

**When Header and Main Databases are Processed Together:**

1. **Database Creation (`createdb`)**:
   - Creates header and sequence databases simultaneously
   - Both use identical numeric IDs for corresponding entries
   - Headers stored in `database_h` and `database_h.index`

2. **Format Conversion Operations**:
   - `convertalis`: Reads both sequence and header databases for output formatting
   - `convert2fasta`: Combines header and sequence data for FASTA output

**When Header and Main Databases are Processed Separately:**

1. **Core Search Operations**:
   - `structuresearch`: Only reads sequence data for k-mer matching
   - `structurealign`: Only reads sequence and coordinate data for alignment
   - `multimersearch`: Only reads structural data for complex analysis

2. **Index-Only Operations**:
   - Operations that only need structural indices for prefiltering
   - GPU-accelerated searches that stream data from disk

### Performance Optimization Patterns

**Memory-Efficient Access:**
```cpp
// Load only what you need
DBReader<unsigned int> reader(dbPath, indexPath, threads,
                             DBReader<unsigned int>::USE_INDEX);  // Index only
DBReader<unsigned int> caReader(caPath, caIndexPath, threads,
                               DBReader<unsigned int>::USE_DATA);   // Data only
```

**Streaming Large Databases:**
```cpp
// Process in chunks for memory efficiency
for (size_t chunkStart = 0; chunkStart < totalEntries; chunkStart += chunkSize) {
    size_t chunkEnd = std::min(chunkStart + chunkSize, totalEntries);
    // Process chunk
    for (size_t i = chunkStart; i < chunkEnd; ++i) {
        const char* data = reader.getData(i, thread_idx);
        // Process data
    }
}
```

**Parallel Database Access:**
```cpp
// Multiple threads accessing different database segments
#pragma omp parallel for
for (size_t i = 0; i < numQueries; ++i) {
    int thread_idx = omp_get_thread_num();
    const char* queryData = queryReader.getData(i, thread_idx);
    // Process query independently
}
```

## Module Documentation

### `createdb`

**Module Type**: Database Creation

**Function**: Converts protein structure files (PDB, mmCIF, mmJSON) into Foldseek databases.

**Database Interactions**:

*   **Input Reading**:
    *   Reads structural data from PDB/mmCIF/mmJSON files
    *   Parses atomic coordinates, chain information, and metadata
    *   Supports compressed files (.gz, .bz2) and piped input

*   **Output Writing**:
    *   **`database`**: Concatenated 3Di sequences, amino acid sequences, and descriptors
    *   **`database_ca`**: Cα coordinates for each residue
    *   **`database_ss`**: Secondary structure assignments
    *   **`database_h`**: Structure headers and metadata
    *   **`database.lookup`**: Maps internal IDs to original structure identifiers
    *   **`database.dbtype`**: Binary type specification

*   **3Di Generation**:
    *   **Secondary Structure Assignment**: Uses DSSP algorithm to assign H/E/C states
    *   **Coordinate Processing**: Extracts Cα coordinates for TM-score calculations
    *   **Chain Handling**: Supports multi-chain structures with configurable naming
    *   **ProstT5 Integration**: Optional 3Di prediction from sequences using language models

### `structuresearch`

**Module Type**: Structural Search

**Function**: Performs fast structural similarity search using 3Di representation.

**Database Interactions**:

*   **Input Reading**:
    *   **Query Database (`<i:queryDB>`)**: Reads 3Di sequences and structural descriptors
    *   **Target Database (`<i:targetDB>`)**: Reads target 3Di sequences for indexing
    *   **Index Files**: Uses precomputed k-mer indices for fast lookup

*   **Output Writing**:
    *   **Result Database (`<o:resultDB>`)**: Structural alignment results
    *   Each entry contains: target ID, structural score, TM-score, LDDT, E-value, coordinates

*   **Structural Scoring**:
    *   **3Di Alignment**: Gotoh-Smith-Waterman with 3Di substitution matrix
    *   **TM-score Calculation**: Global structural alignment using TM-align algorithm
    *   **LDDT Scoring**: Local structural conservation assessment
    *   **E-value Computation**: Statistical significance using extreme value distribution

### `structurealign`

**Module Type**: Structural Alignment

**Function**: Performs detailed structural alignments between query and target structures.

**Database Interactions**:

*   **Input Reading**:
    *   **Query Database (`<i:queryDB>`)**: Reads 3Di sequences and Cα coordinates
    *   **Target Database (`<i:targetDB>`)**: Reads target 3Di sequences and Cα coordinates
    *   **Prefiltering Results**: Uses precomputed candidate pairs

*   **Output Writing**:
    *   **Alignment Database (`<o:alignmentDB>`)**: Detailed structural alignments
    *   Contains: alignment paths, TM-scores, rotation matrices, translation vectors

*   **Alignment Algorithms**:
    *   **3Di+AA Alignment**: Combines 3Di structural and amino acid sequence information
    *   **TM-align**: Global structural alignment with TM-score optimization
    *   **SIMD Optimization**: Vectorized Smith-Waterman for 3Di sequences

### `multimersearch`

**Module Type**: Multimer Search

**Function**: Searches protein complexes (multimers) against target databases.

**Database Interactions**:

*   **Input Reading**:
    *   **Query Complexes (`<i:queryDB>`)**: Reads multi-chain structures
    *   **Target Complexes (`<i:targetDB>`)**: Reads target multi-chain structures
    *   **Chain Information**: Parses chain IDs and interfaces

*   **Output Writing**:
    *   **Complex Alignment Database (`<o:alignmentDB>`)**: Complex-level alignments
    *   Contains: complex TM-scores, chain assignments, interface LDDT scores

*   **Complex Scoring**:
    *   **Chain Matching**: Optimal assignment of query chains to target chains
    *   **Interface Analysis**: LDDT scoring of chain-chain interfaces
    *   **Complex TM-score**: Weighted combination of individual chain TM-scores
    *   **Assignment Optimization**: Hungarian algorithm for optimal chain matching

### `tmalign`

**Module Type**: TM-align Integration

**Function**: Performs TM-align based structural alignments.

**Database Interactions**:

*   **Input Reading**:
    *   **Structure Databases**: Reads Cα coordinates and sequences
    *   **Alignment Parameters**: Uses precomputed structural similarities

*   **Output Writing**:
    *   **TM-align Results**: TM-scores, rotation matrices, translation vectors
    *   Contains: global alignment scores and superposition parameters

*   **TM-score Implementation**:
    *   **Rotation Matrix**: Optimal rotation using quaternion method
    *   **Translation Vector**: Optimal translation for superposition
    *   **Score Normalization**: TM-score normalized by protein length
    *   **Statistical Significance**: P-value calculation using empirical distributions

### `convert2pdb`

**Module Type**: Format Conversion

**Function**: Converts structural alignment results to superimposed PDB files.

**Database Interactions**:

*   **Input Reading**:
    *   **Query Database (`<i:queryDB>`)**: Reads query structures and coordinates
    *   **Target Database (`<i:targetDB>`)**: Reads target structures and coordinates
    *   **Alignment Database (`<i:alignmentDB>`)**: Reads alignment transformations

*   **Output Writing**:
    *   **Superimposed PDB Files**: One PDB file per alignment
    *   Each file contains: superimposed Cα atoms, transformation metadata

*   **Coordinate Transformation**:
    *   **Matrix Application**: Applies rotation and translation matrices
    *   **Chain Preservation**: Maintains original chain IDs and metadata
    *   **Format Compliance**: Generates valid PDB format with proper headers

## Advanced Database Operations

### Index Creation and Management

#### Structural Index Architecture

Foldseek creates specialized indices optimized for different types of structural queries:

**Index Types:**
- **Subset 0 (Comprehensive)**: All data types (sequences, coordinates, secondary structure)
- **Subset 1 (Sequence-only)**: Smaller, faster loading for sequence-based operations
- **Subset 2 (Structure-only)**: Optimized for structural searches and alignments

```bash
# Create comprehensive structural index
foldseek createindex targetDB tmp --index-subset 0

# Create sequence-only index (smaller, faster loading)
foldseek createindex targetDB tmp --index-subset 1

# Create structure-only index (for structural searches)
foldseek createindex targetDB tmp --index-subset 2
```

#### Index File Structure

The index creation process generates several coordinated files:

```
targetDB.index          # Main index file
targetDB.index.dbtype   # Index database type
targetDB.index.lookup   # Index lookup table
targetDB.index_h        # Header index
targetDB.index_h.index  # Header index index
```

#### GPU-Optimized Databases

**Padded Database Creation:**
```bash
# Create padded database for GPU searches
foldseek makepaddeddb targetDB targetDB_gpu

# Use with GPU acceleration
foldseek search queryDB targetDB_gpu resultDB tmp --gpu 1
```

**GPU Database Structure:**
- **Padding**: Sequences padded to fixed lengths for efficient GPU processing
- **Memory Layout**: Optimized for coalesced memory access patterns
- **Streaming**: Supports databases larger than GPU memory through streaming

#### Database Splitting for Large-Scale Operations

**Memory-Efficient Processing:**
```bash
# Split large database for memory management
foldseek splitdb largeDB largeDB_split --split 10

# Process each split separately
for i in {0..9}; do
    foldseek search queryDB largeDB_split_${i}_10 result_${i} tmp_${i}
done

# Merge results
foldseek mergedbs resultDB result_0 result_1 result_2 result_3 result_4 result_5 result_6 result_7 result_8 result_9
```

**Split Database Structure:**
```
largeDB_split_0_10/     # First split (entries 0-9)
largeDB_split_1_10/     # Second split (entries 10-19)
...
largeDB_split_9_10/     # Last split (entries 90-99)
```

#### Custom Database Creation

**From Structure Prediction Results:**
```bash
# Convert AlphaFold results to Foldseek database
foldseek createdb alphafold_results/ afdb

# Add taxonomy information
foldseek createtaxdb afdb tmp --tax-mapping-file uniprot_taxid.tsv
```

**From Experimental Structures:**
```bash
# Process PDB structures with custom chain handling
foldseek createdb pdb_structures/ custom_db --chain-name-mode 1

# Create index optimized for structural searches
foldseek createindex custom_db tmp --index-subset 2
```

#### Database Concatenation

**Combining Multiple Databases:**
```bash
# Concatenate multiple structural databases
foldseek concatdbs db1 db2 combined_db

# Note: Header databases must be concatenated separately
foldseek concatdbs db1_h db2_h combined_db_h
```

**Concatenation Process:**
1. **Key Renumbering**: Assigns new sequential IDs to entries from second database
2. **Index Merging**: Combines index files from both databases
3. **Lookup Table Updates**: Updates lookup tables to maintain ID mapping
4. **Header Integration**: Merges header databases separately

### Database Performance Optimization

#### Memory Usage Optimization

**Reducing Memory Footprint:**
```bash
# Disable structure bits for lower memory usage
foldseek search queryDB targetDB result tmp --sort-by-structure-bits 0

# Use sequence-only operations when coordinates not needed
foldseek search queryDB targetDB result tmp --alignment-type 0
```

**Memory Usage Breakdown:**
| Component | Memory Usage | When to Optimize |
|-----------|--------------|------------------|
| 3Di sequences | ~1 byte/residue | Always present |
| Cα coordinates | ~12 bytes/residue | TM-score calculations |
| Secondary structure | ~1 byte/residue | Structural alignment |
| Index structures | ~8 bytes/entry | Large databases |
| Header data | Variable | Output formatting |

#### Index Optimization Strategies

**Index Subset Selection:**
```bash
# For sequence-only searches (fastest)
foldseek createindex targetDB tmp --index-subset 1

# For structural searches (most comprehensive)
foldseek createindex targetDB tmp --index-subset 2

# For mixed workloads (balanced)
foldseek createindex targetDB tmp --index-subset 0
```

**Index Memory Mapping:**
```cpp
// Load index only (no data) for prefiltering
IndexReader reader(dbPath, threads, IndexReader::INDEX_ONLY);

// Load data only (no index) for sequential access
DBReader<unsigned int> reader(dbPath, indexPath, threads, DBReader<unsigned int>::USE_DATA);

// Load both for random access
DBReader<unsigned int> reader(dbPath, indexPath, threads,
                             DBReader<unsigned int>::USE_DATA |
                             DBReader<unsigned int>::USE_INDEX);
```

#### GPU Database Optimization

**Memory Layout for GPU Processing:**
```bash
# Create GPU-optimized database
foldseek makepaddeddb targetDB targetDB_gpu --padding-mode 1

# Use optimized GPU search
foldseek search queryDB targetDB_gpu result tmp --gpu 1 --prefilter-mode 1
```

**GPU Memory Management:**
- **Streaming**: Automatic handling of databases larger than GPU memory
- **Batching**: Processes queries in batches for optimal GPU utilization
- **Memory Pools**: Reuses GPU memory across multiple operations

### Database Quality Assessment

#### Structural Data Validation

**Coordinate Quality Checks:**
```bash
# Validate Cα coordinates in database
foldseek validateca targetDB validation_report

# Check secondary structure assignments
foldseek validatess targetDB ss_report
```

**Database Integrity Verification:**
```bash
# Verify database consistency
foldseek dbverify targetDB integrity_report

# Check index consistency
foldseek indexverify targetDB index_report
```

#### Performance Benchmarking

**Database Access Benchmarking:**
```bash
# Benchmark random access performance
foldseek benchmark targetDB benchmark_results --access-pattern random

# Benchmark sequential access performance
foldseek benchmark targetDB benchmark_results --access-pattern sequential
```

**Benchmark Results Interpretation:**
- **Random Access**: Tests index efficiency and memory mapping
- **Sequential Access**: Tests streaming performance and I/O efficiency
- **Mixed Access**: Tests real-world usage patterns

### Database Troubleshooting and Maintenance

#### Common Database Issues

**Index Corruption:**
```bash
# Rebuild corrupted index
foldseek createindex targetDB tmp --force-rebuild

# Verify index integrity
foldseek indexverify targetDB verification_report
```

**Memory Mapping Issues:**
```bash
# Check system memory mapping limits
ulimit -a | grep -E "(memlock|vmemory)"

# Increase limits if needed
ulimit -l unlimited  # locked memory
ulimit -v unlimited  # virtual memory
```

**Database File Permissions:**
```bash
# Fix file permissions
chmod 644 targetDB*
chmod 644 targetDB*.index
chmod 644 targetDB*.lookup
```

#### Database Repair and Recovery

**Repair Corrupted Database:**
```bash
# Create backup first
cp -r targetDB targetDB.backup

# Attempt repair
foldseek dbrepair targetDB repair_log.txt

# Verify repair
foldseek dbverify targetDB verification_report
```

**Recover from Partial Database:**
```bash
# Extract valid entries
foldseek extractvalid targetDB partial_db

# Rebuild from valid entries
foldseek createdb partial_db/ rebuilt_db
```

#### Performance Monitoring

**Database Access Monitoring:**
```bash
# Monitor database access patterns
foldseek dbmonitor targetDB monitor.log --duration 3600

# Analyze access patterns
foldseek dbanalyze targetDB analysis_report
```

**Memory Usage Analysis:**
```bash
# Monitor memory usage during operations
foldseek memprofile search queryDB targetDB result tmp profile.log

# Analyze memory bottlenecks
foldseek memanalyze profile.log analysis.txt
```

#### Database Migration and Conversion

**Version Migration:**
```bash
# Migrate from older Foldseek version
foldseek dbmigrate old_format_db new_format_db

# Verify migration
foldseek dbverify new_format_db migration_report
```

**Format Conversion:**
```bash
# Convert between different structural formats
foldseek convertformat input_db output_db --input-format cif --output-format pdb

# Batch conversion
find /path/to/structures -name "*.cif" | foldseek convertformat - output_db
```

#### Database Maintenance Scripts

**Automated Maintenance:**
```bash
#!/bin/bash
# Daily database maintenance script

DB_PATH="/path/to/databases"
LOG_FILE="/var/log/foldseek_maintenance.log"

# Verify database integrity
for db in "$DB_PATH"/*; do
    if [ -d "$db" ] && [ -f "$db/targetDB.dbtype" ]; then
        echo "$(date): Verifying $db" >> "$LOG_FILE"
        foldseek dbverify "$db" "$db.verify.log"
    fi
done

# Clean temporary files
find "$DB_PATH" -name "*.tmp" -mtime +7 -delete

# Rebuild indices if needed
for db in "$DB_PATH"/*; do
    if [ -d "$db" ] && [ -f "$db/targetDB.dbtype" ]; then
        echo "$(date): Checking index for $db" >> "$LOG_FILE"
        foldseek indexverify "$db" "$db.index.log"
    fi
done
```

**Maintenance Scheduling:**
```bash
# Add to crontab for automated maintenance
crontab -e

# Add this line for daily maintenance at 2 AM
0 2 * * * /path/to/maintenance_script.sh
```

#### Database Backup and Recovery

**Backup Strategy:**
```bash
# Full database backup
tar -czf foldseek_databases_$(date +%Y%m%d).tar.gz /path/to/databases/

# Incremental backup
rsync -av --delete /path/to/databases/ /path/to/backup/databases/

# Cloud backup
aws s3 sync /path/to/databases/ s3://my-bucket/foldseek-databases/
```

**Recovery Procedures:**
```bash
# Restore from backup
tar -xzf foldseek_databases_20231201.tar.gz -C /path/to/databases/

# Verify restoration
foldseek dbverify /path/to/databases/* verification_report.txt

# Rebuild indices after restoration
for db in /path/to/databases/*; do
    if [ -d "$db" ]; then
        foldseek createindex "$db" tmp --force-rebuild
    fi
done
```

#### Database Security

**Access Control:**
```bash
# Set appropriate permissions
chmod 750 /path/to/databases/
chmod 640 /path/to/databases/*/*

# Restrict access to specific users
chown -R foldseek_user:foldseek_group /path/to/databases/

# Set up access logging
foldseek dbmonitor /path/to/databases/ access.log --log-access
```

**Encryption (if needed):**
```bash
# Encrypt sensitive databases
gpg -c /path/to/databases/sensitive_db

# Decrypt for use
gpg -d /path/to/databases/sensitive_db.gpg > /tmp/decrypted_db
foldseek createdb /tmp/decrypted_db/ working_db
```

This comprehensive database management section provides users with the tools and knowledge needed to maintain, troubleshoot, and optimize their Foldseek databases for production use.

## Structural Alignment Details

### 3Di Substitution Matrix

The 3Di alphabet uses a specialized substitution matrix optimized for structural similarity:

```
    H   E   C
H  10  -5  -3
E  -5  10  -3
C  -3  -3   5
```

This matrix reflects the structural relationships:
- **H-H**: Strong preference for helical matches
- **E-E**: Strong preference for strand matches
- **C-C**: Moderate preference for coil matches
- **H-E**: Penalty for helix-strand mismatches
- **H-C, E-C**: Moderate penalties for secondary structure mismatches

### TM-score Calculation

TM-score is calculated as:
```
TM-score = max(1/L_target * Σ[1/(1 + (d_i/d_0)^2)] over all alignments)
```

Where:
- `L_target`: Length of target protein
- `d_i`: Distance between i-th pair of residues after superposition
- `d_0`: Distance threshold (0.5 nm for Cα)

### LDDT Score Implementation

LDDT (Local Distance Difference Test) measures local structural conservation:

```
LDDT = (1/4) * Σ[δ(d_i < 0.5) + δ(d_i < 1.0) + δ(d_i < 2.0) + δ(d_i < 4.0)]
```

Where `δ(x)` is 1 if x is true, 0 otherwise.

## Performance Optimization

### GPU Acceleration Details

#### CUDA Implementation
```bash
# Enable GPU acceleration
foldseek search queryDB targetDB resultDB tmp --gpu 1 --prefilter-mode 1

# Multi-GPU usage
CUDA_VISIBLE_DEVICES=0,1 foldseek search queryDB targetDB resultDB tmp --gpu 1
```

#### Memory Management
- **GPU Memory**: ~4GB for typical searches
- **Host Memory**: ~8GB for data structures
- **Streaming**: Automatic handling of databases larger than GPU memory

### Parallel Processing

#### Multi-threading
```bash
# Optimize thread usage
foldseek search queryDB targetDB resultDB tmp --threads 32

# MPI for multi-node processing
RUNNER="mpirun -np 64" foldseek search queryDB targetDB resultDB tmp
```

#### Database Sharding
```bash
# Split large searches across multiple processes
foldseek splitdb queryDB queryDB_split --split 100

# Process shards in parallel
parallel -j 50 "foldseek search queryDB_split_{}_100 targetDB result_{} tmp_{}" ::: {0..99}
```

## Advanced Workflows

### Iterative Structural Refinement
```bash
# First iteration with high sensitivity
foldseek search queryDB targetDB iter1 tmp -s 9.5 --num-iterations 1

# Extract hits and create profile
foldseek result2structprofile queryDB targetDB iter1 profileDB

# Second iteration with profiles
foldseek search profileDB targetDB iter2 tmp --profile-search
```

### Structure-Based Function Annotation
```bash
# Search against functionally annotated structures
foldseek search unknown.pdb annotated_structures.db functional_hits tmp

# Transfer functional annotations
foldseek convertalis unknown.pdb annotated_structures.db functional_hits functional_annotation.tsv
```

### Quality Assessment Integration
```bash
# Assess structure quality using LDDT
foldseek easy-search query.pdb reference.db lddt_scores tmp --format-output "query,target,lddt,lddtfull"

# Filter high-quality alignments
foldseek filterdb lddt_scores high_quality --filter-expression '$3 > 0.7'
```

This expert manual provides the foundation for advanced Foldseek usage, enabling researchers to build sophisticated structural bioinformatics pipelines and optimize performance for large-scale structural analyses.

## Technical Comparison with MMseqs2

### Database Architecture Differences

#### MMseqs2 Database Structure
```
MMseqs2 Database Files:
├── database (Data File): Raw sequence data
├── database.index: Sequence index (id, offset, length)
├── database_h: FASTA headers
├── database_h.index: Header index
├── database.lookup: ID to FASTA identifier mapping
└── database.dbtype: Database type specification
```

#### Foldseek Database Structure
```
Foldseek Database Files:
├── database (Data File): 3Di sequences + amino acid sequences
├── database.index: Structural index (id, offset, length)
├── database_h: Structure headers + metadata
├── database_h.index: Header index
├── database_ca: Cα coordinates for TM-score calculations
├── database_ss: Secondary structure assignments
├── database.lookup: ID to structure identifier mapping
└── database.dbtype: Database type specification
```

### Algorithmic Differences

#### Prefiltering Stage

**MMseqs2 Prefiltering:**
- Uses amino acid k-mers (typically k=6-14)
- Employs reduced alphabet for sensitivity
- Double consecutive k-mer matches on same diagonal
- Ungapped alignment scoring with sequence substitution matrices

**Foldseek Prefiltering:**
- Uses 3Di k-mers (H/E/C alphabet) with 20 internal centroids for classification
- Specialized 3Di substitution matrix:
  ```
      H   E   C
  H  10  -5  -3
  E  -5  10  -3
  C  -3  -3   5
  ```
- **Internal classification**: 20 centroids (states 0-19) for detailed structural discrimination
- **Output mapping**: Internal states mapped to 3-letter alphabet via substitution matrix
- Structural diagonal detection
- Ungapped structural alignment with 3Di scoring

#### Alignment Stage

**MMseqs2 Alignment:**
- SIMD-accelerated Smith-Waterman algorithm
- Sequence identity calculation: `identical_positions / alignment_length`
- E-value computation using Karlin-Altschul statistics
- Memory usage: ~8 bytes per residue for dynamic programming matrices

**Foldseek Alignment:**
- 3Di+AA combined alignment algorithm
- Multiple alignment modes:
  - Mode 0: 3Di Gotoh-Smith-Waterman (local)
  - Mode 1: TM-align (global structural)
  - Mode 2: 3Di+AA Gotoh-Smith-Waterman (local, default)
- TM-score calculation: `max(1/L_target * Σ[1/(1 + (d_i/d_0)^2)])`
- LDDT scoring: `(1/4) * Σ[δ(d_i < 0.5) + δ(d_i < 1.0) + δ(d_i < 2.0) + δ(d_i < 4.0)]`
- Memory usage: ~1 byte per residue for 3Di sequences

### Performance Characteristics

#### Memory Efficiency

| Database Size | MMseqs2 Memory | Foldseek Memory | Reduction Factor |
|---------------|----------------|-----------------|------------------|
| UniProt (55M seq) | ~71 GB | ~35 GB | 2.0x |
| AlphaFold (200M structures) | N/A | ~200 GB | N/A |
| PDB (200K structures) | N/A | ~1 GB | N/A |

#### Speed Comparison

| Operation | MMseqs2 | Foldseek | Speedup |
|-----------|---------|----------|---------|
| Prefiltering | 10,000x vs BLAST | 10,000x vs TM-align | Similar |
| Database Creation | Minutes | Minutes | Similar |
| Index Creation | Minutes | Minutes | Similar |
| GPU Acceleration | Yes | Yes | Similar |

### Data Processing Pipeline Differences

#### MMseqs2 Pipeline
```
FASTA/FASTQ Input
       ↓
   createdb
       ↓
3Di sequences + AA sequences
       ↓
   createindex
       ↓
K-mer index for sequences
       ↓
   search/prefilter
       ↓
Sequence similarity search
       ↓
   align
       ↓
Smith-Waterman alignment
       ↓
   convertalis
       ↓
BLAST-tab output
```

#### Foldseek Pipeline
```
PDB/mmCIF/FASTA Input
       ↓
   createdb
       ↓
3Di sequences + AA sequences + Cα + SS
       ↓
   createindex
       ↓
3Di k-mer index + structural descriptors
       ↓
   structuresearch
       ↓
3Di-based structural similarity search
       ↓
   structurealign
       ↓
3Di+AA or TM-align alignment
       ↓
   convertalis
       ↓
Structural alignment output
```

### Advanced Features Comparison

#### MMseqs2 Advanced Features
- Iterative profile searches (PSI-BLAST style)
- Translated searches (BLASTX, TBLASTN, TBLASTX)
- Taxonomy assignment with LCA
- Profile-profile searches
- GPU acceleration for sequence search

#### Foldseek Advanced Features
- Direct structure-to-structure alignment
- TM-score based global alignment
- LDDT-based local structural conservation
- Multi-chain complex analysis
- Structure-based clustering
- GPU acceleration for structural search
- 3Di prediction from sequences (ProstT5)

### Integration and Compatibility

#### Shared Infrastructure
- Both use memory-mapped I/O for efficient database access
- Compatible database format extensions
- Shared modular architecture
- Common indexing strategies
- Similar parameter interfaces

#### Unique Integration Points
- Foldseek extends MMseqs2's `IndexReader` for structural data
- Compatible with MMseqs2's taxonomy system
- Can use MMseqs2's clustering algorithms
- Shared result processing and output formatting

This technical comparison highlights how Foldseek builds upon MMseqs2's proven architecture while introducing structural biology-specific optimizations and algorithms.