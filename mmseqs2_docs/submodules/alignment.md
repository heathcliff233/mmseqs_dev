## Alignment {#mod-alignment}

Alignment and rescoring modules used after prefiltering to compute pair quality and coordinates.

```{=typst}
#doc_note[
This page is task-oriented. Detailed call topology is centralized in the Dependency Map to avoid repeating large edge lists.
]
```

### `align` {#modcmd-align}

Optimal gapped local alignment.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 5 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs align <i:queryDB> <i:targetDB> <i:resultDB> <o:alignmentDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Upstream command count | `5` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-align) · [Dependency entry](#depcmd-align) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `--alignment-mode` | How to compute the alignment: |
| `--alignment-output-mode` | How to compute the alignment: |
| `--wrapped-scoring` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start |
| `-e` | List matches below this E-value (range 0.0-inf) |

### `alignall` {#modcmd-alignall}

Within-result all-vs-all gapped local alignment.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs alignall <i:sequenceDB> <i:resultDB> <o:alignmentDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-alignall) · [Dependency entry](#depcmd-alignall) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `--alignment-mode` | How to compute the alignment: |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `--min-aln-len` | Minimum alignment length (range 0-INT_MAX) |

### `alignbykmer` {#modcmd-alignbykmer}

Heuristic gapped local k-mer based alignment.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs alignbykmer <i:queryDB> <i:targetDB> <i:resultDB> <o:resultDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-alignbykmer) · [Dependency entry](#depcmd-alignbykmer) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `-k` | k-mer length (0: automatically set to optimum) |
| `--spaced-kmer-mode` | 0: use consecutive positions in k-mers; 1: use spaced k-mers |
| `--spaced-kmer-pattern` | User-specified spaced k-mer pattern |
| `--alph-size` | Alphabet size (range 2-21) |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--cov-mode` | 0: coverage of query and target |

### `expandaln` {#modcmd-expandaln}

Expand an alignment result based on another.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 1 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs expandaln <i:queryDB> <i:targetDB> <i:resultDB> <i:resultDB|ca3mDB> <o:alignmentDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-expandaln) · [Dependency entry](#depcmd-expandaln) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--score-bias` | Score bias when computing SW alignment (in bits) |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |

### `fwbw` {#modcmd-fwbw}

Forward Backward Alignment.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs fwbw <inputDB(s)> <outputDB> [options]` (source-derived synopsis; run `mmseqs fwbw` for exact syntax) |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-fwbw) · [Dependency entry](#depcmd-fwbw) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

### `offsetalignment` {#modcmd-offsetalignment}

Offset alignment by ORF start position.

Low-level DB or utility command used for composition and contract enforcement. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 3 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs offsetalignment <i:queryDB> <i:queryOrfDB> <i:targetDB> <i:targetOrfDB> <i:alnDB> <o:alnDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `3` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows) |
| References | [Full CLI](#refcmd-offsetalignment) · [Dependency entry](#depcmd-offsetalignment) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--search-type` | Search type 0: auto 1: amino acid, 2: translated, 3: nucleotide, 4: translated nucleotide alignment |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `--db-load-mode` | Database preload mode 0: auto, 1: fread, 2: mmap, 3: mmap+touch |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |
| `--chain-alignments` | Chain overlapping alignments |
| `--merge-query` | Combine ORFs/split sequences to a single entry |

### `proteinaln2nucl` {#modcmd-proteinaln2nucl}

Transform protein alignments to nucleotide alignments.

Low-level DB or utility command used for composition and contract enforcement. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs proteinaln2nucl <i:nuclQueryDB> <i:nuclTargetDB> <i:aaQueryDB> <i:aaTargetDB> <i:alnDB> <o:alnDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-proteinaln2nucl) · [Dependency entry](#depcmd-proteinaln2nucl) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--sub-mat` | Substitution matrix file |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `rescorediagonal` {#modcmd-rescorediagonal}

Compute sequence identity for diagonal.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 5 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs rescorediagonal <i:queryDB> <i:targetDB> <i:prefilterDB> <o:resultDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Upstream command count | `5` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`search_workflows`](#mod-search-workflows), [`taxonomy`](#mod-taxonomy) |
| References | [Full CLI](#refcmd-rescorediagonal) · [Dependency entry](#depcmd-rescorediagonal) |

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--add-self-matches` | Artificially add entries of queries with themselves (for clustering) |
| `--wrapped-scoring` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `-c` | List matches above this fraction of aligned (covered) residues (see --cov-mode) |
| `-a` | Add backtrace string (convert to alignments with mmseqs convertalis module) |
| `--cov-mode` | 0: coverage of query and target |
| `--min-seq-id` | List matches above this sequence identity (for clustering) (range 0.0-1.0) |
| `--min-aln-len` | Minimum alignment length (range 0-INT_MAX) |

### `transitivealign` {#modcmd-transitivealign}

Transfer alignments via transitivity.

Mid-level compute module used directly in advanced pipelines and by workflows. Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead. Current coupling is 0 upstream caller(s) and 0 downstream call(s).

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs transitivealign <inputDB(s)> <outputDB> [options]` (source-derived synopsis; run `mmseqs transitivealign` for exact syntax) |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | No direct cross-group coupling detected in the current dependency map. |
| References | [Full CLI](#refcmd-transitivealign) · [Dependency entry](#depcmd-transitivealign) |

No local option snapshot was parsed for this command. Use the Full CLI reference page for details.

