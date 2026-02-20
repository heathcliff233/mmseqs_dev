### `createtaxdb` {#refcmd-createtaxdb}

Add taxonomic labels to sequence DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family maps sequence evidence into taxonomy labels and reports under explicit aggregation rules. The current dependency map records 1 upstream caller(s) and 1 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-createtaxdb); functional module: [`taxonomy`](#mod-taxonomy).

**Usage**

`usage: mmseqs createtaxdb <i:sequenceDB> <tmpDir> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--ncbi-tax-dump` | tax dump directory. The tax dump can be downloaded here "ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz" |
| `--tax-mapping-file` | File to map sequence identifier to taxonomical identifier |
| `--tax-mapping-mode` | Map taxonomy based on sequence database 0: .lookup file 1: .source file |
| `--tax-db-mode` | Create taxonomy database as: 0: .dmp flat files (human readable) 1: binary dump (faster readin) |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

```text
usage: mmseqs createtaxdb <i:sequenceDB> <tmpDir> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                   
 --ncbi-tax-dump STR      NCBI tax dump directory. The tax dump can be downloaded here "ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz" []
 --tax-mapping-file STR   File to map sequence identifier to taxonomical identifier []
 --tax-mapping-mode INT   Map taxonomy based on sequence database 0: .lookup file 1: .source file [0]
 --tax-db-mode INT        Create taxonomy database as: 0: .dmp flat files (human readable) 1: binary dump (faster readin) [1]
common:                 
 --threads INT            Number of CPU-cores used (all by default) [10]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Mirdita M, Steinegger M, Breitwieser F, Soding J, Levy Karin E: Fast and sensitive taxonomic assignment to metagenomic contigs. Bioinformatics, btab184 (2021)
```
