# MMseqs2 Dependency Map {#sec-dependency-map}

This file is generated from `MMseqs2/src/MMseqsBase.cpp` and workflow scripts.

| Metric | Value |
| :--- | :--- |
| Total visible commands | `128` |

`n/a` in connection fields means no direct edge was resolved by static extraction.

## Easy Workflows {#depgroup-easy-workflows}

### `easy-cluster` {#depcmd-easy-cluster}

Slower, sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`cluster`](#depcmd-cluster), [`createdb`](#depcmd-createdb), [`createseqfiledb`](#depcmd-createseqfiledb), [`createtsv`](#depcmd-createtsv), [`result2flat`](#depcmd-result2flat), [`result2repseq`](#depcmd-result2repseq), [`rmdb`](#depcmd-rmdb) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-easy-cluster) |
| Functional module entry | [Open module page](#modcmd-easy-cluster) |

### `easy-linclust` {#depcmd-easy-linclust}

Fast linear time cluster, less sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`createdb`](#depcmd-createdb), [`createseqfiledb`](#depcmd-createseqfiledb), [`createtsv`](#depcmd-createtsv), [`linclust`](#depcmd-linclust), [`result2flat`](#depcmd-result2flat), [`result2repseq`](#depcmd-result2repseq), [`rmdb`](#depcmd-rmdb) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-easy-linclust) |
| Functional module entry | [Open module page](#modcmd-easy-linclust) |

### `easy-linsearch` {#depcmd-easy-linsearch}

Fast, less sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY | COMMAND_EXPERT` |
| Calls | [`convertalis`](#depcmd-convertalis), [`createdb`](#depcmd-createdb), [`createlinindex`](#depcmd-createlinindex), [`linsearch`](#depcmd-linsearch), [`rmdb`](#depcmd-rmdb), [`search`](#depcmd-search), [`summarizeresult`](#depcmd-summarizeresult) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-easy-linsearch) |
| Functional module entry | [Open module page](#modcmd-easy-linsearch) |

### `easy-rbh` {#depcmd-easy-rbh}

Find reciprocal best hit.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`convertalis`](#depcmd-convertalis), [`createdb`](#depcmd-createdb), [`rbh`](#depcmd-rbh), [`rmdb`](#depcmd-rmdb) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-easy-rbh) |
| Functional module entry | [Open module page](#modcmd-easy-rbh) |

### `easy-search` {#depcmd-easy-search}

Sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`convertalis`](#depcmd-convertalis), [`createdb`](#depcmd-createdb), [`createlinindex`](#depcmd-createlinindex), [`linsearch`](#depcmd-linsearch), [`rmdb`](#depcmd-rmdb), [`search`](#depcmd-search), [`summarizeresult`](#depcmd-summarizeresult) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-easy-search) |
| Functional module entry | [Open module page](#modcmd-easy-search) |

### `easy-taxonomy` {#depcmd-easy-taxonomy}

Taxonomic classification.

| Aspect | Value |
| :--- | :--- |
| Layer | `workflow` |
| Category flags | `COMMAND_EASY` |
| Calls | [`addtaxonomy`](#depcmd-addtaxonomy), [`convertalis`](#depcmd-convertalis), [`createdb`](#depcmd-createdb), [`createtsv`](#depcmd-createtsv), [`filterdb`](#depcmd-filterdb), [`lca`](#depcmd-lca), [`rmdb`](#depcmd-rmdb), [`summarizealis`](#depcmd-summarizealis), [`swapresults`](#depcmd-swapresults), [`taxonomy`](#depcmd-taxonomy), [`taxonomyreport`](#depcmd-taxonomyreport) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-easy-taxonomy) |
| Functional module entry | [Open module page](#modcmd-easy-taxonomy) |

## Search Workflows {#depgroup-search-workflows}

### `linsearch` {#depcmd-linsearch}

Fast, less sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN|COMMAND_EXPERT` |
| Calls | [`align`](#depcmd-align), [`concatdbs`](#depcmd-concatdbs), [`extractorfs`](#depcmd-extractorfs), [`filterdb`](#depcmd-filterdb), [`kmersearch`](#depcmd-kmersearch), [`offsetalignment`](#depcmd-offsetalignment), [`rescorediagonal`](#depcmd-rescorediagonal), [`rmdb`](#depcmd-rmdb), [`swapresults`](#depcmd-swapresults) |
| Called by | [`easy-linsearch`](#depcmd-easy-linsearch), [`easy-search`](#depcmd-easy-search) |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-linsearch) |
| Functional module entry | [Open module page](#modcmd-linsearch) |

### `map` {#depcmd-map}

Map nearly identical sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`search`](#depcmd-search) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-map) |
| Functional module entry | [Open module page](#modcmd-map) |

### `rbh` {#depcmd-rbh}

Reciprocal best hit search.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`filterdb`](#depcmd-filterdb), [`mergedbs`](#depcmd-mergedbs), [`result2rbh`](#depcmd-result2rbh), [`rmdb`](#depcmd-rmdb), [`search`](#depcmd-search), [`swapresults`](#depcmd-swapresults) |
| Called by | [`easy-rbh`](#depcmd-easy-rbh) |
| Workflow scripts | `easyrbh.sh` |
| Command reference | [Open page](#refcmd-rbh) |
| Functional module entry | [Open module page](#modcmd-rbh) |

### `search` {#depcmd-search}

Sensitive homology search.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`align`](#depcmd-align), [`createsubdb`](#depcmd-createsubdb), [`expand2profile`](#depcmd-expand2profile), [`expandaln`](#depcmd-expandaln), [`extractframes`](#depcmd-extractframes), [`extractorfs`](#depcmd-extractorfs), [`filterresult`](#depcmd-filterresult), [`lcaalign`](#depcmd-lcaalign), [`mergedbs`](#depcmd-mergedbs), [`mvdb`](#depcmd-mvdb), [`offsetalignment`](#depcmd-offsetalignment), [`prefilter`](#depcmd-prefilter), [`profile2consensus`](#depcmd-profile2consensus), [`rescorediagonal`](#depcmd-rescorediagonal), [`result2profile`](#depcmd-result2profile), [`result2stats`](#depcmd-result2stats), [`rmdb`](#depcmd-rmdb), [`search`](#depcmd-search), [`splitsequence`](#depcmd-splitsequence), [`subtractdbs`](#depcmd-subtractdbs), [`swapresults`](#depcmd-swapresults), [`ungappedprefilter`](#depcmd-ungappedprefilter) |
| Called by | [`clusterupdate`](#depcmd-clusterupdate), [`easy-linsearch`](#depcmd-easy-linsearch), [`easy-search`](#depcmd-easy-search), [`map`](#depcmd-map), [`multihitsearch`](#depcmd-multihitsearch), [`rbh`](#depcmd-rbh), [`search`](#depcmd-search), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `enrich.sh`, `iterativepp.sh`, `map.sh`, `multihitsearch.sh`, `rbh.sh`, `taxonomy.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-search) |
| Functional module entry | [Open module page](#modcmd-search) |

## Clustering {#depgroup-clustering}

### `clust` {#depcmd-clust}

Cluster result by Set-Cover/Connected-Component/Greedy-Incremental.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`linclust`](#depcmd-linclust) |
| Workflow scripts | `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh` |
| Command reference | [Open page](#refcmd-clust) |
| Functional module entry | [Open module page](#modcmd-clust) |

### `cluster` {#depcmd-cluster}

Slower, sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`align`](#depcmd-align), [`clust`](#depcmd-clust), [`clusthash`](#depcmd-clusthash), [`concatdbs`](#depcmd-concatdbs), [`createsubdb`](#depcmd-createsubdb), [`extractframes`](#depcmd-extractframes), [`filterdb`](#depcmd-filterdb), [`linclust`](#depcmd-linclust), [`mergeclusters`](#depcmd-mergeclusters), [`mergedbs`](#depcmd-mergedbs), [`mvdb`](#depcmd-mvdb), [`offsetalignment`](#depcmd-offsetalignment), [`prefilter`](#depcmd-prefilter), [`rescorediagonal`](#depcmd-rescorediagonal), [`rmdb`](#depcmd-rmdb), [`subtractdbs`](#depcmd-subtractdbs), [`swapdb`](#depcmd-swapdb), [`tsv2db`](#depcmd-tsv2db) |
| Called by | [`clusterupdate`](#depcmd-clusterupdate), [`easy-cluster`](#depcmd-easy-cluster) |
| Workflow scripts | `update_clustering.sh` |
| Command reference | [Open page](#refcmd-cluster) |
| Functional module entry | [Open module page](#modcmd-cluster) |

### `clusterupdate` {#depcmd-clusterupdate}

Update previous clustering with new sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`cluster`](#depcmd-cluster), [`concatdbs`](#depcmd-concatdbs), [`createsubdb`](#depcmd-createsubdb), [`diffseqdbs`](#depcmd-diffseqdbs), [`filterdb`](#depcmd-filterdb), [`mergedbs`](#depcmd-mergedbs), [`mvdb`](#depcmd-mvdb), [`prefixid`](#depcmd-prefixid), [`renamedbkeys`](#depcmd-renamedbkeys), [`result2repseq`](#depcmd-result2repseq), [`rmdb`](#depcmd-rmdb), [`search`](#depcmd-search), [`swapdb`](#depcmd-swapdb) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-clusterupdate) |
| Functional module entry | [Open module page](#modcmd-clusterupdate) |

### `clusthash` {#depcmd-clusthash}

Hash-based clustering of equal length sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster) |
| Workflow scripts | `clustering.sh` |
| Command reference | [Open page](#refcmd-clusthash) |
| Functional module entry | [Open module page](#modcmd-clusthash) |

### `linclust` {#depcmd-linclust}

Fast, less sensitive clustering.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`align`](#depcmd-align), [`clust`](#depcmd-clust), [`createsubdb`](#depcmd-createsubdb), [`filterdb`](#depcmd-filterdb), [`kmermatcher`](#depcmd-kmermatcher), [`mergeclusters`](#depcmd-mergeclusters), [`rescorediagonal`](#depcmd-rescorediagonal), [`rmdb`](#depcmd-rmdb) |
| Called by | [`cluster`](#depcmd-cluster), [`easy-linclust`](#depcmd-easy-linclust) |
| Workflow scripts | `cascaded_clustering.sh`, `nucleotide_clustering.sh` |
| Command reference | [Open page](#refcmd-linclust) |
| Functional module entry | [Open module page](#modcmd-linclust) |

### `mergeclusters` {#depcmd-mergeclusters}

Merge multiple cascaded clustering steps.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`linclust`](#depcmd-linclust) |
| Workflow scripts | `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh` |
| Command reference | [Open page](#refcmd-mergeclusters) |
| Functional module entry | [Open module page](#modcmd-mergeclusters) |

### `pickconsensusrep` {#depcmd-pickconsensusrep}

Select new representatives for each cluster based on consensus.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_CLUSTER` |
| Calls | [`align`](#depcmd-align), [`msa2profile`](#depcmd-msa2profile), [`prefixid`](#depcmd-prefixid), [`renamedbkeys`](#depcmd-renamedbkeys), [`result2msa`](#depcmd-result2msa), [`rmdb`](#depcmd-rmdb), [`tsv2db`](#depcmd-tsv2db) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-pickconsensusrep) |
| Functional module entry | [Open module page](#modcmd-pickconsensusrep) |

## Prefiltering {#depgroup-prefiltering}

### `countkmer` {#depcmd-countkmer}

Count k-mers.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-countkmer) |
| Functional module entry | [Open module page](#modcmd-countkmer) |

### `gappedprefilter` {#depcmd-gappedprefilter}

Optimal Smith-Waterman-based prefiltering (slow).

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-gappedprefilter) |
| Functional module entry | [Open module page](#modcmd-gappedprefilter) |

### `kmermatcher` {#depcmd-kmermatcher}

Find bottom-m-hashed k-mer matches within sequence DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | [`linclust`](#depcmd-linclust) |
| Workflow scripts | `linclust.sh` |
| Command reference | [Open page](#refcmd-kmermatcher) |
| Functional module entry | [Open module page](#modcmd-kmermatcher) |

### `kmersearch` {#depcmd-kmersearch}

Find bottom-m-hashed k-mer matches between target and query DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | [`linsearch`](#depcmd-linsearch) |
| Workflow scripts | `linsearch.sh` |
| Command reference | [Open page](#refcmd-kmersearch) |
| Functional module entry | [Open module page](#modcmd-kmersearch) |

### `prefilter` {#depcmd-prefilter}

Double consecutive diagonal k-mer search.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`search`](#depcmd-search), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `enrich.sh`, `iterativepp.sh`, `nucleotide_clustering.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh`, `taxpercontig.sh`, `translated_search.sh` |
| Command reference | [Open page](#refcmd-prefilter) |
| Functional module entry | [Open module page](#modcmd-prefilter) |

### `ungappedprefilter` {#depcmd-ungappedprefilter}

Optimal diagonal score search.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PREFILTER` |
| Calls | `n/a` |
| Called by | [`search`](#depcmd-search) |
| Workflow scripts | `blastp.sh`, `blastpgp.sh` |
| Command reference | [Open page](#refcmd-ungappedprefilter) |
| Functional module entry | [Open module page](#modcmd-ungappedprefilter) |

## Alignment {#depgroup-alignment}

### `align` {#depcmd-align}

Optimal gapped local alignment.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`linclust`](#depcmd-linclust), [`linsearch`](#depcmd-linsearch), [`pickconsensusrep`](#depcmd-pickconsensusrep), [`search`](#depcmd-search) |
| Workflow scripts | `iterativepp.sh`, `nucleotide_clustering.sh`, `pickconsensusrep.sh`, `searchslicedtargetprofile.sh` |
| Command reference | [Open page](#refcmd-align) |
| Functional module entry | [Open module page](#modcmd-align) |

### `alignall` {#depcmd-alignall}

Within-result all-vs-all gapped local alignment.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-alignall) |
| Functional module entry | [Open module page](#modcmd-alignall) |

### `alignbykmer` {#depcmd-alignbykmer}

Heuristic gapped local k-mer based alignment.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-alignbykmer) |
| Functional module entry | [Open module page](#modcmd-alignbykmer) |

### `expandaln` {#depcmd-expandaln}

Expand an alignment result based on another.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Calls | `n/a` |
| Called by | [`search`](#depcmd-search) |
| Workflow scripts | `enrich.sh`, `iterativepp.sh` |
| Command reference | [Open page](#refcmd-expandaln) |
| Functional module entry | [Open module page](#modcmd-expandaln) |

### `fwbw` {#depcmd-fwbw}

Forward Backward Alignment.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-fwbw) |
| Functional module entry | [Open module page](#modcmd-fwbw) |

### `offsetalignment` {#depcmd-offsetalignment}

Offset alignment by ORF start position.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`linsearch`](#depcmd-linsearch), [`search`](#depcmd-search) |
| Workflow scripts | `blastn.sh`, `linsearch.sh`, `nucleotide_clustering.sh`, `translated_search.sh` |
| Command reference | [Open page](#refcmd-offsetalignment) |
| Functional module entry | [Open module page](#modcmd-offsetalignment) |

### `proteinaln2nucl` {#depcmd-proteinaln2nucl}

Transform protein alignments to nucleotide alignments.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-proteinaln2nucl) |
| Functional module entry | [Open module page](#modcmd-proteinaln2nucl) |

### `rescorediagonal` {#depcmd-rescorediagonal}

Compute sequence identity for diagonal.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`linclust`](#depcmd-linclust), [`linsearch`](#depcmd-linsearch), [`search`](#depcmd-search), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `linclust.sh`, `linsearch.sh`, `nucleotide_clustering.sh`, `taxpercontig.sh` |
| Command reference | [Open page](#refcmd-rescorediagonal) |
| Functional module entry | [Open module page](#modcmd-rescorediagonal) |

### `transitivealign` {#depcmd-transitivealign}

Transfer alignments via transitivity.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_ALIGNMENT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-transitivealign) |
| Functional module entry | [Open module page](#modcmd-transitivealign) |

## Profiles {#depgroup-profiles}

### `convertca3m` {#depcmd-convertca3m}

Convert a cA3M DB to a result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-convertca3m) |
| Functional module entry | [Open module page](#modcmd-convertca3m) |

### `convertmsa` {#depcmd-convertmsa}

Convert Stockholm/PFAM MSA file to a MSA DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Calls | `n/a` |
| Called by | [`databases`](#depcmd-databases) |
| Workflow scripts | `databases.sh` |
| Command reference | [Open page](#refcmd-convertmsa) |
| Functional module entry | [Open module page](#modcmd-convertmsa) |

### `convertprofiledb` {#depcmd-convertprofiledb}

Convert a HH-suite HHM DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-convertprofiledb) |
| Functional module entry | [Open module page](#modcmd-convertprofiledb) |

### `expand2profile` {#depcmd-expand2profile}

Expand an alignment result based on another and create a profile.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Calls | `n/a` |
| Called by | [`search`](#depcmd-search) |
| Workflow scripts | `iterativepp.sh` |
| Command reference | [Open page](#refcmd-expand2profile) |
| Functional module entry | [Open module page](#modcmd-expand2profile) |

### `msa2profile` {#depcmd-msa2profile}

Convert a MSA DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE | COMMAND_DATABASE_CREATION` |
| Calls | `n/a` |
| Called by | [`databases`](#depcmd-databases), [`pickconsensusrep`](#depcmd-pickconsensusrep) |
| Workflow scripts | `databases.sh`, `pickconsensusrep.sh` |
| Command reference | [Open page](#refcmd-msa2profile) |
| Functional module entry | [Open module page](#modcmd-msa2profile) |

### `msa2result` {#depcmd-msa2result}

Convert a MSA DB to a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-msa2result) |
| Functional module entry | [Open module page](#modcmd-msa2result) |

### `pairaln` {#depcmd-pairaln}

Pair sequences to match best protein A and B from a species.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-pairaln) |
| Functional module entry | [Open module page](#modcmd-pairaln) |

### `profile2consensus` {#depcmd-profile2consensus}

Extract consensus sequence DB from a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | [`search`](#depcmd-search) |
| Workflow scripts | `iterativepp.sh` |
| Command reference | [Open page](#refcmd-profile2consensus) |
| Functional module entry | [Open module page](#modcmd-profile2consensus) |

### `profile2neff` {#depcmd-profile2neff}

Convert a profile DB to a tab-separated list of Neff scores.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-profile2neff) |
| Functional module entry | [Open module page](#modcmd-profile2neff) |

### `profile2pssm` {#depcmd-profile2pssm}

Convert a profile DB to a tab-separated PSSM file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-profile2pssm) |
| Functional module entry | [Open module page](#modcmd-profile2pssm) |

### `profile2repseq` {#depcmd-profile2repseq}

Extract representative sequence DB from a profile DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-profile2repseq) |
| Functional module entry | [Open module page](#modcmd-profile2repseq) |

### `result2profile` {#depcmd-result2profile}

Compute profile DB from a result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | [`search`](#depcmd-search) |
| Workflow scripts | `blastpgp.sh`, `enrich.sh` |
| Command reference | [Open page](#refcmd-result2profile) |
| Functional module entry | [Open module page](#modcmd-result2profile) |

### `sequence2profile` {#depcmd-sequence2profile}

Turn sequence into profile by adding context specific pseudo counts.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_PROFILE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-sequence2profile) |
| Functional module entry | [Open module page](#modcmd-sequence2profile) |

### `tsv2exprofiledb` {#depcmd-tsv2exprofiledb}

Create a expandable profile db from TSV files.

| Aspect | Value |
| :--- | :--- |
| Layer | `mid_level_api` |
| Category flags | `COMMAND_PROFILE_PROFILE` |
| Calls | [`aliasdb`](#depcmd-aliasdb), [`compress`](#depcmd-compress), [`mvdb`](#depcmd-mvdb), [`rmdb`](#depcmd-rmdb), [`tsv2db`](#depcmd-tsv2db) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-tsv2exprofiledb) |
| Functional module entry | [Open module page](#modcmd-tsv2exprofiledb) |

## Database {#depgroup-database}

### `aliasdb` {#depcmd-aliasdb}

Create relative symlink of DB to another name in the same folder.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | [`tsv2exprofiledb`](#depcmd-tsv2exprofiledb) |
| Workflow scripts | `tsv2exprofiledb.sh` |
| Command reference | [Open page](#refcmd-aliasdb) |
| Functional module entry | [Open module page](#modcmd-aliasdb) |

### `concatdbs` {#depcmd-concatdbs}

Concatenate two DBs, giving new IDs to entries from 2nd DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`clusterupdate`](#depcmd-clusterupdate), [`linsearch`](#depcmd-linsearch) |
| Workflow scripts | `linsearch.sh`, `nucleotide_clustering.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-concatdbs) |
| Functional module entry | [Open module page](#modcmd-concatdbs) |

### `cpdb` {#depcmd-cpdb}

Copy a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-cpdb) |
| Functional module entry | [Open module page](#modcmd-cpdb) |

### `createdb` {#depcmd-createdb}

Convert FASTA/Q file(s) to a sequence DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Calls | `n/a` |
| Called by | [`databases`](#depcmd-databases), [`easy-cluster`](#depcmd-easy-cluster), [`easy-linclust`](#depcmd-easy-linclust), [`easy-linsearch`](#depcmd-easy-linsearch), [`easy-rbh`](#depcmd-easy-rbh), [`easy-search`](#depcmd-easy-search), [`easy-taxonomy`](#depcmd-easy-taxonomy), [`multihitdb`](#depcmd-multihitdb) |
| Workflow scripts | `databases.sh`, `easycluster.sh`, `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh`, `multihitdb.sh` |
| Command reference | [Open page](#refcmd-createdb) |
| Functional module entry | [Open module page](#modcmd-createdb) |

### `createindex` {#depcmd-createindex}

Store precomputed index on disk to reduce search overhead.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Calls | [`extractframes`](#depcmd-extractframes), [`extractorfs`](#depcmd-extractorfs), [`rmdb`](#depcmd-rmdb), [`splitsequence`](#depcmd-splitsequence) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-createindex) |
| Functional module entry | [Open module page](#modcmd-createindex) |

### `createlinindex` {#depcmd-createlinindex}

Create linsearch index.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Calls | [`extractframes`](#depcmd-extractframes), [`extractorfs`](#depcmd-extractorfs), [`rmdb`](#depcmd-rmdb), [`splitsequence`](#depcmd-splitsequence) |
| Called by | [`easy-linsearch`](#depcmd-easy-linsearch), [`easy-search`](#depcmd-easy-search) |
| Workflow scripts | `easysearch.sh` |
| Command reference | [Open page](#refcmd-createlinindex) |
| Functional module entry | [Open module page](#modcmd-createlinindex) |

### `createsubdb` {#depcmd-createsubdb}

Create a subset of a DB from list of DB keys.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`clusterupdate`](#depcmd-clusterupdate), [`linclust`](#depcmd-linclust), [`search`](#depcmd-search), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `blastp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `linclust.sh`, `nucleotide_clustering.sh`, `taxpercontig.sh`, `translated_search.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-createsubdb) |
| Functional module entry | [Open module page](#modcmd-createsubdb) |

### `databases` {#depcmd-databases}

List and download databases.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION` |
| Calls | [`convertmsa`](#depcmd-convertmsa), [`createdb`](#depcmd-createdb), [`createtaxdb`](#depcmd-createtaxdb), [`msa2profile`](#depcmd-msa2profile), [`nrtotaxmapping`](#depcmd-nrtotaxmapping), [`prefixid`](#depcmd-prefixid), [`rmdb`](#depcmd-rmdb), [`tar2db`](#depcmd-tar2db) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-databases) |
| Functional module entry | [Open module page](#modcmd-databases) |

### `db2tar` {#depcmd-db2tar}

Archive contents of a DB to a tar archive.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-db2tar) |
| Functional module entry | [Open module page](#modcmd-db2tar) |

### `lndb` {#depcmd-lndb}

Symlink a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-lndb) |
| Functional module entry | [Open module page](#modcmd-lndb) |

### `mergedbs` {#depcmd-mergedbs}

Merge entries from multiple DBs.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`clusterupdate`](#depcmd-clusterupdate), [`rbh`](#depcmd-rbh), [`search`](#depcmd-search) |
| Workflow scripts | `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `enrich.sh`, `iterativepp.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-mergedbs) |
| Functional module entry | [Open module page](#modcmd-mergedbs) |

### `mvdb` {#depcmd-mvdb}

Move a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`clusterupdate`](#depcmd-clusterupdate), [`search`](#depcmd-search), [`taxonomy`](#depcmd-taxonomy), [`tsv2exprofiledb`](#depcmd-tsv2exprofiledb) |
| Workflow scripts | `blastp.sh`, `cascaded_clustering.sh`, `searchslicedtargetprofile.sh`, `taxonomy.sh`, `tsv2exprofiledb.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-mvdb) |
| Functional module entry | [Open module page](#modcmd-mvdb) |

### `renamedbkeys` {#depcmd-renamedbkeys}

Create a new DB with original keys renamed.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | [`clusterupdate`](#depcmd-clusterupdate), [`pickconsensusrep`](#depcmd-pickconsensusrep) |
| Workflow scripts | `update_clustering.sh` |
| Command reference | [Open page](#refcmd-renamedbkeys) |
| Functional module entry | [Open module page](#modcmd-renamedbkeys) |

### `rmdb` {#depcmd-rmdb}

Remove a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`clusterupdate`](#depcmd-clusterupdate), [`createindex`](#depcmd-createindex), [`createlinindex`](#depcmd-createlinindex), [`databases`](#depcmd-databases), [`easy-cluster`](#depcmd-easy-cluster), [`easy-linclust`](#depcmd-easy-linclust), [`easy-linsearch`](#depcmd-easy-linsearch), [`easy-rbh`](#depcmd-easy-rbh), [`easy-search`](#depcmd-easy-search), [`easy-taxonomy`](#depcmd-easy-taxonomy), [`linclust`](#depcmd-linclust), [`linsearch`](#depcmd-linsearch), [`multihitsearch`](#depcmd-multihitsearch), [`pickconsensusrep`](#depcmd-pickconsensusrep), [`rbh`](#depcmd-rbh), [`search`](#depcmd-search), [`taxonomy`](#depcmd-taxonomy), [`tsv2exprofiledb`](#depcmd-tsv2exprofiledb) |
| Workflow scripts | `blastn.sh`, `blastp.sh`, `blastpgp.sh`, `cascaded_clustering.sh`, `clustering.sh`, `createindex.sh`, `databases.sh`, `easycluster.sh`, `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh`, `iterativepp.sh`, `linclust.sh`, `linsearch.sh`, `multihitsearch.sh`, `nucleotide_clustering.sh`, `pickconsensusrep.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh`, `taxonomy.sh`, `taxpercontig.sh`, `translated_search.sh`, `tsv2exprofiledb.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-rmdb) |
| Functional module entry | [Open module page](#modcmd-rmdb) |

### `splitdb` {#depcmd-splitdb}

Split DB into subsets.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-splitdb) |
| Functional module entry | [Open module page](#modcmd-splitdb) |

### `splitsequence` {#depcmd-splitsequence}

Split sequences by length.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`createindex`](#depcmd-createindex), [`createlinindex`](#depcmd-createlinindex), [`search`](#depcmd-search) |
| Workflow scripts | `blastn.sh`, `createindex.sh` |
| Command reference | [Open page](#refcmd-splitsequence) |
| Functional module entry | [Open module page](#modcmd-splitsequence) |

### `subtractdbs` {#depcmd-subtractdbs}

Remove all entries from first DB occurring in second DB by key.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SET` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`search`](#depcmd-search) |
| Workflow scripts | `blastpgp.sh`, `cascaded_clustering.sh`, `enrich.sh`, `iterativepp.sh`, `nucleotide_clustering.sh` |
| Command reference | [Open page](#refcmd-subtractdbs) |
| Functional module entry | [Open module page](#modcmd-subtractdbs) |

### `swapdb` {#depcmd-swapdb}

Transpose DB with integer values in first column.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`clusterupdate`](#depcmd-clusterupdate), [`multihitdb`](#depcmd-multihitdb), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `cascaded_clustering.sh`, `multihitdb.sh`, `taxpercontig.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-swapdb) |
| Functional module entry | [Open module page](#modcmd-swapdb) |

### `tar2db` {#depcmd-tar2db}

Convert content of tar archives to any DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`databases`](#depcmd-databases) |
| Workflow scripts | `databases.sh` |
| Command reference | [Open page](#refcmd-tar2db) |
| Functional module entry | [Open module page](#modcmd-tar2db) |

### `tsv2db` {#depcmd-tsv2db}

Convert a TSV file to any DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DATABASE_CREATION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`multihitdb`](#depcmd-multihitdb), [`pickconsensusrep`](#depcmd-pickconsensusrep), [`tsv2exprofiledb`](#depcmd-tsv2exprofiledb) |
| Workflow scripts | `cascaded_clustering.sh`, `multihitdb.sh`, `pickconsensusrep.sh`, `tsv2exprofiledb.sh` |
| Command reference | [Open page](#refcmd-tsv2db) |
| Functional module entry | [Open module page](#modcmd-tsv2db) |

## Result Handling {#depgroup-result-handling}

### `convert2fasta` {#depcmd-convert2fasta}

Convert sequence DB to FASTA format.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-convert2fasta) |
| Functional module entry | [Open module page](#modcmd-convert2fasta) |

### `convertalis` {#depcmd-convertalis}

Convert alignment DB to BLAST-tab, SAM or custom format.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Calls | `n/a` |
| Called by | [`easy-linsearch`](#depcmd-easy-linsearch), [`easy-rbh`](#depcmd-easy-rbh), [`easy-search`](#depcmd-easy-search), [`easy-taxonomy`](#depcmd-easy-taxonomy) |
| Workflow scripts | `easyrbh.sh`, `easysearch.sh`, `easytaxonomy.sh` |
| Command reference | [Open page](#refcmd-convertalis) |
| Functional module entry | [Open module page](#modcmd-convertalis) |

### `createseqfiledb` {#depcmd-createseqfiledb}

Create a DB of unaligned FASTA entries.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`easy-cluster`](#depcmd-easy-cluster), [`easy-linclust`](#depcmd-easy-linclust) |
| Workflow scripts | `easycluster.sh` |
| Command reference | [Open page](#refcmd-createseqfiledb) |
| Functional module entry | [Open module page](#modcmd-createseqfiledb) |

### `createtsv` {#depcmd-createtsv}

Convert result DB to tab-separated flat file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION` |
| Calls | `n/a` |
| Called by | [`easy-cluster`](#depcmd-easy-cluster), [`easy-linclust`](#depcmd-easy-linclust), [`easy-taxonomy`](#depcmd-easy-taxonomy) |
| Workflow scripts | `easycluster.sh`, `easytaxonomy.sh` |
| Command reference | [Open page](#refcmd-createtsv) |
| Functional module entry | [Open module page](#modcmd-createtsv) |

### `extractdomains` {#depcmd-extractdomains}

Extract highest scoring alignment regions for each sequence from BLAST-tab file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-extractdomains) |
| Functional module entry | [Open module page](#modcmd-extractdomains) |

### `filterresult` {#depcmd-filterresult}

Pairwise alignment result filter.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`search`](#depcmd-search) |
| Workflow scripts | `searchslicedtargetprofile.sh` |
| Command reference | [Open page](#refcmd-filterresult) |
| Functional module entry | [Open module page](#modcmd-filterresult) |

### `result2dnamsa` {#depcmd-result2dnamsa}

Compute MSA DB with out insertions in the query for DNA sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-result2dnamsa) |
| Functional module entry | [Open module page](#modcmd-result2dnamsa) |

### `result2flat` {#depcmd-result2flat}

Create flat file by adding FASTA headers to DB entries.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_FORMAT_CONVERSION | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`easy-cluster`](#depcmd-easy-cluster), [`easy-linclust`](#depcmd-easy-linclust) |
| Workflow scripts | `easycluster.sh` |
| Command reference | [Open page](#refcmd-result2flat) |
| Functional module entry | [Open module page](#modcmd-result2flat) |

### `result2msa` {#depcmd-result2msa}

Compute MSA DB from a result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`pickconsensusrep`](#depcmd-pickconsensusrep) |
| Workflow scripts | `pickconsensusrep.sh` |
| Command reference | [Open page](#refcmd-result2msa) |
| Functional module entry | [Open module page](#modcmd-result2msa) |

### `result2rbh` {#depcmd-result2rbh}

Filter a merged result DB to retain only reciprocal best hits.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`rbh`](#depcmd-rbh) |
| Workflow scripts | `rbh.sh` |
| Command reference | [Open page](#refcmd-result2rbh) |
| Functional module entry | [Open module page](#modcmd-result2rbh) |

### `result2repseq` {#depcmd-result2repseq}

Get representative sequences from result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`clusterupdate`](#depcmd-clusterupdate), [`easy-cluster`](#depcmd-easy-cluster), [`easy-linclust`](#depcmd-easy-linclust) |
| Workflow scripts | `easycluster.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-result2repseq) |
| Functional module entry | [Open module page](#modcmd-result2repseq) |

### `result2stats` {#depcmd-result2stats}

Compute statistics for each entry in a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`multihitdb`](#depcmd-multihitdb), [`search`](#depcmd-search) |
| Workflow scripts | `multihitdb.sh`, `searchslicedtargetprofile.sh` |
| Command reference | [Open page](#refcmd-result2stats) |
| Functional module entry | [Open module page](#modcmd-result2stats) |

### `sortresult` {#depcmd-sortresult}

Sort a result DB in the same order as the prefilter or align module.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-sortresult) |
| Functional module entry | [Open module page](#modcmd-sortresult) |

### `summarizealis` {#depcmd-summarizealis}

Summarize alignment result to one row (uniq. cov., cov., avg. seq. id.).

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](#depcmd-easy-taxonomy) |
| Workflow scripts | `easytaxonomy.sh` |
| Command reference | [Open page](#refcmd-summarizealis) |
| Functional module entry | [Open module page](#modcmd-summarizealis) |

### `summarizeheaders` {#depcmd-summarizeheaders}

Summarize FASTA headers of result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-summarizeheaders) |
| Functional module entry | [Open module page](#modcmd-summarizeheaders) |

### `summarizeresult` {#depcmd-summarizeresult}

Extract annotations from alignment DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`easy-linsearch`](#depcmd-easy-linsearch), [`easy-search`](#depcmd-easy-search) |
| Workflow scripts | `easysearch.sh` |
| Command reference | [Open page](#refcmd-summarizeresult) |
| Functional module entry | [Open module page](#modcmd-summarizeresult) |

### `swapresults` {#depcmd-swapresults}

Transpose prefilter/alignment DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_RESULT` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](#depcmd-easy-taxonomy), [`linsearch`](#depcmd-linsearch), [`rbh`](#depcmd-rbh), [`search`](#depcmd-search) |
| Workflow scripts | `easytaxonomy.sh`, `linsearch.sh`, `rbh.sh`, `searchslicedtargetprofile.sh`, `searchtargetprofile.sh` |
| Command reference | [Open page](#refcmd-swapresults) |
| Functional module entry | [Open module page](#modcmd-swapresults) |

## Sequence Manipulation {#depgroup-sequence-manipulation}

### `extractalignedregion` {#depcmd-extractalignedregion}

Extract aligned sequence region from query.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-extractalignedregion) |
| Functional module entry | [Open module page](#modcmd-extractalignedregion) |

### `extractframes` {#depcmd-extractframes}

Extract frames from a nucleotide sequence DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`createindex`](#depcmd-createindex), [`createlinindex`](#depcmd-createlinindex), [`search`](#depcmd-search) |
| Workflow scripts | `blastn.sh`, `createindex.sh`, `nucleotide_clustering.sh`, `translated_search.sh` |
| Command reference | [Open page](#refcmd-extractframes) |
| Functional module entry | [Open module page](#modcmd-extractframes) |

### `extractorfs` {#depcmd-extractorfs}

Six-frame extraction of open reading frames.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`createindex`](#depcmd-createindex), [`createlinindex`](#depcmd-createlinindex), [`linsearch`](#depcmd-linsearch), [`multihitdb`](#depcmd-multihitdb), [`search`](#depcmd-search), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `createindex.sh`, `multihitdb.sh`, `taxpercontig.sh`, `translated_search.sh` |
| Command reference | [Open page](#refcmd-extractorfs) |
| Functional module entry | [Open module page](#modcmd-extractorfs) |

### `masksequence` {#depcmd-masksequence}

Soft mask sequence DB using tantan.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-masksequence) |
| Functional module entry | [Open module page](#modcmd-masksequence) |

### `orftocontig` {#depcmd-orftocontig}

Write ORF locations in alignment format.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`multihitdb`](#depcmd-multihitdb) |
| Workflow scripts | `multihitdb.sh` |
| Command reference | [Open page](#refcmd-orftocontig) |
| Functional module entry | [Open module page](#modcmd-orftocontig) |

### `recoverlongestorf` {#depcmd-recoverlongestorf}

Recover longest ORF for taxonomy annotation after elimination.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `taxpercontig.sh` |
| Command reference | [Open page](#refcmd-recoverlongestorf) |
| Functional module entry | [Open module page](#modcmd-recoverlongestorf) |

### `reverseseq` {#depcmd-reverseseq}

Reverse (without complement) sequences.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-reverseseq) |
| Functional module entry | [Open module page](#modcmd-reverseseq) |

### `translateaa` {#depcmd-translateaa}

Translate proteins to lexicographically lowest codons.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-translateaa) |
| Functional module entry | [Open module page](#modcmd-translateaa) |

### `translatenucs` {#depcmd-translatenucs}

Translate nucleotides to proteins.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SEQUENCE` |
| Calls | `n/a` |
| Called by | [`multihitdb`](#depcmd-multihitdb) |
| Workflow scripts | `multihitdb.sh` |
| Command reference | [Open page](#refcmd-translatenucs) |
| Functional module entry | [Open module page](#modcmd-translatenucs) |

## Taxonomy {#depgroup-taxonomy}

### `addtaxonomy` {#depcmd-addtaxonomy}

Add taxonomic labels to result DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](#depcmd-easy-taxonomy) |
| Workflow scripts | `easytaxonomy.sh` |
| Command reference | [Open page](#refcmd-addtaxonomy) |
| Functional module entry | [Open module page](#modcmd-addtaxonomy) |

### `aggregatetax` {#depcmd-aggregatetax}

Aggregate multiple taxon labels to a single label.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-aggregatetax) |
| Functional module entry | [Open module page](#modcmd-aggregatetax) |

### `aggregatetaxweights` {#depcmd-aggregatetaxweights}

Aggregate multiple taxon labels to a single label.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `taxpercontig.sh` |
| Command reference | [Open page](#refcmd-aggregatetaxweights) |
| Functional module entry | [Open module page](#modcmd-aggregatetaxweights) |

### `createbintaxmapping` {#depcmd-createbintaxmapping}

Create binary taxonomy mapping from tabular taxonomy mapping.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-createbintaxmapping) |
| Functional module entry | [Open module page](#modcmd-createbintaxmapping) |

### `createbintaxonomy` {#depcmd-createbintaxonomy}

Create binary taxonomy from NCBI input.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | [`createtaxdb`](#depcmd-createtaxdb) |
| Workflow scripts | `createtaxdb.sh` |
| Command reference | [Open page](#refcmd-createbintaxonomy) |
| Functional module entry | [Open module page](#modcmd-createbintaxonomy) |

### `createdmptaxonomy` {#depcmd-createdmptaxonomy}

Create dmp files from binary taxonomy.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-createdmptaxonomy) |
| Functional module entry | [Open module page](#modcmd-createdmptaxonomy) |

### `createtaxdb` {#depcmd-createtaxdb}

Add taxonomic labels to sequence DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | [`createbintaxonomy`](#depcmd-createbintaxonomy) |
| Called by | [`databases`](#depcmd-databases) |
| Workflow scripts | `databases.sh` |
| Command reference | [Open page](#refcmd-createtaxdb) |
| Functional module entry | [Open module page](#modcmd-createtaxdb) |

### `filtertaxdb` {#depcmd-filtertaxdb}

Filter taxonomy result database.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-filtertaxdb) |
| Functional module entry | [Open module page](#modcmd-filtertaxdb) |

### `filtertaxseqdb` {#depcmd-filtertaxseqdb}

Filter taxonomy sequence database.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-filtertaxseqdb) |
| Functional module entry | [Open module page](#modcmd-filtertaxseqdb) |

### `lca` {#depcmd-lca}

Compute the lowest common ancestor.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](#depcmd-easy-taxonomy), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `taxonomy.sh` |
| Command reference | [Open page](#refcmd-lca) |
| Functional module entry | [Open module page](#modcmd-lca) |

### `lcaalign` {#depcmd-lcaalign}

Efficient gapped alignment for lca computation.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY` |
| Calls | `n/a` |
| Called by | [`search`](#depcmd-search) |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-lcaalign) |
| Functional module entry | [Open module page](#modcmd-lcaalign) |

### `majoritylca` {#depcmd-majoritylca}

Compute the lowest common ancestor using majority voting.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_EXPERT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-majoritylca) |
| Functional module entry | [Open module page](#modcmd-majoritylca) |

### `nrtotaxmapping` {#depcmd-nrtotaxmapping}

Create taxonomy mapping for NR database.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | [`databases`](#depcmd-databases) |
| Workflow scripts | `databases.sh` |
| Command reference | [Open page](#refcmd-nrtotaxmapping) |
| Functional module entry | [Open module page](#modcmd-nrtotaxmapping) |

### `taxonomy` {#depcmd-taxonomy}

Taxonomic classification.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MAIN` |
| Calls | [`aggregatetax`](#depcmd-aggregatetax), [`aggregatetaxweights`](#depcmd-aggregatetaxweights), [`createsubdb`](#depcmd-createsubdb), [`extractorfs`](#depcmd-extractorfs), [`filterdb`](#depcmd-filterdb), [`lca`](#depcmd-lca), [`mergeresultsbyset`](#depcmd-mergeresultsbyset), [`mvdb`](#depcmd-mvdb), [`prefilter`](#depcmd-prefilter), [`recoverlongestorf`](#depcmd-recoverlongestorf), [`rescorediagonal`](#depcmd-rescorediagonal), [`rmdb`](#depcmd-rmdb), [`search`](#depcmd-search), [`swapdb`](#depcmd-swapdb), [`taxonomy`](#depcmd-taxonomy) |
| Called by | [`easy-taxonomy`](#depcmd-easy-taxonomy), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `easytaxonomy.sh`, `taxpercontig.sh` |
| Command reference | [Open page](#refcmd-taxonomy) |
| Functional module entry | [Open module page](#modcmd-taxonomy) |

### `taxonomyreport` {#depcmd-taxonomyreport}

Create a taxonomy report in Kraken or Krona format.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_TAXONOMY | COMMAND_FORMAT_CONVERSION` |
| Calls | `n/a` |
| Called by | [`easy-taxonomy`](#depcmd-easy-taxonomy) |
| Workflow scripts | `easytaxonomy.sh` |
| Command reference | [Open page](#refcmd-taxonomyreport) |
| Functional module entry | [Open module page](#modcmd-taxonomyreport) |

## Multi Hit {#depgroup-multi-hit}

### `besthitperset` {#depcmd-besthitperset}

For each set of sequences compute the best element and update p-value.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | `n/a` |
| Called by | [`multihitsearch`](#depcmd-multihitsearch) |
| Workflow scripts | `multihitsearch.sh` |
| Command reference | [Open page](#refcmd-besthitperset) |
| Functional module entry | [Open module page](#modcmd-besthitperset) |

### `combinepvalperset` {#depcmd-combinepvalperset}

For each set compute the combined p-value.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-combinepvalperset) |
| Functional module entry | [Open module page](#modcmd-combinepvalperset) |

### `mergeresultsbyset` {#depcmd-mergeresultsbyset}

Merge results from multiple ORFs back to their respective contig.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | `n/a` |
| Called by | [`multihitsearch`](#depcmd-multihitsearch), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `multihitsearch.sh`, `taxpercontig.sh` |
| Command reference | [Open page](#refcmd-mergeresultsbyset) |
| Functional module entry | [Open module page](#modcmd-mergeresultsbyset) |

### `multihitdb` {#depcmd-multihitdb}

Create sequence DB for multi hit searches.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | [`createdb`](#depcmd-createdb), [`extractorfs`](#depcmd-extractorfs), [`filterdb`](#depcmd-filterdb), [`orftocontig`](#depcmd-orftocontig), [`result2stats`](#depcmd-result2stats), [`swapdb`](#depcmd-swapdb), [`translatenucs`](#depcmd-translatenucs), [`tsv2db`](#depcmd-tsv2db) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-multihitdb) |
| Functional module entry | [Open module page](#modcmd-multihitdb) |

### `multihitsearch` {#depcmd-multihitsearch}

Search with a grouped set of sequences against another grouped set.

| Aspect | Value |
| :--- | :--- |
| Layer | `high_level_api` |
| Category flags | `COMMAND_MULTIHIT` |
| Calls | [`besthitperset`](#depcmd-besthitperset), [`mergeresultsbyset`](#depcmd-mergeresultsbyset), [`rmdb`](#depcmd-rmdb), [`search`](#depcmd-search) |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-multihitsearch) |
| Functional module entry | [Open module page](#modcmd-multihitsearch) |

## Utilities {#depgroup-utilities}

### `apply` {#depcmd-apply}

Execute given program on each DB entry.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-apply) |
| Functional module entry | [Open module page](#modcmd-apply) |

### `compress` {#depcmd-compress}

Compress DB entries.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | [`tsv2exprofiledb`](#depcmd-tsv2exprofiledb) |
| Workflow scripts | `tsv2exprofiledb.sh` |
| Command reference | [Open page](#refcmd-compress) |
| Functional module entry | [Open module page](#modcmd-compress) |

### `convertkb` {#depcmd-convertkb}

Convert UniProtKB data to a DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-convertkb) |
| Functional module entry | [Open module page](#modcmd-convertkb) |

### `decompress` {#depcmd-decompress}

Decompress DB entries.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-decompress) |
| Functional module entry | [Open module page](#modcmd-decompress) |

### `diffseqdbs` {#depcmd-diffseqdbs}

Compute diff of two sequence DBs.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | [`clusterupdate`](#depcmd-clusterupdate) |
| Workflow scripts | `update_clustering.sh` |
| Command reference | [Open page](#refcmd-diffseqdbs) |
| Functional module entry | [Open module page](#modcmd-diffseqdbs) |

### `filterdb` {#depcmd-filterdb}

DB filtering by given conditions.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | [`cluster`](#depcmd-cluster), [`clusterupdate`](#depcmd-clusterupdate), [`easy-taxonomy`](#depcmd-easy-taxonomy), [`linclust`](#depcmd-linclust), [`linsearch`](#depcmd-linsearch), [`multihitdb`](#depcmd-multihitdb), [`rbh`](#depcmd-rbh), [`taxonomy`](#depcmd-taxonomy) |
| Workflow scripts | `cascaded_clustering.sh`, `easytaxonomy.sh`, `linclust.sh`, `linsearch.sh`, `multihitdb.sh`, `rbh.sh`, `taxonomy.sh`, `taxpercontig.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-filterdb) |
| Functional module entry | [Open module page](#modcmd-filterdb) |

### `gff2db` {#depcmd-gff2db}

Extract regions from a sequence database based on a GFF3 file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-gff2db) |
| Functional module entry | [Open module page](#modcmd-gff2db) |

### `gpuserver` {#depcmd-gpuserver}

Start a GPU server.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-gpuserver) |
| Functional module entry | [Open module page](#modcmd-gpuserver) |

### `maskbygff` {#depcmd-maskbygff}

Mask out sequence regions in a sequence DB by features selected from a GFF3 file.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-maskbygff) |
| Functional module entry | [Open module page](#modcmd-maskbygff) |

### `prefixid` {#depcmd-prefixid}

For each entry in a DB prepend the entry key to the entry itself.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | [`clusterupdate`](#depcmd-clusterupdate), [`databases`](#depcmd-databases), [`pickconsensusrep`](#depcmd-pickconsensusrep) |
| Workflow scripts | `databases.sh`, `pickconsensusrep.sh`, `update_clustering.sh` |
| Command reference | [Open page](#refcmd-prefixid) |
| Functional module entry | [Open module page](#modcmd-prefixid) |

### `setextendeddbtype` {#depcmd-setextendeddbtype}

Write an extended DB.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-setextendeddbtype) |
| Functional module entry | [Open module page](#modcmd-setextendeddbtype) |

### `suffixid` {#depcmd-suffixid}

For each entry in a DB append the entry key to the entry itself.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-suffixid) |
| Functional module entry | [Open module page](#modcmd-suffixid) |

### `summarizetabs` {#depcmd-summarizetabs}

Extract annotations from HHblits BLAST-tab-formatted results.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_SPECIAL` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-summarizetabs) |
| Functional module entry | [Open module page](#modcmd-summarizetabs) |

### `touchdb` {#depcmd-touchdb}

Preload DB into memory (page cache).

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-touchdb) |
| Functional module entry | [Open module page](#modcmd-touchdb) |

### `unpackdb` {#depcmd-unpackdb}

Unpack a DB into separate files.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_STORAGE` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-unpackdb) |
| Functional module entry | [Open module page](#modcmd-unpackdb) |

### `view` {#depcmd-view}

Print DB entries given in --id-list to stdout.

| Aspect | Value |
| :--- | :--- |
| Layer | `low_level_api` |
| Category flags | `COMMAND_DB` |
| Calls | `n/a` |
| Called by | `n/a` |
| Workflow scripts | `n/a` |
| Command reference | [Open page](#refcmd-view) |
| Functional module entry | [Open module page](#modcmd-view) |

