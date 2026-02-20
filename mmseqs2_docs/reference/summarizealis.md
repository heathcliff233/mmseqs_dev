### `summarizealis` {#refcmd-summarizealis}

Summarize alignment result to one row (uniq. cov., cov., avg. seq. id.).

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream.

Dependency entry: [Open in map](#depcmd-summarizealis); functional module: [`result_handling`](#mod-result-handling).

**Usage**

`usage: mmseqs summarizealis <i:alignmentDB> <o:summerizedDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs summarizealis <i:alignmentDB> <o:summerizedDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Mirdita M, von den Driesch L, Galiez C, Martin M, Soding J, Steinegger M: Uniclust databases of clustered and deeply annotated protein sequences and alignments. Nucleic Acids Research 45(D1), D170-D176 (2017)
```
