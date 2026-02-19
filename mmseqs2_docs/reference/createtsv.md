## `createtsv` {#refcmd-createtsv}

Convert result DB to tab-separated flat file.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](#mod-result-handling) |
| Category flags | `COMMAND_FORMAT_CONVERSION` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`easy-cluster`](#refcmd-easy-cluster), [`easy-linclust`](#refcmd-easy-linclust), [`easy-taxonomy`](#refcmd-easy-taxonomy) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `easycluster.sh`, `easytaxonomy.sh` |

### Usage

`usage: mmseqs createtsv <i:queryDB> [<i:targetDB>] <i:resultDB> <o:tsvFile> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--first-seq-as-repr` | Use the first sequence of the clustering result as representative sequence |
| `--target-column` | Select a target column (default 1), 0 if no target id exists |
| `--full-header` | Replace DB ID by its corresponding Full Header |
| `--idx-seq-src` | 0: auto, 1: split/translated sequences, 2: input sequences |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--db-output` | Return a result DB instead of a text file |

### Full CLI Help Snapshot

```text
usage: mmseqs createtsv <i:queryDB> [<i:targetDB>] <i:resultDB> <o:tsvFile> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                    
 --first-seq-as-repr BOOL  Use the first sequence of the clustering result as representative sequence [0]
 --target-column INT       Select a target column (default 1), 0 if no target id exists [1]
 --full-header BOOL        Replace DB ID by its corresponding Full Header [0]
 --idx-seq-src INT         0: auto, 1: split/translated sequences, 2: input sequences [0]
common:                  
 --threads INT             Number of CPU-cores used (all by default) [10]
 --compressed INT          Write compressed output [0]
 -v INT                    Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                  
 --db-output BOOL          Return a result DB instead of a text file [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-createtsv), [command reference index](#sec-command-reference), and [functional module page](#mod-result-handling).

