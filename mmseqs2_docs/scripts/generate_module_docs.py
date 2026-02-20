#!/usr/bin/env python3
"""Generate functional module pages with prose-first command entries."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "mmseqs2_docs"
REF_DIR = DOCS / "reference"
DEP_JSON = REF_DIR / "dependency_map.json"
HELP_DIR = ROOT / "mmseqs_help_output"
OUT_DIR = DOCS / "submodules"

MODULES = [
    (
        "easy_workflows",
        "Easy Workflows",
        "High-level shortcuts that operate directly on FASTA/FASTQ inputs and orchestrate MMseqs2 modules with practical defaults.",
    ),
    (
        "search_workflows",
        "Search Workflows",
        "Search and mapping workflows that compose prefiltering, alignment, and result conversion paths under different sensitivity and runtime envelopes.",
    ),
    (
        "clustering",
        "Clustering",
        "Modules for cluster construction, incremental updates, and representative selection across cascaded and linear-time strategies.",
    ),
    (
        "prefiltering",
        "Prefiltering",
        "Candidate-generation modules that prune comparison space before expensive alignment kernels.",
    ),
    (
        "alignment",
        "Alignment",
        "Alignment and rescoring modules used after prefiltering to compute pair quality and coordinates.",
    ),
    (
        "profiles",
        "Profiles",
        "Profile and MSA modules for profile construction, conversion, and profile-driven search workflows.",
    ),
    (
        "database",
        "Database Management",
        "Database lifecycle modules for creation, indexing, splitting, merging, and contract-preserving transforms.",
    ),
    (
        "result_handling",
        "Result Handling",
        "Modules that filter, summarize, reshape, and export result databases for downstream analysis.",
    ),
    (
        "sequence_manipulation",
        "Sequence Manipulation",
        "Sequence-level transform modules for ORFs, frames, masking, coordinate transforms, and related preprocessing.",
    ),
    (
        "taxonomy",
        "Taxonomy",
        "Modules for taxonomy database preparation, assignment, filtering, and report generation.",
    ),
    (
        "multi_hit",
        "Multi-hit",
        "Set-based modules that aggregate sequence-level evidence into per-set statistics and outputs.",
    ),
    (
        "utilities",
        "Utilities",
        "General-purpose helpers and special-purpose composition commands used in advanced pipelines.",
    ),
]

MODULE_FILE = {
    "easy_workflows": "easy_workflows.md",
    "search_workflows": "search.md",
    "clustering": "clustering.md",
    "prefiltering": "prefiltering.md",
    "alignment": "alignment.md",
    "profiles": "profiles.md",
    "database": "database.md",
    "result_handling": "result_handling.md",
    "sequence_manipulation": "sequence_manipulation.md",
    "taxonomy": "taxonomy.md",
    "multi_hit": "multi_hit.md",
    "utilities": "utilities.md",
}

LAYER_ROLE = {
    "workflow": "Workflow-level entrypoint that orchestrates downstream MMseqs2 modules.",
    "high_level_api": "High-level API command for end-to-end DB workflows with explicit controls.",
    "mid_level_api": "Mid-level compute module used directly in advanced pipelines and by workflows.",
    "low_level_api": "Low-level DB or utility command used for composition and contract enforcement.",
}

GROUP_DESIGN_NOTES = {
    "easy_workflows": "Design priority is fast onboarding with robust defaults; fine-grained behavior is inherited from downstream workflow modules.",
    "search_workflows": "Design priority is balancing sensitivity, candidate pruning, and alignment cost under explicit memory and split constraints.",
    "clustering": "Design priority is reducing graph density early, then applying clustering criteria consistently across workflow steps.",
    "prefiltering": "Design priority is minimizing expensive downstream alignments by aggressively pruning unlikely sequence pairs.",
    "alignment": "Design priority is extracting reliable score/coverage/identity information while controlling DP and backtrace overhead.",
    "profiles": "Design priority is preserving profile semantics across transforms so search and scoring remain interpretable.",
    "database": "Design priority is keeping MMseqs2 DB contracts valid while avoiding unnecessary I/O and recomputation.",
    "result_handling": "Design priority is transforming outputs without silently changing scoring semantics inherited from upstream modules.",
    "sequence_manipulation": "Design priority is sequence-space normalization before heavy compute, especially for translated or masked workflows.",
    "taxonomy": "Design priority is consistent taxonomy mapping and aggregation semantics across assignment and reporting modules.",
    "multi_hit": "Design priority is robust set-level aggregation over sequence-level evidence with transparent statistical behavior.",
    "utilities": "Design priority is composability and operational control for custom pipelines and debugging workflows.",
}


def parse_usage_and_options(help_text: str) -> tuple[str, list[tuple[str, str]]]:
    usage = ""
    options = []
    seen = set()
    for line in help_text.splitlines():
        if line.startswith("usage:"):
            usage = line.strip()
            continue
        m = re.match(r"^\s+(-{1,2}[A-Za-z0-9][A-Za-z0-9-]*)\s+(.*)$", line)
        if not m:
            continue
        flag = m.group(1)
        if flag in seen:
            continue
        seen.add(flag)
        desc = m.group(2).strip()
        desc = re.sub(r"\s+\[[^\]]*\]\s*$", "", desc).strip()
        desc = re.sub(r"^[A-Z][A-Z0-9_/.-]*(?:\s+[A-Z][A-Z0-9_/.-]*)*\s+", "", desc)
        options.append((flag, desc))
    return usage, options


def label_slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def module_anchor(group: str) -> str:
    return f"mod-{label_slug(group)}"


def module_command_anchor(name: str) -> str:
    return f"modcmd-{label_slug(name)}"


def reference_command_anchor(name: str) -> str:
    return f"refcmd-{label_slug(name)}"


def dependency_command_anchor(name: str) -> str:
    return f"depcmd-{label_slug(name)}"


def key_options_for(cmd: str) -> tuple[str, list[tuple[str, str]]]:
    help_file = HELP_DIR / f"{cmd}.txt"
    if not help_file.exists():
        return "", []
    return parse_usage_and_options(help_file.read_text())


def group_links(items: list[str]) -> str:
    if not items:
        return "No direct cross-group coupling detected in the current dependency map."
    links = []
    for group in items:
        if group in MODULE_FILE:
            links.append(f"[`{group}`](#{module_anchor(group)})")
        else:
            links.append(f"`{group}`")
    return ", ".join(links)


def sentence(text: str) -> str:
    if text.endswith((".", "!", "?")):
        return text
    return text + "."


def typst_callout(kind: str, text: str) -> list[str]:
    macro = {
        "note": "doc_note",
        "perf": "doc_perf",
        "warning": "doc_warning",
        "tip": "doc_tip",
    }[kind]
    return [
        "```{=typst}",
        f"#{macro}[",
        text,
        "]",
        "```",
        "",
    ]


def inferred_usage(cmd: str, layer: str) -> str:
    if layer == "workflow":
        return f"usage: mmseqs {cmd} <inputFileOrDB> <outputPrefixOrFile> <tmpDir> [options]"
    if layer == "high_level_api":
        return f"usage: mmseqs {cmd} <inputDB> <targetOrResultDB> <outputDB> [tmpDir] [options]"
    if layer == "mid_level_api":
        return f"usage: mmseqs {cmd} <inputDB(s)> <outputDB> [options]"
    return f"usage: mmseqs {cmd} <DB> [args] [options]"


def command_context(meta: dict, group: str) -> str:
    layer_line = LAYER_ROLE.get(meta["layer"], "Command in the MMseqs2 execution cascade.")
    coupling = (
        f"Current coupling is {len(meta['called_by'])} upstream caller(s) and {len(meta['calls'])} downstream call(s)."
    )
    return sentence(f"{layer_line} {GROUP_DESIGN_NOTES[group]} {coupling}")


def render_module(group: str, title: str, intro: str, dep_map: dict[str, dict]) -> str:
    cmds = sorted([name for name, meta in dep_map.items() if meta["primary_group"] == group])

    lines = []
    lines.append(f"## {title} {{#{module_anchor(group)}}}")
    lines.append("")
    lines.append(intro)
    lines.append("")
    lines.extend(
        typst_callout(
            "note",
            "This page is task-oriented. Detailed call topology is centralized in the Dependency Map to avoid repeating large edge lists.",
        )
    )

    if group in {"search_workflows", "clustering", "easy_workflows"}:
        lines.extend(
            typst_callout(
                "perf",
                "In production, tune index/load and split-memory policy before increasing sensitivity. Infrastructure choices usually dominate runtime swings.",
            )
        )

    if group in {"taxonomy", "sequence_manipulation", "result_handling"}:
        lines.extend(
            typst_callout(
                "warning",
                "Validate DB-type and sidecar contracts before chaining modules. Most pipeline failures are contract mismatches, not algorithmic defects.",
            )
        )

    for cmd in cmds:
        meta = dep_map[cmd]
        usage, options = key_options_for(cmd)

        related_groups = sorted(
            {
                dep_map[x]["primary_group"]
                for x in (meta["calls"] + meta["called_by"])
                if x in dep_map and dep_map[x]["primary_group"] != group
            }
        )

        lines.append(f"### `{cmd}` {{#{module_command_anchor(cmd)}}}")
        lines.append("")
        if meta.get("description"):
            lines.append(sentence(meta["description"]))
        else:
            lines.append("This command is registered in the MMseqs2 source tree but does not expose a short description string.")
        lines.append("")

        lines.append(command_context(meta, group))
        lines.append("")

        lines.append("| Aspect | Value |")
        lines.append("| :--- | :--- |")
        if usage:
            lines.append(f"| Usage | `{usage}` |")
        else:
            lines.append(
                f"| Usage | `{inferred_usage(cmd, meta['layer'])}` (source-derived synopsis; run `mmseqs {cmd}` for exact syntax) |"
            )
        lines.append(f"| API layer | `{meta['layer']}` |")
        lines.append(f"| Category flags | `{meta['category']}` |")
        lines.append(f"| Upstream command count | `{len(meta['called_by'])}` |")
        lines.append(f"| Downstream command count | `{len(meta['calls'])}` |")
        lines.append(f"| Related functional groups | {group_links(related_groups)} |")
        lines.append(
            f"| References | [Full CLI](#{reference_command_anchor(cmd)}) · [Dependency entry](#{dependency_command_anchor(cmd)}) |"
        )
        lines.append("")

        if options:
            lines.append("#### Key Options")
            lines.append("")
            lines.append("| Option | Purpose |")
            lines.append("| :--- | :--- |")
            for flag, desc in options[:8]:
                lines.append(f"| `{flag}` | {desc} |")
            lines.append("")
        else:
            lines.append("No local option snapshot was parsed for this command. Use the Full CLI reference page for details.")
            lines.append("")

    if not cmds:
        lines.append("No commands are currently assigned to this functional group.")
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    dep_map = json.loads(DEP_JSON.read_text())

    for group, title, intro in MODULES:
        out_file = OUT_DIR / MODULE_FILE[group]
        out_file.write_text(render_module(group, title, intro, dep_map))
        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
