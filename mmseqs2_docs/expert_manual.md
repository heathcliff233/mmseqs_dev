# MMseqs2 Expert Manual: Database Interactions

This document provides a detailed look into how various MMseqs2 modules interact with the MMseqs2 database format. Understanding these interactions is key to building custom workflows and troubleshooting complex pipelines.

## Core Concepts

The MMseqs2 database format is designed for high performance. It consists of several files:

-   **Data File**: Raw sequence or result data, concatenated and separated by `\0` bytes.
-   **Index File (`.index`)**: A tab-separated text file (`id\toffset\tlength`) that enables fast random access to any entry in the data file.
-   **Header Database (`_h`)**: A separate database for FASTA headers, allowing for fast access to either sequences or headers.
-   **Lookup File (`.lookup`)**: Maps internal numeric IDs to original FASTA identifiers.
-   **Database Type File (`.dbtype`)**: A binary file specifying the data type (protein, nucleotide, profile, etc.).

MMseqs2 modules primarily use `mmap` for reading database files, which maps the file content directly into memory for fast, on-demand access.

```{=typst}
#horizontalrule
```

## Module Documentation

### `createdb`

**Module Type**: Database Creation

**Function**: Converts one or more FASTA or FASTQ files into an MMseqs2 database.

**Database Interactions**:

*   **Input Reading**:
    *   Reads sequence data from one or more plain-text FASTA/FASTQ files. Input can also be piped from `stdin`.
    *   It does not read from MMseqs2 databases.

*   **Output Writing**:
    *   This module is a primary writer of MMseqs2 databases. It generates a set of files for the specified output database name (e.g., `myDB`).
    *   **`myDB` (Data File)**: Contains the raw sequence data, with each sequence terminated by a `\0` byte.
    *   **`myDB.index` (Index File)**: A tab-separated text file with three columns: `numeric_id`, `offset`, `length`. This file allows for random access to any sequence in the data file.
    *   **`myDB_h` (Header Data File)**: Contains the FASTA headers for each sequence, also terminated by `\0`.
    *   **`myDB_h.index` (Header Index File)**: The index for the header data file, with the same format as `myDB.index`.
    *   **`myDB.lookup` (Lookup File)**: If `--write-lookup 1` is set, this file is created. It's a tab-separated file mapping the generated `numeric_id` to the original FASTA header identifier and the source file number.
    *   **`myDB.dbtype` (Database Type File)**: A binary file containing an integer that specifies the db type (e.g., amino acid, nucleotide).

*   **Indexing and Headers**:
    *   By default, `createdb` assigns new, sequential, 0-based numeric IDs to each sequence.
    *   The original FASTA header is stored in the header database (`_h`).
    *   The header is not modified, except for the removal of the leading `>`.
    *   The index is not reset or modified if the database already exists; `createdb` will overwrite existing database files.

*   **Header Database Creation**:
    *   **Simultaneous Creation**: Creates both sequence and header databases together using separate `DBWriter` objects:
       - `DBWriter hdrWriter(hdrDataFile.c_str(), hdrIndexFile.c_str(), shuffleSplits, par.compressed, Parameters::DBTYPE_GENERIC_DB)`
       - `DBWriter seqWriter(dataFile.c_str(), indexFile.c_str(), shuffleSplits, par.compressed, dbType)`
    *   **ID Correspondence**: Both databases use identical numeric IDs for corresponding entries
    *   **Header Processing**: Headers are written to the header database using `hdrWriter.writeData(header.c_str(), header.length(), id, splitIdx)`
```{=typst}
#horizontalrule
```
### `IndexReader` Class

**Module Type**: Database Access Utility

**Function**: Provides a unified interface for reading different types of MMseqs2 databases, including header databases.

**Header Database Handling**:

*   **Header Database Access**: Uses specific flags to access header databases:
    - `IndexReader::SRC_HEADERS`: Access headers from the source database (e.g., `database_seq_h`)
    - `IndexReader::HEADERS`: Access headers from the main header database (e.g., `database_h`)

