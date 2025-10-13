
# Search Modules

This document describes the search submodules of MMseqs2.

## `search`

**Description:**

> Sensitive homology search

**Usage:**
```bash
mmseqs search <i:queryDB> <i:targetDB> <o:alignmentDB> <tmpDir> [options]
```

**Parameters:**

### Prefilter Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `--comp-bias-corr <INT>` | Correct for locally biased amino acid composition (range 0-1) | `1` |
| `--comp-bias-corr-scale <FLOAT>` | Correct for locally biased amino acid composition (range 0-1) | `1.000` |
| `--add-self-matches <BOOL>` | Artificially add entries of queries with themselves (for clustering) | `0` |
| `--seed-sub-mat <TWIN>` | Substitution matrix file for k-mer generation | `aa:VTML80.out,nucl:nucleotide.out` |
| `-s <FLOAT>` | Sensitivity: 1.0 faster; 4.0 fast; 7.5 sensitive | `5.700` |
| `-k <INT>` | k-mer length (0: automatically set to optimum) | `0` |
| `--target-search-mode <INT>` | target search mode (0: regular k-mer, 1: similar k-mer) | `0` |
| `--k-score <TWIN>` | k-mer threshold for generating similar k-mer lists | `seq:2147483647,prof:2147483647` |
| `--alph-size <TWIN>` | Alphabet size (range 2-21) | `aa:21,nucl:5` |
| `--max-seqs <INT>` | Maximum results per query sequence allowed to pass the prefilter (affects sensitivity) | `300` |
| `--split <INT>` | Split input into N equally distributed chunks. 0: set the best split automatically | `0` |
| `--split-mode <INT>` | 0: split target db; 1: split query db; 2: auto, depending on main memory | `2` |
| `--split-memory-limit <BYTE>` | Set max memory per split. E.g. 800B, 5K, 10M, 1G. Default (0) to all available system memory | `0` |
| `--diag-score <BOOL>` | Use ungapped diagonal scoring during prefilter | `1` |
| `--exact-kmer-matching <INT>` | Extract only exact k-mers for matching (range 0-1) | `0` |
| `--mask <INT>` | Mask sequences in prefilter stage with tantan: 0: w/o low complexity masking, 1: with low complexity masking | `1` |
| `--mask-prob <FLOAT>` | Mask sequences is probablity is above threshold | `0.900` |
| `--mask-lower-case <INT>` | Lowercase letters will be excluded from k-mer search 0: include region, 1: exclude region | `0` |
| `--mask-n-repeat <INT>` | Repeat letters that occure > threshold in a rwo | `0` |
| `--min-ungapped-score <INT>` | Accept only matches with ungapped alignment score above threshold | `15` |
| `--spaced-kmer-mode <INT>` | 0: use consecutive positions in k-mers; 1: use spaced k-mers | `1` |
| `--spaced-kmer-pattern <STR>` | User-specified spaced k-mer pattern | `[]` |
| `--local-tmp <STR>` | Path where some of the temporary files will be created | `[]` |
| `--disk-space-limit <BYTE>` | Set max disk space to use for reverse profile searches. E.g. 800B, 5K, 10M, 1G. Default (0) to all available disk space in the temp folder | `0` |

### Align Options
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-a <BOOL>` | Add backtrace string (convert to alignments with mmseqs convertalis module) | `0` |
| `--alignment-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment | `2` |
| `--alignment-output-mode <INT>` | How to compute the alignment: 0: automatic, 1: only score and end_pos, 2: also start_pos and cov, 3: also seq.id, 4: only ungapped alignment, 5: score only (output) cluster format | `0` |
| `--wrapped-scoring <BOOL>` | Double the (nucleotide) query sequence during the scoring process to allow wrapped diagonal scoring around end and start | `0` |
| `-e <DOUBLE>` | List matches below this E-value (range 0.0-inf) | `1.000E-03` |
| `--min-seq-id <FLOAT>` | List matches above this sequence identity (for clustering) (range 0.0-1.0) | `0.000` |
| `--min-aln-len <INT>` | Minimum alignment length (range 0-INT_MAX) | `0` |
| `--seq-id-mode <INT>` | 0: alignment length, 1: shorter, 2: longer sequence | `0` |
| `--alt-ali <INT>` | Show up to this many alternative alignments | `0` |
| `-c <FLOAT>` | List matches above this fraction of aligned (covered) residues (see --cov-mode) | `0.000` |
| `--cov-mode <INT>` | 0: coverage of
