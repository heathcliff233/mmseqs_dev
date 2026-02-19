## `filterdb` {#refcmd-filterdb}

DB filtering by given conditions.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`utilities`](#mod-utilities) |
| Category flags | `COMMAND_DB` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`cluster`](#refcmd-cluster), [`clusterupdate`](#refcmd-clusterupdate), [`easy-taxonomy`](#refcmd-easy-taxonomy), [`linclust`](#refcmd-linclust), [`linsearch`](#refcmd-linsearch), [`multihitdb`](#refcmd-multihitdb), [`rbh`](#refcmd-rbh), [`taxonomy`](#refcmd-taxonomy) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `cascaded_clustering.sh`, `easytaxonomy.sh`, `linclust.sh`, `linsearch.sh`, `multihitdb.sh`, `rbh.sh`, `taxonomy.sh`, `taxpercontig.sh`, `update_clustering.sh` |

### Usage

`usage: mmseqs filterdb <i:resultDB> <o:resultDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--filter-expression` | Specify a mathematical expression to filter lines |
| `--filter-column` | column |
| `--column-to-take` | column to take in join mode. If -1, the whole line is taken |
| `--filter-regex` | Regex to select column (example float: [0-9]*(.[0-9]+)? int:[1-9]{1}[0-9]) |
| `--positive-filter` | Used in conjunction with --filter-file. If true, out  = in \intersect filter ; if false, out = in - filter |
| `--filter-file` | Specify a file that contains the filtering elements |
| `--beats-first` | Filter by comparing each entry to the first entry |
| `--mapping-file` | Specify a file that translates the keys of a DB to new keys, TSV format |
| `--weights` | Weights used for cluster priorization |
| `--trim-to-one-column` | Output only the column specified by --filter-column |
| `--extract-lines` | Extract n lines of each entry |

### Full CLI Help Snapshot

```text
usage: mmseqs filterdb <i:resultDB> <o:resultDB> [options]
 By Clovis Galiez & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:                 
 --add-self-matches BOOL     Artificially add entries of queries with themselves (for clustering) [0]
misc:                      
 --filter-expression STR     Specify a mathematical expression to filter lines []
 --filter-column INT         column [1]
 --column-to-take INT        column to take in join mode. If -1, the whole line is taken [-1]
 --filter-regex STR          Regex to select column (example float: [0-9]*(.[0-9]+)? int:[1-9]{1}[0-9]) [^.*$]
 --positive-filter BOOL      Used in conjunction with --filter-file. If true, out  = in \intersect filter ; if false, out = in - filter [1]
 --filter-file STR           Specify a file that contains the filtering elements []
 --beats-first BOOL          Filter by comparing each entry to the first entry [0]
 --mapping-file STR          Specify a file that translates the keys of a DB to new keys, TSV format []
 --weights STR               Weights used for cluster priorization []
 --trim-to-one-column BOOL   Output only the column specified by --filter-column [0]
 --extract-lines INT         Extract n lines of each entry [0]
 --comparison-operator STR   Filter by comparing each entry row numerically by using the le) less-than-equal, ge) greater-than-equal or e) equal operator []
 --comparison-value DOUBLE   Filter by comparing each entry to this value [0.000E+00]
 --sort-entries INT          Sort column set by --filter-column, by 0: no sorting, 1: increasing, 2: decreasing, 3: random shuffle, 4: priority [0]
 --join-db STR               Join another database entry with respect to the database identifier in the chosen column []
common:                    
 --threads INT               Number of CPU-cores used (all by default) [10]
 --compressed INT            Write compressed output [0]
 -v INT                      Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Retain top alignment for each query (alignment DBs are sorted by E-value)
 mmseqs filterdb alignmentDB topHitAlignmentDB --extract-lines 1
 
 # Extract alignments with Seq.id. greater than 90%
 mmseqs filterdb alignmentDB scoreGreater35AlignmentDB --comparison-operator ge --comparison-value 0.9 --filter-column 2
 
 # Retain all hits matching a regular expression
 mmseqs filterdb alignmentDB regexFilteredDB --filter-regex '^[1-9].$' --filter-column 2
 
 # Remove all hits to target keys contained in file db.index
 mmseqs filterdb --filter-file db.index --positive-filter false
 
 # Retain all hits matching any boolean expression
 mmseqs filterdb --filter-expression '$1 * $2 >= 200'
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-filterdb), [command reference index](#sec-command-reference), and [functional module page](#mod-utilities).

