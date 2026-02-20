### `view` {#refcmd-view}

Print DB entries given in --id-list to stdout.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family provides compositional utilities for custom pipelines, migration tasks, and diagnostics. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-view); functional module: [`utilities`](#mod-utilities).

**Usage**

`usage: mmseqs view <i:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--id-list` | Entries to be printed separated by ',' |
| `--id-mode` | Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) |
| `--idx-entry-type` | 0: sequence, 1: src sequence, 2: header, 3: src header |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs view <i:DB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                 
 --id-list STR          Entries to be printed separated by ',' []
 --id-mode INT          Select DB entries based on 0: database keys, 1: FASTA identifiers (.lookup) [0]
 --idx-entry-type INT   0: sequence, 1: src sequence, 2: header, 3: src header [0]
common:               
 -v INT                 Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Print entries with keys 1, 2 and 3 from a sequence DB to stdout
 mmseqs view sequenecDB --id-list 1,2,3
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
