# AGENTS_mmseqs.md

This guide defines how to maintain and improve the MMseqs2 documentation in this repository. It is written for human and AI contributors working across `mmseqs2_docs/`, `MMseqs2/`, and `mmseqs_help_output/`.

The main goal is not only correctness, but also clarity of explanation: readers should understand what to run, why it behaves that way, and how modules connect across the MMseqs2 cascade.

## Mission and Scope

Use this repository to produce a source-grounded MMseqs2 manual with a stable narrative architecture:

1. Overview and mental model.
2. Algorithmic and systems acceleration foundations.
3. Functional modules and submodules.
4. Expert operation and source-development guidance.
5. Full command reference and dependency topology.

Primary workspace and boundaries:

| Area | Role |
| :--- | :--- |
| `MMseqs2/` | Source of truth for behavior and architecture |
| `mmseqs_help_output/` | Local CLI help snapshots (`mmseqs <cmd> -h`) |
| `mmseqs2_docs/` | Markdown sources, generators, validator, PDF build |
| `AGENTS_mmseqs.md` | This operating handbook |

## Source-of-Truth Policy

When documents disagree, use this precedence order:

1. MMseqs2 source code and workflow scripts.
2. Local help snapshots generated from the active `mmseqs` binary.
3. Generated docs (`reference/*.md`, `submodules/*.md`) after regeneration.
4. Narrative chapters (`introduction.md`, `foundations.md`, `system_map.md`, `expert_manual.md`, `manual.md`).

Canonical source anchors:

| Topic | Primary files |
| :--- | :--- |
| Command visibility, categories, descriptions | `MMseqs2/src/MMseqsBase.cpp` |
| Command entry declarations | `MMseqs2/src/CommandDeclarations.h` |
| Workflow orchestration | `MMseqs2/src/workflow/*.cpp`, `MMseqs2/data/workflow/*.sh` |
| Prefiltering and k-mer candidate generation | `MMseqs2/src/prefiltering/*` |
| Alignment and scoring kernels | `MMseqs2/src/alignment/*` |
| Clustering and Linclust internals | `MMseqs2/src/clustering/*`, `MMseqs2/src/linclust/*` |
| Taxonomy logic | `MMseqs2/src/taxonomy/*` |
| Multi-hit logic | `MMseqs2/src/multihit/*` |
| Shared infrastructure and DB contracts | `MMseqs2/src/commons/*`, `MMseqs2/src/util/*` |

## Current Manual Architecture

The PDF is assembled by `mmseqs2_docs/build_pdf.sh` in this order:

1. `cover.md`
2. `numbering.md`
3. `toc.md`
4. `introduction.md`
5. `foundations.md`
6. `system_map.md`
7. `manual.md`
8. all functional module pages in `mmseqs2_docs/submodules/` (explicit order in script)
9. `expert_manual.md`
10. `reference/index.md`
11. generated command pages (`reference/*.md`, excluding `index.md` and `dependency_map.md`)
12. `reference/dependency_map.md`

`appendix_wiki_reference.md`, `appendix_developer.md`, and `sharp_bits.md` are legacy files and are not part of the current PDF build.

`developer_manual.md` is retained as a lightweight standalone context file, but the canonical developer guidance in the manual is `expert_manual.md`, section `MMseqs2 Source Development Guide`.

## Documentation Logic Requirements

The documentation should present a consistent cascade-aware logic:

1. Start with a systems overview and reading strategy.
2. Explain algorithmic and systems acceleration as coupled design.
3. Map command layers and module interactions.
4. Present task-oriented functional module pages.
5. End with expert operation rules and source tracing guidance.
6. Provide full command and dependency references as generated evidence.

Do not flatten this into disconnected command descriptions. MMseqs2 behavior is defined by stage composition, not isolated modules.

## Writing Principles

Prefer prose that explains causality and design tradeoffs. Use bullets only where they are structurally necessary (checklists, concise enumerations, procedural sequences). Use tables for dense comparisons and metadata summaries; do not replace explanatory paragraphs with large bullet dumps.

Core writing rules:

1. Explain "why" before "how" for every major section.
2. Keep one canonical explanation per concept; cross-link instead of duplicating.
3. Avoid empty placeholders (`none`, `n/a`, or vacuous text) in command/module narratives unless they represent real unavailable data.
4. Use consistent terminology: workflow, high-level API, mid-level API, low-level API, functional group, DB contract, sidecar, split policy.
5. Make performance claims traceable to source files or measured behavior.
6. Separate semantic changes from formatting changes whenever possible.

A good section should let a reader answer three questions quickly:

1. What is this component for?
2. Where does it sit in the cascade and what does it depend on?
3. What tradeoffs control speed, memory, and output semantics?

## Cross-Link and Anchor Rules

Internal links must be anchor-based, not file-path based, so PDF navigation works.

Use:

- `[Performance Foundations](#sec-performance-foundations)`
- `[Dependency Map](#sec-dependency-map)`
- `[Full CLI](#refcmd-search)`

Do not use:

- `](./file.md#section)`
- `](../submodules/x.md)`

Anchor naming conventions in generated docs:

| Anchor type | Pattern | Example |
| :--- | :--- | :--- |
| Major sections | `sec-*` | `#sec-functional-modules-manual` |
| Functional groups | `mod-*` | `#mod-search-workflows` |
| Functional command entries | `modcmd-*` | `#modcmd-search` |
| Reference command pages | `refcmd-*` | `#refcmd-search` |
| Dependency command entries | `depcmd-*` | `#depcmd-search` |
| Dependency groups | `depgroup-*` | `#depgroup-search-workflows` |

