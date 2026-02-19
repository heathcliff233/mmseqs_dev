## `translatenucs` {#refcmd-translatenucs}

Translate nucleotides to proteins.

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

`usage: mmseqs translatenucs <i:sequenceDB> <o:sequenceDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--translation-table` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE |
| `--add-orf-stop` | Add stop codon '*' at complete start and end |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |

### Full CLI Help Snapshot

```text
usage: mmseqs translatenucs <i:sequenceDB> <o:sequenceDB> [options]
 By Milot Mirdita <milot@mirdita.de>
options: misc:                    
 --translation-table INT   1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE
                           9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL
                           15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL
                           23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA
                            29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA [1]
 --add-orf-stop BOOL       Add stop codon '*' at complete start and end [0]
common:                  
 -v INT                    Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
 --compressed INT          Write compressed output [0]
 --threads INT             Number of CPU-cores used (all by default) [10]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-translatenucs), [command reference index](#sec-command-reference), and [functional module page](#mod-sequence-manipulation).

