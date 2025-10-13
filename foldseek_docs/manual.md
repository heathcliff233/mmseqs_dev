# Foldseek User Manual

This document provides a detailed manual for each module in Foldseek, the fast and sensitive protein structure search and clustering tool.

## Common Command Line Arguments

The following are some of the most common command line arguments used across various Foldseek modules.

| Flag | Description | Default |
| :--- | :--- | :--- |
| `-s <float>` | Sensitivity parameter for structural search (higher is more sensitive). | `9.5` |
| `-c <float>` | Coverage threshold for clustering and alignment. | `0.0` |
| `--cov-mode <int>` | Coverage mode (0: coverage of query and target, 1: coverage of target, 2: coverage of query). | `0` |
| `--min-seq-id <float>` | Minimum sequence identity for clustering and alignment. | `0.0` |
| `--alignment-type <int>` | Alignment type (0: 3Di only, 1: TMalign, 2: 3Di+AA). | `2` |
| `--tmscore-threshold <float>` | TM-score threshold for accepting alignments. | `0.0` |
| `--lddt-threshold <float>` | LDDT threshold for accepting alignments. | `0.0` |
| `--threads <int>` | Number of threads to use. | `1` |
| `-v <int>` | Verbosity level (0: quiet, 1: default, 2: verbose, 3: debug). | `1` |
| `<tmpDir>` | A temporary directory for intermediate files. | |

For more specific parameters, please refer to the documentation for each module.

## Modules

Foldseek is composed of many different modules that can be combined to create powerful structural analysis workflows. The modules are grouped by their functionality below.

*   [Easy Workflows](./submodules/easy_workflows.md)
*   [Structure Search](./submodules/structure_search.md)
*   [Structure Clustering](./submodules/structure_clustering.md)
*   [Multimer Analysis](./submodules/multimer.md)
*   [Structure Manipulation](./submodules/structure_manipulation.md)
*   [Database Management](./submodules/databases.md)

### Easy Workflows
High-level workflows for common tasks. See `foldseek_docs/submodules/easy_workflows.md` for full usage, parameters, and examples.

### Structure Search Modules
Core search and alignment modules. See `foldseek_docs/submodules/structure_search.md` for details. (Note: `aln2tmscore` and `convert2pdb` are documented under structure manipulation.)

### Structure Clustering Modules
Clustering algorithms and workflows. See `foldseek_docs/submodules/structure_clustering.md`.

### Multimer Analysis Modules
Complex (multimer) search, clustering, and reporting. See `foldseek_docs/submodules/multimer.md`.

### Structure Manipulation Modules
Database creation, conversion, and post-processing. See `foldseek_docs/submodules/structure_manipulation.md`.

### Database Management Modules
Database downloads, indexing, and cluster search DBs. See `foldseek_docs/submodules/databases.md`.

## Easy Workflows
See `foldseek_docs/submodules/easy_workflows.md` for full usage, parameters, and examples for `easy-search`, `easy-cluster`, `easy-rbh`, `easy-multimersearch`, and `easy-multimercluster`.

## Structure Search Modules
See `foldseek_docs/submodules/structure_search.md` for search and alignment modules: `search`, `structurealign`, `tmalign`, and `structurerescorediagonal`.

## Structure Clustering Modules
See `foldseek_docs/submodules/structure_clustering.md` for `cluster` and `clust` usage and algorithms.


## Multimer Analysis Modules
See `foldseek_docs/submodules/multimer.md` for multimer search, clustering, scoring, filtering, and reports.


## Structure Manipulation Modules
See `foldseek_docs/submodules/structure_manipulation.md` for `createdb`, `compressca`, `convertalis`, `aln2tmscore`, `result2profile`, and `convert2pdb`.


## Database Management Modules
See `foldseek_docs/submodules/databases.md` for `databases`, `createindex`, and `createclusearchdb`.


## Output Formats

### Tab-Separated Format (Default)
The default output format includes columns for query, target, sequence identity, alignment length, mismatches, gap openings, start/end positions, E-value, and bit score.

### Custom Output Formats
Use `--format-output` to specify custom columns:

```bash
foldseek easy-search query target result tmp --format-output "query,target,fident,alntmscore,u,t"
```

**Available Fields:**
- `query`: Query identifier
- `target`: Target identifier
- `fident`: Sequence identity
- `alnlen`: Alignment length
- `qstart`, `qend`: Query start/end positions
- `tstart`, `tend`: Target start/end positions
- `evalue`: E-value
- `bits`: Bit score
- `alntmscore`: TM-score of alignment
- `qtmscore`: TM-score normalized by query
- `ttmscore`: TM-score normalized by target
- `lddt`: Average LDDT
- `prob`: Hit probability
- `u`: Rotation matrix
- `t`: Translation vector

### HTML Output
Interactive HTML visualization:

```bash
foldseek easy-search query target result.html tmp --format-mode 3
```

### PDB Superposition
Superimposed PDB files:

```bash
foldseek easy-search query target result tmp --format-mode 5
```

## Performance Optimization

### GPU Acceleration
Enable GPU acceleration for faster searches:

```bash
foldseek easy-search query target result tmp --gpu 1 --prefilter-mode 1
```

### Memory Optimization
For large databases, consider:
- Using `--sort-by-structure-bits 0` to reduce memory usage
- Splitting large searches into smaller chunks
- Using precomputed indexes for repeated searches

### Sensitivity vs Speed Trade-offs
- Lower `-s` values: Faster but less sensitive
- Higher `-s` values: Slower but more sensitive
- Use `--exhaustive-search` for maximum sensitivity (very slow)
- Use `--num-iterations` for iterative refinement

## Integration with External Tools

### Converting Results to Other Formats
```bash
# Convert alignment results to various formats
foldseek convertalis queryDB targetDB alignmentDB results.tsv --format-output query,target,fident,alnlen,evalue,bits

# Create profiles from search results
foldseek result2profile queryDB targetDB search_results profileDB
```

### Using with Structure Prediction
```bash
# Predict structures with ColabFold
colabfold_batch sequences.fasta structures/

# Search predicted structures
foldseek easy-search structures/ targetDB results tmp
```

<!-- Comparative overview removed to avoid duplication with introduction.md. -->
