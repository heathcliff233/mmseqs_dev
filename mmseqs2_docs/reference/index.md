# MMseqs2 Command Reference Index

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

Primary maps: [Dependency map](./dependency_map.md).

## Easy Workflows

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`easy-cluster`](./easy-cluster.md) | `workflow` | `help` |
| [`easy-linclust`](./easy-linclust.md) | `workflow` | `help` |
| [`easy-linsearch`](./easy-linsearch.md) | `workflow` | `help` |
| [`easy-rbh`](./easy-rbh.md) | `workflow` | `help` |
| [`easy-search`](./easy-search.md) | `workflow` | `help` |
| [`easy-taxonomy`](./easy-taxonomy.md) | `workflow` | `help` |

## Search Workflows

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`linsearch`](./linsearch.md) | `high_level_api` | `help` |
| [`map`](./map.md) | `high_level_api` | `help` |
| [`rbh`](./rbh.md) | `high_level_api` | `help` |
| [`search`](./search.md) | `high_level_api` | `help` |

## Clustering

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`clust`](./clust.md) | `mid_level_api` | `help` |
| [`cluster`](./cluster.md) | `high_level_api` | `help` |
| [`clusterupdate`](./clusterupdate.md) | `high_level_api` | `help` |
| [`clusthash`](./clusthash.md) | `mid_level_api` | `help` |
| [`linclust`](./linclust.md) | `high_level_api` | `help` |
| [`mergeclusters`](./mergeclusters.md) | `mid_level_api` | `help` |
| [`pickconsensusrep`](./pickconsensusrep.md) | `mid_level_api` | `missing-help` |

## Prefiltering

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`countkmer`](./countkmer.md) | `low_level_api` | `missing-help` |
| [`gappedprefilter`](./gappedprefilter.md) | `mid_level_api` | `help` |
| [`kmermatcher`](./kmermatcher.md) | `mid_level_api` | `help` |
| [`kmersearch`](./kmersearch.md) | `mid_level_api` | `help` |
| [`prefilter`](./prefilter.md) | `mid_level_api` | `help` |
| [`ungappedprefilter`](./ungappedprefilter.md) | `mid_level_api` | `help` |

## Alignment

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`align`](./align.md) | `mid_level_api` | `help` |
| [`alignall`](./alignall.md) | `mid_level_api` | `help` |
| [`alignbykmer`](./alignbykmer.md) | `mid_level_api` | `help` |
| [`expandaln`](./expandaln.md) | `mid_level_api` | `help` |
| [`fwbw`](./fwbw.md) | `mid_level_api` | `missing-help` |
| [`offsetalignment`](./offsetalignment.md) | `low_level_api` | `help` |
| [`proteinaln2nucl`](./proteinaln2nucl.md) | `low_level_api` | `help` |
| [`rescorediagonal`](./rescorediagonal.md) | `mid_level_api` | `help` |
| [`transitivealign`](./transitivealign.md) | `mid_level_api` | `missing-help` |

## Profiles

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`convertca3m`](./convertca3m.md) | `mid_level_api` | `missing-help` |
| [`convertmsa`](./convertmsa.md) | `low_level_api` | `help` |
| [`convertprofiledb`](./convertprofiledb.md) | `low_level_api` | `missing-help` |
| [`expand2profile`](./expand2profile.md) | `mid_level_api` | `missing-help` |
| [`msa2profile`](./msa2profile.md) | `low_level_api` | `help` |
| [`msa2result`](./msa2result.md) | `low_level_api` | `help` |
| [`pairaln`](./pairaln.md) | `low_level_api` | `missing-help` |
| [`profile2consensus`](./profile2consensus.md) | `low_level_api` | `missing-help` |
| [`profile2neff`](./profile2neff.md) | `low_level_api` | `missing-help` |
| [`profile2pssm`](./profile2pssm.md) | `low_level_api` | `missing-help` |
| [`profile2repseq`](./profile2repseq.md) | `low_level_api` | `missing-help` |
| [`result2profile`](./result2profile.md) | `low_level_api` | `help` |
| [`sequence2profile`](./sequence2profile.md) | `low_level_api` | `missing-help` |
| [`tsv2exprofiledb`](./tsv2exprofiledb.md) | `mid_level_api` | `help` |

## Database

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`aliasdb`](./aliasdb.md) | `low_level_api` | `help` |
| [`concatdbs`](./concatdbs.md) | `low_level_api` | `help` |
| [`cpdb`](./cpdb.md) | `low_level_api` | `help` |
| [`createdb`](./createdb.md) | `low_level_api` | `help` |
| [`createindex`](./createindex.md) | `low_level_api` | `help` |
| [`createlinindex`](./createlinindex.md) | `low_level_api` | `help` |
| [`createsubdb`](./createsubdb.md) | `low_level_api` | `help` |
| [`databases`](./databases.md) | `low_level_api` | `missing-help` |
| [`db2tar`](./db2tar.md) | `low_level_api` | `help` |
| [`lndb`](./lndb.md) | `low_level_api` | `help` |
| [`mergedbs`](./mergedbs.md) | `low_level_api` | `help` |
| [`mvdb`](./mvdb.md) | `low_level_api` | `help` |
| [`renamedbkeys`](./renamedbkeys.md) | `low_level_api` | `help` |
| [`rmdb`](./rmdb.md) | `low_level_api` | `missing-help` |
| [`splitdb`](./splitdb.md) | `low_level_api` | `help` |
| [`splitsequence`](./splitsequence.md) | `low_level_api` | `help` |
| [`subtractdbs`](./subtractdbs.md) | `low_level_api` | `help` |
| [`swapdb`](./swapdb.md) | `low_level_api` | `help` |
| [`tar2db`](./tar2db.md) | `low_level_api` | `help` |
| [`tsv2db`](./tsv2db.md) | `low_level_api` | `help` |

