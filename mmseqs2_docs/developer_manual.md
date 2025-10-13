# MMseqs2 Developer Manual: Submodule Classification

## Overview

MMseqs2 is organized into submodules that can be classified into four hierarchical categories based on their level of abstraction and functionality:

1. **Workflow**: High-level user-facing workflows that provide convenient interfaces for common tasks.
2. **High Level API**: Workflows that combine multiple lower-level modules to perform complex operations like searching or clustering.
3. **Mid-level API**: Core algorithmic modules that implement the main computational methods for sequence comparison.
4. **Low Level API**: Fundamental modules for data manipulation, I/O operations, and utility functions.

## Classification

### Workflow
These are high-level user-facing workflows that provide convenient interfaces for common tasks, chaining multiple lower-level modules together.

- **easy-search**: Sensitive homology search workflow.
- **easy-cluster**: Clustering workflow using cascaded clustering.
- **easy-linclust**: Fast clustering workflow using linear time clustering.
- **easy-taxonomy**: Taxonomy assignment workflow.
- **easy-rbh**: Reciprocal best hit workflow.
- **easy-linsearch**: Linear search workflow.

### High Level API
These workflows combine multiple lower-level modules to perform complex operations.

- **search**: Sequence search workflow that combines prefiltering and alignment.
- **cluster**: Clustering workflow that combines prefiltering, alignment, and clustering algorithms.
- **linclust**: Linear time clustering workflow.
- **clust**: Core clustering algorithm.
- **clusthash**: Hash-based clustering for equal length sequences.
- **clusterupdate**: Update existing clustering with new sequences.
- **mergeclusters**: Merge multiple clustering results.
- **taxonomy**: Taxonomy assignment workflow.
- **multihitdb**: Create sequence database for multi-hit searches.
- **multihitsearch**: Multi-hit search workflow.
- **map**: Sequence mapping workflow.
- **rbh**: Reciprocal best hit workflow.
- **enrich**: Search enrichment workflow (expandaln, expand2profile).

### Mid-level API
Core algorithmic modules that implement the main computational methods.

- **prefilter**: Double consecutive diagonal k-mer search for candidate identification.
- **ungappedprefilter**: Optimal diagonal score search.
- **gappedprefilter**: Smith-Waterman-based prefiltering.
- **kmermatcher**: Find bottom-m-hashed k-mer matches within sequence database.
- **kmersearch**: k-mer search using index.
- **align**: Optimal gapped local alignment.
- **alignall**: Within-result all-vs-all gapped local alignment.
- **alignbykmer**: Heuristic gapped local k-mer based alignment.
- **expandaln**: Expand alignment results.
- **offsetalignment**: Offset alignment by ORF start position.
- **proteinaln2nucl**: Transform protein alignments to nucleotide alignments.
- **rescorediagonal**: Compute sequence identity for diagonal.
- **msa2profile**: Convert MSA to profile database.
- **msa2result**: Convert MSA to profile and result databases.
- **result2profile**: Compute profile from result database.
- **convertmsa**: Convert STOCKHOLM file to MSA database.
- **tsv2exprofiledb**: Create expandable profile database from TSV files.

### Low Level API
Fundamental modules for data manipulation, I/O operations, and utility functions.

#### Database Management
- **createdb**: Convert FASTA/Q files to sequence database.
- **createindex**: Store precomputed index on disk.
- **createlinindex**: Create linsearch index.
- **subtractdbs**: Subtract databases.
- **tar2db**: Create database from tar archive.
- **swapdb**: Swap query and target in result database.
- **aliasdb**: Alias database.
- **cpdb**: Copy database.
- **concatdbs**: Concatenate databases.
- **createsubdb**: Create sub-database.
- **db2tar**: Create tar from database.
- **lndb**: Hard link database.
- **mergedbs**: Merge multiple databases.
- **splitsequence**: Split sequences into smaller chunks.
- **mvdb**: Move database.
- **renamedbkeys**: Rename database keys.
- **splitdb**: Split database into chunks.
- **tsv2db**: Convert TSV file to database.

#### Sequence Manipulation
- **extractorfs**: Six-frame extraction of open reading frames.
- **extractframes**: Extract frames from nucleotide sequence database.
- **reverseseq**: Reverse sequences.
- **translateaa**: Translate amino acid sequences.
- **translatenucs**: Translate nucleotide sequences.
- **recoverlongestorf**: Recover longest open reading frame.
- **orftocontig**: ORF to contig.
- **makepaddedseqdb**: Make padded sequence database.
- **masksequence**: Mask sequences.
- **extractalignedregion**: Extract aligned regions from sequences.

