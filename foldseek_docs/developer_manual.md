# Foldseek Developer Manual: Architecture and Module Classification

## Overview

Foldseek is built on top of the MMseqs2 framework and extends it with structural biology capabilities. It is organized into hierarchical layers based on abstraction and functionality, similar to MMseqs2 but specialized for structural data processing.

## Architecture Overview

### Core Components

Foldseek consists of several key architectural components:

1. **3Di Engine**: Converts protein structures to 3D-interaction sequences
2. **Structural Database Layer**: Manages structural data storage and retrieval
3. **Alignment Engine**: Performs structural alignments using multiple algorithms
4. **Search Engine**: Combines prefiltering and alignment for fast structural search
5. **Clustering Engine**: Groups structures by structural similarity

### Data Flow Architecture

```
Input Structures (PDB/mmCIF)
        ↓
   Structure Parser
        ↓
3Di Conversion Engine
        ↓
  Database Creation
        ↓
Structural Search/Cluster
        ↓
   Result Processing
        ↓
Output (Alignments, Clusters)
```

## Module Classification

### Easy Workflows
High-level user-facing workflows that provide convenient interfaces for common structural analysis tasks.

- **easy-search**: Sensitive structural homology search workflow
- **easy-cluster**: Structure-based clustering workflow
- **easy-multimersearch**: Protein complex search workflow
- **easy-multimercluster**: Protein complex clustering workflow

### Structure Search Modules
Core modules for structural similarity searching and alignment.

- **structuresearch**: Main structural search combining prefiltering and alignment
- **structurealign**: Direct structural alignment between structure sets
- **tmalign**: TM-align based global structural alignment
- **aln2tmscore**: Convert alignments to TM-scores and transformations
- **structureungappedalign**: Fast ungapped structural alignment

### Structure Clustering Modules
Modules for clustering structures based on similarity.

- **structurecluster**: Main structure-based clustering workflow
- **cluster**: Core clustering algorithm for structural data
- **structureeasyrbh**: Reciprocal best hit for structural data

### Multimer Analysis Modules
Specialized modules for protein complex analysis.

- **multimersearch**: Core multimer search functionality
- **multimercluster**: Core multimer clustering functionality
- **scoremultimer**: Score multimer alignments
- **filtermultimer**: Filter multimer results
- **createmultimerreport**: Generate complex alignment reports
- **expandmultimer**: Expand multimer search results

### Structure Manipulation Modules
Modules for processing and converting structural data.

- **createdb**: Create structural databases from PDB/mmCIF files
- **structureto3didescriptor**: Convert structures to 3Di descriptors
- **convert2pdb**: Convert alignment results to superimposed PDB files
- **compressca**: Compress Cα coordinate data
- **createstructsubdb**: Create structural sub-databases
- **lolalign**: Local structural alignment

### Database Management Modules
Modules for managing structural databases.

- **databases**: Download pre-built structural databases
- **createindex**: Create precomputed indices for structural searches
- **makepaddeddb**: Create GPU-optimized padded databases
- **structureindex**: Structural indexing functionality

## Hierarchical Dependencies

### Easy Workflows → Core Modules
Easy workflows call core modules to perform their tasks:

- `easy-search` internally calls `structuresearch` workflow
- `easy-cluster` internally calls `structurecluster` workflow
- `easy-multimersearch` internally calls `multimersearch` workflow
- `easy-multimercluster` internally calls `multimercluster` workflow

### Core Modules → Structural Engines
Core modules use specialized structural engines:

- `structuresearch` calls 3Di prefiltering followed by structural alignment
- `structurecluster` calls structural search followed by clustering algorithms
- `multimersearch` calls complex matching followed by interface analysis
- `tmalign` calls TM-score optimization algorithms

### Structural Engines → Data Access Layer
Structural engines use the data access layer for efficient I/O:

- All modules use `DBReader` for memory-mapped structural database access
- Coordinate transformations use optimized linear algebra routines
- 3Di processing uses SIMD-accelerated pattern matching

## 3Di Engine Architecture: Two-Tier System

### 3Di Conversion Pipeline

```cpp
// Core 3Di conversion process
StructureParser parser(inputFile);
SecondaryStructureAssigner ssAssigner;
CoordinateProcessor coordProcessor;
ThreeDiEncoder encoder;

// Process each structure
for each structure in input:
    ssAssigner.assignSecondaryStructure(structure);
    coordProcessor.extractCAlpha(structure);
    encoder.generate3DiSequence(structure);
```