*   **Implementation Details**:
    - Creates separate `DBReader` objects for header databases
    - Handles fallback logic when header databases don't exist
    - Uses `PrefilteringIndexReader::openNewHeaderReader()` for header-specific access

*   **Usage Pattern**:
    ```cpp
    IndexReader qDbrHeader(par.db1, par.threads, IndexReader::SRC_HEADERS, preloadMode);
    size_t qHeaderId = qDbrHeader.sequenceReader->getId(queryKey);
    const char *qHeader = qDbrHeader.sequenceReader->getData(qHeaderId, thread_idx);
    ```
```{=typst}
#horizontalrule
```
### `prefilter`

**Module Type**: Prefiltering

**Function**: Performs a fast k-mer based search to identify potential homologous sequences, creating a list of candidate pairs for the more expensive alignment stage.

**Database Interactions**:

*   **Input Reading**:
    *   **Query Database (`<i:queryDB>`)**: Reads query sequences to extract k-mers.
    *   **Target Database (`<i:targetDB>`)**: Reads target sequences to build an in-memory index of k-mer locations. For performance, the target database is often split into multiple parts, and the index is built for each part sequentially.

*   **Output Writing**:
    *   **Prefiltering Result Database (`<o:prefilterDB>`)**: Writes the results of the prefiltering.
    *   Each entry in the output database corresponds to a query sequence.
    *   The data for each entry is a list of lines, where each line represents a potential target match.
    *   A typical line format is `targetId\tscore\tdiagonal`. The `score` is an ungapped alignment score along the diagonal, and `diagonal` is the diagonal on which the double k-mer match was found.

*   **Indexing and Headers**:
    *   The output database `prefilterDB` uses the same keys as the input `queryDB`.
    *   **Header Database Usage**: This module does not interact with header databases - it only processes sequence data for k-mer matching.
```{=typst}
#horizontalrule
```
### `align`

**Module Type**: Alignment

**Function**: Performs gapped local alignment for pairs of sequences identified in a prefiltering step.

**Database Interactions**:

*   **Input Reading**:
    *   **Query Database (`<i:queryDB>`)**: Reads query sequences. It uses the `.index` file to find the offset and length of each sequence and then reads the sequence data from the main data file.
    *   **Target Database (`<i:targetDB>`)**: Reads target sequences in the same way as the query database.
    *   **Prefiltering Result Database (`<i:resultDB>`)**: This is the main driver for the module. It reads a prefiltering result database, which contains, for each query, a list of potential target IDs.

*   **Output Writing**:
    *   **Alignment Database (`<o:alignmentDB>`)**: Writes the results of the alignments to a new database.
    *   The output is an alignment result database. Each entry corresponds to a query, and the data for each entry is a list of alignment results against different targets.
    *   Each line in an alignment result entry is tab-separated and contains columns such as: `targetId`, `score`, `E-value`, `qStart`, `qEnd`, `qLen`, `tStart`, `tEnd`, `tLen`, and optionally the CIGAR string (backtrace) if `-a` is enabled.

*   **Indexing and Headers**:
    *   The output database `alignmentDB` uses the same keys as the input `queryDB`. The index is created based on the query keys.
    *   **Header Database Usage**: This module does not interact with header databases - it only processes sequence data for alignment computation. Headers are not directly read or written by this module. To get header information for results, `convertalis` must be used later with the appropriate header databases.
```{=typst}
#horizontalrule
```
### `mergeclusters`

**Module Type**: Clustering

**Function**: Merges multiple clustering results from a cascaded workflow into a single, transitive clustering. It takes a base sequence database and a series of clustering result databases as input.

**Database Interactions**:

*   **Input Reading**:
    *   **`<i:sequenceDB>`**: The main sequence database. This is used to resolve sequence information but the primary logic operates on the cluster files. The module needs this to know the full set of sequence IDs.
    *   **`<i:clusterDB1> ... <i:clusterDBn>`**: A variadic list of cluster result databases from different steps of a cascaded clustering run. Each of these databases contains pairs of `(representative_id, member_id)`.

*   **Output Writing**:
    *   **`<o:clusterDB>`**: A new, merged cluster database. The keys of this database are the representative sequences from the *first* input cluster database (`clusterDB1`). The entries contain all member IDs that have been transitively linked to that representative through the various clustering steps.

