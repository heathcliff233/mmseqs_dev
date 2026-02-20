### `mergedbs` {#refcmd-mergedbs}

Merge entries from multiple DBs.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 4 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-mergedbs); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs mergedbs <i:DB> <o:DB> <i:DB1> ... <i:DBn> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--prefixes` | Comma separated list of prefixes for each entry |
| `--merge-stop-empty` | Don't continue merging entries after an empty entry |

**Full CLI Help Snapshot**

```text
usage: mmseqs mergedbs <i:DB> <o:DB> <i:DB1> ... <i:DBn> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: common:                 
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                 
 --prefixes STR           Comma separated list of prefixes for each entry []
 --merge-stop-empty BOOL  Don't continue merging entries after an empty entry [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
