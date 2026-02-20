### `result2flat` {#refcmd-result2flat}

Create flat file by adding FASTA headers to DB entries.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes. The current dependency map records 2 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream.

Dependency entry: [Open in map](#depcmd-result2flat); functional module: [`result_handling`](#mod-result-handling).

**Usage**

`usage: mmseqs result2flat <i:queryDB> <i:targetDB> <i:resultDB> <o:fastaDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--use-fasta-header` | Use the id parsed from the fasta header as the index key instead of using incrementing numeric identifiers |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs result2flat <i:queryDB> <i:targetDB> <i:resultDB> <o:fastaDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                   
 --use-fasta-header BOOL  Use the id parsed from the fasta header as the index key instead of using incrementing numeric identifiers [0]
common:                 
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