#### Result Handling
- **convertalis**: Convert alignment database to BLAST-tab, SAM or custom format.
- **createtsv**: Convert result database to tab-separated flat file.
- **result2flat**: Create flat file by adding FASTA headers to database entries.
- **createseqfiledb**: Create database of unaligned FASTA entries.
- **swapresults**: Transpose prefilter/alignment database.
- **result2rbh**: Filter merged result database to retain reciprocal best hits.
- **result2msa**: Compute MSA database from result database.
- **result2dnamsa**: Compute MSA database with insertions in query for DNA sequences.
- **result2stats**: Compute statistics for each entry in database.
- **filterresult**: Pairwise alignment result filter.
- **result2repseq**: Get representative sequences from result database.
- **sortresult**: Sort result database.
- **summarizealis**: Summarize alignment result to one row.
- **summarizeresult**: Extract annotations from alignment database.

#### Utilities
- **compress**: Compress database entries.
- **decompress**: Decompress database entries.
- **gpuserver**: Start GPU server.
- **apply**: Apply external program to each entry in database.
- **prefixid**: Prefix database keys.
- **suffixid**: Suffix database keys.
- **touchdb**: Touch database.
- **unpackdb**: Unpack database entries to flat files.
- **view**: View database entries.
- **filterdb**: Filter database entries.
- **setextendeddbtype**: Set extended database type.
- **besthitperset**: Best hit per set.
- **combinepvalperset**: Combine p-values per set.
- **mergeresultsbyset**: Merge results by set.

## Hierarchical Dependencies

### Workflow → High Level API
Workflow modules call high-level API modules to perform their tasks. For example:
- `easy-search` (workflow) internally calls the `search` workflow via `easysearch.sh` script.
- `easy-cluster` (workflow) internally calls the `cluster` workflow.
- `easy-linclust` (workflow) internally calls the `linclust` workflow.
- `easy-taxonomy` (workflow) internally calls the `taxonomy` workflow.
- `easy-rbh` (workflow) internally calls the `rbh` workflow.
- `easy-linsearch` (workflow) internally calls the `linsearch` workflow.

### High Level API → Mid-level API
High-level workflows combine mid-level modules:
- The `search` workflow calls `prefilter` followed by `align` (or `rescorediagonal` for ungapped mode).
- The `cluster` workflow calls `prefilter`, `align`, and `clust` in sequence.
- The `linclust` workflow uses `kmermatcher` and `clust`.
- The `taxonomy` workflow calls `search` followed by taxonomy-specific modules like `lca`.
- The `multihitsearch` workflow calls `prefilter` and `align`.
- The `map` workflow calls `prefilter` and `align` with specific parameters for mapping.
- The `rbh` workflow calls `search` twice (forward and reverse) and `result2rbh`.

From the source code in `Search.cpp`:
```cpp
cmd.addVariable("PREFILTER_PAR", par.createParameterString(par.prefilter).c_str());
cmd.addVariable("ALIGNMENT_PAR", par.createParameterString(par.align).c_str());
```

From the source code in `Cluster.cpp`:
```cpp
cmd.addVariable("PREFILTER_PAR", par.createParameterString(par.prefilter).c_str());
cmd.addVariable("ALIGNMENT_PAR", par.createParameterString(par.align).c_str());
cmd.addVariable("CLUSTER_PAR", par.createParameterString(par.clust).c_str());
```

### Mid-level API → Low Level API
Mid-level modules use low-level APIs for data access and manipulation:
- `prefilter` reads sequence databases using `DBReader` (database module), uses `masksequence` for low-complexity masking, and writes results via `DBWriter`.
- `align` performs alignments using SIMD-accelerated Smith-Waterman and writes results using database I/O functions.
- `clust` uses database modules for reading/writing cluster results and connected component algorithms.
- Profile modules like `result2profile` use `result2msa` and sequence manipulation for MSA processing.
- `kmermatcher` uses k-mer indexing and database access for linear-time matching.
- All modules use `Parameters` for configuration and utility functions from the commons.

For example, in prefiltering modules, database access is handled through:
```cpp
DBReader<unsigned int> qdbr(queryDb, par.threads, DBReader<unsigned int>::USE_INDEX);
```

Alignment modules write results using:
```cpp
DBWriter writer(outDb, outIndex, par.threads, par.compressed, Parameters::DBTYPE_ALIGNMENT_RES);
```

### Low Level API → Core Infrastructure
Low-level modules provide the foundation:
- **Database Management**: `createdb`, `createindex`, `concatdbs`, etc., handle file I/O, indexing, and database operations using `DBReader`, `DBWriter`, and `FileUtil`.
- **Sequence Manipulation**: `extractorfs`, `translatenucs`, `masksequence`, etc., process raw sequence data using utilities like `Sequence`, `TranslateNucl`, and `Masker`.
- **Result Handling**: `convertalis`, `filterdb`, `result2stats`, etc., format and filter outputs using database operations and expression parsing.
- **Utilities**: `compress`, `decompress`, `apply`, `view`, `filterdb`, etc., provide common functionality for database management and external program execution.

This hierarchical structure allows for modular development and easy extension of MMseqs2's capabilities.