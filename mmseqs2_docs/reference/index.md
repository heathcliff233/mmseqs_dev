# MMseqs2 Command Reference Index {#sec-command-reference}

This reference is generated from source metadata and local help snapshots.

| Metric | Value |
| :--- | :--- |
| Total visible commands | `128` |
| Commands with help snapshots | `97` |
| Commands missing snapshots | `31` |

```{=typst}
#doc_warning[
Some visible commands do not have local help snapshots. Use `generate_mmseqs_docs.sh` to refresh before publishing final CLI defaults.
]
```

| Command | Snapshot status |
| :--- | :--- |
| `addtaxonomy` | missing |
| `aggregatetax` | missing |
| `aggregatetaxweights` | missing |
| `convert2fasta` | missing |
| `convertca3m` | missing |
| `convertkb` | missing |
| `convertprofiledb` | missing |
| `countkmer` | missing |
| `createbintaxmapping` | missing |
| `createbintaxonomy` | missing |
| `createdmptaxonomy` | missing |
| `databases` | missing |
| `diffseqdbs` | missing |
| `expand2profile` | missing |
| `extractdomains` | missing |
| `fwbw` | missing |
| `gff2db` | missing |
| `majoritylca` | missing |
| `maskbygff` | missing |
| `nrtotaxmapping` | missing |
| `pairaln` | missing |
| `pickconsensusrep` | missing |
| `profile2consensus` | missing |
| `profile2neff` | missing |
| `profile2pssm` | missing |
| `profile2repseq` | missing |
| `rmdb` | missing |
| `sequence2profile` | missing |
| `summarizeheaders` | missing |
| `summarizetabs` | missing |
| `transitivealign` | missing |

