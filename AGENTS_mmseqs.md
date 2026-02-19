# AGENTS.md

This repository contains MMseqs2/Foldseek sources plus local documentation workspaces.
This guide is for agents working on `mmseqs2_docs` and the MMseqs2 source tree.

## Scope

- Primary documentation workspace: `mmseqs2_docs/`
- Primary source of truth for MMseqs2 behavior: `MMseqs2/`
- Command help snapshots for docs authoring: `mmseqs_help_output/`
- PDF build entrypoint: `mmseqs2_docs/build_pdf.sh`

## Repository Map

- `MMseqs2/src/`: C++ implementation of commands and workflows.
- `MMseqs2/data/workflow/`: shell workflow templates embedded at build time.
- `MMseqs2/src/MMseqsBase.cpp`: central command registry (command name, description, categories, examples).
- `MMseqs2/src/CommandDeclarations.h`: full list of command entry points.
- `mmseqs2_docs/`: markdown sources for the MMseqs2 PDF manual.
- `mmseqs_help_output/`: `mmseqs <module> -h` outputs (generated snapshots).
- `generate_mmseqs_docs.sh`: helper to refresh `mmseqs_help_output/`.

## Build and Refresh Workflows

1. Refresh help snapshots (when command-line options change):
```bash
./generate_mmseqs_docs.sh /path/to/mmseqs
```

2. Build the MMseqs2 PDF:
```bash
./mmseqs2_docs/build_pdf.sh
```

3. Expected output:
- `mmseqs2_docs/mmseqs2_doc.pdf`

## Source-of-Truth Rules for Docs

- Command list + one-line command intent:
  - `MMseqs2/src/MMseqsBase.cpp`
- Exact CLI flags/defaults:
  - `mmseqs_help_output/*.txt` (regenerate from the current binary when needed)
- Workflow orchestration behavior:
  - `MMseqs2/src/workflow/*.cpp`
  - `MMseqs2/data/workflow/*.sh`
- Core algorithm/data behavior:
  - `MMseqs2/src/{prefiltering,alignment,clustering,taxonomy,linclust,multihit,commons,util}/`

When docs and help snapshots disagree, treat regenerated help output from the current binary as canonical for argument tables.

## MMseqs2 Source Modules (Code-Level)

- `MMseqs2/src/workflow`
  - High-level orchestrators (`search`, `cluster`, `taxonomy`, `easy-*`, etc.) that wire modules into end-to-end workflows.
- `MMseqs2/src/prefiltering`
  - K-mer based candidate generation, indexing, ungapped filtering, and prefilter database production.
- `MMseqs2/src/alignment`
  - Gapped/ungapped alignment engines, scoring, backtraces, profile/MSA-related alignment components.
- `MMseqs2/src/clustering`
  - Cluster graph/algorithm implementations (`clust`, connected components, set-cover style clustering).
- `MMseqs2/src/linclust`
  - Linear-time clustering/search indexing and k-mer matching primitives.
- `MMseqs2/src/taxonomy`
  - LCA, taxonomy DB creation/mapping/filtering, taxonomy report generation.
- `MMseqs2/src/multihit`
  - Multi-sequence-set search and aggregation (`multihit*`, per-set p-value/best-hit operations).
- `MMseqs2/src/util`
  - Utility/format-conversion/database-manipulation commands (large command surface).
- `MMseqs2/src/commons`
  - Shared infrastructure: DB I/O (`DBReader`/`DBWriter`), parameters, command plumbing, file/memory helpers.

## Documentation Modules (Docs-Level) and Command Descriptions

### `mmseqs2_docs/submodules/easy_workflows.md`
- `easy-search`: Sensitive homology search.
- `easy-linsearch`: Fast, less sensitive homology search.
- `easy-cluster`: Slower, sensitive clustering.
- `easy-linclust`: Fast linear time cluster, less sensitive clustering.
- `easy-taxonomy`: Taxonomic classification.
- `easy-rbh`: Find reciprocal best hit.
- Code anchors:
  - `MMseqs2/src/workflow/EasySearch.cpp`
  - `MMseqs2/src/workflow/EasyLinclust.cpp`
  - `MMseqs2/src/workflow/EasyCluster.cpp`
  - `MMseqs2/src/workflow/EasyTaxonomy.cpp`
  - `MMseqs2/src/workflow/EasyRbh.cpp`
  - `MMseqs2/data/workflow/easysearch.sh`
  - `MMseqs2/data/workflow/easycluster.sh`
  - `MMseqs2/data/workflow/easytaxonomy.sh`
  - `MMseqs2/data/workflow/easyrbh.sh`

