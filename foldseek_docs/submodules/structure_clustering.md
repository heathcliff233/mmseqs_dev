### Structure Clustering Modules {#fs-cluster-root}

Foldseek clustering is built on the same search/alignment backbone used for hit finding, followed by graph or greedy clustering in `clust`. The high-level command (`cluster`) runs this sequence end-to-end, while `clust` performs clustering from an existing result graph.

#### `cluster` {#fs-cluster-command}

**Usage**

```bash
foldseek cluster <i:sequenceDB> <o:clusterDB> <tmpDir> [options]
```

`cluster` runs candidate generation, alignment filtering, and clustering in one workflow. It is the preferred command when you start from a structure DB and want production clustering output.

Core controls:

| Option | Effect |
| :--- | :--- |
| `-s` | Search sensitivity before clustering. |
| `-c` and `--cov-mode` | Coverage gating before edges become cluster links. |
| `--min-seq-id` | Sequence-identity threshold for accepting edges. |
| `--cluster-mode` | `0`: set-cover, `1`: connected component, `2/3`: greedy by length. |
| `--single-step-clustering` | Disables cascaded workflow and runs one clustering pass. |
| `--cluster-steps` | Number of cascaded stages in cascaded mode. |
| `--cluster-reassign` | Reassignment pass to correct cascade artifacts. |

Although the command name says sequence DB, in Foldseek this DB includes structural channels (`_ss`, `_ca`) used by structural scoring modules.

#### `clust` {#fs-cluster-clust}

**Usage**

```bash
foldseek clust <i:sequenceDB> <i:resultDB> <o:clusterDB> [options]
```

`clust` performs only the clustering stage from a precomputed edge/result DB. Use this when you want to rerun cluster strategy without recomputing search/alignment.

The most relevant options are `--cluster-mode`, `--max-iterations`, `--similarity-type`, and optional weighting knobs (`--weights`, `--cluster-weight-threshold`).

#### Clustering Semantics {#fs-cluster-semantics}

Set-cover mode tends to produce compact representative sets. Connected-component mode favors transitive closure and typically creates larger, looser clusters. Greedy length-prioritized modes are useful when representative length should dominate assignment order.

In practical tuning, the edge-generation parameters (`-c`, `--cov-mode`, `--min-seq-id`, and structural thresholds inherited from search) usually affect outcomes more strongly than switching between clustering algorithms on the same edge set.

#### Result Interpretation {#fs-cluster-results}

Cluster output is stored as a cluster DB. Typical post-processing is:

```bash
foldseek createsubdb clusterDB sequenceDB repDB
foldseek convert2fasta repDB rep.fasta
```

For adjacency-style exports, convert through standard result/TSV tooling depending on downstream format requirements.

#### Related Modules {#fs-cluster-related}

- Raw-input wrapper: [easy-cluster](#fs-easy-cluster)
- Complex-level clustering: [multimercluster](#fs-multimercluster)
- Index/layout preparation for repeated search+cluster loops: [Database Management](#fs-db-modules)
