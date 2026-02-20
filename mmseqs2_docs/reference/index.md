# MMseqs2 Command Reference Index {#sec-command-reference}

This index is generated from command metadata, dependency topology, and local CLI help snapshots where available. Use it to move quickly from command name to functional placement and detailed page content.

| Metric | Value |
| :--- | :--- |
| Total visible commands | `128` |
| Commands with help snapshots | `97` |
| Commands with source-derived fallback pages | `31` |

```{=typst}
#doc_note[
Some commands currently use source-derived fallback text because local help snapshots were not present in `mmseqs_help_output`.
]
```

| Command | Snapshot status |
| :--- | :--- |
| `addtaxonomy` | source-derived fallback |
| `aggregatetax` | source-derived fallback |
| `aggregatetaxweights` | source-derived fallback |
| `convert2fasta` | source-derived fallback |
| `convertca3m` | source-derived fallback |
| `convertkb` | source-derived fallback |
| `convertprofiledb` | source-derived fallback |
| `countkmer` | source-derived fallback |
| `createbintaxmapping` | source-derived fallback |
| `createbintaxonomy` | source-derived fallback |
| `createdmptaxonomy` | source-derived fallback |
| `databases` | source-derived fallback |
| `diffseqdbs` | source-derived fallback |
| `expand2profile` | source-derived fallback |
| `extractdomains` | source-derived fallback |
| `fwbw` | source-derived fallback |
| `gff2db` | source-derived fallback |
| `majoritylca` | source-derived fallback |
| `maskbygff` | source-derived fallback |
| `nrtotaxmapping` | source-derived fallback |
| `pairaln` | source-derived fallback |
| `pickconsensusrep` | source-derived fallback |
| `profile2consensus` | source-derived fallback |
| `profile2neff` | source-derived fallback |
| `profile2pssm` | source-derived fallback |
| `profile2repseq` | source-derived fallback |
| `rmdb` | source-derived fallback |
| `sequence2profile` | source-derived fallback |
| `summarizeheaders` | source-derived fallback |
| `summarizetabs` | source-derived fallback |
| `transitivealign` | source-derived fallback |