### Secondary Structure Assignment

The 3Di engine uses a multi-step process for secondary structure assignment:

1. **DSSP Algorithm**: Computes hydrogen bond patterns
2. **Geometric Analysis**: Analyzes Cα backbone geometry
3. **Context Smoothing**: Reduces noise in assignments
4. **3Di Encoding**: Maps to H/E/C alphabet

### Two-Tier 3Di System

#### Tier 1: Internal Classification (20 States)
- **Location**: `foldseek/lib/3di/structureto3di.cpp`, `discretizeEmbeddings()` function (lines 233-255)
- **Process**: Assigns each residue to closest of 20 centroids using Euclidean distance
- **Code**:
```cpp
void StructureTo3Di::discretizeEmbeddings(std::vector<char> & states, std::vector<Embedding> & embeddings,
                                        std::vector<bool> & mask, const size_t len){
    for (size_t i = 0; i < len; i++){
        if (mask[i]){
            // Find closest of 20 centroids
            for (size_t j = 0; j < Alphabet3Di::CENTROID_CNT; j++){ // CENTROID_CNT = 20
                double sum = 0.0;
                for (size_t k = 0; k < Alphabet3Di::EMBEDDING_DIM; k++){
                    sum += pow(embeddings[i].f[k] - Alphabet3Di::centroids[j][k], 2);
                }
                if (sum < minDistance){
                    closestState = j; // States 0-19
                    minDistance = sum;
                }
            }
        }
        states[i] = closestState; // Internal states 0-19
    }
}
```

#### Tier 2: External Mapping (3-Letter Alphabet)
- **Location**: `foldseek/src/strucclustutils/structcreatedb.cpp` (lines 518-530)
- **Process**: Maps internal states (0-19) to 3-letter alphabet (H/E/C)
- **Code**:
```cpp
char * states = structureTo3Di.structure2states(&readStructure.ca[chainStart],
                                                &readStructure.n[chainStart],
                                                &readStructure.c[chainStart],
                                                &readStructure.cb[chainStart],
                                                chainLen);
// Map internal states (0-19) to 3-letter alphabet
alphabet3di.push_back(mat.num2aa[static_cast<int>(states[pos])]);
```

#### Internal vs. External Alphabet

The 3Di encoding process uses a two-stage classification system:

**Internal Classification (20 states):**
- Uses **20 trained centroids** for detailed structural classification
- Each centroid represents a cluster of similar structural features
- Provides rich discrimination between different structural conformations
- States are numbered 0-19 for internal processing

**External Representation (3 letters):**
- Maps internal states to 3-letter alphabet (H/E/C)
- Uses substitution matrix lookup: `output = mat3Di.num2aa[internal_state]`
- Enables efficient k-mer indexing and alignment
- Reduces computational complexity from 20×20 to 3×3 operations

This design achieves the optimal balance between:
- **Classification accuracy** (20 internal states)
- **Computational efficiency** (3-letter output)
- **Memory usage** (~1 byte per residue vs ~8 bytes for coordinates)

### AA and 3Di Integration: Combined Storage and Usage

#### Storage Architecture

From `foldseek/src/strucclustutils/structcreatedb.cpp` (lines 518-570), AA and 3Di sequences are stored together but in separate coordinated database files:

```cpp
// Generate both sequences for each structure
char * states = structureTo3Di.structure2states(&readStructure.ca[chainStart],
                                                &readStructure.n[chainStart],
                                                &readStructure.c[chainStart],
                                                &readStructure.cb[chainStart],
                                                chainLen);

// Store 3Di sequence (H/E/C alphabet)
for (size_t pos = 0; pos < chainLen; pos++) {
    alphabet3di.push_back(mat.num2aa[static_cast<int>(states[pos])]);
}

// Store AA sequence (20-letter alphabet)
for (size_t pos = 0; pos < chainLen; pos++) {
    alphabetAA.push_back(readStructure.ami[chainStart+pos]);
}

// Write to separate but coordinated database files
torsiondbw.writeData(alphabet3di.data(), alphabet3di.size(), dbKey, thread_idx);  // 3Di sequences
aadbw.writeData(alphabetAA.data(), alphabetAA.size(), dbKey, thread_idx);        // AA sequences
```

#### Database File Structure

