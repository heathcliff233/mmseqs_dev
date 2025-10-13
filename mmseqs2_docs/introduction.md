# Introduction to MMseqs2 Core Concepts

MMseqs2 is a powerful software suite for fast and sensitive sequence searching and clustering. Its high performance comes from a combination of clever algorithmic choices and efficient implementation. This document delves into the core ideas behind MMseqs2 to help users understand how it works and how to leverage its modularity for custom bioinformatics pipelines.

## Why is MMseqs2 so fast? The Multi-Stage Search Strategy

The key to MMseqs2's speed is a multi-stage prefiltering pipeline that quickly eliminates dissimilar sequences, ensuring that the computationally expensive Smith-Waterman alignment is only performed on a small fraction of promising candidates.

### 1. K-mer Matching

Instead of comparing full sequences, MMseqs2 starts by finding short, matching words of a fixed length, called **k-mers**.

*   **Sensitivity through Reduced Alphabets**: For protein sequences, simply matching k-mers in the 20-letter amino acid alphabet would miss many homologous sequences. MMseqs2 groups amino acids with similar physicochemical properties into a **reduced alphabet**. This increases the chance of finding a k-mer match between homologous sequences. For example, `D` and `E` (acidic) might be grouped into one character. This is a key source of sensitivity at the prefiltering stage.

*   **Spaced K-mers**: MMseqs2 can also use **spaced k-mers**, where the k-mer is not a consecutive block of residues but follows a specific pattern of match/don't-care positions (e.g., `110101` for a 4-mer in a 6-residue pattern). This further increases sensitivity, especially for more divergent sequences.

### 2. Filtering by Double Consecutive K-mer Matches

A single k-mer match can occur frequently by chance. To filter out these random matches, MMseqs2 requires at least two consecutive k-mer matches that lie on the same diagonal. A diagonal is defined by `i - j`, where `i` is the position in the query and `j` is the position in the target. A match on the same diagonal suggests a longer, gapless alignment. This simple but effective filter dramatically reduces the number of random hits.

### 3. Ungapped Alignment Check

Sequences that pass the double-diagonal k-mer filter are then subjected to an ungapped alignment along the found diagonals. This is very fast to compute. Only sequences that pass a certain score threshold in this step are passed to the final alignment stage.

### 4. SIMD-accelerated Gapped Alignment

Only a very small fraction of the initial sequence pairs (often less than 1%) make it to the final stage. Here, MMseqs2 performs a standard, gapped Smith-Waterman alignment. This stage is heavily optimized using **SIMD (Single Instruction, Multiple Data)** instructions (SSE4.1, AVX2), which allows the CPU to perform the same operation on multiple data points simultaneously, leading to a significant speed-up.

## The MMseqs2 Database: A Key to Performance

A major bottleneck in bioinformatics is often I/O. Working with millions of sequences in separate FASTA files can cripple a filesystem. MMseqs2 overcomes this by using a custom, high-performance database format.

### Database Organization

When you run `mmseqs createdb`, your FASTA/FASTQ file is converted into several files that form the MMseqs2 database. For a database named `myDB`, you will see:

*   **`myDB` (Data File)**: This is the main data file. It contains all sequence records from your input file, concatenated together and separated by a `\0` (null) byte.
*   **`myDB.index` (Index File)**: A plain-text, tab-separated file that allows for fast random access to any sequence in the data file. Each line corresponds to one entry and has the format: `[numeric ID]\t[offset]\t[length]`.
    *   `numeric ID`: A unique integer assigned to each entry.
    *   `offset`: The starting position (in bytes) of the sequence record in the data file.
    *   `length`: The length of the sequence record (in bytes), including the null terminator.
*   **`myDB_h` & `myDB_h.index` (Header Database)**: A separate database pair that stores the FASTA headers, organized in the same way as the sequence database. This separation allows for faster access to either sequences or headers without needing to parse the other.
*   **`myDB.lookup` (Lookup File)**: A tab-separated file that maps the internal numeric IDs back to the original FASTA identifiers. This is useful for interpreting results.
*   **`myDB.dbtype` (Type File)**: A small binary file containing an integer that specifies the type of data in the database (e.g., amino acid sequences, nucleotide sequences, profiles, etc.). This allows MMseqs2 modules to validate their inputs.

### How MMseqs2 Reads and Writes Data

MMseqs2's speed is not just from its algorithms, but also from its efficient data handling. Instead of using standard file reading functions, MMseqs2 uses `mmap` to map the database files directly into virtual memory. This technique lets the operating system's kernel manage loading data from disk into RAM on-demand, which is significantly faster than manual file I/O. The core logic for this is implemented in the `DBReader` and `DBWriter` classes within the MMseqs2 source code (`src/commons/`).

This memory-mapped approach means that accessing any sequence, no matter how large the database, is nearly instantaneous, as it only requires a pointer lookup.

## The Power of Modularity: Hacking Your Workflow

MMseqs2 is not a single program but a suite of interoperable modules. The `easy-*` workflows are just convenient shell scripts that chain these modules together for common tasks. Understanding this modularity unlocks the full power of MMseqs2, allowing you to build custom analysis pipelines.

### A Modular Example: Clustering

Let's look at the clustering process from a modular perspective:

1.  **Input**: The process starts with a set of sequences. First, you must convert them into an MMseqs2 database using `createdb`.
    ```bash
    mmseqs createdb my_sequences.fasta myDB
    ```
2.  **Core Task**: The `cluster` module takes this database, performs an all-vs-all comparison (internally using the `search` workflow), and produces a result database where each entry corresponds to a cluster.
    ```bash
    mmseqs cluster myDB myDB_clu tmp
    ```
3.  **Output**: The output `myDB_clu` is another MMseqs2 database. For each entry (a cluster), the data record is a list of numeric IDs of the member sequences, with the representative sequence ID on the first line.

### Hacking the Workflow

Because the inputs and outputs are well-defined MMseqs2 databases, you can "hack" the process by inserting your own steps or using other tools.

**Example: Extracting and Aligning a Single Cluster**

Suppose you want to extract all sequences from the cluster represented by ID `123` and create a multiple sequence alignment.

1.  **View Cluster Members**: Use `view` to see the contents of the cluster entry.
    ```bash
    mmseqs view myDB_clu --id-list 123
    # This will output the IDs of all members of cluster 123.
    ```

2.  **Create a Sub-database**: Pipe the output of `view` to `createsubdb` to create a new database containing only the sequences of that cluster.
    ```bash
    mmseqs createsubdb <(mmseqs view myDB_clu --id-list 123) myDB subDB
    ```

3.  **Convert to FASTA**: Convert the new sub-database to a standard FASTA file.
    ```bash
    mmseqs convert2fasta subDB subDB.fasta
    ```

4.  **Use an External Tool**: Now you can use any standard MSA tool, like ClustalOmega or MAFFT.
    ```bash
    mafft subDB.fasta > subDB.aln
    ```

### Integrating with Other Tools

The simplicity of the MMseqs2 database format makes it possible to integrate with your own scripts. Since the `.index` file is plain text and the data file is a simple concatenation, you can:

*   **Create custom databases**: Write scripts in Python, Perl, or even `awk` to generate data and index files in the correct format. This allows you to import data from virtually any source into MMseqs2.
*   **Modify results**: You could, for example, write a script to parse an alignment result database, filter it based on complex criteria not available in `filterdb`, and write a new valid result database to be used in downstream MMseqs2 modules.

This modular, file-based approach makes MMseqs2 not just a tool, but a flexible and extensible bioinformatics workbench.