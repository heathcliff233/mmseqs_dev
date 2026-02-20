# AGENTS_foldseek.md

This handbook defines how to maintain and improve Foldseek documentation in this repository.

It is intended for contributors working across:

- `foldseek/` (source of truth for behavior)
- `foldseek_help_output/` (local CLI help snapshots)
- `foldseek_docs/` (manual sources and PDF build)

## Mission and Scope

The Foldseek manual should remain:

1. Source-grounded.
2. Task-oriented for users.
3. Architecture-aware for advanced users.
4. Consistent with actual CLI behavior in this repo.

Primary objective: readers should be able to move from "what command should I run?" to "why does this run behave this way?" without conflicting descriptions.

## Repository Map

### Source of truth

| Area | Purpose |
| :--- | :--- |
| `foldseek/src/FoldseekBase.cpp` | Command registry: visible/hidden commands, descriptions, examples, usage signatures |
| `foldseek/src/LocalCommandDeclarations.h` | Entry-point declaration map for local Foldseek modules |
| `foldseek/src/commons/LocalParameters.cpp` | Foldseek-specific parameter definitions/defaults/categories |
| `foldseek/src/workflow/*.cpp` | High-level workflow orchestration (`search`, `cluster`, multimer workflows, easy workflows) |
| `foldseek/src/strucclustutils/*.cpp` | Core structural algorithms and conversions (`structurealign`, `tmalign`, `structcreatedb`, etc.) |
| `foldseek/lib/3di/` | 3Di representation and structural encoding internals |
| `foldseek/lib/tmalign/` | TM-align backend |
| `foldseek/data/*.sh` | Workflow shell templates used by workflow modules |

### Documentation and artifacts

| Area | Purpose |
| :--- | :--- |
| `foldseek_docs/` | Markdown manual sources + PDF build |
| `foldseek_docs/build_pdf.sh` | PDF build entrypoint |
| `foldseek_docs/fix-rule.lua` | Pandoc Typst filter for table behavior |
| `foldseek_help_output/` | Per-command `foldseek <cmd> -h` outputs |
| `generate_foldseek_docs.sh` | Refresh helper for `foldseek_help_output/` |

## Source-of-Truth Policy

When documentation and implementation disagree, resolve in this order:

1. `foldseek/src/FoldseekBase.cpp` + implementation in `foldseek/src/workflow/` and `foldseek/src/strucclustutils/`.
2. `foldseek_help_output/*.txt` generated from the active Foldseek binary.
3. `foldseek_docs/*.md` narrative and module pages.

Never treat markdown as canonical for command semantics if code/help snapshots disagree.

## Current PDF Architecture

`foldseek_docs/build_pdf.sh` currently assembles the PDF in this order:

1. `cover.md`
2. `numbering.md`
3. `toc.md`
4. `introduction.md`
5. `wiki.md`
6. `manual.md`
7. `submodules/easy_workflows.md`
8. `submodules/structure_search.md`
9. `submodules/structure_clustering.md`
10. `submodules/multimer.md`
11. `submodules/structure_manipulation.md`
12. `submodules/databases.md`
13. `expert_manual.md`
14. `developer_manual.md`

Maintain this order unless you intentionally redesign the manual structure.

## Documentation Logic Requirements

Keep the narrative flow coherent:

1. Introduction and Foldseek mental model.
2. User guide and practical operational constraints.
3. Functional module manuals grouped by task.
4. Expert behavior and advanced operational guidance.
5. Developer/source-level architecture guidance.

Avoid repeating full explanations across chapters. Keep one canonical explanation per concept and cross-reference it.

## Writing Principles

Prefer concise explanatory paragraphs over long bullet chains. Use tables when they improve readability of parameter matrices or comparisons.

Rules:

1. Explain mechanism and tradeoff, not just command syntax.
2. Keep module pages task-first (when to use, what it changes, key limits).
3. Keep architecture sections source-first (where behavior is implemented).
4. Remove duplicated prose aggressively.
5. Replace placeholders like `none` with concrete source-derived text.

## Link and Navigation Policy

Current Foldseek docs still contain markdown file-path links (for example `./submodules/...md`). Those links are fragile in PDF navigation.

Policy for future edits:

1. Prefer anchor links (`#section-anchor`) for internal navigation.
2. Keep heading IDs explicit for stable cross-reference targets.
3. Avoid cross-file markdown path links in finalized manuals.

If link strategy is refactored, do it consistently across all chapter files in one change.

## Typst and Formatting Policy

Use standard markdown as default. Use raw Typst only where markdown cannot express required PDF behavior.

`foldseek_docs/fix-rule.lua` is part of the rendering contract. Keep it in sync with table/callout formatting decisions.

`foldseek_docs/build_pdf.sh` currently requires a Pandoc build that supports `--pdf-engine=typst`.

## Help Snapshot Workflow

Refresh command help snapshots with:

