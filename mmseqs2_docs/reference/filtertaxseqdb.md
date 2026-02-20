## `filtertaxseqdb` {#refcmd-filtertaxseqdb}

Filter taxonomy sequence database.

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
| Detailed dependency entry | [Open in map](#depcmd-filtertaxseqdb) |

### Usage

`usage: mmseqs filtertaxseqdb <i:taxSeqDB> <o:taxSeqDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--taxon-list` | Taxonomy ID, possibly multiple values separated by ',' |
| `--subdb-mode` | Subdb mode 0: copy data 1: soft link data and write index |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs filtertaxseqdb <i:taxSeqDB> <o:taxSeqDB> [options]
 By Eli Levy Karin <eli.levy.karin@gmail.com> & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:             
 --taxon-list STR   Taxonomy ID, possibly multiple values separated by ',' []
 --subdb-mode INT   Subdb mode 0: copy data 1: soft link data and write index [0]
common:           
 --compressed INT   Write compressed output [0]
 --threads INT      Number of CPU-cores used (all by default) [10]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

examples:
 # Download a sequence database with taxonomy information
 mmseqs databases UniProtKB/Swiss-Prot swissprotDB tmp
 
 # Retain all bacterial sequences
 mmseqs filtertaxseqdb swissprotDB swissprotDB_only_bac --taxon-list 2
 
 # Retain all eukaryotic sequences except fungi
 mmseqs filtertaxseqdb swissprotDB swissprotDB_euk_wo_fungi --taxon-list '2759&&!4751'
 
 # Retain all human and chlamydia sequences
 mmseqs filtertaxseqdb swissprotDB swissprotDB_human_and_chlamydia --taxon-list '9606||810'
 
 
references:
 - Mirdita M, Steinegger M, Breitwieser F, Soding J, Levy Karin E: Fast and sensitive taxonomic assignment to metagenomic contigs. Bioinformatics, btab184 (2021)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-filtertaxseqdb), [command reference index](#sec-command-reference), and [functional module page](#mod-taxonomy).

