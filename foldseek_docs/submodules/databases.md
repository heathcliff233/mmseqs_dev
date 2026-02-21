### Database Management Modules {#fs-db-modules}

Foldseek performance is tightly coupled to how databases are stored on disk. The search and clustering workflows do not read one monolithic file; they read coordinated channels (`DB`, `DB_ss`, `DB_ca`, `DB_h`) plus index and metadata sidecars. This chapter documents those files as an operational format specification, then explains how `databases`, `createindex`, and `createclusearchdb` manipulate that layout.

#### Canonical Database Layout {#fs-db-layout}

A standard `createdb` output with prefix `X` produces a synchronized family of files:

| Path | Role | Primary readers |
| :--- | :--- | :--- |
| `X`, `X.index`, `X.dbtype` | Amino-acid channel (one entry per chain) | `search`, `structurealign`, `cluster`, `convertalis` |
| `X_ss`, `X_ss.index`, `X_ss.dbtype` | 3Di channel, residue-aligned to `X` | prefilter/alignment stages |
| `X_ca`, `X_ca.index`, `X_ca.dbtype` | C-alpha coordinates for TM/LDDT/structure-bit sorting | `structurealign`, `tmalign`, converters |
| `X_h`, `X_h.index`, `X_h.dbtype` | Header channel (entry identifiers/metadata text) | converters/reporting |
| `X.lookup` | Entry mapping `id -> accession -> fileNumber` | lookup-based conversion and tooling |
| `X.source` | `fileNumber -> source file/model label` | provenance-aware exports |
| `X_mapping` (optional) | `id -> taxId` mapping (`--write-mapping 1`) | taxonomy-aware downstream workflows |

The key design invariant is shared IDs across channels: for a given internal key, `X`, `X_ss`, `X_ca`, and `X_h` describe the same chain entry.

#### Core File Formats {#fs-db-file-format}

`<DB>.index` is a tab-separated text index. Each line is:

```text
<id>\t<offset>\t<length>\n
```

`id` is the internal key, `offset` points into `<DB>` data payload, and `length` is the stored entry length. This format is written in `DBWriter::indexToBuffer` (`MMseqs2/src/commons/DBWriter.cpp`) and parsed by `DBReader::readIndex` (`MMseqs2/src/commons/DBReader.cpp`).

`<DB>.dbtype` is a 4-byte integer (`int32`) describing logical DB type plus compression flag. The high bit (bit 31) indicates compressed storage; the lower bits hold the base DB type (`DBTYPE_AMINO_ACIDS`, `DBTYPE_GENERIC_DB`, Foldseek `DBTYPE_CA_ALPHA=101`, and so on).

`<DB>` stores concatenated entry payloads separated by a null terminator. In compressed writer mode, per-entry framing is handled by the writer and the same index file still resolves entry boundaries.

`<DB>.lookup` is line-based text with exactly three columns:

```text
<id>\t<entryName>\t<fileNumber>\n
```

This is the exact serializer used by `DBReader<unsigned int>::lookupEntryToBuffer` in `MMseqs2/src/commons/DBReader.cpp`.

`<DB>.source` maps `fileNumber` to an original source label:

```text
<fileNumber>\t<sourceName>\n
```

It is written during `createdb` lookup generation in `foldseek/src/strucclustutils/structcreatedb.cpp`.

#### Channel Payload Semantics {#fs-db-payload-semantics}

For `createdb` outputs, the payload format inside each channel is:

| Channel | Entry payload |
| :--- | :--- |
| `X` | Amino-acid one-letter sequence plus trailing newline (`\n`) |
| `X_ss` | 3Di token sequence (one residue, one symbol) plus trailing newline |
| `X_h` | Header text plus trailing newline |
| `X_ca` | Binary or text coordinate encoding (`--coord-store-mode`) |

`X` and `X_ss` are residue-synchronized: position `i` in `X_ss` describes the same residue as position `i` in `X`. That invariant is what enables 3Di+AA alignment (`--alignment-type 2`) without conversion steps.

#### C-alpha Storage Modes (`X_ca`) {#fs-db-ca-format}

`X_ca` has three encodings, selected at creation time (`createdb`) or rewritten later (`compressca`).

