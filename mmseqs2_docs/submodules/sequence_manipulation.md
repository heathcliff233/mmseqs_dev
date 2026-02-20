## Sequence Manipulation {#mod-sequence-manipulation}

Modules that transform sequence content, frames, ORFs, and masked/aligned regions.

```{=typst}
#doc_note[
This page focuses on task-oriented usage and practical options. Detailed call topology is centralized in the Dependency Map to reduce duplicated edge listings.
]
```

```{=typst}
#doc_warning[
Validate database-type and sidecar compatibility before chaining modules. Most pipeline failures come from DB contract mismatches.
]
```

### `extractalignedregion` {#modcmd-extractalignedregion}

Extract aligned sequence region from query.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs extractalignedregion <i:queryDB> <i:targetDB> <i:resultDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-extractalignedregion), [Dependency entry](#depcmd-extractalignedregion).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--extract-mode` | Extract from 1: Query, 2: Target |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `extractframes` {#modcmd-extractframes}

Extract frames from a nucleotide sequence DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs extractframes <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `4` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`database`](#mod-database), [`search_workflows`](#mod-search-workflows) |

Reference links: [Full CLI](#refcmd-extractframes), [Dependency entry](#depcmd-extractframes).

#### Key Options

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

### `extractorfs` {#modcmd-extractorfs}

Six-frame extraction of open reading frames.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs extractorfs <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `6` |
| Downstream command count | `0` |
| Related functional groups | [`database`](#mod-database), [`multi_hit`](#mod-multi-hit), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |

Reference links: [Full CLI](#refcmd-extractorfs), [Dependency entry](#depcmd-extractorfs).

#### Key Options

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

### `masksequence` {#modcmd-masksequence}

Soft mask sequence DB using tantan.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs masksequence <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-masksequence), [Dependency entry](#depcmd-masksequence).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--mask` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking |
| `--mask-prob` | Mask sequences is probablity is above threshold |
| `--mask-lower-case` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region |
| `--mask-n-repeat` | Repeat letters that occure > threshold in a rwo |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `orftocontig` {#modcmd-orftocontig}

Write ORF locations in alignment format.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs orftocontig <i:contigsSequenceDB> <i:extractedOrfsHeadersDB> <o:orfsAlignedToContigDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`multi_hit`](#mod-multi-hit) |

Reference links: [Full CLI](#refcmd-orftocontig), [Dependency entry](#depcmd-orftocontig).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `recoverlongestorf` {#modcmd-recoverlongestorf}

Recover longest ORF for taxonomy annotation after elimination.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs recoverlongestorf <i:orfDB> <i:resultDB> <o:tsvFile> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_EXPERT` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`taxonomy`](#mod-taxonomy) |

Reference links: [Full CLI](#refcmd-recoverlongestorf), [Dependency entry](#depcmd-recoverlongestorf).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `reverseseq` {#modcmd-reverseseq}

Reverse (without complement) sequences.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs reverseseq <i:sequenceDB> <o:revSequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-reverseseq), [Dependency entry](#depcmd-reverseseq).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `translateaa` {#modcmd-translateaa}

Translate proteins to lexicographically lowest codons.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs translateaa <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-translateaa), [Dependency entry](#depcmd-translateaa).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `translatenucs` {#modcmd-translatenucs}

Translate nucleotides to proteins.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs translatenucs <i:sequenceDB> <o:sequenceDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`multi_hit`](#mod-multi-hit) |

Reference links: [Full CLI](#refcmd-translatenucs), [Dependency entry](#depcmd-translatenucs).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--translation-table` | 1) CANONICAL, 2) VERT_MITOCHONDRIAL, 3) YEAST_MITOCHONDRIAL, 4) MOLD_MITOCHONDRIAL, 5) INVERT_MITOCHONDRIAL, 6) CILIATE |
| `--add-orf-stop` | Add stop codon '*' at complete start and end |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--compressed` | Write compressed output |
| `--threads` | Number of CPU-cores used (all by default) |

