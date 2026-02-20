### `concatdbs` {#refcmd-concatdbs}

Concatenate two DBs, giving new IDs to entries from 2nd DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 3 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-concatdbs); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs concatdbs <i:DB> <i:DB> <o:DB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--preserve-keys` | The keys of the two DB should be distinct, and they will be preserved in the concatenation |
| `--take-larger-entry` | Only keep the larger entry (dataSize >) in the concatenation, both databases need the same keys in the index |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs concatdbs <i:DB> <i:DB> <o:DB> [options]
 By Clovis Galiez, Eli Levy Karin & Martin Steinegger (martin.steinegger@snu.ac.kr)
options: misc:                    
 --preserve-keys BOOL      The keys of the two DB should be distinct, and they will be preserved in the concatenation [0]
 --take-larger-entry BOOL  Only keep the larger entry (dataSize >) in the concatenation, both databases need the same keys in the index [0]
common:                  
 --compressed INT          Write compressed output [0]
 --threads INT             Number of CPU-cores used (all by default) [1]
 -v INT                    Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Download two sequences databases and concat them
 mmseqs databases PDB pdbDB tmp
 mmseqs UniProtKB/Swiss-Prot swissprotDB tmp
 # Works only single threaded since seq. and header DB need the same ordering
 mmseqs concatdbs pdbDB swissprotDB pdbAndSwissprotDB --threads 1
 mmseqs concatdbs pdbDB_h swissprotDB_h pdbAndSwissprotDB_h --threads 1
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
