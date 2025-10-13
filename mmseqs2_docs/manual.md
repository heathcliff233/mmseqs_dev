# MMseqs2 User Manual

This document provides a detailed manual for each submodule in MMseqs2.

## Common Command Line Arguments

The following are some of the most common command line arguments used across various MMseqs2 modules.

| Flag | Description | Default |
| :--- | :--- | :--- |
| `-s <float>` | Sensitivity parameter (higher is more sensitive). | `7.5` |
| `-c <float>` | Coverage threshold for clustering and alignment. | `0.8` |
| `--cov-mode <int>` | Coverage mode (0: coverage of query and target, 1: coverage of target, 2: coverage of query). | `0` |
| `--min-seq-id <float>` | Minimum sequence identity for clustering and alignment. | `0.3` |
| `--threads <int>` | Number of threads to use. | `1` |
| `-v <int>` | Verbosity level (0: quiet, 1: default, 2: verbose, 3: debug). | `1` |
| `<tmpDir>` | A temporary directory for intermediate files. | |

For more specific parameters, please refer to the documentation for each module.

## Modules

MMseqs2 is composed of many different modules that can be combined to create powerful workflows. The modules are grouped by their functionality below.

*   [Easy Workflows](./submodules/easy_workflows.md)
*   [Database Management](./submodules/database.md)
*   [Search](./submodules/search.md)
*   [Clustering](./submodules/clustering.md)
*   [Taxonomy](./submodules/taxonomy.md)
*   [Multi-hit](./submodules/multi_hit.md)
*   [Prefiltering](./submodules/prefiltering.md)
*   [Alignment](./submodules/alignment.md)
*   [Result Handling](./submodules/result_handling.md)
*   [Sequence Manipulation](./submodules/sequence_manipulation.md)
*   [Profiles](./submodules/profiles.md)
*   [Utilities](./submodules/utilities.md)
