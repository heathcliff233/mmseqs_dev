## `offsetalignment` {#refcmd-offsetalignment}

Offset alignment by ORF start position.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`alignment`](#mod-alignment) |
| Category flags | `COMMAND_RESULT` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`cluster`](#refcmd-cluster), [`linsearch`](#refcmd-linsearch), [`search`](#refcmd-search) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `blastn.sh`, `linsearch.sh`, `nucleotide_clustering.sh`, `translated_search.sh` |

### Usage

`usage: mmseqs offsetalignment <i:queryDB> <i:queryOrfDB> <i:targetDB> <i:targetOrfDB> <i:alnDB> <o:alnDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--search-type` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--chain-alignments` | Chain overlapping alignments |
| `--merge-query` | Combine ORFs/split sequences to a single entry |

### Full CLI Help Snapshot

```text
usage: mmseqs offsetalignment <i:queryDB> <i:queryOrfDB> <i:targetDB> <i:targetOrfDB> <i:alnDB> <o:alnDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                   
 --search-type INT        Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment [0]
common:                 
 --threads INT            Number of CPU-cores used (all by default) [10]
 --compressed INT         Write compressed output [0]
 --db-load-mode INT       Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                 
 --chain-alignments INT   Chain overlapping alignments [0]
 --merge-query INT        Combine ORFs/split sequences to a single entry [1]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-offsetalignment), [command reference index](#sec-command-reference), and [functional module page](#mod-alignment).

