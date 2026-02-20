## Profiles {#mod-profiles}

Modules for profile/MSA conversion, profile construction, and profile-driven workflow components.

```{=typst}
#doc_note[
This page focuses on task-oriented usage and practical options. Detailed call topology is centralized in the Dependency Map to reduce duplicated edge listings.
]
```

### `convertca3m` {#modcmd-convertca3m}

Convert a cA3M DB to a result DB.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-convertca3m), [Dependency entry](#depcmd-convertca3m).

### `convertmsa` {#modcmd-convertmsa}

Convert Stockholm/PFAM MSA file to a MSA DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs convertmsa <i:msaFile.sto[.gz]> <o:msaDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`database`](#mod-database) |

Reference links: [Full CLI](#refcmd-convertmsa), [Dependency entry](#depcmd-convertmsa).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--identifier-field` | Field from STOCKHOLM comments for choosing the MSA identifier: 0: ID, 1: AC. If the respective comment does not exist, the name of the first sequence will become the identifier |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

### `convertprofiledb` {#modcmd-convertprofiledb}

Convert a HH-suite HHM DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-convertprofiledb), [Dependency entry](#depcmd-convertprofiledb).

### `expand2profile` {#modcmd-expand2profile}

Expand an alignment result based on another and create a profile.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |

Reference links: [Full CLI](#refcmd-expand2profile), [Dependency entry](#depcmd-expand2profile).

### `msa2profile` {#modcmd-msa2profile}

Convert a MSA DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs msa2profile <i:msaDB> <o:profileDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE | COMMAND_DATABASE_CREATION` |
| Upstream command count | `2` |
| Downstream command count | `0` |
| Related functional groups | [`clustering`](#mod-clustering), [`database`](#mod-database) |

Reference links: [Full CLI](#refcmd-msa2profile), [Dependency entry](#depcmd-msa2profile).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--match-mode` | 0: Columns that have a residue in the first sequence are kept, 1: columns that have a residue in --match-ratio of all sequences are kept |
| `--match-ratio` | Columns that have a residue in this ratio of all sequences are kept |
| `--pseudo-cnt-mode` | use 0: substitution-matrix or 1: context-specific pseudocounts |
| `--pca` | Pseudo count admixture strength |

### `msa2result` {#modcmd-msa2result}

Convert a MSA DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs msa2result <i:msaDB> <o:seqDB> <o:profileDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE | COMMAND_EXPERT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-msa2result), [Dependency entry](#depcmd-msa2result).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--match-mode` | 0: Columns that have a residue in the first sequence are kept, 1: columns that have a residue in --match-ratio of all sequences are kept |
| `--match-ratio` | Columns that have a residue in this ratio of all sequences are kept |
| `--pseudo-cnt-mode` | use 0: substitution-matrix or 1: context-specific pseudocounts |
| `--pca` | Pseudo count admixture strength |

### `pairaln` {#modcmd-pairaln}

Pair sequences to match best protein A and B from a species.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_EXPERT` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-pairaln), [Dependency entry](#depcmd-pairaln).

### `profile2consensus` {#modcmd-profile2consensus}

Extract consensus sequence DB from a profile DB.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |

Reference links: [Full CLI](#refcmd-profile2consensus), [Dependency entry](#depcmd-profile2consensus).

### `profile2neff` {#modcmd-profile2neff}

Convert a profile DB to a tab-separated list of Neff scores.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-profile2neff), [Dependency entry](#depcmd-profile2neff).

### `profile2pssm` {#modcmd-profile2pssm}

Convert a profile DB to a tab-separated PSSM file.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-profile2pssm), [Dependency entry](#depcmd-profile2pssm).

### `profile2repseq` {#modcmd-profile2repseq}

Extract representative sequence DB from a profile DB.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-profile2repseq), [Dependency entry](#depcmd-profile2repseq).

### `result2profile` {#modcmd-result2profile}

Compute profile DB from a result DB.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs result2profile <i:queryDB> <i:targetDB> <i:resultDB> <o:profileDB> [options]` |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Upstream command count | `1` |
| Downstream command count | `0` |
| Related functional groups | [`search_workflows`](#mod-search-workflows) |

Reference links: [Full CLI](#refcmd-result2profile), [Dependency entry](#depcmd-result2profile).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--comp-bias-corr` | Correct for locally biased amino acid composition (range 0-1) |
| `--comp-bias-corr-scale` | Correct for locally biased amino acid composition (range 0-1) |
| `-e` | List matches below this E-value (range 0.0-inf) |
| `--gap-open` | Gap open cost |
| `--gap-extend` | Gap extension cost |
| `--mask-profile` | Mask query sequence of profile using tantan [0,1] |
| `--e-profile` | Include sequences matches with < E-value thr. into the profile (>=0.0) |
| `--wg` | Use global sequence weighting for profile calculation |

### `sequence2profile` {#modcmd-sequence2profile}

Turn sequence into profile by adding context specific pseudo counts.

| Aspect | Value |
| :--- | :--- |
| Usage | Help snapshot unavailable locally. |
| API layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Upstream command count | `0` |
| Downstream command count | `0` |
| Related functional groups | `n/a` |

Reference links: [Full CLI](#refcmd-sequence2profile), [Dependency entry](#depcmd-sequence2profile).

### `tsv2exprofiledb` {#modcmd-tsv2exprofiledb}

Create a expandable profile db from TSV files.

| Aspect | Value |
| :--- | :--- |
| Usage | `usage: mmseqs tsv2exprofiledb <i:tsvFilesBase> <o:exprofileDB> [options]` |
| API layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Upstream command count | `0` |
| Downstream command count | `5` |
| Related functional groups | [`database`](#mod-database), [`utilities`](#mod-utilities) |

Reference links: [Full CLI](#refcmd-tsv2exprofiledb), [Dependency entry](#depcmd-tsv2exprofiledb).

#### Key Options

| Option | Purpose |
| :--- | :--- |
| `--gpu` | Use GPU (CUDA) if possible |
| `--threads` | Number of CPU-cores used (all by default) |
| `--compressed` | Write compressed output |
| `-v` | Verbosity level: 0: quiet, 1: +errors, 2: +warnings, 3: +info |

