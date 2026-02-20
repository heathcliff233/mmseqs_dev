### `tar2db` {#refcmd-tar2db}

Convert content of tar archives to any DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-tar2db); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs tar2db <i:tar[.gz]> ... <i:tar[.gz]> <o:resultDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--output-dbtype` | Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 |
| `--tar-include` | Include file names based on this regex |
| `--tar-exclude` | Exclude file names based on this regex |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs tar2db <i:tar[.gz]> ... <i:tar[.gz]> <o:resultDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:                
 --output-dbtype INT   Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 [12]
 --tar-include STR     Include file names based on this regex [.*]
 --tar-exclude STR     Exclude file names based on this regex [^$]
common:              
 --compressed INT      Write compressed output [0]
 --threads INT         Number of CPU-cores used (all by default) [10]
 -v INT                Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Assuming tar archive containing three aligned FASTA files:
 #  * folder/msa1.fa.gz  * folder/msa2.fa  * folder/msa3.fa
 # Create a msaDB with three DB entries each containing a separate MSA
 mmseqs tar2db archive.tar.gz msaDB --output-dbtype 11
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
