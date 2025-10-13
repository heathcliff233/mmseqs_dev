# MMseqs2 CD-HIT 2D-like Script

This script implements a CD-HIT 2D-like workflow using MMseqs2. It performs the first step of incremental clustering by searching new sequences against old representative sequences and outputting the results.

## Overview

CD-HIT 2D compares two protein datasets and outputs sequences from the second dataset that do not have significant matches in the first dataset. This script replicates this functionality using MMseqs2's efficient search capabilities.

## Usage

```bash
./mmseqs-cdhit-2d-like.sh <oldSequenceDB> <newSequenceDB> <oldClusteringDB> <outputFasta> <outputTsv> <tmpDir>
```

### Parameters

- `oldSequenceDB`: Path to the old sequence database (MMseqs2 format)
- `newSequenceDB`: Path to the new sequence database (MMseqs2 format)
- `oldClusteringDB`: Path to the old clustering results (MMseqs2 format)
- `outputFasta`: Output path for unassigned sequences in FASTA format
- `outputTsv`: Output path for assignments in TSV format
- `tmpDir`: Temporary directory for intermediate files

### Output Files

1. **FASTA file**: Contains sequences from the new database that were not assigned to any cluster in the old clustering
2. **TSV file**: Contains the assignment results showing which new sequences matched which old representatives

## Workflow

The script performs the following steps:

1. **Key Mapping**: Creates a mapping to avoid key conflicts between old and new sequences
2. **Re-keying**: Updates the keys of new sequences to avoid conflicts
3. **Representative Extraction**: Extracts representative sequences from the old clustering
4. **Index Creation**: Creates a searchable index for the old representatives
5. **Search**: Performs linsearch to find matches between new sequences and old representatives
6. **Assignment Filtering**: Gets the best assignment for each new sequence
7. **Unassigned Extraction**: Identifies sequences that were not assigned to any old cluster
8. **Output Generation**: Converts results to FASTA and TSV formats

## Requirements

- MMseqs2 must be installed and available in your PATH
- Input databases must be in MMseqs2 format (created with `mmseqs createdb`)
- Sufficient disk space for temporary files

## Example

```bash
# Create MMseqs2 databases
mmseqs createdb old_sequences.fasta oldDB
mmseqs createdb new_sequences.fasta newDB
mmseqs createdb representatives.fasta oldRepsDB

# Perform initial clustering on old sequences
mmseqs cluster oldDB oldClustering tmp1

# Run CD-HIT 2D-like analysis
./mmseqs-cdhit-2d-like.sh oldDB newDB oldClustering unassigned.fasta assignments.tsv tmp2
```

## Comparison with Original Incremental Clustering

This script performs only the first part of the full incremental clustering workflow:

- ✅ **This script**: Searches new sequences against old representatives and outputs unassigned sequences
- ❌ **Full incremental**: Also clusters the unassigned sequences and merges everything together

## Performance Notes

- Uses the same parameters as the original incremental clustering script (`--min-seq-id 0.3 -c 0.8`)
- Leverages MMseqs2's linsearch for fast similarity searching
- Creates temporary files that can be reused if the script is interrupted and restarted

## Troubleshooting

- Ensure all input databases exist and are in MMseqs2 format
- Check that MMseqs2 is properly installed and accessible
- Verify that the temporary directory has sufficient space
- Use the `-v` flag with MMseqs2 commands for more detailed output