*   **Key Matching Logic**:
    *   The module works by building a graph where nodes are sequences (represented by their numeric IDs) and edges are the cluster memberships from all input cluster databases.
    *   It then finds the connected components in this graph.
    *   For each connected component, it identifies the sequence that was a representative in the earliest clustering stage (i.e., from `clusterDB1`) and makes that the representative for the entire merged cluster. All other sequences in the component become members.
    *   This ensures that the final representatives are from the original, unclustered set, providing stability to the clustering output.
```{=typst}
#horizontalrule
```
### `filterdb`

**Module Type**: Database Manipulation

**Function**: Filters a database based on user-defined conditions on its columns. It is a versatile tool for manipulating any line-based, tab-separated MMseqs2 database (like alignment or prefiltering results).

**Database Interactions**:

*   **Input Reading**:
    *   **`<i:resultDB>`**: Reads any MMseqs2 database where each entry consists of one or more lines, and each line is tab-separated.

*   **Output Writing**:
    *   **`<o:resultDB>`**: Writes a new database of the same type, containing only the entries and lines that passed the filter conditions.

*   **Column-based Filtering**:
    *   `filterdb`'s power comes from its ability to inspect specific columns. The `--filter-column` parameter (1-based) selects which column to evaluate.
    *   **Numeric Filtering**: You can filter based on numerical comparisons using `--comparison-operator` (e.g., `ge` for >=, `le` for <=) and `--comparison-value`. For example, to keep only alignments with a sequence identity of at least 50% (column 3 in a standard BLAST-tab output), you would use: `--filter-column 3 --comparison-operator ge --comparison-value 0.5`.
    *   **String Filtering**: You can filter based on regular expressions using `--filter-regex`. This is useful for matching specific identifiers or patterns in text-based columns.
    *   **Expression Filtering**: The `--filter-expression` parameter allows for complex filtering using mathematical expressions involving multiple columns (e.g., `'$3 * $12 > 100'` to filter on sequence identity multiplied by alignment length).
    *   **File-based Filtering**: With `--filter-file`, you can provide a list of keys. The module will then either keep only the lines where the value in the specified column matches a key in the file (`--positive-filter 1`) or remove them (`--positive-filter 0`).
```{=typst}
#horizontalrule
```
### Header Database Handling

**Overview**: Header databases (files with `_h` suffix) are separate database files that store FASTA headers independently from sequence data. This design allows for efficient access to either sequences or headers without needing to read both.

**When Header and Main Databases are Processed Together**:

1. **Database Creation (`createdb`)**:
   - Header and sequence databases are created simultaneously
   - Both use the same numeric IDs for corresponding entries
   - Headers are stored in `database_h` and `database_h.index`
   - Sequences are stored in `database` and `database.index`

2. **Database Operations Requiring Both**:
   - `convertalis`: Reads both sequence and header databases to combine sequence data with FASTA headers in output
   - `view`: May need headers for display purposes
   - Any operation that needs to output human-readable identifiers

**When Header and Main Databases are Processed Separately**:

1. **Sequence-Only Operations**:
   - `prefilter`: Only reads sequence data for k-mer extraction
   - `align`: Only reads sequence data for alignment computation
   - `clust`: Only reads sequence data for clustering operations

2. **Header-Only Operations**:
   - Operations that only need FASTA identifiers for output formatting
   - Taxonomy annotation processes that work with identifiers

**Key Implementation Details**:

- **IndexReader Class**: Handles header database access through `SRC_HEADERS` or `HEADERS` flags
- **Separate File Structure**: Header databases have their own index files (`_h.index`) and data files (`_h`)
- **Memory Mapping**: Both header and sequence databases use memory mapping for efficient access
- **ID Correspondence**: Numeric IDs in header and sequence databases correspond to the same entries

**Performance Implications**:

- **Advantage**: Separating headers from sequences reduces memory usage for sequence-only operations
- **Disadvantage**: Operations needing both require opening two database readers
- **Optimization**: MMseqs2 automatically handles the complexity of managing both databases
```{=typst}
#horizontalrule
```
### `concatdbs`

