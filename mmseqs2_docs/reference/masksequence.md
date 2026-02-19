## `masksequence` {#refcmd-masksequence}

Soft mask sequence DB using tantan.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`sequence_manipulation`](#mod-sequence-manipulation) |
| Category flags | `COMMAND_SEQUENCE` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Seen in workflow scripts | `n/a` |

### Usage

`usage: mmseqs masksequence <i:sequenceDB> <o:sequenceDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs masksequence <i:sequenceDB> <o:sequenceDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: prefilter:             
 --mask INT              Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking [1]
 --mask-prob FLOAT       Mask sequences is probablity is above threshold [0.900]
 --mask-lower-case INT   Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region [0]
 --mask-n-repeat INT     Repeat letters that occure > threshold in a rwo [0]
common:                
 --threads INT           Number of CPU-cores used (all by default) [10]
 --compressed INT        Write compressed output [0]
 -v INT                  Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-masksequence), [command reference index](#sec-command-reference), and [functional module page](#mod-sequence-manipulation).

