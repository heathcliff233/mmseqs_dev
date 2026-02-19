## `orftocontig` {#refcmd-orftocontig}

Write ORF locations in alignment format.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`sequence_manipulation`](#mod-sequence-manipulation) |
| Category flags | `COMMAND_SEQUENCE` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`multihitdb`](#refcmd-multihitdb) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `multihitdb.sh` |

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

