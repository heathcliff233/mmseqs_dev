#!/usr/bin/env python3
"""Generate normalized functional module pages with crosslinks and reduced duplication."""

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
        "High-level shortcuts that operate directly on FASTA/FASTQ and produce user-facing outputs with minimal setup.",
    ),
    (
        "search_workflows",
        "Search Workflows",
        "Workflow-level search and mapping modules that orchestrate prefiltering and alignment under different modes.",
    ),
    (
        "clustering",
        "Clustering",
        "Modules for cluster construction, updates, and representative handling across different clustering strategies.",
    ),
    (
        "prefiltering",
        "Prefiltering",
        "Core candidate-generation modules used to reduce search space before expensive alignment stages.",
    ),
    (
        "alignment",
        "Alignment",
        "Core alignment and alignment-adjacent modules for scoring, rescoring, and coordinate transformations.",
    ),
    (
        "profiles",
        "Profiles",
        "Modules for profile/MSA conversion, profile construction, and profile-driven workflow components.",
    ),
    (
        "database",
        "Database Management",
        "Modules for creating, indexing, splitting, merging, and maintaining MMseqs2 database artifacts.",
    ),
    (
        "result_handling",
        "Result Handling",
        "Modules that transform, filter, summarize, and export result databases.",
    ),
    (
        "sequence_manipulation",
        "Sequence Manipulation",
        "Modules that transform sequence content, frames, ORFs, and masked/aligned regions.",
    ),
    (
        "taxonomy",
        "Taxonomy",
        "Modules for taxonomy DB preparation, assignment, filtering, and reporting workflows.",
    ),
    (
        "multi_hit",
        "Multi-hit",
        "Modules for grouped-sequence (set-based) search and per-set aggregation pipelines.",
    ),
    (
        "utilities",
        "Utilities",
        "General-purpose helpers and special-purpose modules that support advanced workflow composition.",
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

NO_EDGE_TEXT = "`n/a`"


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
        return NO_EDGE_TEXT
    links = []
    for group in items:
        file_name = MODULE_FILE.get(group)
        if file_name:
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
                "This page focuses on task-oriented usage and practical options. "
                + "Detailed call topology is centralized in the Dependency Map to reduce duplicated edge listings.",
            )
        )
    if group in {"search_workflows", "clustering", "easy_workflows"}:
        lines.extend(
            typst_callout(
                "perf",
                "For repeated runs against stable targets, prioritize index reuse and split-memory tuning before increasing sensitivity.",
            )
        )
    if group in {"taxonomy", "sequence_manipulation", "result_handling"}:
        lines.extend(
            typst_callout(
                "warning",
                "Validate database-type and sidecar compatibility before chaining modules. Most pipeline failures come from DB contract mismatches.",
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
            lines.append("No short description is available in the command registry.")
        lines.append("")

        lines.append("| Aspect | Value |")
        lines.append("| :--- | :--- |")
        lines.append(f"| Usage | `{usage}` |" if usage else "| Usage | Help snapshot unavailable locally. |")
        lines.append(f"| API layer | `{meta['layer']}` |")
        lines.append(f"| Category flags | `{meta['category']}` |")
        lines.append(f"| Upstream command count | `{len(meta['called_by'])}` |")
        lines.append(f"| Downstream command count | `{len(meta['calls'])}` |")
        lines.append(f"| Related functional groups | {group_links(related_groups)} |")
        lines.append("")

        lines.append(
            f"Reference links: [Full CLI](#{reference_command_anchor(cmd)}), "
            f"[Dependency entry](#{dependency_command_anchor(cmd)})."
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