| Mode | Option | On-disk payload | Notes |
| :--- | :--- | :--- | :--- |
| Float | `--coord-store-mode 1` | `3 * L` float32 values (`x[0..L-1], y[0..L-1], z[0..L-1]`) | Highest compatibility, largest footprint |
| Diff16 | `--coord-store-mode 2` | Per axis: `start:int32` + `(L-1)` deltas `int16`; packed for x, y, z, plus one trailing compatibility byte | Default mode in Foldseek; values are scaled by 1000 before integer encoding |
| Plain text | `compressca --coord-store-mode 3` | Comma-separated float list + newline | Stored as generic DB type; useful for inspection/interchange |

In Diff16 mode, `createdb` attempts integer delta encoding and falls back to float payload for entries that overflow `int16` during conversion. Decoding is handled by `Coordinate16::read` (`foldseek/src/commons/Coordinate16.h`).

#### `databases` {#fs-databases-command}

**Usage**

```bash
foldseek databases <name> <o:sequenceDB> <tmpDir> [options]
```

`databases` downloads curated structural datasets and model assets (AlphaFold subsets, PDB snapshots, BFMD/BFVD, ProstT5 weights). Use `--tsv 1` when you need a machine-readable catalog for reproducible provisioning scripts.

#### `createindex` {#fs-createindex}

**Usage**

```bash
foldseek createindex <i:sequenceDB> <tmpDir> [options]
```

`createindex` is a Foldseek workflow wrapper around MMseqs indexing plus Foldseek-specific channel handling (`foldseek/src/workflow/StructureIndex.cpp` and `foldseek/data/structureindex.sh`). Operationally it does three things:

1. Builds index data for the AA channel and the 3Di channel.
2. Links header/cluster side channels needed by Foldseek workflows.
3. Optionally appends C-alpha channels into the `.idx` container unless excluded.

The two high-impact controls are:

| Option | Effect |
| :--- | :--- |
| `--index-subset` | Drops selected index components (`1`: no headers, `2`: no prefilter data, `4`: no alignment payloads) to reduce index size. |
| `--index-exclude` | Bit flags for Foldseek-specific exclusions (`1`: omit k-mer index, `2`: omit C-alpha append into index). |

When `--index-exclude 2` is used, coordinate-aware ranking and threshold paths may be disabled later unless raw `_ca` side databases are still available.

#### `createclusearchdb` {#fs-createclusearchdb}

**Usage**

```bash
foldseek createclusearchdb <i:sequenceDB> <i:clusterDB> <o:sequenceDB> [options]
```

`createclusearchdb` transforms clustering output into representative/member search layout for `--cluster-search 1`. For each selected suffix (default `_h,_ss,_ca` in Foldseek help), it writes:

- representative channel: `<out><suffix>`
- member channel: `<out>_seq<suffix>`

It also copies cluster topology to `<out>_clu` and propagates metadata sidecars (`.lookup`, `.source`, `_mapping`, taxonomy files) with aliases for `_seq` views.

A source-level detail that matters for debugging: `_seq` channels are assembled as a two-part DB where representatives and non-representatives can live in separate backing files, while one merged `_seq.index` maps IDs to the correct offsets. This is normal and expected.

For cluster-search compatibility, `StructureSearch.cpp` checks for at least:

- `<target>_seq`, `<target>_seq_ss`, `<target>_seq_h`
- one of `<target>_clu` or `<target>_aln`

If coordinate-aware ranking/filtering is required, keep `<target>_seq_ca` available as well.

#### Practical Layout Strategies {#fs-db-strategy}

If you run repeated searches on a fixed target, build and validate indices once (`--check-compatible 1`) and keep full coordinate channels. If you are strictly ungapped or no-structure-bit ranking, excluding selected index parts can reduce RAM and startup time, but apply those exclusions only after confirming that downstream modules do not need TM/LDDT or structure-bit sorting.

#### Minimal End-to-End Example {#fs-db-example}

```bash
foldseek databases Alphafold/Swiss-Prot afdb tmp
foldseek createindex afdb tmp --check-compatible 1
foldseek search queryDB afdb alnDB tmp
```

For sequence-to-3Di prediction workflows:

```bash
foldseek databases ProstT5 weights tmp
foldseek createdb query.fasta queryDB --prostt5-model weights
```
