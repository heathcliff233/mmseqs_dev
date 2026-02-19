## `splitsequence` {#refcmd-splitsequence}

Split sequences by length.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](#mod-database) |
| Category flags | `COMMAND_SEQUENCE` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`createindex`](#refcmd-createindex), [`createlinindex`](#refcmd-createlinindex), [`search`](#refcmd-search) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `blastn.sh`, `createindex.sh` |

### Usage

`usage: mmseqs splitsequence <i:sequenceDB> <o:sequenceDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--sequence-overlap` | Overlap between sequences |
| `--sequence-split-mode` | Sequence split mode 0: copy data, 1: soft link data and write new index, |
| `--headers-split-mode` | Header split mode: 0: split position, 1: original header |
| `--max-seq-len` | Maximum sequence length |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--create-lookup` | Create database lookup file (can be very large) |

### Full CLI Help Snapshot

```text
usage: mmseqs splitsequence <i:sequenceDB> <o:sequenceDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                      
 --sequence-overlap INT      Overlap between sequences [300]
 --sequence-split-mode INT   Sequence split mode 0: copy data, 1: soft link data and write new index, [1]
 --headers-split-mode INT    Header split mode: 0: split position, 1: original header [0]
common:                    
 --max-seq-len INT           Maximum sequence length [10000]
 --threads INT               Number of CPU-cores used (all by default) [10]
 --compressed INT            Write compressed output [0]
 -v INT                      Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                    
 --create-lookup INT         Create database lookup file (can be very large) [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-splitsequence), [command reference index](#sec-command-reference), and [functional module page](#mod-database).

