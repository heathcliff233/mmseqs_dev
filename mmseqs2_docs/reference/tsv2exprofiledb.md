### `tsv2exprofiledb` {#refcmd-tsv2exprofiledb}

Create a expandable profile db from TSV files.

Execution role: core compute module typically called by workflows and advanced custom pipelines.

This command family preserves profile semantics across conversion and search steps. The current dependency map records 0 upstream caller(s) and 5 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-tsv2exprofiledb); functional module: [`profiles`](#mod-profiles).

**Usage**

`usage: mmseqs tsv2exprofiledb <i:tsvFilesBase> <o:exprofileDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--gpu` | Use GPU (CUDA) if possible |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs tsv2exprofiledb <i:tsvFilesBase> <o:exprofileDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:           
 --gpu INT          Use GPU (CUDA) if possible [0]
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [1]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
