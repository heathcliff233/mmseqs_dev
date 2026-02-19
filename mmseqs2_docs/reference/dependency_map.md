# MMseqs2 Dependency Map

This file is generated from `MMseqs2/src/MMseqsBase.cpp` and workflow scripts.

| Metric | Value |
| :--- | :--- |
| Total visible commands | `128` |

`n/a` in connection fields means no direct edge was resolved by static extraction.

## Easy Workflows

### `easy-cluster` {#cmd-easycluster}

Slower, sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`cluster`](./cluster.md), [`createdb`](./createdb.md), [`createseqfiledb`](./createseqfiledb.md), [`createtsv`](./createtsv.md), [`result2flat`](./result2flat.md), [`result2repseq`](./result2repseq.md), [`rmdb`](./rmdb.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./easy-cluster.md) |

### `easy-linclust` {#cmd-easylinclust}

Fast linear time cluster, less sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`createdb`](./createdb.md), [`createseqfiledb`](./createseqfiledb.md), [`createtsv`](./createtsv.md), [`linclust`](./linclust.md), [`result2flat`](./result2flat.md), [`result2repseq`](./result2repseq.md), [`rmdb`](./rmdb.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./easy-linclust.md) |

### `easy-linsearch` {#cmd-easylinsearch}

Fast, less sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY | COMMAND_EXPERT` |
| Calls | [`convertalis`](./convertalis.md), [`createdb`](./createdb.md), [`createlinindex`](./createlinindex.md), [`linsearch`](./linsearch.md), [`rmdb`](./rmdb.md), [`search`](./search.md), [`summarizeresult`](./summarizeresult.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./easy-linsearch.md) |

### `easy-rbh` {#cmd-easyrbh}

Find reciprocal best hit.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`convertalis`](./convertalis.md), [`createdb`](./createdb.md), [`rbh`](./rbh.md), [`rmdb`](./rmdb.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./easy-rbh.md) |

### `easy-search` {#cmd-easysearch}

Sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`convertalis`](./convertalis.md), [`createdb`](./createdb.md), [`createlinindex`](./createlinindex.md), [`linsearch`](./linsearch.md), [`rmdb`](./rmdb.md), [`search`](./search.md), [`summarizeresult`](./summarizeresult.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./easy-search.md) |

### `easy-taxonomy` {#cmd-easytaxonomy}

Taxonomic classification.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`addtaxonomy`](./addtaxonomy.md), [`convertalis`](./convertalis.md), [`createdb`](./createdb.md), [`createtsv`](./createtsv.md), [`filterdb`](./filterdb.md), [`lca`](./lca.md), [`rmdb`](./rmdb.md), [`summarizealis`](./summarizealis.md), [`swapresults`](./swapresults.md), [`taxonomy`](./taxonomy.md), [`taxonomyreport`](./taxonomyreport.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./easy-taxonomy.md) |

## Search Workflows

### `linsearch` {#cmd-linsearch}

Fast, less sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN|COMMAND_EXPERT` |
| Calls | [`align`](./align.md), [`concatdbs`](./concatdbs.md), [`extractorfs`](./extractorfs.md), [`filterdb`](./filterdb.md), [`kmersearch`](./kmersearch.md), [`offsetalignment`](./offsetalignment.md), [`rescorediagonal`](./rescorediagonal.md), [`rmdb`](./rmdb.md), [`swapresults`](./swapresults.md) |
| Called by | [`easy-linsearch`](./easy-linsearch.md), [`easy-search`](./easy-search.md) |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./linsearch.md) |

### `map` {#cmd-map}

Map nearly identical sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`search`](./search.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./map.md) |

### `rbh` {#cmd-rbh}

Reciprocal best hit search.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`filterdb`](./filterdb.md), [`mergedbs`](./mergedbs.md), [`result2rbh`](./result2rbh.md), [`rmdb`](./rmdb.md), [`search`](./search.md), [`swapresults`](./swapresults.md) |
| Called by | [`easy-rbh`](./easy-rbh.md) |
| Workflow scripts | `easyrbh.sh` |
| Command reference | [Open page](./rbh.md) |

### `search` {#cmd-search}

Sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`align`](./align.md), [`createsubdb`](./createsubdb.md), [`expand2profile`](./expand2profile.md), [`expandaln`](./expandaln.md), [`extractframes`](./extractframes.md), [`extractorfs`](./extractorfs.md), [`filterresult`](./filterresult.md), [`lcaalign`](./lcaalign.md), [`mergedbs`](./mergedbs.md), [`mvdb`](./mvdb.md), [`offsetalignment`](./offsetalignment.md), [`prefilter`](./prefilter.md), [`profile2consensus`](./profile2consensus.md), [`rescorediagonal`](./rescorediagonal.md), [`result2profile`](./result2profile.md), [`result2stats`](./result2stats.md), [`rmdb`](./rmdb.md), [`search`](./search.md), [`splitsequence`](./splitsequence.md), [`subtractdbs`](./subtractdbs.md), [`swapresults`](./swapresults.md), [`ungappedprefilter`](./ungappedprefilter.md) |
| Called by | [`clusterupdate`](./clusterupdate.md), [`easy-linsearch`](./easy-linsearch.md), [`easy-search`](./easy-search.md), [`map`](./map.md), [`multihitsearch`](./multihitsearch.md), [`rbh`](./rbh.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `enrich.sh`, `iterativepp.sh`, `map.sh`, `multihitsearch.sh`, `rbh.sh`, `taxonomy.sh`, `update_clustering.sh` |
| Command reference | [Open page](./search.md) |

## Clustering

### `clust` {#cmd-clust}

Cluster result by Set-Cover/Connected-Component/Greedy-Incremental.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`linclust`](./linclust.md) |
| Workflow scripts | `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh` |
| Command reference | [Open page](./clust.md) |

### `cluster` {#cmd-cluster}

Slower, sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`align`](./align.md), [`clust`](./clust.md), [`clusthash`](./clusthash.md), [`concatdbs`](./concatdbs.md), [`createsubdb`](./createsubdb.md), [`extractframes`](./extractframes.md), [`filterdb`](./filterdb.md), [`linclust`](./linclust.md), [`mergeclusters`](./mergeclusters.md), [`mergedbs`](./mergedbs.md), [`mvdb`](./mvdb.md), [`offsetalignment`](./offsetalignment.md), [`prefilter`](./prefilter.md), [`rescorediagonal`](./rescorediagonal.md), [`rmdb`](./rmdb.md), [`subtractdbs`](./subtractdbs.md), [`swapdb`](./swapdb.md), [`tsv2db`](./tsv2db.md) |
| Called by | [`clusterupdate`](./clusterupdate.md), [`easy-cluster`](./easy-cluster.md) |
| Workflow scripts | `update_clustering.sh` |
| Command reference | [Open page](./cluster.md) |

### `clusterupdate` {#cmd-clusterupdate}

Update previous clustering with new sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`cluster`](./cluster.md), [`concatdbs`](./concatdbs.md), [`createsubdb`](./createsubdb.md), [`diffseqdbs`](./diffseqdbs.md), [`filterdb`](./filterdb.md), [`mergedbs`](./mergedbs.md), [`mvdb`](./mvdb.md), [`prefixid`](./prefixid.md), [`renamedbkeys`](./renamedbkeys.md), [`result2repseq`](./result2repseq.md), [`rmdb`](./rmdb.md), [`search`](./search.md), [`swapdb`](./swapdb.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./clusterupdate.md) |

### `clusthash` {#cmd-clusthash}

Hash-based clustering of equal length sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md) |
| Workflow scripts | `clustering.sh` |
| Command reference | [Open page](./clusthash.md) |

### `linclust` {#cmd-linclust}

Fast, less sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`align`](./align.md), [`clust`](./clust.md), [`createsubdb`](./createsubdb.md), [`filterdb`](./filterdb.md), [`kmermatcher`](./kmermatcher.md), [`mergeclusters`](./mergeclusters.md), [`rescorediagonal`](./rescorediagonal.md), [`rmdb`](./rmdb.md) |
| Called by | [`cluster`](./cluster.md), [`easy-linclust`](./easy-linclust.md) |
| Workflow scripts | `cascaded_clustering.sh`, `nucleotide_clustering.sh` |
| Command reference | [Open page](./linclust.md) |

### `mergeclusters` {#cmd-mergeclusters}

Merge multiple cascaded clustering steps.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`linclust`](./linclust.md) |
| Workflow scripts | `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh` |
| Command reference | [Open page](./mergeclusters.md) |

### `pickconsensusrep` {#cmd-pickconsensusrep}

Select new representatives for each cluster based on consensus.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Calls | [`align`](./align.md), [`msa2profile`](./msa2profile.md), [`prefixid`](./prefixid.md), [`renamedbkeys`](./renamedbkeys.md), [`result2msa`](./result2msa.md), [`rmdb`](./rmdb.md), [`tsv2db`](./tsv2db.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./pickconsensusrep.md) |

## Prefiltering

### `countkmer` {#cmd-countkmer}

Count k-mers.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./countkmer.md) |

### `gappedprefilter` {#cmd-gappedprefilter}

Optimal Smith-Waterman-based prefiltering (slow).

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./gappedprefilter.md) |

### `kmermatcher` {#cmd-kmermatcher}

