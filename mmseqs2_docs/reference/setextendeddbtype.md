### `setextendeddbtype` {#refcmd-setextendeddbtype}

Write an extended DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family provides compositional utilities for custom pipelines, migration tasks, and diagnostics. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-setextendeddbtype); functional module: [`utilities`](#mod-utilities).

**Usage**

`usage: mmseqs setextendeddbtype <i:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--extended-dbtype` | Set extended dbtype 1: compressed, 2: need src, 4: context pseudoe cnts |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs setextendeddbtype <i:DB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                  
 --extended-dbtype INT   Set extended dbtype 1: compressed, 2: need src, 4: context pseudoe cnts [0]
common:                
 -v INT                  Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Print entries with keys 1, 2 and 3 from a sequence DB to stdout
 mmseqs setextendedbtype db --extended-dbtype 2
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
