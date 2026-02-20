### `masksequence` {#refcmd-masksequence}

Soft mask sequence DB using tantan.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family transforms sequence space before or after major compute stages. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-masksequence); functional module: [`sequence_manipulation`](#mod-sequence-manipulation).

**Usage**

`usage: mmseqs masksequence <i:sequenceDB> <o:sequenceDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

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