### `mmseqs2_docs/submodules/search.md`
- `search`: Sensitive homology search.
- Code anchors:
  - `MMseqs2/src/workflow/Search.cpp`
  - `MMseqs2/data/workflow/blastp.sh`
  - `MMseqs2/data/workflow/blastpgp.sh`
  - `MMseqs2/data/workflow/blastn.sh`
  - `MMseqs2/data/workflow/translated_search.sh`
  - `MMseqs2/data/workflow/searchtargetprofile.sh`
  - `MMseqs2/data/workflow/searchslicedtargetprofile.sh`
  - `MMseqs2/data/workflow/iterativepp.sh`

### `mmseqs2_docs/submodules/clustering.md`
- `linclust`: Fast, less sensitive clustering.
- `cluster`: Slower, sensitive clustering.
- `clust`: Cluster result by Set-Cover/Connected-Component/Greedy-Incremental.
- `clusthash`: Hash-based clustering of equal length sequences.
- `clusterupdate`: Update previous clustering with new sequences.
- `mergeclusters`: Merge multiple cascaded clustering steps.
- Code anchors:
  - `MMseqs2/src/workflow/Linclust.cpp`
  - `MMseqs2/src/workflow/Cluster.cpp`
  - `MMseqs2/src/workflow/ClusterUpdate.cpp`
  - `MMseqs2/src/clustering/Main.cpp`
  - `MMseqs2/src/util/mergeclusters.cpp`
  - `MMseqs2/data/workflow/linclust.sh`
  - `MMseqs2/data/workflow/clustering.sh`
  - `MMseqs2/data/workflow/cascaded_clustering.sh`
  - `MMseqs2/data/workflow/update_clustering.sh`
  - `MMseqs2/data/workflow/nucleotide_clustering.sh`

### `mmseqs2_docs/submodules/prefiltering.md`
- `prefilter`: Double consecutive diagonal k-mer search.
- `ungappedprefilter`: Optimal diagonal score search.
- `gappedprefilter`: Optimal Smith-Waterman-based prefiltering (slow).
- `kmermatcher`: Find bottom-m-hashed k-mer matches within sequence DB.
- `kmersearch`: Find bottom-m-hashed k-mer matches between target and query DB.
- Code anchors:
  - `MMseqs2/src/prefiltering/Main.cpp`
  - `MMseqs2/src/prefiltering/Prefiltering.cpp`
  - `MMseqs2/src/prefiltering/ungappedprefilter.cpp`
  - `MMseqs2/src/linclust/kmermatcher.cpp`
  - `MMseqs2/src/linclust/kmersearch.cpp`

### `mmseqs2_docs/submodules/alignment.md`
- `align`: Optimal gapped local alignment.
- `alignall`: Within-result all-vs-all gapped local alignment.
- `alignbykmer`: Heuristic gapped local k-mer based alignment.
- `expandaln`: Expand an alignment result based on another.
- `offsetalignment`: Offset alignment by ORF start position.
- `proteinaln2nucl`: Transform protein alignments to nucleotide alignments.
- `rescorediagonal`: Compute sequence identity for diagonal.
- Code anchors:
  - `MMseqs2/src/alignment/Main.cpp`
  - `MMseqs2/src/alignment/Alignment.cpp`
  - `MMseqs2/src/alignment/rescorediagonal.cpp`
  - `MMseqs2/src/util/alignall.cpp`
  - `MMseqs2/src/util/alignbykmer.cpp`
  - `MMseqs2/src/util/expandaln.cpp`
  - `MMseqs2/src/util/offsetalignment.cpp`
  - `MMseqs2/src/util/proteinaln2nucl.cpp`

### `mmseqs2_docs/submodules/profiles.md`
- `msa2profile`: Convert a MSA DB to a profile DB.
- `msa2result`: Convert a MSA DB to a profile DB/result representation.
- `result2profile`: Compute profile DB from a result DB.
- `convertmsa`: Convert Stockholm/PFAM MSA file to a MSA DB.
- `tsv2exprofiledb`: Create an expandable profile DB from TSV files.
- Code anchors:
  - `MMseqs2/src/util/msa2profile.cpp`
  - `MMseqs2/src/util/msa2result.cpp`
  - `MMseqs2/src/util/result2profile.cpp`
  - `MMseqs2/src/util/convertmsa.cpp`
  - `MMseqs2/src/util/tsv2exprofiledb.cpp`
  - `MMseqs2/data/workflow/tsv2exprofiledb.sh`

