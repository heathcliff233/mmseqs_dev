# Introduction to Foldseek Core Concepts

Foldseek is a revolutionary software suite for fast and sensitive protein structure searching and clustering. It achieves unprecedented speed by representing protein structures using a compact 3D-interaction (3Di) alphabet, enabling structural comparisons at sequence-like speeds while maintaining high sensitivity.

## Why is Foldseek so fast? The 3Di Revolution

The key innovation behind Foldseek's speed is the **3Di alphabet** - a compact representation that captures essential structural information while dramatically reducing the complexity of structural comparisons.

### The 3Di Alphabet: Two-Tier System

Traditional structural alignment methods compare full 3D coordinates, which is computationally expensive. Foldseek uses a sophisticated **two-tier system** for structural representation:

#### Internal Classification (20 States)
- **20 structural centroids** (states 0-19) trained via neural network embedding
- Each residue is assigned to the closest centroid using Euclidean distance
- Provides maximum structural discrimination for accurate similarity detection
- **Used in**: Structure-to-structure alignment and initial classification

#### External Representation (3-Letter Alphabet)
- **H** (Helix): α-helical conformations
- **E** (Strand): β-strand conformations
- **C** (Coil): Loop and irregular conformations
- **Used in**: Database storage and all search operations

#### Internal vs. Output Representation

The 3Di system uses a sophisticated two-tier approach for structural classification:

1. **Internal Classification**: Uses **20 centroids** (states 0-19) trained on structural features to provide detailed structural discrimination
2. **Final Output**: Maps these 20 internal states to the **3-letter alphabet** (H/E/C) through a substitution matrix for efficient k-mer matching and alignment

This design enables:
- **Rich structural classification** with 20 internal states for high sensitivity
- **Compact representation** with 3-letter output for fast searching
- **Memory efficiency** with ~1 byte per residue instead of ~8 bytes for coordinates
- **10,000x faster** prefiltering compared to coordinate-based methods

#### AA and 3Di Integration

Foldseek stores and uses both amino acid (AA) sequences and 3Di sequences together:

- **AA sequences** (20-letter alphabet): Stored in `database` files for sequence-based operations
- **3Di sequences** (3-letter alphabet): Stored in `database_ss` files for structural operations
- **Combined alignment**: Uses both AA and 3Di scoring matrices for optimal sensitivity
- **Synchronized storage**: Both sequence types have identical structure and indexing

### Multi-Stage Structural Search Strategy

Foldseek employs a hierarchical search strategy similar to sequence-based tools but optimized for structural data:

1. **3Di K-mer Matching**: Fast identification of structurally similar regions using 3Di k-mers
2. **Structural Prefiltering**: Double consecutive k-mer matches on the same diagonal identify promising candidates
3. **Ungapped Structural Alignment**: Fast verification of structural similarity
4. **Full Structural Alignment**: TM-align or 3Di+AA Smith-Waterman alignment for final scoring

## The Foldseek Database

High-level overview: Foldseek uses compact 3Di sequences plus optional coordinates to enable fast structural search. For file layout and operational details, see:
- Databases (`foldseek_docs/submodules/databases.md`)
- Developer Manual (`foldseek_docs/developer_manual.md`)

## Structural Similarity Measures

### 3Di Score
The primary scoring mechanism uses 3Di sequences with position-specific scoring matrices optimized for structural similarity detection.

### TM-Score
For high-precision alignment, Foldseek can use TM-score, which provides:
- **Global alignment** quality assessment
- **Statistical significance** estimates
- **Superposition** capabilities for visualization

### LDDT Score
Local Distance Difference Test (LDDT) provides residue-level quality assessment, particularly useful for:
- **Local structural conservation** analysis
- **Domain identification**
- **Quality assessment** of predicted structures

## The Power of Modularity: Building Structural Workflows

Foldseek inherits MMseqs2's modular architecture, allowing users to build custom structural analysis pipelines:

### Example: Custom Structure-Based Clustering

```bash
# Create structural database
foldseek createdb structures/ structDB

# Perform structural search
foldseek search structDB structDB aln tmp

# Convert to structural clustering
foldseek cluster structDB structDB aln structDB_clu tmp

# Extract representatives
foldseek createsubdb structDB_clu structDB structDB_reps
foldseek convert2fasta structDB_reps structDB_reps.fasta
```

### Integration with External Tools

The modular design enables seamless integration with other structural biology tools:

```bash
# Extract cluster members
foldseek createseqfiledb structDB structDB_clu structDB_members

# Run external analysis on each cluster
foldseek apply structDB_members structDB_analysis -- your_analysis_tool -i -
```

## Foldseek vs MMseqs2: Key Differences

While Foldseek builds upon the MMseqs2 framework, it introduces fundamental differences in search methodology, database structure, and alignment algorithms to enable efficient structural comparisons.

### Search Methodology Comparison

| Aspect | MMseqs2 | Foldseek |
|--------|---------|----------|
| **Core Algorithm** | K-mer based sequence similarity search | 3Di-based structural similarity search |
| **Alphabet** | 20 amino acids (reduced alphabet for sensitivity) | 3-letter 3Di alphabet (H/E/C) with 20 internal centroids |
| **Search Strategy** | 1. K-mer matching<br>2. Double consecutive k-mer filtering<br>3. Ungapped alignment<br>4. SIMD-accelerated Smith-Waterman | 1. 3Di k-mer matching<br>2. Structural prefiltering<br>3. Ungapped structural alignment<br>4. 3Di+AA or TM-align |
| **Speed Advantage** | 10,000x faster than BLAST | 10,000x faster than coordinate-based methods |
| **Memory Usage** | ~7 bytes per residue for index | ~1 byte per residue for 3Di sequences |

<!-- Database structure comparison moved to databases.md to avoid duplication. -->

### Alignment Algorithm Comparison

| Feature | MMseqs2 | Foldseek |
|---------|---------|----------|
| **Primary Algorithm** | Smith-Waterman sequence alignment | 3Di+AA combined alignment |
| **Scoring** | Sequence identity, E-values | TM-score, LDDT, 3Di scores |
| **Structural Alignment** | Not available | TM-align integration |
| **GPU Support** | Yes (sequence search) | Yes (structural search) |
| **Substitution Matrix** | BLOSUM62, VTML matrices | 3Di substitution matrix |

## Applications of Foldseek

### Large-Scale Structure Comparison
- **AlphaFold Database** screening
- **PDB-wide** structural similarity searches
- **Metagenomic** structure annotation

### Structure-Based Function Prediction
- **SCOPe/CATH** domain classification
- **EC number** assignment via structural similarity
- **GO term** prediction from structural neighbors

### Drug Discovery
- **Binding site** identification
- **Off-target** effect prediction
- **Lead optimization** through structural similarity

This modular, efficient approach makes Foldseek not just a tool, but a comprehensive platform for structural bioinformatics research.
