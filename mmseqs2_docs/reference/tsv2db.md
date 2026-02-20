### `tsv2db` {#refcmd-tsv2db}

Convert a TSV file to any DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 4 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-tsv2db); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs tsv2db <i:tsvFile> <o:resultDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--output-dbtype` | Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs tsv2db <i:tsvFile> <o:resultDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: prefilter:              
 --add-self-matches BOOL  Artificially add entries of queries with themselves (for clustering) [0]
misc:                   
 --output-dbtype INT      Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 [12]
common:                 
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