### `mmseqs2_docs/submodules/database.md`
- `createdb`: Convert FASTA/Q file(s) to a sequence DB.
- `createindex`: Store precomputed index on disk to reduce search overhead.
- `createlinindex`: Create linsearch index.
- `subtractdbs`: Remove entries from first DB that occur in second DB by key.
- `tar2db`: Convert tar archive content to a DB.
- `swapdb`: Transpose DB with integer values in first column.
- `aliasdb`: Create relative symlink of DB to another name in the same folder.
- `cpdb`: Copy a DB.
- `concatdbs`: Concatenate two DBs, reassigning IDs from second DB.
- `createsubdb`: Create subset DB from DB keys/list.
- `db2tar`: Archive DB contents to tar.
- `lndb`: Symlink a DB.
- `mergedbs`: Merge entries from multiple DBs.
- `splitsequence`: Split sequences by length.
- `mvdb`: Move a DB.
- `renamedbkeys`: Create DB with renamed keys.
- `splitdb`: Split DB into subsets.
- `tsv2db`: Convert TSV file to DB.
- Code anchors:
  - `MMseqs2/src/util/createdb.cpp`
  - `MMseqs2/src/workflow/CreateIndex.cpp`
  - `MMseqs2/src/util/indexdb.cpp`
  - `MMseqs2/src/linclust/kmerindexdb.cpp` (lin index backend)
  - `MMseqs2/src/util/subtractdbs.cpp`
  - `MMseqs2/src/util/tar2db.cpp`
  - `MMseqs2/src/util/cpmvrmlndb.cpp` (`cpdb`/`mvdb`/`lndb`/`aliasdb`/`swapdb` implementation group)
  - `MMseqs2/src/commons/DBConcat.cpp` (`concatdbs` implementation)
  - `MMseqs2/src/util/createsubdb.cpp`
  - `MMseqs2/src/util/db2tar.cpp`
  - `MMseqs2/src/util/mergedbs.cpp`
  - `MMseqs2/src/util/splitsequence.cpp`
  - `MMseqs2/src/util/renamedbkeys.cpp`
  - `MMseqs2/src/util/splitdb.cpp`
  - `MMseqs2/src/util/tsv2db.cpp`
  - `MMseqs2/data/workflow/createindex.sh`

### `mmseqs2_docs/submodules/sequence_manipulation.md`
- `extractorfs`: Six-frame extraction of open reading frames.
- `extractframes`: Extract frames from nucleotide sequence DB.
- `reverseseq`: Reverse sequences (no complement).
- `translateaa`: Translate proteins to lexicographically lowest codons.
- `translatenucs`: Translate nucleotides to proteins.
- `recoverlongestorf`: Recover longest ORF after filtering/elimination.
- `orftocontig`: Write ORF locations in alignment format.
- `makepaddedseqdb`: Generate padded sequence DB.
- `masksequence`: Soft-mask sequence DB using tantan.
- `extractalignedregion`: Extract aligned query region.
- Code anchors:
  - `MMseqs2/src/util/extractorfs.cpp`
  - `MMseqs2/src/util/extractframes.cpp`
  - `MMseqs2/src/util/reverseseq.cpp`
  - `MMseqs2/src/util/translateaa.cpp`
  - `MMseqs2/src/util/translatenucs.cpp`
  - `MMseqs2/src/util/recoverlongestorf.cpp`
  - `MMseqs2/src/util/orftocontig.cpp`
  - `MMseqs2/src/util/makepaddedseqdb.cpp`
  - `MMseqs2/src/util/masksequence.cpp`
  - `MMseqs2/src/util/extractalignedregion.cpp`
  - `MMseqs2/src/commons/Orf.cpp`
  - `MMseqs2/src/commons/TranslateNucl.h`
  - `MMseqs2/src/commons/Masker.cpp`

### `mmseqs2_docs/submodules/result_handling.md`
- `convertalis`: Convert alignment DB to BLAST-tab/SAM/custom format.
- `createtsv`: Convert result DB to tab-separated flat file.
- `result2flat`: Add FASTA headers to DB entries in flat output.
- `createseqfiledb`: Create DB of unaligned FASTA entries.
- `swapresults`: Transpose prefilter/alignment DB.
- `result2rbh`: Keep reciprocal best hits from merged result DB.
- `result2msa`: Compute MSA DB from result DB.
- `result2dnamsa`: Compute DNA MSA DB without query insertions.
- `result2stats`: Compute per-entry statistics.
- `filterresult`: Pairwise alignment result filter.
- `result2repseq`: Extract representative sequences from result DB.
- `sortresult`: Sort result DB in canonical order.
- `summarizealis`: Summarize alignment result to one row.
- `summarizeresult`: Extract annotations from alignment DB.
- Code anchors:
  - `MMseqs2/src/util/convertalignments.cpp`
  - `MMseqs2/src/util/createtsv.cpp`
  - `MMseqs2/src/util/result2flat.cpp`
  - `MMseqs2/src/util/createseqfiledb.cpp`
  - `MMseqs2/src/util/swapresults.cpp`
  - `MMseqs2/src/util/result2rbh.cpp`
  - `MMseqs2/src/util/result2msa.cpp`
  - `MMseqs2/src/util/result2dnamsa.cpp`
  - `MMseqs2/src/util/result2stats.cpp`
  - `MMseqs2/src/util/result2profile.cpp` (`filterresult` implementation)
  - `MMseqs2/src/util/result2repseq.cpp`
  - `MMseqs2/src/util/sortresult.cpp`
  - `MMseqs2/src/util/summarizealis.cpp`
  - `MMseqs2/src/util/summarizeresult.cpp`

