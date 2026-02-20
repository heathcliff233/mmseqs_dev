### `extractframes` {#refcmd-extractframes}

Extract frames from a nucleotide sequence DB.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family transforms sequence space before or after major compute stages. The current dependency map records 4 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-extractframes); functional module: [`sequence_manipulation`](#mod-sequence-manipulation).

**Usage**

`usage: mmseqs extractframes <i:sequenceDB> <o:sequenceDB> [options]`

**Key Options**

| Option | Purpose |
| :--- | :--- |
| `--forward-frames` | Comma-separated list of frames on the forward strand to be extracted |
| `--reverse-frames` | Comma-separated list of frames on the reverse strand to be extracted |
| `--translation-table` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE |
| `--translate` | Translate ORF to amino acid |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--create-lookup` | Create database lookup file (can be very large) |

**Full CLI Help Snapshot**

```text
usage: mmseqs extractframes <i:sequenceDB> <o:sequenceDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr> 
options: misc:                    
 --forward-frames STR      Comma-separated list of frames on the forward strand to be extracted [1,2,3]
 --reverse-frames STR      Comma-separated list of frames on the reverse strand to be extracted [1,2,3]
 --translation-table INT   1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE
                           9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL
                           15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL
                           23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA
                            29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA [1]
 --translate INT           Translate ORF to amino acid [0]
common:                  
 --threads INT             Number of CPU-cores used (all by default) [10]
 --compressed INT          Write compressed output [0]
 -v INT                    Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:                  
 --create-lookup INT       Create database lookup file (can be very large) [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
