# Structure Manipulation Modules

Foldseek provides various modules for processing, converting, and manipulating protein structure data, from database creation to format conversion and structural analysis.

## Database Creation and Management

### `createdb`

**Description**: Create a Foldseek database from protein structure files.

**Usage**:
```bash
foldseek createdb <i:directory|.tsv>|<i:PDB|mmCIF[.gz]|tar[.gz]|DB> ... <i:PDB|mmCIF[.gz]|tar|DB> <o:sequenceDB> [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--prostt5-model <string>` | Path to ProstT5 model for 3Di prediction | "" |
| `--gpu <int>` | Enable GPU acceleration for ProstT5 | 0 |
| `--chain-name-mode <int>` | Add chain to name: 0: auto, 1: always add | 0 |
| `--write-lookup <int>` | Write lookup file containing mapping from internal id, fasta id and file number | 1 |
| `--coord-store-mode <int>` | Coordinate storage mode: 1: C-alpha as float, 2: C-alpha as difference (uint16_t) | 2 |
| `--write-mapping <int>` | Write _mapping file containing mapping from internal id to taxonomic identifier | 0 |
| `--input-format <int>` | Format of input structures: 0: Auto-detect by extension, 1: PDB, 2: mmCIF, 3: mmJSON, 4: ChemComp, 5: Foldcomp | 0 |
| `--file-include <string>` | Include file names based on this regex | ".*" |
| `--file-exclude <string>` | Exclude file names based on this regex | "^$" |

**Examples**:

```bash
# Process multiple files
foldseek createdb examples/1tim.pdb.gz examples/8tim.pdb.gz DB

# Process a directory containing PDB|mmCIF[.gz]|tar[.gz]|DB recursively, only one directory can be given
foldseek createdb examples/ DB

# Process a TSV file with a list of PDB|mmCIF[.gz]|tar[.gz]|DB, only one TSV can be given
foldseek createdb examples.tsv DB

# Process a directory or tar file and filter based on file name
# Note: --file-include and --file-exclude only apply to directory or tar input
foldseek createdb examples/ DB --file-include "pdb.gz$"

# Predict 3Di sequences from an amino acid FASTA file using ProstT5
foldseek databases ProstT5 weights tmp
foldseek createdb QUERY.fasta DB --prostt5-model weights

# Accelerate inference by one to two magnitudes using GPU(s) (--gpu 1)
foldseek createdb db.fasta db --prostt5-model weights --gpu 1
```

### `compressca`

**Description**: Compress Cα coordinate data.

**Usage**:
```bash
foldseek compressca <i:DB> <o:caDB> [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--coord-store-mode <int>` | Coordinate storage mode: 1: C-alpha as float, 2: C-alpha as difference (uint16_t), 3: Plain text list of floats | 2 |

**Examples**:

```bash
# Compress Cα coordinates
foldseek compressca structDB structDB_compressed
```

## Format Conversion Modules

### `convert2pdb`

**Description**: Convert alignment results to superimposed PDB files.

**Usage**:
```bash
foldseek convert2pdb <i:Db> <o:pdbFile|pdbDir> [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--pdb-output-mode <int>` | PDB output mode: 0: Single multi-model PDB file, 1: One PDB file per chain, 2: One PDB file per complex | 0 |

**Examples**:

```bash
# Generate superimposed PDB files
foldseek convert2pdb queryDB superimposed_pdbs/
```

### `convertalis`

**Description**: Convert alignment results to various output formats.

**Usage**:
```bash
foldseek convertalis <i:queryDb> <i:targetDb> <i:alignmentDB> <o:alignmentFile> [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--format-mode <int>` | Output format: 0: BLAST-TAB, 1: SAM, 2: BLAST-TAB + query/db length, 3: Pretty HTML, 4: BLAST-TAB + column headers, 5: Calpha only PDB super-posed to query | 0 |
| `--format-output <string>` | Choose comma separated list of output columns from: query,target,evalue,gapopen,pident,fident,nident,qstart,qend,qlen,tstart,tend,tlen,alnlen,raw,bits,cigar,qseq,tseq,qheader,theader,qaln,taln,mismatch,qcov,tcov,qset,qsetid,tset,tsetid,taxid,taxname,taxlineage,lddt,lddtfull,qca,tca,t,u,qtmscore,ttmscore,alntmscore,rmsd,prob,complexqtmscore,complexttmscore,complexu,complext,complexassignid | "query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits" |
| `--exact-tmscore <int>` | Turn on fast exact TMscore (slow), default is approximate | 0 |
| `--gap-open <twin>` | Gap open cost | "aa:10,nucl:10" |
| `--gap-extend <twin>` | Gap extension cost | "aa:1,nucl:1" |
| `--threads <int>` | Number of CPU-cores used (all by default) | 10 |
| `--compressed <int>` | Write compressed output | 0 |
| `--db-output <bool>` | Return a result DB instead of a text file | 0 |

