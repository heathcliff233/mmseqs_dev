## `orftocontig` {#refcmd-orftocontig}

Write ORF locations in alignment format.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`sequence_manipulation`](#mod-sequence-manipulation) |
| Category flags | `COMMAND_SEQUENCE` |

### Topology

| Aspect | Value |
| :--- | :--- |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Workflow script count | `1` |
| Detailed dependency entry | [Open in map](#depcmd-orftocontig) |

### Usage

`usage: mmseqs orftocontig <i:contigsSequenceDB> <i:extractedOrfsHeadersDB> <o:orfsAlignedToContigDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs orftocontig <i:contigsSequenceDB> <i:extractedOrfsHeadersDB> <o:orfsAlignedToContigDB> [options]
 By Eli Levy Karin <eli.levy.karin@gmail.com> 
options: common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-orftocontig), [command reference index](#sec-command-reference), and [functional module page](#mod-sequence-manipulation).