Primary maps: [Dependency map](#sec-dependency-map).

## Easy Workflows {#refgroup-easy-workflows}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`easy-cluster`](#refcmd-easy-cluster) | `workflow` | `help` |
| [`easy-linclust`](#refcmd-easy-linclust) | `workflow` | `help` |
| [`easy-linsearch`](#refcmd-easy-linsearch) | `workflow` | `help` |
| [`easy-rbh`](#refcmd-easy-rbh) | `workflow` | `help` |
| [`easy-search`](#refcmd-easy-search) | `workflow` | `help` |
| [`easy-taxonomy`](#refcmd-easy-taxonomy) | `workflow` | `help` |

## Search Workflows {#refgroup-search-workflows}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`linsearch`](#refcmd-linsearch) | `high_level_api` | `help` |
| [`map`](#refcmd-map) | `high_level_api` | `help` |
| [`rbh`](#refcmd-rbh) | `high_level_api` | `help` |
| [`search`](#refcmd-search) | `high_level_api` | `help` |

## Clustering {#refgroup-clustering}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`clust`](#refcmd-clust) | `mid_level_api` | `help` |
| [`cluster`](#refcmd-cluster) | `high_level_api` | `help` |
| [`clusterupdate`](#refcmd-clusterupdate) | `high_level_api` | `help` |
| [`clusthash`](#refcmd-clusthash) | `mid_level_api` | `help` |
| [`linclust`](#refcmd-linclust) | `high_level_api` | `help` |
| [`mergeclusters`](#refcmd-mergeclusters) | `mid_level_api` | `help` |
| [`pickconsensusrep`](#refcmd-pickconsensusrep) | `mid_level_api` | `missing-help` |

## Prefiltering {#refgroup-prefiltering}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`countkmer`](#refcmd-countkmer) | `low_level_api` | `missing-help` |
| [`gappedprefilter`](#refcmd-gappedprefilter) | `mid_level_api` | `help` |
| [`kmermatcher`](#refcmd-kmermatcher) | `mid_level_api` | `help` |
| [`kmersearch`](#refcmd-kmersearch) | `mid_level_api` | `help` |
| [`prefilter`](#refcmd-prefilter) | `mid_level_api` | `help` |
| [`ungappedprefilter`](#refcmd-ungappedprefilter) | `mid_level_api` | `help` |

## Alignment {#refgroup-alignment}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`align`](#refcmd-align) | `mid_level_api` | `help` |
| [`alignall`](#refcmd-alignall) | `mid_level_api` | `help` |
| [`alignbykmer`](#refcmd-alignbykmer) | `mid_level_api` | `help` |
| [`expandaln`](#refcmd-expandaln) | `mid_level_api` | `help` |
| [`fwbw`](#refcmd-fwbw) | `mid_level_api` | `missing-help` |
| [`offsetalignment`](#refcmd-offsetalignment) | `low_level_api` | `help` |
| [`proteinaln2nucl`](#refcmd-proteinaln2nucl) | `low_level_api` | `help` |
| [`rescorediagonal`](#refcmd-rescorediagonal) | `mid_level_api` | `help` |
| [`transitivealign`](#refcmd-transitivealign) | `mid_level_api` | `missing-help` |

## Profiles {#refgroup-profiles}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`convertca3m`](#refcmd-convertca3m) | `mid_level_api` | `missing-help` |
| [`convertmsa`](#refcmd-convertmsa) | `low_level_api` | `help` |
| [`convertprofiledb`](#refcmd-convertprofiledb) | `low_level_api` | `missing-help` |
| [`expand2profile`](#refcmd-expand2profile) | `mid_level_api` | `missing-help` |
| [`msa2profile`](#refcmd-msa2profile) | `low_level_api` | `help` |
| [`msa2result`](#refcmd-msa2result) | `low_level_api` | `help` |
| [`pairaln`](#refcmd-pairaln) | `low_level_api` | `missing-help` |
| [`profile2consensus`](#refcmd-profile2consensus) | `low_level_api` | `missing-help` |
| [`profile2neff`](#refcmd-profile2neff) | `low_level_api` | `missing-help` |
| [`profile2pssm`](#refcmd-profile2pssm) | `low_level_api` | `missing-help` |
| [`profile2repseq`](#refcmd-profile2repseq) | `low_level_api` | `missing-help` |
| [`result2profile`](#refcmd-result2profile) | `low_level_api` | `help` |
| [`sequence2profile`](#refcmd-sequence2profile) | `low_level_api` | `missing-help` |
| [`tsv2exprofiledb`](#refcmd-tsv2exprofiledb) | `mid_level_api` | `help` |

## Database {#refgroup-database}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`aliasdb`](#refcmd-aliasdb) | `low_level_api` | `help` |
| [`concatdbs`](#refcmd-concatdbs) | `low_level_api` | `help` |
| [`cpdb`](#refcmd-cpdb) | `low_level_api` | `help` |
| [`createdb`](#refcmd-createdb) | `low_level_api` | `help` |
| [`createindex`](#refcmd-createindex) | `low_level_api` | `help` |
| [`createlinindex`](#refcmd-createlinindex) | `low_level_api` | `help` |
| [`createsubdb`](#refcmd-createsubdb) | `low_level_api` | `help` |
| [`databases`](#refcmd-databases) | `low_level_api` | `missing-help` |
| [`db2tar`](#refcmd-db2tar) | `low_level_api` | `help` |
| [`lndb`](#refcmd-lndb) | `low_level_api` | `help` |
| [`mergedbs`](#refcmd-mergedbs) | `low_level_api` | `help` |
| [`mvdb`](#refcmd-mvdb) | `low_level_api` | `help` |
| [`renamedbkeys`](#refcmd-renamedbkeys) | `low_level_api` | `help` |
| [`rmdb`](#refcmd-rmdb) | `low_level_api` | `missing-help` |
| [`splitdb`](#refcmd-splitdb) | `low_level_api` | `help` |
| [`splitsequence`](#refcmd-splitsequence) | `low_level_api` | `help` |
| [`subtractdbs`](#refcmd-subtractdbs) | `low_level_api` | `help` |
| [`swapdb`](#refcmd-swapdb) | `low_level_api` | `help` |
| [`tar2db`](#refcmd-tar2db) | `low_level_api` | `help` |
| [`tsv2db`](#refcmd-tsv2db) | `low_level_api` | `help` |

## Result Handling {#refgroup-result-handling}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`convert2fasta`](#refcmd-convert2fasta) | `low_level_api` | `missing-help` |
| [`convertalis`](#refcmd-convertalis) | `low_level_api` | `help` |
| [`createseqfiledb`](#refcmd-createseqfiledb) | `low_level_api` | `help` |
| [`createtsv`](#refcmd-createtsv) | `low_level_api` | `help` |
| [`extractdomains`](#refcmd-extractdomains) | `low_level_api` | `missing-help` |
| [`filterresult`](#refcmd-filterresult) | `low_level_api` | `help` |
| [`result2dnamsa`](#refcmd-result2dnamsa) | `low_level_api` | `help` |
| [`result2flat`](#refcmd-result2flat) | `low_level_api` | `help` |
| [`result2msa`](#refcmd-result2msa) | `low_level_api` | `help` |
| [`result2rbh`](#refcmd-result2rbh) | `low_level_api` | `help` |
| [`result2repseq`](#refcmd-result2repseq) | `low_level_api` | `help` |
| [`result2stats`](#refcmd-result2stats) | `low_level_api` | `help` |
| [`sortresult`](#refcmd-sortresult) | `low_level_api` | `help` |
| [`summarizealis`](#refcmd-summarizealis) | `low_level_api` | `help` |
| [`summarizeheaders`](#refcmd-summarizeheaders) | `low_level_api` | `missing-help` |
| [`summarizeresult`](#refcmd-summarizeresult) | `low_level_api` | `help` |
| [`swapresults`](#refcmd-swapresults) | `low_level_api` | `help` |

## Sequence Manipulation {#refgroup-sequence-manipulation}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`extractalignedregion`](#refcmd-extractalignedregion) | `low_level_api` | `help` |
| [`extractframes`](#refcmd-extractframes) | `low_level_api` | `help` |
| [`extractorfs`](#refcmd-extractorfs) | `low_level_api` | `help` |
| [`masksequence`](#refcmd-masksequence) | `low_level_api` | `help` |
| [`orftocontig`](#refcmd-orftocontig) | `low_level_api` | `help` |
| [`recoverlongestorf`](#refcmd-recoverlongestorf) | `low_level_api` | `help` |
| [`reverseseq`](#refcmd-reverseseq) | `low_level_api` | `help` |
| [`translateaa`](#refcmd-translateaa) | `low_level_api` | `help` |
| [`translatenucs`](#refcmd-translatenucs) | `low_level_api` | `help` |

## Taxonomy {#refgroup-taxonomy}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`addtaxonomy`](#refcmd-addtaxonomy) | `low_level_api` | `missing-help` |
| [`aggregatetax`](#refcmd-aggregatetax) | `low_level_api` | `missing-help` |
| [`aggregatetaxweights`](#refcmd-aggregatetaxweights) | `low_level_api` | `missing-help` |
| [`createbintaxmapping`](#refcmd-createbintaxmapping) | `low_level_api` | `missing-help` |
| [`createbintaxonomy`](#refcmd-createbintaxonomy) | `low_level_api` | `missing-help` |
| [`createdmptaxonomy`](#refcmd-createdmptaxonomy) | `low_level_api` | `missing-help` |
| [`createtaxdb`](#refcmd-createtaxdb) | `low_level_api` | `help` |
| [`filtertaxdb`](#refcmd-filtertaxdb) | `low_level_api` | `help` |
| [`filtertaxseqdb`](#refcmd-filtertaxseqdb) | `low_level_api` | `help` |
| [`lca`](#refcmd-lca) | `low_level_api` | `help` |
| [`lcaalign`](#refcmd-lcaalign) | `low_level_api` | `help` |
| [`majoritylca`](#refcmd-majoritylca) | `low_level_api` | `missing-help` |
| [`nrtotaxmapping`](#refcmd-nrtotaxmapping) | `low_level_api` | `missing-help` |
| [`taxonomy`](#refcmd-taxonomy) | `high_level_api` | `help` |
| [`taxonomyreport`](#refcmd-taxonomyreport) | `low_level_api` | `help` |

## Multi Hit {#refgroup-multi-hit}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`besthitperset`](#refcmd-besthitperset) | `high_level_api` | `help` |
| [`combinepvalperset`](#refcmd-combinepvalperset) | `high_level_api` | `help` |
| [`mergeresultsbyset`](#refcmd-mergeresultsbyset) | `high_level_api` | `help` |
| [`multihitdb`](#refcmd-multihitdb) | `high_level_api` | `help` |
| [`multihitsearch`](#refcmd-multihitsearch) | `high_level_api` | `help` |

## Utilities {#refgroup-utilities}

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`apply`](#refcmd-apply) | `low_level_api` | `help` |
| [`compress`](#refcmd-compress) | `low_level_api` | `help` |
| [`convertkb`](#refcmd-convertkb) | `low_level_api` | `missing-help` |
| [`decompress`](#refcmd-decompress) | `low_level_api` | `help` |
| [`diffseqdbs`](#refcmd-diffseqdbs) | `low_level_api` | `missing-help` |
| [`filterdb`](#refcmd-filterdb) | `low_level_api` | `help` |
| [`gff2db`](#refcmd-gff2db) | `low_level_api` | `missing-help` |
| [`gpuserver`](#refcmd-gpuserver) | `low_level_api` | `help` |
| [`maskbygff`](#refcmd-maskbygff) | `low_level_api` | `missing-help` |
| [`prefixid`](#refcmd-prefixid) | `low_level_api` | `help` |
| [`setextendeddbtype`](#refcmd-setextendeddbtype) | `low_level_api` | `help` |
| [`suffixid`](#refcmd-suffixid) | `low_level_api` | `help` |
| [`summarizetabs`](#refcmd-summarizetabs) | `low_level_api` | `missing-help` |
| [`touchdb`](#refcmd-touchdb) | `low_level_api` | `help` |
| [`unpackdb`](#refcmd-unpackdb) | `low_level_api` | `help` |
| [`view`](#refcmd-view) | `low_level_api` | `help` |