Find bottom-m-hashed k-mer matches within sequence DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | [`linclust`](./linclust.md) |
| Workflow scripts | `linclust.sh` |
| Command reference | [Open page](./kmermatcher.md) |

### `kmersearch` {#cmd-kmersearch}

Find bottom-m-hashed k-mer matches between target and query DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | [`linsearch`](./linsearch.md) |
| Workflow scripts | `linsearch.sh` |
| Command reference | [Open page](./kmersearch.md) |

### `prefilter` {#cmd-prefilter}

Double consecutive diagonal k-mer search.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `enrich.sh`, `iterativepp.sh`, `nucleotide_clustering.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh`, `taxpercontig.sh`, `translated_search.sh` |
| Command reference | [Open page](./prefilter.md) |

### `ungappedprefilter` {#cmd-ungappedprefilter}

Optimal diagonal score search.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | [`search`](./search.md) |
| Workflow scripts | `blastp.sh`, `blastpgp.sh` |
| Command reference | [Open page](./ungappedprefilter.md) |

## Alignment

### `align` {#cmd-align}

Optimal gapped local alignment.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`linclust`](./linclust.md), [`linsearch`](./linsearch.md), [`pickconsensusrep`](./pickconsensusrep.md), [`search`](./search.md) |
| Workflow scripts | `iterativepp.sh`, `nucleotide_clustering.sh`, `pickconsensusrep.sh`, `searchslicedtargetprofile.sh` |
| Command reference | [Open page](./align.md) |

### `alignall` {#cmd-alignall}

Within-result all-vs-all gapped local alignment.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./alignall.md) |

### `alignbykmer` {#cmd-alignbykmer}

Heuristic gapped local k-mer based alignment.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./alignbykmer.md) |

### `expandaln` {#cmd-expandaln}

Expand an alignment result based on another.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Calls | `n/a` |
| Called by | [`search`](./search.md) |
| Workflow scripts | `enrich.sh`, `iterativepp.sh` |
| Command reference | [Open page](./expandaln.md) |

### `fwbw` {#cmd-fwbw}

Forward Backward Alignment.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./fwbw.md) |

### `offsetalignment` {#cmd-offsetalignment}

Offset alignment by ORF start position.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`linsearch`](./linsearch.md), [`search`](./search.md) |
| Workflow scripts | `blastn.sh`, `linsearch.sh`, `nucleotide_clustering.sh`, `translated_search.sh` |
| Command reference | [Open page](./offsetalignment.md) |

### `proteinaln2nucl` {#cmd-proteinaln2nucl}

Transform protein alignments to nucleotide alignments.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./proteinaln2nucl.md) |

### `rescorediagonal` {#cmd-rescorediagonal}

Compute sequence identity for diagonal.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`linclust`](./linclust.md), [`linsearch`](./linsearch.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `linclust.sh`, `linsearch.sh`, `nucleotide_clustering.sh`, `taxpercontig.sh` |
| Command reference | [Open page](./rescorediagonal.md) |

### `transitivealign` {#cmd-transitivealign}

Transfer alignments via transitivity.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./transitivealign.md) |

## Profiles

### `convertca3m` {#cmd-convertca3m}

Convert a cA3M DB to a result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./convertca3m.md) |

### `convertmsa` {#cmd-convertmsa}

Convert Stockholm/PFAM MSA file to a MSA DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Calls | `n/a` |
| Called by | [`databases`](./databases.md) |
| Workflow scripts | `databases.sh` |
| Command reference | [Open page](./convertmsa.md) |

### `convertprofiledb` {#cmd-convertprofiledb}

Convert a HH-suite HHM DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./convertprofiledb.md) |

### `expand2profile` {#cmd-expand2profile}

Expand an alignment result based on another and create a profile.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Calls | `n/a` |
| Called by | [`search`](./search.md) |
| Workflow scripts | `iterativepp.sh` |
| Command reference | [Open page](./expand2profile.md) |

### `msa2profile` {#cmd-msa2profile}