| File | Content | Size Impact | Purpose |
|------|---------|-------------|---------|
| **`database`** | Amino acid sequences (20-letter alphabet) | ~1 byte/residue | Sequence-based operations |
| **`database_ss`** | 3Di sequences (H/E/C alphabet) | ~1 byte/residue | Structural operations |
| **`database_ca`** | Cα coordinates | ~12 bytes/residue | TM-score calculations |
| **`database_h`** | Headers/metadata | Variable | Structure identification |

#### Combined Alignment Process

From `foldseek/src/strucclustutils/structurealign.cpp`, AA and 3Di are combined during alignment:

```cpp
// Initialize alignment with both sequence types
StructureSmithWaterman structureSmithWaterman(par.maxSeqLen, subMat3Di.alphabetSize,
                                            par.compBiasCorrection, par.compBiasCorrectionScale,
                                            &subMatAA, &subMat3Di);

// Use both sequences in alignment scoring
StructureSmithWaterman::s_align align = structureSmithWaterman.alignScoreEndPos<StructureSmithWaterman::PROFILE>(
    tSeqAA.numSequence, tSeq3Di.numSequence, targetSeqLen,
    par.gapOpen.values.aminoacid(), par.gapExtend.values.aminoacid(), querySeqLen / 2
);

// Weighting: 3Di+AA alignment uses both scoring matrices
float aaFactor = (par.alignmentType == LocalParameters::ALIGNMENT_TYPE_3DI_AA) ? 1.4 : 0.0;
SubstitutionMatrix subMatAA(blosum.c_str(), aaFactor, par.scoreBias);
```

#### Key Implementation Details

1. **Synchronized Storage**: Both sequences have identical:
   - Length (same number of residues)
   - Database keys (same identifiers)
   - Indexing (same positions in database files)

2. **Combined Scoring**: The 3Di+AA alignment uses:
   - **3Di substitution matrix** for structural similarity
   - **AA substitution matrix** (BLOSUM62) for sequence similarity
   - **Weighted combination** (AA factor = 1.4 for 3Di+AA mode)

3. **Module Usage Patterns**:
   - **Search operations**: Load both AA and 3Di for combined scoring
   - **Structure-only operations**: Load only 3Di sequences
   - **Sequence-only operations**: Load only AA sequences
   - **TM-score calculations**: Load Cα coordinates + sequences

### SIMD Optimization

Foldseek uses SIMD instructions for performance-critical operations:

```cpp
// SIMD-accelerated 3Di alignment
__m256i query_3di = _mm256_loadu_si256((__m256i*)query_ptr);
__m256i target_3di = _mm256_loadu_si256((__m256i*)target_ptr);
__m256i score = _mm256_subs_epi8(query_3di, target_3di);
```

## Structural Database Layer

### Database File Architecture

Foldseek extends the MMseqs2 database format with structural data components:

#### Database File Components

| File | Content | Description/Size/Access |
|------|---------|--------|
| **`database`** | Concatenated 3Di sequences, amino acid sequences, and structural descriptors | Main data file<br>~2 bytes/residue<br>Sequential/Indexed |
| **`database.index`** | Tab-separated: `id\toffset\tlength` for random access | Index file<br>Minimal<br>Memory-mapped |
| **`database_ca`** | Binary Cα coordinates for TM-score calculations | Cα coordinates<br>~12 bytes/residue<br>Random access |
| **`database_ca.index`** | Index for coordinate data access | Cα index<br>Minimal<br>Memory-mapped |
| **`database_ss`** | 3Di sequences (H/E/C) and structural assignments | Secondary structure<br>~1 byte/residue<br>Sequential/Indexed |
| **`database_ss.index`** | Index for secondary structure data | SS index<br>Minimal<br>Memory-mapped |
| **`database_h`** | FASTA headers and structural metadata | Header database<br>Variable<br>Random access |
| **`database_h.index`** | Index for header data access | Header index<br>Minimal<br>Memory-mapped |
| **`database.lookup`** | Maps internal numeric IDs to original structure identifiers | Lookup table<br>Minimal<br>Hash lookup |
| **`database.dbtype`** | Binary file specifying data types (type 10 for structural) | Database type<br>4 bytes<br>Read-once |
#### Index Structure and Memory Mapping

Foldseek uses memory-mapped I/O for efficient database access:

