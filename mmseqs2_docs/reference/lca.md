### `lca` {#refcmd-lca}

Compute the lowest common ancestor.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family maps sequence evidence into taxonomy labels and reports under explicit aggregation rules. The current dependency map records 2 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-lca); functional module: [`taxonomy`](#mod-taxonomy).

**Usage**

`usage: mmseqs lca <i:targetDB> <i:resultDB> <o:taxaDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--lca-ranks` | Add column with specified ranks (',' separated) |
| `--blacklist` | Comma separated list of ignored taxa in LCA computation |
| `--tax-lineage` | 0: don't show, 1: add all lineage names, 2: add all lineage taxids |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs lca <i:targetDB> <i:resultDB> <o:taxaDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:              
 --lca-ranks STR     Add column with specified ranks (',' separated) []
 --blacklist STR     Comma separated list of ignored taxa in LCA computation [12908:unclassified sequences,28384:other sequences]
 --tax-lineage INT   0: don't show, 1: add all lineage names, 2: add all lineage taxids [0]
common:            
 --compressed INT    Write compressed output [0]
 --threads INT       Number of CPU-cores used (all by default) [10]
 -v INT              Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Mirdita M, Steinegger M, Breitwieser F, Soding J, Levy Karin E: Fast and sensitive taxonomic assignment to metagenomic contigs. Bioinformatics, btab184 (2021)
```