Convert a MSA DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE | COMMAND_DATABASE_CREATION` |
| Calls | `n/a` |
| Called by | [`databases`](./databases.md), [`pickconsensusrep`](./pickconsensusrep.md) |
| Workflow scripts | `databases.sh`, `pickconsensusrep.sh` |
| Command reference | [Open page](./msa2profile.md) |

### `msa2result` {#cmd-msa2result}

Convert a MSA DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./msa2result.md) |

### `pairaln` {#cmd-pairaln}

Pair sequences to match best protein A and B from a species.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./pairaln.md) |

### `profile2consensus` {#cmd-profile2consensus}

Extract consensus sequence DB from a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | [`search`](./search.md) |
| Workflow scripts | `iterativepp.sh` |
| Command reference | [Open page](./profile2consensus.md) |

### `profile2neff` {#cmd-profile2neff}

Convert a profile DB to a tab-separated list of Neff scores.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./profile2neff.md) |

### `profile2pssm` {#cmd-profile2pssm}

Convert a profile DB to a tab-separated PSSM file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./profile2pssm.md) |

### `profile2repseq` {#cmd-profile2repseq}

Extract representative sequence DB from a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./profile2repseq.md) |

### `result2profile` {#cmd-result2profile}

Compute profile DB from a result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | [`search`](./search.md) |
| Workflow scripts | `blastpgp.sh`, `enrich.sh` |
| Command reference | [Open page](./result2profile.md) |

### `sequence2profile` {#cmd-sequence2profile}

Turn sequence into profile by adding context specific pseudo counts.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./sequence2profile.md) |

### `tsv2exprofiledb` {#cmd-tsv2exprofiledb}

Create a expandable profile db from TSV files.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Calls | [`aliasdb`](./aliasdb.md), [`compress`](./compress.md), [`mvdb`](./mvdb.md), [`rmdb`](./rmdb.md), [`tsv2db`](./tsv2db.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./tsv2exprofiledb.md) |

## Database

### `aliasdb` {#cmd-aliasdb}

Create relative symlink of DB to another name in the same folder.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | [`tsv2exprofiledb`](./tsv2exprofiledb.md) |
| Workflow scripts | `tsv2exprofiledb.sh` |
| Command reference | [Open page](./aliasdb.md) |

### `concatdbs` {#cmd-concatdbs}

Concatenate two DBs, giving new IDs to entries from 2nd DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`linsearch`](./linsearch.md) |
| Workflow scripts | `linsearch.sh`, `nucleotide_clustering.sh`, `update_clustering.sh` |
| Command reference | [Open page](./concatdbs.md) |

### `cpdb` {#cmd-cpdb}

Copy a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./cpdb.md) |

### `createdb` {#cmd-createdb}

Convert FASTA/Q file(s) to a sequence DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Calls | `n/a` |
| Called by | [`databases`](./databases.md), [`easy-cluster`](./easy-cluster.md), [`easy-linclust`](./easy-linclust.md), [`easy-linsearch`](./easy-linsearch.md), [`easy-rbh`](./easy-rbh.md), [`easy-search`](./easy-search.md), [`easy-taxonomy`](./easy-taxonomy.md), [`multihitdb`](./multihitdb.md) |
| Workflow scripts | `databases.sh`, `easycluster.sh`, `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh`, `multihitdb.sh` |
| Command reference | [Open page](./createdb.md) |

### `createindex` {#cmd-createindex}

Store precomputed index on disk to reduce search overhead.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Calls | [`extractframes`](./extractframes.md), [`extractorfs`](./extractorfs.md), [`rmdb`](./rmdb.md), [`splitsequence`](./splitsequence.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./createindex.md) |

### `createlinindex` {#cmd-createlinindex}

Create linsearch index.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Calls | [`extractframes`](./extractframes.md), [`extractorfs`](./extractorfs.md), [`rmdb`](./rmdb.md), [`splitsequence`](./splitsequence.md) |
| Called by | [`easy-linsearch`](./easy-linsearch.md), [`easy-search`](./easy-search.md) |
| Workflow scripts | `easysearch.sh` |
| Command reference | [Open page](./createlinindex.md) |

### `createsubdb` {#cmd-createsubdb}

Create a subset of a DB from list of DB keys.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`linclust`](./linclust.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `blastp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh`, `taxpercontig.sh`, `translated_search.sh`, `update_clustering.sh` |
| Command reference | [Open page](./createsubdb.md) |

### `databases` {#cmd-databases}

List and download databases.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Calls | [`convertmsa`](./convertmsa.md), [`createdb`](./createdb.md), [`createtaxdb`](./createtaxdb.md), [`msa2profile`](./msa2profile.md), [`nrtotaxmapping`](./nrtotaxmapping.md), [`prefixid`](./prefixid.md), [`rmdb`](./rmdb.md), [`tar2db`](./tar2db.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./databases.md) |

### `db2tar` {#cmd-db2tar}

Archive contents of a DB to a tar archive.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./db2tar.md) |

### `lndb` {#cmd-lndb}

Symlink a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./lndb.md) |

### `mergedbs` {#cmd-mergedbs}

Merge entries from multiple DBs.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`rbh`](./rbh.md), [`search`](./search.md) |
| Workflow scripts | `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `enrich.sh`, `iterativepp.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `update_clustering.sh` |
| Command reference | [Open page](./mergedbs.md) |

### `mvdb` {#cmd-mvdb}

Move a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md), [`tsv2exprofiledb`](./tsv2exprofiledb.md) |
| Workflow scripts | `blastp.sh`, `cascaded_clustering.sh`, `searchslicedtargetprofile.sh`, `taxonomy.sh`, `tsv2exprofiledb.sh`, `update_clustering.sh` |
| Command reference | [Open page](./mvdb.md) |

### `renamedbkeys` {#cmd-renamedbkeys}

Create a new DB with original keys renamed.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | [`clusterupdate`](./clusterupdate.md), [`pickconsensusrep`](./pickconsensusrep.md) |
| Workflow scripts | `update_clustering.sh` |
| Command reference | [Open page](./renamedbkeys.md) |

### `rmdb` {#cmd-rmdb}

Remove a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`createindex`](./createindex.md), [`createlinindex`](./createlinindex.md), [`databases`](./databases.md), [`easy-cluster`](./easy-cluster.md), [`easy-linclust`](./easy-linclust.md), [`easy-linsearch`](./easy-linsearch.md), [`easy-rbh`](./easy-rbh.md), [`easy-search`](./easy-search.md), [`easy-taxonomy`](./easy-taxonomy.md), [`linclust`](./linclust.md), [`linsearch`](./linsearch.md), [`multihitsearch`](./multihitsearch.md), [`pickconsensusrep`](./pickconsensusrep.md), [`rbh`](./rbh.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md), [`tsv2exprofiledb`](./tsv2exprofiledb.md) |
| Workflow scripts | `blastn.sh`, `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `createindex.sh`, `databases.sh`, `easycluster.sh`, `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh`, `iterativepp.sh`, `linclust.sh`, `linsearch.sh`, `multihitsearch.sh`, `nucleotide_clustering.sh`, `pickconsensusrep.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh`, `taxonomy.sh`, `taxpercontig.sh`, `translated_search.sh`, `tsv2exprofiledb.sh`, `update_clustering.sh` |
| Command reference | [Open page](./rmdb.md) |