**Examples**:

```bash
# Create output in BLAST M8 format (12 columns):
#  (1,2) identifiers for query and target sequences/profiles,
#  (3) sequence identity, (4) alignment length, (5) number of mismatches,
#  (6) number of gap openings, (7-8, 9-10) alignment start and end-position in query and in target,
#  (11) E-value, and (12) bit score
foldseek convertalis queryDB targetDB result.m8

# Create a TSV containing pairwise alignments
foldseek convertalis queryDB targetDB result.tsv --format-output query,target,qaln,taln

# Annotate a alignment result with taxonomy information from targetDB
foldseek convertalis queryDB targetDB result.tsv --format-output query,target,taxid,taxname,taxlineage

# Create SAM output
foldseek convertalis queryDB targetDB result.sam --format-mode 1

# Create a TSV containing which query file a result comes from
foldseek createdb euk_queries.fasta bac_queries.fasta queryDB
foldseek convertalis queryDB targetDB result.tsv --format-output qset,query,target
```

## Structure Analysis Modules

### `aln2tmscore`

**Description**: Convert alignment results to TM-scores.

**Usage**:
```bash
foldseek aln2tmscore <i:queryDB> <i:targetDB> <i:alnDB> <o:resultDB> [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--threads <int>` | Number of CPU-cores used (all by default) | 10 |
| `--compressed <int>` | Write compressed output | 0 |

**Examples**:

```bash
# Convert alignments to TM-scores
foldseek aln2tmscore queryDB targetDB alignments tm_scores
```

### `result2profile`

**Description**: Convert search results to sequence profiles.

**Usage**:
```bash
foldseek result2profile <i:queryDB> <i:targetDB> <i:resultDB> <o:profileDB> [options]
```

**Parameters**:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--comp-bias-corr <int>` | Correct for locally biased amino acid composition (range 0-1) | 1 |
| `--comp-bias-corr-scale <float>` | Correct for locally biased amino acid composition (range 0-1) | 1.000 |
| `-e <double>` | List matches below this E-value (range 0.0-inf) | 10.0 |
| `--gap-open <twin>` | Gap open cost | "aa:10,nucl:10" |
| `--gap-extend <twin>` | Gap extension cost | "aa:1,nucl:1" |
| `--mask-profile <int>` | Mask query sequence of profile using tantan | 1 |
| `--e-profile <double>` | Include sequences matches with < E-value thr. into the profile (>=0.0) | 0.001 |
| `--wg <bool>` | Use global sequence weighting for profile calculation | 0 |
| `--filter-msa <int>` | Filter msa: 0: do not filter, 1: filter | 1 |
| `--filter-min-enable <int>` | Only filter MSAs with more than N sequences, 0 always filters | 0 |
| `--max-seq-id <float>` | Reduce redundancy of output MSA using max. pairwise sequence identity | 0.900 |
| `--qid <string>` | Reduce diversity of output MSAs using min.seq. identity with query sequences | "0.0" |
| `--qsc <float>` | Reduce diversity of output MSAs using min. score per aligned residue with query sequences | -20.000 |
| `--cov <float>` | Filter output MSAs using min. fraction of query residues covered by matched sequences | 0.000 |
| `--diff <int>` | Filter MSAs by selecting most diverse set of sequences, keeping at least this many seqs in each MSA block of length 50 | 1000 |
| `--pseudo-cnt-mode <int>` | Use 0: substitution-matrix or 1: context-specific pseudocounts | 0 |
| `--profile-output-mode <int>` | Profile output mode: 0: binary log-odds 1: human-readable frequencies | 0 |
| `--allow-deletion <bool>` | Allow deletions in a MSA | 0 |
| `--threads <int>` | Number of CPU-cores used (all by default) | 10 |
| `--compressed <int>` | Write compressed output | 0 |

**Examples**:

```bash
# Convert search results to profiles
foldseek result2profile queryDB targetDB search_results profileDB

# Custom profile filtering
foldseek result2profile queryDB targetDB search_results profileDB --max-seq-id 0.8 --qid 0.3 --cov 0.5
```

## Structure Processing Workflows

### Structure Database Creation Pipeline

```bash
# 1. Create basic database
foldseek createdb structures/ structDB

# 2. Create index for fast search
foldseek createindex structDB tmp

# 3. Compress coordinates
foldseek compressca structDB structDB_compressed
```

### Structure Conversion Pipeline

```bash
# 1. Perform structural search
foldseek easy-search query.pdb structDB search_results tmp

# 2. Convert to superimposed PDBs
foldseek convert2pdb queryDB superimposed_structures/

# 3. Convert to various formats
foldseek convertalis queryDB structDB search_results results.tsv --format-output query,target,fident,alnlen,evalue,bits

# 4. Create profiles from results
foldseek result2profile queryDB structDB search_results struct_profiles
```

### Quality Assessment Pipeline

```bash
# 1. Perform alignment
foldseek structurealign queryDB targetDB alignments

# 2. Convert to TM-scores
foldseek aln2tmscore queryDB targetDB alignments tm_scores

# 3. Generate quality report
foldseek convertalis queryDB targetDB tm_scores quality_report.tsv --format-output query,target,alntmscore,qtmscore,ttmscore
```

## Advanced Structure Manipulation

### Custom Structure Filtering

```bash
# 1. Create alignment database
foldseek structurealign queryDB targetDB alignments

# 2. Filter by TM-score
foldseek filterdb alignments filtered_alignments --filter-expression '$3 > 0.7'

# 3. Convert to readable format
foldseek convertalis queryDB targetDB filtered_alignments filtered_results.tsv
```

### Structure Profile Creation

```bash
# 1. Perform search
foldseek easy-search query.pdb structDB search_results tmp

# 2. Create profiles from results
foldseek result2profile queryDB structDB search_results struct_profiles

# 3. Search with profiles
foldseek search struct_profiles structDB profile_search_results tmp
```

### Batch Structure Processing

```bash
# Process multiple structure files
for i in {1..100}; do
    foldseek createdb batch_${i}/ batch_${i}_db
    foldseek easy-search batch_${i}_db reference_db batch_${i}_results tmp_${i}
done

# Merge all results
foldseek mergedbs all_results batch_*_results tmp
```

## Performance Optimization

### Database Creation Optimization
- Use `--chain-name-mode 0` for automatic chain naming
- Use `--coord-store-mode 2` for efficient coordinate storage
- Use `--write-lookup 1` to enable fast lookups
- Use GPU acceleration for ProstT5 when available

### Memory Optimization
- Use `--sort-by-structure-bits 0` to reduce memory usage
- Process large datasets in batches
- Use compressed databases when possible
- Monitor memory usage with `-v 2`

### Speed Optimization
- Use precomputed indexes for repeated operations
- Enable GPU acceleration for 3Di prediction
- Use appropriate compression levels
- Split large operations into smaller chunks

## Integration Examples

### With Structure Prediction
```bash
# Predict structures with AlphaFold
alphafold --fasta sequences.fasta --output structures/

# Create Foldseek database
foldseek createdb structures/ predicted_structDB

# Search against reference
foldseek easy-search predicted_structDB reference_structDB validation_results tmp
```

### With Experimental Validation
```bash
# Convert experimental structures to database
foldseek createdb experimental_structures/ exp_structDB

# Compare predicted vs experimental
foldseek structurealign predicted_structDB exp_structDB comparison_results

# Generate quality metrics
foldseek aln2tmscore predicted_structDB exp_structDB comparison_results quality_metrics
```

### Large-Scale Processing
```bash
# Process large structure datasets
foldseek splitdb large_structDB large_structDB_split --split 100

# Process each split
for i in {0..99}; do
    foldseek createdb large_structDB_split_${i}_100 large_split_${i}_db
    foldseek easy-search large_split_${i}_db reference_db split_${i}_results tmp_${i}
done

# Merge results
foldseek mergedbs all_struct_results split_*_results tmp
```

These structure manipulation modules provide comprehensive functionality for processing, converting, and analyzing protein structure data at scale.