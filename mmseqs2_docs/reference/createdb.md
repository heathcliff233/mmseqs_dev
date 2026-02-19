# `createdb`

Convert FASTA/Q file(s) to a sequence DB.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

## Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `low_level_api` |
| Primary functional group | [`database`](../submodules/database.md) |
| Category flags | `COMMAND_DATABASE_CREATION` |

## Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`databases`](./databases.md), [`easy-cluster`](./easy-cluster.md), [`easy-linclust`](./easy-linclust.md), [`easy-linsearch`](./easy-linsearch.md), [`easy-rbh`](./easy-rbh.md), [`easy-search`](./easy-search.md), [`easy-taxonomy`](./easy-taxonomy.md), [`multihitdb`](./multihitdb.md) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `databases.sh`, `easycluster.sh`, `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh`, `multihitdb.sh` |

## Usage

`usage: mmseqs createdb <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]>|<i:stdin> <o:sequenceDB> [options]`

## Key Options

| Option | Purpose |
| :--- | :--- |
| `--dbtype` | Database type 0: auto, 1: amino acid 2: nucleotides |
| `--shuffle` | Shuffle input database |
| `--createdb-mode` | Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) |
| `--id-offset` | Numeric ids in index file are offset by this value |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--write-lookup` | write .lookup file containing mapping from internal id, fasta id and file number |

## Full CLI Help Snapshot

```text
usage: mmseqs createdb <i:fastaFile1[.gz|.bz2]> ... <i:fastaFileN[.gz|.bz2]>|<i:stdin> <o:sequenceDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr>
options: misc:                
 --dbtype INT          Database type 0: auto, 1: amino acid 2: nucleotides [0]
 --shuffle BOOL        Shuffle input database [1]
 --createdb-mode INT   Createdb mode 0: copy data, 1: soft link data and write new index (works only with single line fasta/q) [0]
 --id-offset INT       Numeric ids in index file are offset by this value [0]
common:              
 --compressed INT      Write compressed output [0]
 -v INT                Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]
expert:              
 --write-lookup INT    write .lookup file containing mapping from internal id, fasta id and file number [1]

examples:
 # Create a sequence database from multiple FASTA files
 mmseqs createdb file1.fa file2.fa.gz file3.fa sequenceDB
 
 # Create a seqDB from stdin
 cat seq.fasta | mmseqs createdb stdin sequenceDB
 
 # Create a seqDB by indexing existing FASTA/Q (for single line fasta entries only)
 mmseqs createdb seq.fasta sequenceDB --createdb-mode 1
 
references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
```
## Cross References

See [Dependency map](./dependency_map.md), [Command reference index](./index.md), and [functional module page](../submodules/database.md).