The validator rejects legacy local file-path links.

## Section Numbering and TOC Discipline

Keep heading levels stable to avoid confusing Contents output:

1. Major chapter files use `#`.
2. Functional module files use `##` for module headers and `###` for command entries.
3. Command reference index starts at `#`; generated command pages start at `###` so they stay subordinate to index structure in the merged PDF.

Do not create extra top-level chapter files for narrow topics that belong inside existing chapters.

## Typst and Formatting Policy

Default to Markdown grammar. Use raw Typst blocks only when required for PDF-specific behavior (callouts, page control, or other formatting that Markdown cannot express cleanly).

Current Typst helper macros are defined in `mmseqs2_docs/numbering.md`:

- `doc_note`
- `doc_perf`
- `doc_warning`
- `doc_tip`

Table behavior and image fallback handling are controlled by `mmseqs2_docs/fix-rule.lua`. Do not bypass this pipeline with ad hoc formatting hacks.

## Generated Artifacts and Ownership

Treat these as generated outputs:

| Generated file set | Generator |
| :--- | :--- |
| `mmseqs2_docs/reference/dependency_map.json` | `scripts/build_dependency_graph.py` |
| `mmseqs2_docs/reference/dependency_map.md` | `scripts/build_dependency_graph.py` |
| `mmseqs2_docs/reference/index.md` + `reference/*.md` command pages | `scripts/generate_command_reference.py` |
| `mmseqs2_docs/submodules/*.md` | `scripts/generate_module_docs.py` |

If you need durable structural changes, edit the generator scripts rather than hand-editing generated pages and expecting changes to persist.

## Standard Update Workflow

### 1) Refresh help snapshots (if CLI changed)

```bash
./generate_mmseqs_docs.sh /path/to/mmseqs
```

This writes `mmseqs_help_output/*.txt` for visible commands.

### 2) Regenerate topology, command reference, and functional pages

```bash
./mmseqs2_docs/scripts/build_dependency_graph.py
./mmseqs2_docs/scripts/generate_command_reference.py
./mmseqs2_docs/scripts/generate_module_docs.py
```

Or run the full refresh:

```bash
./mmseqs2_docs/scripts/rebuild_docs.sh
```

### 3) Validate structural consistency

```bash
python3 mmseqs2_docs/scripts/validate_docs.py
```

Warnings for missing help snapshots are acceptable when snapshots are not yet available. Errors must be resolved before finishing.

### 4) Build PDF

```bash
./mmseqs2_docs/build_pdf.sh
```

The script prefers `typst`, then falls back to `xelatex`, then `pdflatex`. Use the `foldcomp` conda environment when available.

## Algorithm Coverage Expectations

`foundations.md` is the canonical chapter for speed architecture and should be kept deep and source-linked. It must continue to cover:

1. Shared comparison backbone between search and clustering.
2. Candidate generation via k-mer indexing/expansion.
3. Diagonal and ungapped filters.
4. SIMD gapped alignment and output-cost tradeoffs.
5. Clustering-specific acceleration design.
6. Masking and composition-bias controls.
7. GPU search backend (`ungappedprefilter`, `gpuserver`) and scope limits.
8. Internal DB/storage contract model.
9. Index/load strategy.
10. Memory split and parallel execution tradeoffs.

When algorithm behavior changes in source, update this chapter first, then update module/reference wording if needed.

## Command and Module Mapping Maintenance

Dependency extraction quality depends on explicit mapping tables in `build_dependency_graph.py`:

- `SCRIPT_OWNERS`
- `WORKFLOW_CPP_OWNERS`
- `GROUP_HINT_OVERRIDES`
- `GROUP_ORDER`

When new workflows or command groups are added, update these maps; otherwise grouping and edges will degrade.

Keep command classification concise. The prior per-command classification block was removed by design because it added noise without improving task decisions.

## Anti-Duplication Policy

Redundant text is a real maintenance bug. Before finalizing:

1. Search for repeated paragraphs across chapters (`rg` on key phrases).
2. Keep the strongest version in the most canonical chapter.
3. Replace duplicates with short bridge text plus anchor links.

A command should have one detailed definition, then be referenced elsewhere.

## Quality Gate (Definition of Done)

Before finalizing doc changes:

1. Source claims have been cross-checked in `MMseqs2/` and/or fresh help snapshots.
2. No broken anchors and no `.md` path links remain.
3. No duplicate command entries across submodule pages.
4. No command section contains empty placeholder prose.
5. TOC hierarchy is readable and section numbering is coherent.
6. `validate_docs.py` reports zero errors.
7. `build_pdf.sh` succeeds and PDF navigation works for cross-links.
8. Any architecture-level changes are reflected in this `AGENTS_mmseqs.md`.

## Fast Triage Guide

If a user reports a docs issue, debug in this order:

1. Wrong command description or missing command:
   check `MMseqs2/src/MMseqsBase.cpp`, then regenerate dependency/reference/module pages.
2. Wrong options/defaults:
   refresh `mmseqs_help_output` from the current binary and regenerate reference pages.
3. Broken PDF links:
   replace file-path links with anchors; confirm anchor existence; rerun validator.
4. Confusing module placement:
   adjust group inference/mapping in `build_dependency_graph.py`, regenerate submodules and index.
5. Bloated or repetitive narrative:
   consolidate in canonical chapters and cross-link out.

## Contributor Notes

When making broad rewrites, keep commits reviewable by separating:

1. generator logic changes,
2. regenerated artifacts,
3. manual narrative edits.

If this guidance and active repository behavior diverge, update this file immediately as part of the same change set.
