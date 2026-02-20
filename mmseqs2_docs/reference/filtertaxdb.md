## `filtertaxdb` {#refcmd-filtertaxdb}

Filter taxonomy result database.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`taxonomy`](#mod-taxonomy) |
| Category flags | `COMMAND_TAXONOMY` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Workflow script count | `0` |
| Detailed dependency entry | [Open in map](#depcmd-filtertaxdb) |

### Usage

`usage: mmseqs filtertaxdb <i:targetDB> <i:taxDB> <o:taxDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs filtertaxdb <i:targetDB> <i:taxDB> <o:taxDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:             
 --taxon-list STR   Taxonomy ID, possibly multiple values separated by ',' []
common:           
 --compressed INT   Write compressed output [0]
 --threads INT      Number of CPU-cores used (all by default) [10]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Download a sequence database with taxonomy information
 mmseqs databases UniProtKB/Swiss-Prot swissprotDB tmp
 # Annotate a queryDB with taxonomy information
 mmseqs taxonomy queryDB swissprotDB taxDB tmp
 
 # Retain all unclassified hits
 mmseqs filtertaxdb swissprotDB taxDB filteredTaxDB --taxon-list 0
 mmseqs createsubdb <(awk '$3 == 1' filteredTaxDB.index) queryDB queryUnclassifiedDB
 
 # Retain all eukaryotic hits except fungi
 mmseqs filtertaxdb swissprotDB taxDB filteredTaxDB --taxon-list '2759&&!4751'
 
 # Retain all human and chlamydia hits
 mmseqs filtertaxdb swissprotDB taxDB filteredTaxDB --taxon-list '9606||810'
 
references:
 - Mirdita M, Steinegger M, Breitwieser F, Soding J, Levy Karin E: Fast and sensitive taxonomic assignment to metagenomic contigs. Bioinformatics, btab184 (2021)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-filtertaxdb), [command reference index](#sec-command-reference), and [functional module page](#mod-taxonomy).

