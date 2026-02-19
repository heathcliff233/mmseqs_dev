## `multihitdb` {#refcmd-multihitdb}

Create sequence DB for multi hit searches.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `high_level_api` |
| Primary functional group | [`multi_hit`](#mod-multi-hit) |
| Category flags | `COMMAND_MULTIHIT` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | `n/a` |
| Calls modules | [`createdb`](#refcmd-createdb), [`extractorfs`](#refcmd-extractorfs), [`filterdb`](#refcmd-filterdb), [`orftocontig`](#refcmd-orftocontig), [`result2stats`](#refcmd-result2stats), [`swapdb`](#refcmd-swapdb), [`translatenucs`](#refcmd-translatenucs), [`tsv2db`](#refcmd-tsv2db) |
| Seen in workflow scripts | `n/a` |

### Usage

`usage: mmseqs multihitdb <i:fastaFile1[.gz|bz2]> ... <i:fastaFileN[.gz|bz2]> <o:setDB> <tmpDir> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--dbtype` | Database type 0: auto, 1: amino acid 2: nucleotides |
| `--shuffle` | Shuffle input database |
| `--createdb-mode` | Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) |
| `--id-offset` | Numeric ids in index file are offset by this value |
| `--min-length` | Minimum codon number in open reading frames |
| `--max-length` | Maximum codon number in open reading frames |
| `--max-gaps` | Maximum number of codons with gaps or unknown residues before an open reading frame is rejected |
| `--contig-start-mode` | Contig start can be 0: incomplete, 1: complete, 2: both |
| `--contig-end-mode` | Contig end can be 0: incomplete, 1: complete, 2: both |
| `--orf-start-mode` | Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) |
| `--forward-frames` | Comma-separated list of frames on the forward strand to be extracted |
| `--reverse-frames` | Comma-separated list of frames on the reverse strand to be extracted |

### Full CLI Help Snapshot

```text
usage: mmseqs multihitdb <i:fastaFile1[.gz|bz2]> ... <i:fastaFileN[.gz|bz2]> <o:setDB> <tmpDir> [options]
 By Ruoshi Zhang, Clovis Norroy & Milot Mirdita <milot@mirdita.de>
options: misc:                       
 --dbtype INT                 Database type 0: auto, 1: amino acid 2: nucleotides [0]
 --shuffle BOOL               Shuffle input database [1]
 --createdb-mode INT          Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) [0]
 --id-offset INT              Numeric ids in index file are offset by this value [0]
 --min-length INT             Minimum codon number in open reading frames [30]
 --max-length INT             Maximum codon number in open reading frames [32734]
 --max-gaps INT               Maximum number of codons with gaps or unknown residues before an open reading frame is rejected [2147483647]
 --contig-start-mode INT      Contig start can be 0: incomplete, 1: complete, 2: both [2]
 --contig-end-mode INT        Contig end can be 0: incomplete, 1: complete, 2: both [2]
 --orf-start-mode INT         Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) [1]
 --forward-frames STR         Comma-separated list of frames on the forward strand to be extracted [1,2,3]
 --reverse-frames STR         Comma-separated list of frames on the reverse strand to be extracted [1,2,3]
 --translation-table INT      1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE
                              9) FLATWORM_MITOCHONDRIAL, 10) EUPLOTID, 11) PROKARYOTE, 12) ALT_YEAST, 13) ASCIDIAN_MITOCHONDRIAL, 14) ALT_FLATWORM_MITOCHONDRIAL
                              15) BLEPHARISMA, 16) CHLOROPHYCEAN_MITOCHONDRIAL, 21) TREMATODE_MITOCHONDRIAL, 22) SCENEDESMUS_MITOCHONDRIAL
                              23) THRAUSTOCHYTRIUM_MITOCHONDRIAL, 24) PTEROBRANCHIA_MITOCHONDRIAL, 25) GRACILIBACTERIA, 26) PACHYSOLEN, 27) KARYORELICT, 28) CONDYLOSTOMA
                               29) MESODINIUM, 30) PERTRICH, 31) BLASTOCRITHIDIA [1]
 --translate INT              Translate ORF to amino acid [0]
 --use-all-table-starts BOOL  Use all alternatives for a start codon in the genetic table, if false - only ATG (AUG) [0]
 --add-orf-stop BOOL          Add stop codon '*' at complete start and end [0]
 --stat STR                   One of: linecount, mean, min, max, doolittle, charges, seqlen, firstline []
 --tsv BOOL                   Return output in TSV format [0]
common:                     
 --compressed INT             Write compressed output [0]
 -v INT                       Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
 --threads INT                Number of CPU-cores used (all by default) [10]
expert:                     
 --write-lookup INT           write .lookup file containing mapping from internal id, fasta id and file number [1]
 --create-lookup INT          Create database lookup file (can be very large) [0]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-multihitdb), [command reference index](#sec-command-reference), and [functional module page](#mod-multi-hit).