```cpp
// Memory-mapped database access pattern
DBReader<unsigned int> sequenceReader(dbPath, indexPath, threads,
                                     DBReader<unsigned int>::USE_DATA |
                                     DBReader<unsigned int>::USE_INDEX |
                                     DBReader<unsigned int>::USE_HEADER);
DBReader<unsigned int> caReader(caPath, caIndexPath, threads,
                               DBReader<unsigned int>::USE_DATA |
                               DBReader<unsigned int>::USE_INDEX);
DBReader<unsigned int> ssReader(ssPath, ssIndexPath, threads,
                               DBReader<unsigned int>::USE_DATA |
                               DBReader<unsigned int>::USE_INDEX);
```

#### Index File Format

The index files follow the MMseqs2 format optimized for structural data:

**`database.index` format:**
```
id    offset    length
0     0         1247      # First structure: 1247 bytes
1     1247      892       # Second structure: 892 bytes
2     2139      1456      # Third structure: 1456 bytes
...
```

Where:
- `id`: Internal numeric identifier (0-based, sequential)
- `offset`: Byte offset in the data file
- `length`: Length of the entry in bytes

#### Structural Index Architecture

Foldseek creates specialized indices for different types of structural queries:

```cpp
// 3Di k-mer index for structural search
struct StructuralIndex {
    std::vector<uint64_t> kmerTable;      // 3Di k-mer hash table
    std::vector<uint32_t> positionTable;  // Position lookup table
    std::vector<float> scoreMatrix;       // 3Di substitution scores
    std::vector<char> sequenceData;       // 3Di sequences for fast access
};

// Index creation for different subsets
enum IndexSubset {
    INDEX_SUBSET_ALL = 0,        // All data types
    INDEX_SUBSET_SEQUENCE = 1,   // Sequence data only
    INDEX_SUBSET_STRUCTURE = 2   // Structural data only
};
```

#### Database Type Specifications

The `database.dbtype` file contains binary type information:

```cpp
enum DatabaseType {
    DBTYPE_GENERIC_DB = 0,      // Basic sequence data
    DBTYPE_AMINO_ACID = 1,      // Protein sequences
    DBTYPE_NUCLEOTIDE = 2,      // DNA/RNA sequences
    DBTYPE_STRUCTURAL_DB = 10,  // 3Di + coordinates + secondary structure
    DBTYPE_PROFILE_DB = 11,     // PSSM data
    DBTYPE_ALIGNMENT_DB = 12    // Alignment results
};
```

#### Memory Mapping Strategy

Foldseek uses memory-mapped files for instant access to any structure:

```cpp
// Example: Accessing structural data by ID
size_t entryId = 42;
const char* sequenceData = sequenceReader.getData(entryId, thread_idx);
const char* caData = caReader.getData(entryId, thread_idx);
const char* ssData = ssReader.getData(entryId, thread_idx);

// Memory-efficient access patterns
enum AccessMode {
    USE_DATA = 1,        // Load data file
    USE_INDEX = 2,       // Load index file
    USE_HEADER = 4,      // Load header data
    USE_LOOKUP = 8       // Load lookup table
};
```

This architecture enables:
- **Random access** to millions of structures without loading entire database
- **Parallel processing** across multiple cores
- **Efficient caching** by the operating system
- **Memory efficiency** - only active data is resident in RAM

## Alignment Engine Architecture

### Multiple Alignment Algorithms

Foldseek supports multiple alignment algorithms:

1. **3Di+AA Alignment**: Combines structural and sequence information
2. **TM-align**: Global structural alignment
3. **Local Structural Alignment**: Smith-Waterman on 3Di sequences

### TM-score Implementation

The TM-score engine implements the TM-align algorithm:

```cpp
// Core TM-score calculation
float calculateTMScore(const std::vector<CAlpha>& query,
                      const std::vector<CAlpha>& target,
                      const Matrix3x3& rotation,
                      const Vector3& translation) {
    float score = 0.0f;
    float d0 = 1.24f * pow(query.size() - 15.0f, 1.0f/3.0f) - 1.8f;
    for (size_t i = 0; i < query.size(); ++i) {
        float distance = calculateDistance(query[i], target[i], rotation, translation);
        score += 1.0f / (1.0f + pow(distance / d0, 2.0f));
    }
    return score / query.size();
}
```

### SIMD Alignment Acceleration

Alignment operations use SIMD instructions for performance:

