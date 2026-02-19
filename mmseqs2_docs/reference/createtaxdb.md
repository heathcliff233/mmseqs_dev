## `createtaxdb` {#refcmd-createtaxdb}

Add taxonomic labels to sequence DB.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`taxonomy`](#mod-taxonomy) |
| Category flags | `COMMAND_TAXONOMY` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`databases`](#refcmd-databases) |
| Calls modules | [`createbintaxonomy`](#refcmd-createbintaxonomy) |
| Seen in workflow scripts | `databases.sh` |

### Usage

`usage: mmseqs createtaxdb <i:sequenceDB> <tmpDir> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--ncbi-tax-dump` | tax dump directory. The tax dump can be downloaded here "ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz" |
| `--tax-mapping-file` | File to map sequence identifier to taxonomical identifier |
| `--tax-mapping-mode` | Map taxonomy based on sequence database 0: .lookup file 1: .source file |
| `--tax-db-mode` | Create taxonomy database as: 0: .dmp flat files (human readable) 1: binary dump (faster readin) |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

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
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-createtaxdb), [command reference index](#sec-command-reference), and [functional module page](#mod-taxonomy).

