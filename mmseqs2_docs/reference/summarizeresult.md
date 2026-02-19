## `summarizeresult` {#refcmd-summarizeresult}

Extract annotations from alignment DB.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`result_handling`](#mod-result-handling) |
| Category flags | `COMMAND_RESULT` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`easy-linsearch`](#refcmd-easy-linsearch), [`easy-search`](#refcmd-easy-search) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `easysearch.sh` |

### Usage

`usage: mmseqs summarizeresult <i:alignmentDB> <o:alignmentDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `--overlap` | Maximum overlap of covered regions |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs summarizeresult <i:alignmentDB> <o:alignmentDB> [options]
 By Milot Mirdita <milot@mirdita.de> & Martin Steinegger <martin.steinegger@snu.ac.kr>
options: align:            
 -a BOOL            Add backtrace string (convert to alignments with mmseqs convertalis module) [0]
 -c FLOAT           List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.000]
misc:             
 --overlap FLOAT    Maximum overlap of covered regions [0.000]
common:           
 --threads INT      Number of CPU-cores used (all by default) [10]
 --compressed INT   Write compressed output [0]
 -v INT             Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Mirdita M, von den Driesch L, Galiez C, Martin M, Soding J, Steinegger M: Uniclust databases of clustered and deeply annotated protein sequences and alignments. Nucleic Acids Research 45(D1), D170-D176 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-summarizeresult), [command reference index](#sec-command-reference), and [functional module page](#mod-result-handling).

