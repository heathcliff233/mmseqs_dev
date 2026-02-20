### `convertmsa` {#refcmd-convertmsa}

Convert Stockholm/PFAM MSA file to a MSA DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family preserves profile semantics across conversion and search steps. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-convertmsa); functional module: [`profiles`](#mod-profiles).

**Usage**

`usage: mmseqs convertmsa <i:msaFile.sto[.gz]> <o:msaDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--identifier-field` | Field from STOCKHOLM comments for choosing the MSA identifier: 0: ID, 1: AC. If the respective comment does not exist, the name of the first sequence will become the identifier |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs convertmsa <i:msaFile.sto[.gz]> <o:msaDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:                 
 --identifier-field INT   Field from STOCKHOLM comments for choosing the MSA identifier: 0: ID, 1: AC. If the respective comment does not exist, the name of the first sequence will become the identifier [1]
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Mirdita M, Steinegger M, Soding J: MMseqs2 desktop and local web server app for fast, interactive sequence searches. Bioinformatics, 35(16), 2856-2858 (2019)
```
