### `gpuserver` {#refcmd-gpuserver}

Start a GPU server.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family provides compositional utilities for custom pipelines, migration tasks, and diagnostics. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-gpuserver); functional module: [`utilities`](#mod-utilities).

**Usage**

`usage: mmseqs gpuserver <i:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--prefilter-mode` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped |
| `--gpu` | Use GPU (CUDA) if possible |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |

**Full CLI Help Snapshot**

```text
usage: mmseqs gpuserver <i:DB> [options]
 By Milot Mirdita <milot@mirdita.de> & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:            
 --max-seqs INT         Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) [300]
misc:                 
 --prefilter-mode INT   prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped [0]
common:               
 --gpu INT              Use GPU (CUDA) if possible [0]
 --db-load-mode INT     Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch [0]

references:
 - Kallenborn F, Chacon A, Hundt C, Sirelkhatim H, Didi K, Dallago C, Mirdita M, Schmidt B, Steinegger M: GPU-accelerated homology search with MMseqs2. bioRxiv, 2024.11.13.623350 (2024)
```
