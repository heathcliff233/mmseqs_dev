### `taxonomyreport` {#refcmd-taxonomyreport}

Create a taxonomy report in Kraken or Krona format.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family maps sequence evidence into taxonomy labels and reports under explicit aggregation rules. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-taxonomyreport); functional module: [`taxonomy`](#mod-taxonomy).

**Usage**

`usage: mmseqs taxonomyreport <i:seqTaxDB> <i:taxResultDB/resultDB/sequenceDB> <o:taxonomyReport> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--report-mode` | Taxonomy report mode 0: Kraken 1: Krona |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

**Full CLI Help Snapshot**

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