```bash
./generate_foldseek_docs.sh /path/to/foldseek
```

This writes outputs under `foldseek_help_output/`.

Important: `generate_foldseek_docs.sh` currently uses a static module list. When Foldseek commands change, update the list to prevent stale/missing snapshots.

Minimum sync rule:

1. Review visible commands in `foldseek/src/FoldseekBase.cpp`.
2. Ensure all user-facing commands are represented in `generate_foldseek_docs.sh`.
3. Regenerate `foldseek_help_output/`.

## Standard Documentation Update Workflow

1. Validate source behavior in `foldseek/src/` (command registry + implementation paths).
2. Refresh help snapshots if CLI or defaults changed.
3. Update markdown chapters/submodules.
4. Build PDF:

```bash
./foldseek_docs/build_pdf.sh
```

If Typst support is environment-specific, use a known working environment (for example your `foldcomp` conda env).

## Foldseek Module Responsibility Map

Use this map to keep descriptions consistent:

| Functional area | Main command families | Primary source roots |
| :--- | :--- | :--- |
| Easy workflows | `easy-search`, `easy-cluster`, `easy-rbh`, `easy-multimersearch`, `easy-multimercluster` | `foldseek/src/workflow/Easy*.cpp`, `foldseek/data/easy*.sh` |
| Structure search | `search`, `structurealign`, `structurerescorediagonal`, `tmalign` | `foldseek/src/workflow/StructureSearch.cpp`, `foldseek/src/strucclustutils/{structurealign,structurerescorediagonal,tmalign}.cpp` |
| Structure clustering | `cluster`, `clust` | `foldseek/src/workflow/StructureCluster.cpp`, MMseqs clustering backend |
| Multimer | `multimersearch`, `multimercluster`, `scoremultimer`, `createmultimerreport`, `expandmultimer` | `foldseek/src/workflow/{MultimerSearch,MultimerCluster}.cpp`, `foldseek/src/strucclustutils/*multimer*.cpp` |
| Structure manipulation | `createdb`, `compressca`, `convertalis`, `convert2pdb`, `aln2tmscore`, `result2profile` | `foldseek/src/strucclustutils/{structcreatedb,compressca,structureconvertalis,convert2pdb,aln2tmscore,result2structprofile}.cpp` |
| Databases/indexing | `databases`, `createindex`, `createclusearchdb` | `foldseek/src/FoldseekBase.cpp`, `foldseek/src/workflow/StructureIndex.cpp`, `foldseek/data/structdatabases.sh` |

## Feature Coverage Expectations

The docs should explicitly cover Foldseek-specific speed/design mechanisms, including:

1. 3Di representation and AA+3Di combined scoring.
2. Prefilter and alignment mode interactions (`--prefilter-mode`, `--alignment-type`).
3. TM-score/LDDT thresholds and ranking implications.
4. Index variants and exclusions (`--index-exclude`, `--index-subset`, compatibility behavior).
5. Multimer chain assignment/reporting controls.
6. GPU-related paths (`--gpu`, padded DB usage).

If these mechanisms are changed in source, update conceptual chapters and module pages together.

## Anti-Duplication Policy

Duplication is a maintenance defect.

Before finalizing:

1. Search repeated explanations across `introduction.md`, `manual.md`, `expert_manual.md`, `developer_manual.md`, and `submodules/*.md`.
2. Keep one canonical version.
3. Replace duplicates with short contextual links.

## Quality Gate (Definition of Done)

Before closing a Foldseek docs change:

1. Claims are verified against `foldseek/src/` and/or refreshed `foldseek_help_output/`.
2. No stale command names remain after command-registry updates.
3. No contradictory defaults across docs for the same parameter.
4. Internal navigation strategy is consistent (especially when touching links/headings).
5. PDF builds successfully via `foldseek_docs/build_pdf.sh`.
6. If command inventory changed, `generate_foldseek_docs.sh` and `foldseek_help_output/` were reconciled.

## Fast Triage Guide

If a report comes in:

1. Wrong command description:
   check `foldseek/src/FoldseekBase.cpp` and the owning implementation file.
2. Wrong flags/defaults:
   refresh `foldseek_help_output/` from current binary and update docs accordingly.
3. Broken pipeline or unclear workflow behavior:
   inspect `foldseek/src/workflow/*.cpp` and corresponding `foldseek/data/*.sh`.
4. Confusing architecture wording:
   align `developer_manual.md` with source module boundaries in `workflow`, `strucclustutils`, `lib/3di`, and `commons`.

## Commit Hygiene

When possible, separate commits by intent:

1. Source-grounded content edits.
2. Help snapshot refresh.
3. Formatting or structural link cleanups.
4. Generated PDF artifact updates (only when intentionally versioned).

If this guide diverges from the actual Foldseek docs pipeline, update `AGENTS_foldseek.md` in the same change set that introduced the divergence.