### `mmseqs2_docs/submodules/multi_hit.md`
- `multihitdb`: Create sequence DB for multi-hit searches.
- `besthitperset`: Best element per set with updated p-value.
- `combinepvalperset`: Combine p-values per set.
- `mergeresultsbyset`: Merge ORF-level results back to set/contig level.
- `multihitsearch`: Search grouped sequence sets.
- Code anchors:
  - `MMseqs2/src/multihit/MultiHitDb.cpp`
  - `MMseqs2/src/multihit/MultiHitSearch.cpp`
  - `MMseqs2/src/multihit/besthitperset.cpp`
  - `MMseqs2/src/multihit/combinepvalperset.cpp`
  - `MMseqs2/src/multihit/Aggregation.cpp`
  - `MMseqs2/src/util/mergeresultsbyset.cpp`
  - `MMseqs2/data/workflow/multihitdb.sh`
  - `MMseqs2/data/workflow/multihitsearch.sh`

### `mmseqs2_docs/submodules/taxonomy.md`
- `taxonomy`: Taxonomic classification workflow.
- Related taxonomy modules often cross-referenced:
  - `createtaxdb`, `taxonomyreport`, `filtertaxdb`, `filtertaxseqdb`, `lca`, `lcaalign`, `aggregatetax`.
- Code anchors:
  - `MMseqs2/src/workflow/Taxonomy.cpp`
  - `MMseqs2/src/workflow/EasyTaxonomy.cpp`
  - `MMseqs2/src/taxonomy/createtaxdb.cpp`
  - `MMseqs2/src/taxonomy/lca.cpp`
  - `MMseqs2/src/taxonomy/filtertaxdb.cpp`
  - `MMseqs2/src/taxonomy/filtertaxseqdb.cpp`
  - `MMseqs2/src/taxonomy/aggregatetax.cpp`
  - `MMseqs2/src/taxonomy/taxonomyreport.cpp`
  - `MMseqs2/src/taxonomy/addtaxonomy.cpp`
  - `MMseqs2/data/workflow/taxonomy.sh`
  - `MMseqs2/data/workflow/taxpercontig.sh`
  - `MMseqs2/data/workflow/createtaxdb.sh`

### `mmseqs2_docs/submodules/utilities.md`
- `compress`: Compress DB entries.
- `decompress`: Decompress DB entries.
- `gpuserver`: Start a GPU server.
- `apply`: Execute external program on each DB entry.
- `prefixid`: Prefix each entry with its key.
- `suffixid`: Suffix each entry with its key.
- `touchdb`: Preload DB into page cache.
- `unpackdb`: Unpack DB into files.
- `view`: Print selected DB entries.
- `filterdb`: Filter DB by conditions/sort/filter expressions.
- `setextendeddbtype`: Set/write extended DB type metadata.
- `map`: Map nearly identical sequences.
- `rbh`: Reciprocal best hit search.
- Code anchors:
  - `MMseqs2/src/util/compress.cpp`
  - `MMseqs2/src/util/apply.cpp`
  - `MMseqs2/src/util/prefixid.cpp`
  - `MMseqs2/src/util/touchdb.cpp`
  - `MMseqs2/src/util/unpackdb.cpp`
  - `MMseqs2/src/util/view.cpp`
  - `MMseqs2/src/util/filterdb.cpp`
  - `MMseqs2/src/util/setextendeddbtype.cpp`
  - `MMseqs2/src/workflow/Map.cpp`
  - `MMseqs2/src/workflow/Rbh.cpp`
  - `MMseqs2/data/workflow/map.sh`
  - `MMseqs2/data/workflow/rbh.sh`

## Hidden/Advanced Commands

- Commands marked `COMMAND_HIDDEN` in `MMseqs2/src/MMseqsBase.cpp` are generally not part of user-facing docs unless there is an explicit doc goal.
- If adding/removing documented modules, check:
  - `mmseqs2_docs/manual.md` module index
  - corresponding `mmseqs2_docs/submodules/*.md`
  - `mmseqs2_docs/build_pdf.sh` inclusion order

## PDF Assembly Order (Current)

`mmseqs2_docs/build_pdf.sh` builds in this order:
- `cover.md`
- `numbering.md`
- `toc.md`
- `introduction.md`
- `wiki.md`
- `manual.md`
- all files in `mmseqs2_docs/submodules/` (explicit list)
- `expert_manual.md`
- `developer_manual.md`

Keep this order stable unless you intentionally change document structure.