### `splitdb` {#cmd-splitdb}

Split DB into subsets.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./splitdb.md) |

### `splitsequence` {#cmd-splitsequence}

Split sequences by length.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`createindex`](./createindex.md), [`createlinindex`](./createlinindex.md), [`search`](./search.md) |
| Workflow scripts | `blastn.sh`, `createindex.sh` |
| Command reference | [Open page](./splitsequence.md) |

### `subtractdbs` {#cmd-subtractdbs}

Remove all entries from first DB occurring in second DB by key.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`search`](./search.md) |
| Workflow scripts | `blastpgp.sh`, `cascaded_clustering.sh`, `enrich.sh`, `iterativepp.sh`, `nucleotide_clustering.sh` |
| Command reference | [Open page](./subtractdbs.md) |

### `swapdb` {#cmd-swapdb}

Transpose DB with integer values in first column.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`multihitdb`](./multihitdb.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `cascaded_clustering.sh`, `multihitdb.sh`, `taxpercontig.sh`, `update_clustering.sh` |
| Command reference | [Open page](./swapdb.md) |

### `tar2db` {#cmd-tar2db}

Convert content of tar archives to any DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`databases`](./databases.md) |
| Workflow scripts | `databases.sh` |
| Command reference | [Open page](./tar2db.md) |

### `tsv2db` {#cmd-tsv2db}

Convert a TSV file to any DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`multihitdb`](./multihitdb.md), [`pickconsensusrep`](./pickconsensusrep.md), [`tsv2exprofiledb`](./tsv2exprofiledb.md) |
| Workflow scripts | `cascaded_clustering.sh`, `multihitdb.sh`, `pickconsensusrep.sh`, `tsv2exprofiledb.sh` |
| Command reference | [Open page](./tsv2db.md) |

## Result Handling

### `convert2fasta` {#cmd-convert2fasta}

Convert sequence DB to FASTA format.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./convert2fasta.md) |

### `convertalis` {#cmd-convertalis}

Convert alignment DB to BLAST-tab, SAM or custom format.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Calls | `n/a` |
| Called by | [`easy-linsearch`](./easy-linsearch.md), [`easy-rbh`](./easy-rbh.md), [`easy-search`](./easy-search.md), [`easy-taxonomy`](./easy-taxonomy.md) |
| Workflow scripts | `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh` |
| Command reference | [Open page](./convertalis.md) |

### `createseqfiledb` {#cmd-createseqfiledb}

Create a DB of unaligned FASTA entries.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`easy-cluster`](./easy-cluster.md), [`easy-linclust`](./easy-linclust.md) |
| Workflow scripts | `easycluster.sh` |
| Command reference | [Open page](./createseqfiledb.md) |

### `createtsv` {#cmd-createtsv}

