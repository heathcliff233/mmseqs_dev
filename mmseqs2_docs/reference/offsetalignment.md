### `offsetalignment` {#refcmd-offsetalignment}

Offset alignment by ORF start position.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family computes pair quality and coordinates and usually dominates per-pair compute cost after prefiltering. The current dependency map records 3 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-offsetalignment); functional module: [`alignment`](#mod-alignment).

**Usage**

`usage: mmseqs offsetalignment <i:queryDB> <i:queryOrfDB> <i:targetDB> <i:targetOrfDB> <i:alnDB> <o:alnDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--search-type` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--chain-alignments` | Chain overlapping alignments |
| `--merge-query` | Combine ORFs/split sequences to a single entry |

**Full CLI Help Snapshot**

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