**Module Type**: Database Manipulation

**Function**: Concatenates two MMseqs2 databases, giving new IDs to entries from the second database.

**Database Interactions**:

*   **Input Reading**:
    *   **`<i:DB>` (first database)**: Reads the first database to be concatenated.
    *   **`<i:DB>` (second database)**: Reads the second database to be concatenated.
    *   Both databases are read using `DBReader` with appropriate modes for data, index, and auxiliary files.

*   **Output Writing**:
    *   **`<o:DB>`**: Creates a new concatenated database.
    *   The output database contains all entries from both input databases.
    *   Entries from the first database keep their original keys (if `--preserve-keys` is used) or get new sequential keys.
    *   Entries from the second database get new keys starting from `maxKeyA + 1`.

*   **Key Processing Logic**:
    *   **Key Renumbering**: The module handles key mapping between old and new IDs using internal mapping arrays (`keysA`, `keysB`).
    *   **Auxiliary Files**: Also concatenates auxiliary files like `_mapping`, `.lookup`, and `.source` if they exist.
    *   **ID Consistency**: Maintains consistency between the main database and its auxiliary files during concatenation.

*   **Header Database Processing**:
    *   **Separate Processing**: This module does NOT process header databases (`_h` files) together with main databases.
    *   **Manual Concatenation Required**: Users must run `concatdbs` separately for header databases:
      ```bash
      mmseqs concatdbs sequenceDB addedSequenceDB allSequenceDB
      mmseqs concatdbs sequenceDB_h addedSequenceDB_h allSequenceDB_h
      ```
    *   **No Header Handling**: The implementation in `DBConcat.cpp` only handles main database files and auxiliary files, not header databases.

*   **Important Notes**:
    *   **Single-threaded Operation**: Works only single-threaded because sequence and header databases need the same ordering.
    *   **Key Preservation**: Supports preserving original keys with `--preserve-keys` parameter.
    *   **Size-based Selection**: Can take the larger entry when there are conflicts using `--take-larger-entry`.
```{=typst}
#horizontalrule
```
### `convert2fasta`

**Module Type**: Format Conversion

**Function**: Converts an MMseqs2 sequence database back to FASTA format.

**Database Interactions**:

*   **Input Reading**:
    *   **`<i:sequenceDB>`**: The main sequence database to be converted.
    *   **Header Database Handling**: Opens and reads the corresponding header database (`_h`) to get FASTA headers:
       ```cpp
       DBReader<unsigned int> db_header(par.hdr1.c_str(), par.hdr1Index.c_str(), 1, DBReader<unsigned int>::USE_DATA|DBReader<unsigned int>::USE_INDEX);
       ```
    *   Uses the same numeric keys to access corresponding entries in both databases.

*   **Output Writing**:
    *   **`<o:fastaFile>`**: Creates a FASTA file with proper headers and sequences.
    *   Combines header data from the header database with sequence data from the main database.
    *   Each output FASTA entry consists of: `>header\nsequence\n`

*   **Key Matching Logic**:
    *   **ID Correspondence**: Uses identical numeric IDs to match headers and sequences:
       ```cpp
       unsigned int headerKey = db_header.getId(key);
       const char* headerData = db_header.getData(headerKey, 0);
       unsigned int bodyKey = db.getId(key);
       const char* bodyData = db.getData(bodyKey, 0);
       ```
    *   **Header Processing**: Reads header data and removes trailing characters (typically `\0\0`) before writing to FASTA.

*   **Header Database Processing**:
    *   **Simultaneous Processing**: Processes both header and main databases together to create complete FASTA entries.
    *   **Memory Efficiency**: Opens both databases but only loads data as needed.
    *   **Optional Header Source**: Can use a separate header file if specified via `--use-header-file` parameter.

*   **Important Notes**:
    *   **Header Integration**: This module demonstrates the typical pattern of combining header and sequence data for human-readable output.
    *   **Format Conversion**: Converts from MMseqs2's efficient binary format back to the standard FASTA text format.