Convert result DB to tab-separated flat file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Calls | `n/a` |
| Called by | [`easy-cluster`](./easy-cluster.md), [`easy-linclust`](./easy-linclust.md), [`easy-taxonomy`](./easy-taxonomy.md) |
| Workflow scripts | `easycluster.sh`, `easytaxonomy.sh` |
| Command reference | [Open page](./createtsv.md) |

### `extractdomains` {#cmd-extractdomains}

Extract highest scoring alignment regions for each sequence from BLAST-tab file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./extractdomains.md) |

### `filterresult` {#cmd-filterresult}

Pairwise alignment result filter.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`search`](./search.md) |
| Workflow scripts | `searchslicedtargetprofile.sh` |
| Command reference | [Open page](./filterresult.md) |

### `result2dnamsa` {#cmd-result2dnamsa}

Compute MSA DB with out insertions in the query for DNA sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./result2dnamsa.md) |

### `result2flat` {#cmd-result2flat}

Create flat file by adding FASTA headers to DB entries.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`easy-cluster`](./easy-cluster.md), [`easy-linclust`](./easy-linclust.md) |
| Workflow scripts | `easycluster.sh` |
| Command reference | [Open page](./result2flat.md) |

### `result2msa` {#cmd-result2msa}

Compute MSA DB from a result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`pickconsensusrep`](./pickconsensusrep.md) |
| Workflow scripts | `pickconsensusrep.sh` |
| Command reference | [Open page](./result2msa.md) |

### `result2rbh` {#cmd-result2rbh}

Filter a merged result DB to retain only reciprocal best hits.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`rbh`](./rbh.md) |
| Workflow scripts | `rbh.sh` |
| Command reference | [Open page](./result2rbh.md) |

### `result2repseq` {#cmd-result2repseq}

Get representative sequences from result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`clusterupdate`](./clusterupdate.md), [`easy-cluster`](./easy-cluster.md), [`easy-linclust`](./easy-linclust.md) |
| Workflow scripts | `easycluster.sh`, `update_clustering.sh` |
| Command reference | [Open page](./result2repseq.md) |

### `result2stats` {#cmd-result2stats}

Compute statistics for each entry in a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`multihitdb`](./multihitdb.md), [`search`](./search.md) |
| Workflow scripts | `multihitdb.sh`, `searchslicedtargetprofile.sh` |
| Command reference | [Open page](./result2stats.md) |

### `sortresult` {#cmd-sortresult}

Sort a result DB in the same order as the prefilter or align module.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./sortresult.md) |

### `summarizealis` {#cmd-summarizealis}

Summarize alignment result to one row (uniq. cov., cov., avg. seq. id.).

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](./easy-taxonomy.md) |
| Workflow scripts | `easytaxonomy.sh` |
| Command reference | [Open page](./summarizealis.md) |

### `summarizeheaders` {#cmd-summarizeheaders}

Summarize FASTA headers of result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./summarizeheaders.md) |

### `summarizeresult` {#cmd-summarizeresult}

Extract annotations from alignment DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`easy-linsearch`](./easy-linsearch.md), [`easy-search`](./easy-search.md) |
| Workflow scripts | `easysearch.sh` |
| Command reference | [Open page](./summarizeresult.md) |

### `swapresults` {#cmd-swapresults}

Transpose prefilter/alignment DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](./easy-taxonomy.md), [`linsearch`](./linsearch.md), [`rbh`](./rbh.md), [`search`](./search.md) |
| Workflow scripts | `easytaxonomy.sh`, `linsearch.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh` |
| Command reference | [Open page](./swapresults.md) |

## Sequence Manipulation

### `extractalignedregion` {#cmd-extractalignedregion}

Extract aligned sequence region from query.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./extractalignedregion.md) |

### `extractframes` {#cmd-extractframes}

Extract frames from a nucleotide sequence DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`createindex`](./createindex.md), [`createlinindex`](./createlinindex.md), [`search`](./search.md) |
| Workflow scripts | `blastn.sh`, `createindex.sh`, `nucleotide_clustering.sh`, `translated_search.sh` |
| Command reference | [Open page](./extractframes.md) |

### `extractorfs` {#cmd-extractorfs}

Six-frame extraction of open reading frames.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`createindex`](./createindex.md), [`createlinindex`](./createlinindex.md), [`linsearch`](./linsearch.md), [`multihitdb`](./multihitdb.md), [`search`](./search.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `createindex.sh`, `multihitdb.sh`, `taxpercontig.sh`, `translated_search.sh` |
| Command reference | [Open page](./extractorfs.md) |

### `masksequence` {#cmd-masksequence}

Soft mask sequence DB using tantan.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./masksequence.md) |

