## `clust` {#refcmd-clust}

Cluster result by Set-Cover/Connected-Component/Greedy-Incremental.

In connection tables, `n/a` means no direct static edge was resolved by static extraction.

### Classification

| Aspect | Value |
| :--- | :--- |
| API layer | `mid_level_api` |
| Primary functional group | [`clustering`](#mod-clustering) |
| Category flags | `COMMAND_CLUSTER` |

### Connections

| Aspect | Value |
| :--- | :--- |
| Called by modules | [`cluster`](#refcmd-cluster), [`linclust`](#refcmd-linclust) |
| Calls modules | `n/a` |
| Seen in workflow scripts | `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh` |

### Usage

`usage: mmseqs clust <i:sequenceDB> <i:resultDB> <o:clusterDB> [options]`

### Key Options

| Option | Purpose |
| :--- | :--- |
| `--cluster-mode` | 0: Set-Cover (greedy) |
| `--max-iterations` | Maximum depth of breadth first search in connected component clustering |
| `--similarity-type` | Type of score used for clustering. 1: alignment score 2: sequence identity |
| `--weights` | Weights used for cluster priorization |
| `--cluster-weight-threshold` | Weight threshold used for cluster priorization |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### Full CLI Help Snapshot

```text
usage: mmseqs clust <i:sequenceDB> <i:resultDB> <o:clusterDB> [options]
 By Martin Steinegger <martin.steinegger@snu.ac.kr> & Lars von den Driesch & Maria Hauser
options: clust:                          
 --cluster-mode INT               0: Set-Cover (greedy)
                                  1: Connected component (BLASTclust)
                                  2,3: Greedy clustering by sequence length (CDHIT) [0]
 --max-iterations INT             Maximum depth of breadth first search in connected component clustering [1000]
 --similarity-type INT            Type of score used for clustering. 1: alignment score 2: sequence identity [2]
kmermatcher:                    
 --weights STR                    Weights used for cluster priorization []
 --cluster-weight-threshold FLOAT Weight threshold used for cluster priorization [0.900]
common:                         
 --threads INT                    Number of CPU-cores used (all by default) [10]
 --compressed INT                 Write compressed output [0]
 -v INT                           Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info [3]

references:
 - Steinegger M, Soding J: MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11), 1026-1028 (2017)
 - Hauser M, Steinegger M, Soding J: MMseqs software suite for fast and deep clustering and searching of large protein sequence sets. Bioinformatics, 32(9), 1323-1330 (2016)
```
### Cross References

See [Dependency map section](#sec-dependency-map), [dependency entry](#depcmd-clust), [command reference index](#sec-command-reference), and [functional module page](#mod-clustering).

