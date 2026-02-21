### Structure Manipulation Modules {#fs-manip-root}

This chapter covers modules that prepare structure databases, transform structural data layouts, and convert internal result DBs into analysis outputs.

#### `createdb` {#fs-createdb}

**Usage**

```bash
foldseek createdb <i:directory|.tsv>|<i:PDB|mmCIF[.gz]|tar[.gz]|DB> ... <i:PDB|mmCIF[.gz]|tar|DB> <o:sequenceDB> [options]
```

`createdb` is the ingestion point for Foldseek. It parses structures, builds synchronized AA/3Di/CA/header channels, and writes the DB layout consumed by all search and clustering modules.

The exact on-disk file specification for these channels is documented in [Database Management: Core File Formats](#fs-db-file-format) and [Database Management: C-alpha Storage Modes](#fs-db-ca-format).

Important options:

| Option | Role |
| :--- | :--- |
| `--db-extraction-mode` | `0`: chain-level entries, `1`: interface extraction mode. |
| `--input-format` | Force parser mode when autodetection is not sufficient. |
| `--file-include`, `--file-exclude` | Regex-based filtering for directory/tar inputs. |
| `--prostt5-model` | Enables 3Di prediction from sequence input using ProstT5. |
| `--gpu` | Enables GPU path for ProstT5 inference when available. |
| `--coord-store-mode` | C-alpha storage encoding (`float` or `uint16` diff). |
| `--write-lookup`, `--write-mapping` | Metadata mapping outputs for downstream integration. |

#### `compressca` {#fs-compressca}

**Usage**

```bash
foldseek compressca <i:DB> <o:caDB> [options]
```

`compressca` rewrites C-alpha coordinate storage, typically to reduce I/O and footprint. `--coord-store-mode` controls encoding (`1` float, `2` diff16, `3` plain text floats).

#### `convertalis` {#fs-convertalis}

**Usage**

```bash
foldseek convertalis <i:queryDb> <i:targetDb> <i:alignmentDB> <o:alignmentFile> [options]
```

`convertalis` is the primary result exporter. It converts internal alignment DBs to tabular, SAM, HTML, or superposed-structure style outputs and can expose structural metrics such as TM-score and LDDT columns.

`--format-output` is central for custom analysis pipelines. When requesting columns like `alntmscore`, `qtmscore`, `ttmscore`, `lddt`, `u`, or `t`, `convertalis` triggers the required internal computations from stored coordinates and backtraces.

#### `convert2pdb` {#fs-convert2pdb}

**Usage**

```bash
foldseek convert2pdb <i:Db> <o:pdbFile|pdbDir> [options]
```

`convert2pdb` materializes superposed C-alpha coordinates into PDB output. `--pdb-output-mode` selects whether output is one multi-model file, per-chain files, or per-complex files.

#### `aln2tmscore` {#fs-aln2tmscore}

**Usage**

```bash
foldseek aln2tmscore <i:queryDB> <i:targetDB> <i:alnDB> <o:resultDB> [options]
```

`aln2tmscore` converts existing alignment DBs into TM-score-focused result DBs. This is useful when TM-score conversion is needed as a standalone post-processing stage.

#### `result2profile` {#fs-result2profile}

**Usage**

```bash
foldseek result2profile <i:queryDB> <i:targetDB> <i:resultDB> <o:profileDB> [options]
```

`result2profile` builds profile DBs from result alignments. It is mainly relevant for iterative/profile-oriented workflows where profile diversity and redundancy controls (`--max-seq-id`, `--qid`, `--cov`, `--diff`) matter.

#### Typical Data-Preparation Flow {#fs-manip-flow}

```bash
foldseek createdb structures/ structDB
foldseek createindex structDB tmp
foldseek search structDB targetDB alnDB tmp
foldseek convertalis structDB targetDB alnDB result.tsv --format-output query,target,alntmscore,lddt,bits,evalue
```

This flow keeps ingestion, indexing, search, and conversion explicitly separated, which makes reruns and parameter sweeps easier to reproduce.
