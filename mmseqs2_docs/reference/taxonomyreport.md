## `taxonomyreport` {#refcmd-taxonomyreport}

Create a taxonomy report in Kraken or Krona format.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`taxonomy`](#mod-taxonomy) |
| Category flags | `COMMAND_TAXONOMY | COMMAND_FORMAT_CONVERSION` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`easy-taxonomy`](#refcmd-easy-taxonomy) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `easytaxonomy.sh` |

### Usage

`usage: mmseqs taxonomyreport <i:seqTaxDB> <i:taxResultDB/resultDB/sequenceDB> <o:taxonomyReport> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--report-mode` | Taxonomy report mode 0: Kraken 1: Krona |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs taxonomyreport <i:seqTaxDB> <i:taxResultDB/resultDB/sequenceDB> <o:taxonomyReport> [options]
 By Milot Mirdita <milot@mirdita.de> & Florian Breitwieser <florian.bw@gmail.com>
options: misc:              
 --report-mode INT   Taxonomy report mode 0: Kraken 1: Krona [0]
common:            
 --threads INT       Number of CPU-cores used (all by default) [10]
 -v INT              Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Mirdita M, Steinegger M, Breitwieser F, Soding J, Levy Karin E: Fast and sensitive taxonomic assignment to metagenomic contigs. Bioinformatics, btab184 (2021)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-taxonomyreport), [command reference index](#sec-command-reference), and [functional module page](#mod-taxonomy).

