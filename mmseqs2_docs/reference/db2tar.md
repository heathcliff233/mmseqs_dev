### `db2tar` {#refcmd-db2tar}

Archive contents of a DB to a tar archive.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-db2tar); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs db2tar <i:DB> <o:tar[.gz]> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs db2tar <i:DB> <o:tar[.gz]> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common: 
 -v INT   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Create a tar from a MSA DB
 mmseqs db2tar msaDB archive.tar.gz
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