```cpp
// SIMD-accelerated dynamic programming
void alignSIMD(const char* query, const char* target,
               __m256i* scoreMatrix, __m256i* tracebackMatrix) {
    // Vectorized alignment computation
    for (size_t i = 1; i < queryLen; ++i) {
        for (size_t j = 1; j < targetLen; ++j) {
            // SIMD operations for score calculation
        }
    }
}
```

## Multimer Engine Architecture

### Complex Representation

Multimer structures are represented as collections of chains:

```cpp
struct Multimer {
    std::vector<Chain> chains;
    std::vector<Interface> interfaces;
    Matrix4x4 transformation;
    float complexScore;
};
```

### Chain Matching Algorithm

The multimer engine uses optimal assignment algorithms:

```cpp
// Hungarian algorithm for chain matching
std::vector<int> matchChains(const std::vector<Chain>& queryChains,
                           const std::vector<Chain>& targetChains) {
    // Compute similarity matrix
    Matrix similarityMatrix = computeChainSimilarities(queryChains, targetChains);
    // Apply Hungarian algorithm
    return hungarianAlgorithm(similarityMatrix);
}
```

### Interface Analysis

Interface analysis computes interaction scores:

```cpp
// Interface LDDT calculation
float calculateInterfaceLDDT(const Interface& interface,
                           const Matrix4x4& transformation) {
    float totalScore = 0.0f;
    for (const auto& contact : interface.contacts) {
        float distance = calculateContactDistance(contact, transformation);
        totalScore += lddtScore(distance);
    }
    return totalScore / interface.contacts.size();
}
```

## GPU Acceleration Architecture

### CUDA Integration

Foldseek integrates CUDA for GPU acceleration:

```cpp
// CUDA kernel for structural alignment
__global__ void structuralAlignmentKernel(const float* queryCoords,
                                        const float* targetCoords,
                                        float* scoreMatrix,
                                        int querySize, int targetSize) {
    // GPU-accelerated alignment computation
}
```

### Memory Management

GPU memory is managed efficiently:

```cpp
// GPU memory allocation and transfer
void allocateGPUResources(const StructuralDatabase& db) {
    // Allocate GPU memory for coordinates
    cudaMalloc(&gpuQueryCoords, querySize * sizeof(float3));
    cudaMalloc(&gpuTargetCoords, targetSize * sizeof(float3));
    // Transfer data to GPU
    cudaMemcpy(gpuQueryCoords, hostQueryCoords, querySize * sizeof(float3),
               cudaMemcpyHostToDevice);
}
```

## Performance Optimization

### Parallel Processing

Foldseek uses multiple levels of parallelism:

1. **Thread-level**: OpenMP for multi-core processing
2. **SIMD-level**: Vector instructions for data-parallel operations
3. **GPU-level**: CUDA for massively parallel computations
4. **MPI-level**: Multi-node processing for large-scale analyses

### Memory Optimization

Memory usage is optimized through:

1. **Memory-mapped I/O**: Avoids loading entire databases into RAM
2. **Streaming processing**: Processes data in chunks
3. **Compression**: Compresses structural data when possible
4. **Caching**: Intelligent caching of frequently accessed data

### Algorithmic Optimization

Key optimizations include:

1. **Early termination**: Stops computation when results are unlikely to improve
2. **Pruning**: Eliminates unpromising candidates early
3. **Approximation**: Uses fast approximations for initial scoring
4. **Indexing**: Precomputed indices for fast lookup

## Development Guidelines

### Code Organization

Foldseek follows a modular architecture:

```
src/
├── commons/           # Shared utilities and data structures
├── alignment/         # Alignment algorithms
├── clustering/        # Clustering algorithms
├── prefiltering/      # Prefiltering algorithms
├── strucclustutils/   # Structural clustering utilities
├── workflow/          # High-level workflow implementations
└── version/           # Version information
```

### Testing Strategy

Comprehensive testing includes:

1. **Unit tests**: Individual function testing
2. **Integration tests**: Module interaction testing
3. **Performance tests**: Benchmarking against known datasets
4. **Regression tests**: Ensuring compatibility with previous versions

### Performance Profiling

Profiling tools are used to identify bottlenecks:

1. **gprof**: CPU profiling
2. **nvprof**: GPU profiling
3. **perf**: System-level profiling
4. **Custom timers**: Module-specific timing

This hierarchical architecture allows for modular development, easy extension of Foldseek's capabilities, and efficient processing of large-scale structural data.