## Result Handling

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`convert2fasta`](./convert2fasta.md) | `low_level_api` | `missing-help` |
| [`convertalis`](./convertalis.md) | `low_level_api` | `help` |
| [`createseqfiledb`](./createseqfiledb.md) | `low_level_api` | `help` |
| [`createtsv`](./createtsv.md) | `low_level_api` | `help` |
| [`extractdomains`](./extractdomains.md) | `low_level_api` | `missing-help` |
| [`filterresult`](./filterresult.md) | `low_level_api` | `help` |
| [`result2dnamsa`](./result2dnamsa.md) | `low_level_api` | `help` |
| [`result2flat`](./result2flat.md) | `low_level_api` | `help` |
| [`result2msa`](./result2msa.md) | `low_level_api` | `help` |
| [`result2rbh`](./result2rbh.md) | `low_level_api` | `help` |
| [`result2repseq`](./result2repseq.md) | `low_level_api` | `help` |
| [`result2stats`](./result2stats.md) | `low_level_api` | `help` |
| [`sortresult`](./sortresult.md) | `low_level_api` | `help` |
| [`summarizealis`](./summarizealis.md) | `low_level_api` | `help` |
| [`summarizeheaders`](./summarizeheaders.md) | `low_level_api` | `missing-help` |
| [`summarizeresult`](./summarizeresult.md) | `low_level_api` | `help` |
| [`swapresults`](./swapresults.md) | `low_level_api` | `help` |

## Sequence Manipulation

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`extractalignedregion`](./extractalignedregion.md) | `low_level_api` | `help` |
| [`extractframes`](./extractframes.md) | `low_level_api` | `help` |
| [`extractorfs`](./extractorfs.md) | `low_level_api` | `help` |
| [`masksequence`](./masksequence.md) | `low_level_api` | `help` |
| [`orftocontig`](./orftocontig.md) | `low_level_api` | `help` |
| [`recoverlongestorf`](./recoverlongestorf.md) | `low_level_api` | `help` |
| [`reverseseq`](./reverseseq.md) | `low_level_api` | `help` |
| [`translateaa`](./translateaa.md) | `low_level_api` | `help` |
| [`translatenucs`](./translatenucs.md) | `low_level_api` | `help` |

## Taxonomy

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`addtaxonomy`](./addtaxonomy.md) | `low_level_api` | `missing-help` |
| [`aggregatetax`](./aggregatetax.md) | `low_level_api` | `missing-help` |
| [`aggregatetaxweights`](./aggregatetaxweights.md) | `low_level_api` | `missing-help` |
| [`createbintaxmapping`](./createbintaxmapping.md) | `low_level_api` | `missing-help` |
| [`createbintaxonomy`](./createbintaxonomy.md) | `low_level_api` | `missing-help` |
| [`createdmptaxonomy`](./createdmptaxonomy.md) | `low_level_api` | `missing-help` |
| [`createtaxdb`](./createtaxdb.md) | `low_level_api` | `help` |
| [`filtertaxdb`](./filtertaxdb.md) | `low_level_api` | `help` |
| [`filtertaxseqdb`](./filtertaxseqdb.md) | `low_level_api` | `help` |
| [`lca`](./lca.md) | `low_level_api` | `help` |
| [`lcaalign`](./lcaalign.md) | `low_level_api` | `help` |
| [`majoritylca`](./majoritylca.md) | `low_level_api` | `missing-help` |
| [`nrtotaxmapping`](./nrtotaxmapping.md) | `low_level_api` | `missing-help` |
| [`taxonomy`](./taxonomy.md) | `high_level_api` | `help` |
| [`taxonomyreport`](./taxonomyreport.md) | `low_level_api` | `help` |

## Multi Hit

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`besthitperset`](./besthitperset.md) | `high_level_api` | `help` |
| [`combinepvalperset`](./combinepvalperset.md) | `high_level_api` | `help` |
| [`mergeresultsbyset`](./mergeresultsbyset.md) | `high_level_api` | `help` |
| [`multihitdb`](./multihitdb.md) | `high_level_api` | `help` |
| [`multihitsearch`](./multihitsearch.md) | `high_level_api` | `help` |

## Utilities

| Command | Layer | Snapshot |
| :--- | :--- | :--- |
| [`apply`](./apply.md) | `low_level_api` | `help` |
| [`compress`](./compress.md) | `low_level_api` | `help` |
| [`convertkb`](./convertkb.md) | `low_level_api` | `missing-help` |
| [`decompress`](./decompress.md) | `low_level_api` | `help` |
| [`diffseqdbs`](./diffseqdbs.md) | `low_level_api` | `missing-help` |
| [`filterdb`](./filterdb.md) | `low_level_api` | `help` |
| [`gff2db`](./gff2db.md) | `low_level_api` | `missing-help` |
| [`gpuserver`](./gpuserver.md) | `low_level_api` | `help` |
| [`maskbygff`](./maskbygff.md) | `low_level_api` | `missing-help` |
| [`prefixid`](./prefixid.md) | `low_level_api` | `help` |
| [`setextendeddbtype`](./setextendeddbtype.md) | `low_level_api` | `help` |
| [`suffixid`](./suffixid.md) | `low_level_api` | `help` |
| [`summarizetabs`](./summarizetabs.md) | `low_level_api` | `missing-help` |
| [`touchdb`](./touchdb.md) | `low_level_api` | `help` |
| [`unpackdb`](./unpackdb.md) | `low_level_api` | `help` |
| [`view`](./view.md) | `low_level_api` | `help` |