Primary topology view: [Dependency map](#sec-dependency-map).

## Command Group Map {#sec-command-group-map}

| Group | Command count | Commands |
| :--- | :--- | :--- |
| `easy_workflows` | `6` | [`easy-cluster`](#refcmd-easy-cluster), [`easy-linclust`](#refcmd-easy-linclust), [`easy-linsearch`](#refcmd-easy-linsearch), [`easy-rbh`](#refcmd-easy-rbh), [`easy-search`](#refcmd-easy-search), [`easy-taxonomy`](#refcmd-easy-taxonomy) |
| `search_workflows` | `4` | [`linsearch`](#refcmd-linsearch), [`map`](#refcmd-map), [`rbh`](#refcmd-rbh), [`search`](#refcmd-search) |
| `clustering` | `7` | [`clust`](#refcmd-clust), [`cluster`](#refcmd-cluster), [`clusterupdate`](#refcmd-clusterupdate), [`clusthash`](#refcmd-clusthash), [`linclust`](#refcmd-linclust), [`mergeclusters`](#refcmd-mergeclusters), [`pickconsensusrep`](#refcmd-pickconsensusrep) |
| `prefiltering` | `6` | [`countkmer`](#refcmd-countkmer), [`gappedprefilter`](#refcmd-gappedprefilter), [`kmermatcher`](#refcmd-kmermatcher), [`kmersearch`](#refcmd-kmersearch), [`prefilter`](#refcmd-prefilter), [`ungappedprefilter`](#refcmd-ungappedprefilter) |
| `alignment` | `9` | [`align`](#refcmd-align), [`alignall`](#refcmd-alignall), [`alignbykmer`](#refcmd-alignbykmer), [`expandaln`](#refcmd-expandaln), [`fwbw`](#refcmd-fwbw), [`offsetalignment`](#refcmd-offsetalignment), [`proteinaln2nucl`](#refcmd-proteinaln2nucl), [`rescorediagonal`](#refcmd-rescorediagonal), [`transitivealign`](#refcmd-transitivealign) |
| `profiles` | `14` | [`convertca3m`](#refcmd-convertca3m), [`convertmsa`](#refcmd-convertmsa), [`convertprofiledb`](#refcmd-convertprofiledb), [`expand2profile`](#refcmd-expand2profile), [`msa2profile`](#refcmd-msa2profile), [`msa2result`](#refcmd-msa2result), [`pairaln`](#refcmd-pairaln), [`profile2consensus`](#refcmd-profile2consensus), [`profile2neff`](#refcmd-profile2neff), [`profile2pssm`](#refcmd-profile2pssm), [`profile2repseq`](#refcmd-profile2repseq), [`result2profile`](#refcmd-result2profile), [`sequence2profile`](#refcmd-sequence2profile), [`tsv2exprofiledb`](#refcmd-tsv2exprofiledb) |
| `database` | `20` | [`aliasdb`](#refcmd-aliasdb), [`concatdbs`](#refcmd-concatdbs), [`cpdb`](#refcmd-cpdb), [`createdb`](#refcmd-createdb), [`createindex`](#refcmd-createindex), [`createlinindex`](#refcmd-createlinindex), [`createsubdb`](#refcmd-createsubdb), [`databases`](#refcmd-databases), [`db2tar`](#refcmd-db2tar), [`lndb`](#refcmd-lndb), [`mergedbs`](#refcmd-mergedbs), [`mvdb`](#refcmd-mvdb), [`renamedbkeys`](#refcmd-renamedbkeys), [`rmdb`](#refcmd-rmdb), [`splitdb`](#refcmd-splitdb), [`splitsequence`](#refcmd-splitsequence), [`subtractdbs`](#refcmd-subtractdbs), [`swapdb`](#refcmd-swapdb), [`tar2db`](#refcmd-tar2db), [`tsv2db`](#refcmd-tsv2db) |
| `result_handling` | `17` | [`convert2fasta`](#refcmd-convert2fasta), [`convertalis`](#refcmd-convertalis), [`createseqfiledb`](#refcmd-createseqfiledb), [`createtsv`](#refcmd-createtsv), [`extractdomains`](#refcmd-extractdomains), [`filterresult`](#refcmd-filterresult), [`result2dnamsa`](#refcmd-result2dnamsa), [`result2flat`](#refcmd-result2flat), [`result2msa`](#refcmd-result2msa), [`result2rbh`](#refcmd-result2rbh), [`result2repseq`](#refcmd-result2repseq), [`result2stats`](#refcmd-result2stats), [`sortresult`](#refcmd-sortresult), [`summarizealis`](#refcmd-summarizealis), [`summarizeheaders`](#refcmd-summarizeheaders), [`summarizeresult`](#refcmd-summarizeresult), [`swapresults`](#refcmd-swapresults) |
| `sequence_manipulation` | `9` | [`extractalignedregion`](#refcmd-extractalignedregion), [`extractframes`](#refcmd-extractframes), [`extractorfs`](#refcmd-extractorfs), [`masksequence`](#refcmd-masksequence), [`orftocontig`](#refcmd-orftocontig), [`recoverlongestorf`](#refcmd-recoverlongestorf), [`reverseseq`](#refcmd-reverseseq), [`translateaa`](#refcmd-translateaa), [`translatenucs`](#refcmd-translatenucs) |
| `taxonomy` | `15` | [`addtaxonomy`](#refcmd-addtaxonomy), [`aggregatetax`](#refcmd-aggregatetax), [`aggregatetaxweights`](#refcmd-aggregatetaxweights), [`createbintaxmapping`](#refcmd-createbintaxmapping), [`createbintaxonomy`](#refcmd-createbintaxonomy), [`createdmptaxonomy`](#refcmd-createdmptaxonomy), [`createtaxdb`](#refcmd-createtaxdb), [`filtertaxdb`](#refcmd-filtertaxdb), [`filtertaxseqdb`](#refcmd-filtertaxseqdb), [`lca`](#refcmd-lca), [`lcaalign`](#refcmd-lcaalign), [`majoritylca`](#refcmd-majoritylca), [`nrtotaxmapping`](#refcmd-nrtotaxmapping), [`taxonomy`](#refcmd-taxonomy), [`taxonomyreport`](#refcmd-taxonomyreport) |
| `multi_hit` | `5` | [`besthitperset`](#refcmd-besthitperset), [`combinepvalperset`](#refcmd-combinepvalperset), [`mergeresultsbyset`](#refcmd-mergeresultsbyset), [`multihitdb`](#refcmd-multihitdb), [`multihitsearch`](#refcmd-multihitsearch) |
| `utilities` | `16` | [`apply`](#refcmd-apply), [`compress`](#refcmd-compress), [`convertkb`](#refcmd-convertkb), [`decompress`](#refcmd-decompress), [`diffseqdbs`](#refcmd-diffseqdbs), [`filterdb`](#refcmd-filterdb), [`gff2db`](#refcmd-gff2db), [`gpuserver`](#refcmd-gpuserver), [`maskbygff`](#refcmd-maskbygff), [`prefixid`](#refcmd-prefixid), [`setextendeddbtype`](#refcmd-setextendeddbtype), [`suffixid`](#refcmd-suffixid), [`summarizetabs`](#refcmd-summarizetabs), [`touchdb`](#refcmd-touchdb), [`unpackdb`](#refcmd-unpackdb), [`view`](#refcmd-view) |

## Command Pages {#sec-command-pages}

Full command pages follow below. Each page keeps local usage/options snapshots plus dependency links.

