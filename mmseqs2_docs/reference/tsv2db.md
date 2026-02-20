## `tsv2db` {#refcmd-tsv2db}

Convert a TSV file to any DB.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](#mod-database) |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `4` |
| Downstream command count | `0` |
| Workflow script count | `4` |
| Detailed dependency entry | [Open in map](#depcmd-tsv2db) |

### Usage

`usage: mmseqs tsv2db <i:tsvFile> <o:resultDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--output-dbtype` | Set database type for resulting database: Amino acid sequences 0, Nucl. seq. 1, Profiles 2, Alignment result 5, Clustering result 6, Prefiltering result 7, Taxonomy result 8, Indexed database 9, cA3M MSAs 10, FASTA or A3M MSAs 11, Generic database 12, Omit dbtype file 13, Bi-directional prefiltering result 14, Offsetted headers 15 |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

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
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-tsv2db), [command reference index](#sec-command-reference), and [functional module page](#mod-database).

