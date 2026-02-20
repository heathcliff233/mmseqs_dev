## `convertmsa` {#refcmd-convertmsa}

Convert Stockholm/PFAM MSA file to a MSA DB.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`profiles`](#mod-profiles) |
| Category flags | `COMMAND_DATABASE_CREATION` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Workflow script count | `1` |
| Detailed dependency entry | [Open in map](#depcmd-convertmsa) |

### Usage

`usage: mmseqs convertmsa <i:msaFile.sto[.gz]> <o:msaDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--identifier-field` | Field from STOCKHOLM comments for choosing the MSA identifier: 0: ID, 1: AC. If the respective comment does not exist, the name of the first sequence will become the identifier |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs convertmsa <i:msaFile.sto[.gz]> <o:msaDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: common:                 
 --identifier-field INT   Field from STOCKHOLM comments for choosing the MSA identifier: 0: ID, 1: AC. If the respective comment does not exist, the name of the first sequence will become the identifier [1]
 --compressed INT         Write compressed output [0]
 -v INT                   Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Mirdita M, Steinegger M, Soding J: MMseqs2 desktop and local web server app for fast, interactive sequence searches. Bioinformatics, 35(16), 2856-2858 (2019)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-convertmsa), [command reference index](#sec-command-reference), and [functional module page](#mod-profiles).