### `orftocontig` {#cmd-orftocontig}

Write ORF locations in alignment format.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`multihitdb`](./multihitdb.md) |
| Workflow scripts | `multihitdb.sh` |
| Command reference | [Open page](./orftocontig.md) |

### `recoverlongestorf` {#cmd-recoverlongestorf}

Recover longest ORF for taxonomy annotation after elimination.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `taxpercontig.sh` |
| Command reference | [Open page](./recoverlongestorf.md) |

### `reverseseq` {#cmd-reverseseq}

Reverse (without complement) sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./reverseseq.md) |

### `translateaa` {#cmd-translateaa}

Translate proteins to lexicographically lowest codons.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./translateaa.md) |

### `translatenucs` {#cmd-translatenucs}

Translate nucleotides to proteins.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`multihitdb`](./multihitdb.md) |
| Workflow scripts | `multihitdb.sh` |
| Command reference | [Open page](./translatenucs.md) |

## Taxonomy

### `addtaxonomy` {#cmd-addtaxonomy}

Add taxonomic labels to result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](./easy-taxonomy.md) |
| Workflow scripts | `easytaxonomy.sh` |
| Command reference | [Open page](./addtaxonomy.md) |

### `aggregatetax` {#cmd-aggregatetax}

Aggregate multiple taxon labels to a single label.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./aggregatetax.md) |

### `aggregatetaxweights` {#cmd-aggregatetaxweights}

Aggregate multiple taxon labels to a single label.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `taxpercontig.sh` |
| Command reference | [Open page](./aggregatetaxweights.md) |

### `createbintaxmapping` {#cmd-createbintaxmapping}

Create binary taxonomy mapping from tabular taxonomy mapping.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./createbintaxmapping.md) |

### `createbintaxonomy` {#cmd-createbintaxonomy}

Create binary taxonomy from NCBI input.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`createtaxdb`](./createtaxdb.md) |
| Workflow scripts | `createtaxdb.sh` |
| Command reference | [Open page](./createbintaxonomy.md) |

### `createdmptaxonomy` {#cmd-createdmptaxonomy}

Create dmp files from binary taxonomy.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./createdmptaxonomy.md) |

### `createtaxdb` {#cmd-createtaxdb}

Add taxonomic labels to sequence DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | [`createbintaxonomy`](./createbintaxonomy.md) |
| Called by | [`databases`](./databases.md) |
| Workflow scripts | `databases.sh` |
| Command reference | [Open page](./createtaxdb.md) |

### `filtertaxdb` {#cmd-filtertaxdb}

Filter taxonomy result database.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./filtertaxdb.md) |

### `filtertaxseqdb` {#cmd-filtertaxseqdb}

Filter taxonomy sequence database.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./filtertaxseqdb.md) |

### `lca` {#cmd-lca}

Compute the lowest common ancestor.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](./easy-taxonomy.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `taxonomy.sh` |
| Command reference | [Open page](./lca.md) |

### `lcaalign` {#cmd-lcaalign}

Efficient gapped alignment for lca computation.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | [`search`](./search.md) |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./lcaalign.md) |

### `majoritylca` {#cmd-majoritylca}

Compute the lowest common ancestor using majority voting.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./majoritylca.md) |

### `nrtotaxmapping` {#cmd-nrtotaxmapping}

Create taxonomy mapping for NR database.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | [`databases`](./databases.md) |
| Workflow scripts | `databases.sh` |
| Command reference | [Open page](./nrtotaxmapping.md) |

### `taxonomy` {#cmd-taxonomy}