```{=typst}
#horizontalrule
```
### `convertalis`

**Module Type**: Format Conversion

**Function**: Converts a binary alignment result database into a human-readable, tab-separated format (like BLAST-tab).

**Database Interactions**:

*   **Input Reading**:
    *   **`<i:queryDb>`**: The query sequence database.
    *   **`<i:targetDb>`**: The target sequence database.
    *   **`<i:alignmentDB>`**: The alignment result database to be converted.
    *   **Header Database Handling**: Creates separate `IndexReader` objects for header databases using `IndexReader::SRC_HEADERS` flag:
       - `IndexReader qDbrHeader(par.db1, par.threads, IndexReader::SRC_HEADERS, ...)`
       - `IndexReader tDbrHeader(par.db2, par.threads, IndexReader::SRC_HEADERS, ...)`
    *   Reads headers using: `qDbrHeader.sequenceReader->getData(qHeaderId, thread_idx)`

*   **Output Writing**:
    *   **`<o:alignmentFile>`**: A plain-text file. The format is controlled by `--format-output`.
    *   By default, it produces a 12-column BLAST-compatible tab-separated file.
    *   The `--format-output` parameter allows for custom output formats, including columns like `qheader`, `theader`, `qseq`, `tseq`, `cigar`, and taxonomic information (`taxid`, `taxname`, `taxlineage`).

*   **Key Matching Logic**:
    *   It iterates through the `alignmentDB`. For each query, it reads the alignment results.
    *   It uses the query and target IDs from the alignment result to look up the corresponding sequences and headers in the respective databases.
    *   This allows it to combine information from multiple databases into a single, comprehensive output file.

*   **Header Database Processing**:
    *   **Separate Processing**: Header databases are processed independently from sequence databases
    *   **Memory Efficiency**: Only loads headers when needed for output formatting
    *   **ID Correspondence**: Uses the same numeric IDs as the main sequence databases
```{=typst}
#horizontalrule
```
## Summary: Header Database Usage Patterns

### **Modules That Process Header and Main Databases Together**:
- **`createdb`**: Creates header databases alongside sequence databases simultaneously
- **`convertalis`**: Reads both sequence and header databases to combine sequence data with FASTA headers in output
- **`convert2fasta`**: Reads both sequence and header databases to create complete FASTA entries with headers and sequences

### **Modules That Process Header and Main Databases Separately**:
- **`concatdbs`**: Only processes main databases; header databases must be concatenated separately:
  ```bash
  mmseqs concatdbs sequenceDB addedSequenceDB allSequenceDB
  mmseqs concatdbs sequenceDB_h addedSequenceDB_h allSequenceDB_h
  ```
- **`prefilter`**: Only processes sequence data for k-mer matching
- **`align`**: Only processes sequence data for alignment computation
- **`clust`**: Only processes sequence data for clustering operations

### **Utility Classes for Header Database Access**:
- **`IndexReader`**: Provides unified access to header databases through specific flags (`SRC_HEADERS`, `HEADERS`)
- **`DBReader`**: Core class supporting header database access through `HEADER`, `HEADER_INDEX`, `HEADER_DBTYPE` flags

### **Key Design Principles**:
1. **Separation of Concerns**: Headers and sequences are stored separately for memory efficiency
2. **ID Correspondence**: Both databases use identical numeric IDs for corresponding entries
3. **Lazy Loading**: Header databases are only accessed when header information is needed
4. **Unified Access**: `IndexReader` class provides consistent interface for accessing different database types
5. **Manual Coordination**: Some operations require manual coordination between main and header databases

### **Performance Benefits**:
- **Memory Efficiency**: Sequence-only operations don't need to load header data
- **I/O Optimization**: Only the required database files are memory-mapped
- **Scalability**: Large databases can be processed without loading unnecessary header information

### **Common Usage Patterns**:
- **Database Creation**: Always creates both sequence and header databases together
- **Sequence Processing**: Most core algorithms only access sequence databases
- **Output Formatting**: Final steps like `convertalis` combine sequence results with headers for human-readable output
- **Database Concatenation**: Requires separate operations for main and header databases
