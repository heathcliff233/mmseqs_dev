# Sequence Manipulation

Modules that transform sequence content, frames, ORFs, and masked/aligned regions.

```{=typst}
#doc_note[
This page emphasizes module relationships and practical options. For complete CLI details, open the linked command reference pages. In connection tables, `n/a` means no direct static edge was resolved.
]
```

```{=typst}
#doc_warning[
Validate database-type and sidecar compatibility before chaining modules. Most pipeline failures come from DB contract mismatches.
]
```

## `extractalignedregion`

Extract aligned sequence region from query.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs extractalignedregion <i:queryDB> <i:targetDB> <i:resultDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/extractalignedregion.md), [Dependency map](../reference/dependency_map.md#cmd-extractalignedregion).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--extract-mode` | Extract from 1: Query, 2: Target |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `extractframes`

Extract frames from a nucleotide sequence DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs extractframes <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | [`cluster`](../reference/cluster.md), [`createindex`](../reference/createindex.md), [`createlinindex`](../reference/createlinindex.md), [`search`](../reference/search.md) |
| Calls modules | `n/a` |
| Related functional groups | [`clustering`](./clustering.md), [`database`](./database.md), [`search_workflows`](./search.md) |
| Workflow script usage | `blastn.sh`, `createindex.sh`, `nucleotide_clustering.sh`, `translated_search.sh` |

Reference links: [Full CLI](../reference/extractframes.md), [Dependency map](../reference/dependency_map.md#cmd-extractframes).

### Key Options

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

## `extractorfs`

Six-frame extraction of open reading frames.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs extractorfs <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | [`createindex`](../reference/createindex.md), [`createlinindex`](../reference/createlinindex.md), [`linsearch`](../reference/linsearch.md), [`multihitdb`](../reference/multihitdb.md), [`search`](../reference/search.md), [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | [`database`](./database.md), [`multi_hit`](./multi_hit.md), [`search_workflows`](./search.md), [`taxonomy`](./taxonomy.md) |
| Workflow script usage | `createindex.sh`, `multihitdb.sh`, `taxpercontig.sh`, `translated_search.sh` |

Reference links: [Full CLI](../reference/extractorfs.md), [Dependency map](../reference/dependency_map.md#cmd-extractorfs).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--min-length` | Minimum codon number in open reading frames |
| `--max-length` | Maximum codon number in open reading frames |
| `--max-gaps` | Maximum number of codons with gaps or unknown residues before an open reading frame is rejected |
| `--contig-start-mode` | Contig start can be 0: incomplete, 1: complete, 2: both |
| `--contig-end-mode` | Contig end can be 0: incomplete, 1: complete, 2: both |
| `--orf-start-mode` | Orf fragment can be 0: from start to stop, 1: from any to stop, 2: from last encountered start to stop (no start in the middle) |
| `--forward-frames` | Comma-separated list of frames on the forward strand to be extracted |
| `--reverse-frames` | Comma-separated list of frames on the reverse strand to be extracted |

## `masksequence`

Soft mask sequence DB using tantan.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs masksequence <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/masksequence.md), [Dependency map](../reference/dependency_map.md#cmd-masksequence).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `orftocontig`

Write ORF locations in alignment format.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs orftocontig <i:contigsSequenceDB> <i:extractedOrfsHeadersDB> <o:orfsAlignedToContigDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | [`multihitdb`](../reference/multihitdb.md) |
| Calls modules | `n/a` |
| Related functional groups | [`multi_hit`](./multi_hit.md) |
| Workflow script usage | `multihitdb.sh` |

Reference links: [Full CLI](../reference/orftocontig.md), [Dependency map](../reference/dependency_map.md#cmd-orftocontig).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `recoverlongestorf`

Recover longest ORF for taxonomy annotation after elimination.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs recoverlongestorf <i:orfDB> <i:resultDB> <o:tsvFile> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_EXPERT` |
| Called by modules | [`taxonomy`](../reference/taxonomy.md) |
| Calls modules | `n/a` |
| Related functional groups | [`taxonomy`](./taxonomy.md) |
| Workflow script usage | `taxpercontig.sh` |

Reference links: [Full CLI](../reference/recoverlongestorf.md), [Dependency map](../reference/dependency_map.md#cmd-recoverlongestorf).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `reverseseq`

Reverse (without complement) sequences.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs reverseseq <i:sequenceDB> <o:revSequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/reverseseq.md), [Dependency map](../reference/dependency_map.md#cmd-reverseseq).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `translateaa`

Translate proteins to lexicographically lowest codons.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs translateaa <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | `n/a` |
| Calls modules | `n/a` |
| Related functional groups | `n/a` |
| Workflow script usage | `n/a` |

Reference links: [Full CLI](../reference/translateaa.md), [Dependency map](../reference/dependency_map.md#cmd-translateaa).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

## `translatenucs`

Translate nucleotides to proteins.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs translatenucs <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Called by modules | [`multihitdb`](../reference/multihitdb.md) |
| Calls modules | `n/a` |
| Related functional groups | [`multi_hit`](./multi_hit.md) |
| Workflow script usage | `multihitdb.sh` |

Reference links: [Full CLI](../reference/translatenucs.md), [Dependency map](../reference/dependency_map.md#cmd-translatenucs).

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--translation-table` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE |
| `--add-orf-stop` | Add stop codon '*' at complete start and end |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |

