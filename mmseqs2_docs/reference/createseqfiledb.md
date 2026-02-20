## `createseqfiledb` {#refcmd-createseqfiledb}

Create a DB of unaligned FASTA entries.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](#mod-result-handling) |
| Category flags | `COMMAND_FORMAT_CONVERSION | COMMAND_EXPERT` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Workflow script count | `1` |
| Detailed dependency entry | [Open in map](#depcmd-createseqfiledb) |

### Usage

`usage: mmseqs createseqfiledb <i:sequenceDB> <i:resultDB> <o:fastaDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--min-sequences` | Minimum number of sequences a cluster may contain |
| `--max-sequences` | Maximum number of sequences a cluster may contain |
| `--hh-format` | Format entries to use with hhsuite (for singleton clusters) |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs createseqfiledb <i:sequenceDB> <i:resultDB> <o:fastaDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:                
 --min-sequences INT   Minimum number of sequences a cluster may contain [1]
 --max-sequences INT   Maximum number of sequences a cluster may contain [2147483647]
 --hh-format BOOL      Format entries to use with hhsuite (for singleton clusters) [0]
common:              
 --db-load-mode INT    Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 --threads INT         Number of CPU-cores used (all by default) [10]
 --compressed INT      Write compressed output [0]
 -v INT                Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Gather all sequences from a cluster DB
 mmseqs createseqfiledb sequenceDB clusterDB unalignedDB --min-sequences 2
 # Build MSAs with Clustal-Omega
 mmseqs apply unalignedDB msaDB -- clustalo -i - -o stdout --threads=1
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-createseqfiledb), [command reference index](#sec-command-reference), and [functional module page](#mod-result-handling).