Taxonomic classification.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`aggregatetax`](./aggregatetax.md), [`aggregatetaxweights`](./aggregatetaxweights.md), [`createsubdb`](./createsubdb.md), [`extractorfs`](./extractorfs.md), [`filterdb`](./filterdb.md), [`lca`](./lca.md), [`mergeresultsbyset`](./mergeresultsbyset.md), [`mvdb`](./mvdb.md), [`prefilter`](./prefilter.md), [`recoverlongestorf`](./recoverlongestorf.md), [`rescorediagonal`](./rescorediagonal.md), [`rmdb`](./rmdb.md), [`search`](./search.md), [`swapdb`](./swapdb.md), [`taxonomy`](./taxonomy.md) |
| Called by | [`easy-taxonomy`](./easy-taxonomy.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `easytaxonomy.sh`, `taxpercontig.sh` |
| Command reference | [Open page](./taxonomy.md) |

### `taxonomyreport` {#cmd-taxonomyreport}

Create a taxonomy report in Kraken or Krona format.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_FORMAT_CONVERSION` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](./easy-taxonomy.md) |
| Workflow scripts | `easytaxonomy.sh` |
| Command reference | [Open page](./taxonomyreport.md) |

## Multi Hit

### `besthitperset` {#cmd-besthitperset}

For each set of sequences compute the best element and update p-value.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | `n/a` |
| Called by | [`multihitsearch`](./multihitsearch.md) |
| Workflow scripts | `multihitsearch.sh` |
| Command reference | [Open page](./besthitperset.md) |

### `combinepvalperset` {#cmd-combinepvalperset}

For each set compute the combined p-value.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./combinepvalperset.md) |

### `mergeresultsbyset` {#cmd-mergeresultsbyset}

Merge results from multiple ORFs back to their respective contig.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | `n/a` |
| Called by | [`multihitsearch`](./multihitsearch.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `multihitsearch.sh`, `taxpercontig.sh` |
| Command reference | [Open page](./mergeresultsbyset.md) |

### `multihitdb` {#cmd-multihitdb}

Create sequence DB for multi hit searches.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | [`createdb`](./createdb.md), [`extractorfs`](./extractorfs.md), [`filterdb`](./filterdb.md), [`orftocontig`](./orftocontig.md), [`result2stats`](./result2stats.md), [`swapdb`](./swapdb.md), [`translatenucs`](./translatenucs.md), [`tsv2db`](./tsv2db.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./multihitdb.md) |

### `multihitsearch` {#cmd-multihitsearch}

Search with a grouped set of sequences against another grouped set.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | [`besthitperset`](./besthitperset.md), [`mergeresultsbyset`](./mergeresultsbyset.md), [`rmdb`](./rmdb.md), [`search`](./search.md) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./multihitsearch.md) |

## Utilities

### `apply` {#cmd-apply}

Execute given program on each DB entry.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./apply.md) |

### `compress` {#cmd-compress}

Compress DB entries.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | [`tsv2exprofiledb`](./tsv2exprofiledb.md) |
| Workflow scripts | `tsv2exprofiledb.sh` |
| Command reference | [Open page](./compress.md) |

### `convertkb` {#cmd-convertkb}

Convert UniProtKB data to a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./convertkb.md) |

### `decompress` {#cmd-decompress}

Decompress DB entries.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./decompress.md) |

### `diffseqdbs` {#cmd-diffseqdbs}

Compute diff of two sequence DBs.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | [`clusterupdate`](./clusterupdate.md) |
| Workflow scripts | `update_clustering.sh` |
| Command reference | [Open page](./diffseqdbs.md) |

### `filterdb` {#cmd-filterdb}

DB filtering by given conditions.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | [`cluster`](./cluster.md), [`clusterupdate`](./clusterupdate.md), [`easy-taxonomy`](./easy-taxonomy.md), [`linclust`](./linclust.md), [`linsearch`](./linsearch.md), [`multihitdb`](./multihitdb.md), [`rbh`](./rbh.md), [`taxonomy`](./taxonomy.md) |
| Workflow scripts | `cascaded_clustering.sh`, `easytaxonomy.sh`, `linclust.sh`, `linsearch.sh`, `multihitdb.sh`, `rbh.sh`, `taxonomy.sh`, `taxpercontig.sh`, `update_clustering.sh` |
| Command reference | [Open page](./filterdb.md) |

### `gff2db` {#cmd-gff2db}

Extract regions from a sequence database based on a GFF3 file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./gff2db.md) |

### `gpuserver` {#cmd-gpuserver}

Start a GPU server.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./gpuserver.md) |

### `maskbygff` {#cmd-maskbygff}

Mask out sequence regions in a sequence DB by features selected from a GFF3 file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./maskbygff.md) |

### `prefixid` {#cmd-prefixid}

For each entry in a DB prepend the entry key to the entry itself.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | [`clusterupdate`](./clusterupdate.md), [`databases`](./databases.md), [`pickconsensusrep`](./pickconsensusrep.md) |
| Workflow scripts | `databases.sh`, `pickconsensusrep.sh`, `update_clustering.sh` |
| Command reference | [Open page](./prefixid.md) |

### `setextendeddbtype` {#cmd-setextendeddbtype}

Write an extended DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./setextendeddbtype.md) |

### `suffixid` {#cmd-suffixid}

For each entry in a DB append the entry key to the entry itself.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./suffixid.md) |

### `summarizetabs` {#cmd-summarizetabs}

Extract annotations from HHblits BLAST-tab-formatted results.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./summarizetabs.md) |

### `touchdb` {#cmd-touchdb}

Preload DB into memory (page cache).

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./touchdb.md) |

### `unpackdb` {#cmd-unpackdb}

Unpack a DB into separate files.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./unpackdb.md) |

### `view` {#cmd-view}

Print DB entries given in --id-list to stdout.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](./view.md) |

