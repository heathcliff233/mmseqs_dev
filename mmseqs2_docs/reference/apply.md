### `apply` {#refcmd-apply}

Execute given program on each DB entry.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family provides compositional utilities for custom pipelines, migration tasks, and diagnostics. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-apply); functional module: [`utilities`](#mod-utilities).

**Usage**

`usage: mmseqs apply <i:DB> <o:DB> -- program [args...] [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs apply <i:DB> <o:DB> -- program [args...] [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Gather all sequences from a cluster DB
 mmseqs createseqfiledb sequenceDB clusterDB unalignedDB --min-sequences 2
 # Build MSAs with Clustal-Omega
 mmseqs apply unalignedDB msaDB -- clustalo -i - -o stdout --threads=1
 
 # Count lines in each DB entry inefficiently (result2stats is way faster)
 mmseqs apply DB wcDB -- awk '{ counter++; } END { print counter; }'
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
