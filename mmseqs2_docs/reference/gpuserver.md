## `gpuserver` {#refcmd-gpuserver}

Start a GPU server.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`utilities`](#mod-utilities) |
| Category flags | `COMMAND_STORAGE` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Workflow script count | `0` |
| Detailed dependency entry | [Open in map](#depcmd-gpuserver) |

### Usage

`usage: mmseqs gpuserver <i:DB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--max-seqs` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) |
| `--prefilter-mode` | prefilter mode: 0: kmer/ungapped 1: ungapped, 2: nofilter, 3: ungapped&gapped |
| `--gpu` | Use GPU (CUDA) if possible |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |

### Full CLI Help Snapshot

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
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-gpuserver), [command reference index](#sec-command-reference), and [functional module page](#mod-utilities).

