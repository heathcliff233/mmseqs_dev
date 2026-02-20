#!/usr/bin/env python3
"""Generate compact command reference pages from dependency map + local help snapshots."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "mmseqs2_docs"
REF_DIR = DOCS / "reference"
HELP_DIR = ROOT / "mmseqs_help_output"
DEP_JSON = REF_DIR / "dependency_map.json"
INDEX_MD = REF_DIR / "index.md"

GROUP_ORDER = [
    "easy_workflows",
    "search_workflows",
    "clustering",
    "prefiltering",
    "alignment",
    "profiles",
    "database",
    "result_handling",
    "sequence_manipulation",
    "taxonomy",
    "multi_hit",
    "utilities",
]

GROUP_DESIGN_NOTES = {
    "easy_workflows": "This command family favors fast adoption and default-safe orchestration over maximal low-level control.",
    "search_workflows": "This command family balances sensitivity against runtime by controlling candidate generation, alignment workload, and split policy.",
    "clustering": "This command family controls graph construction and cluster assignment behavior, so early filter decisions strongly affect downstream structure.",
    "prefiltering": "This command family is the main acceleration gate that prunes candidate pairs before expensive alignment.",
    "alignment": "This command family computes pair quality and coordinates and usually dominates per-pair compute cost after prefiltering.",
    "profiles": "This command family preserves profile semantics across conversion and search steps.",
    "database": "This command family enforces DB contracts and storage/index integrity used by all workflows.",
    "result_handling": "This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes.",
    "sequence_manipulation": "This command family transforms sequence space before or after major compute stages.",
    "taxonomy": "This command family maps sequence evidence into taxonomy labels and reports under explicit aggregation rules.",
    "multi_hit": "This command family aggregates sequence-level hits into set-level statistics and decisions.",
    "utilities": "This command family provides compositional utilities for custom pipelines, migration tasks, and diagnostics.",
}


def parse_usage_and_options(help_text: str) -> tuple[str, list[tuple[str, str]]]:
    usage = ""
    option_rows: list[tuple[str, str]] = []

    for line in help_text.splitlines():
        if line.startswith("usage:"):
            usage = line.strip()
            continue
        m = re.match(r"^\s+(-{1,2}[A-Za-z0-9][A-Za-z0-9-]*)\s+(.*)$", line)
        if m:
            flag = m.group(1)
            desc = m.group(2).strip()
            desc = re.sub(r"\s+\[[^\]]*\]\s*$", "", desc).strip()
            desc = re.sub(r"^[A-Z][A-Z0-9_/.-]*(?:\s+[A-Z][A-Z0-9_/.-]*)*\s+", "", desc)
            option_rows.append((flag, desc))

    unique: list[tuple[str, str]] = []
    seen = set()
    for flag, desc in option_rows:
        if flag in seen:
            continue
        seen.add(flag)
        unique.append((flag, desc))

    return usage, unique


def label_slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def module_anchor(group: str) -> str:
    return f"mod-{label_slug(group)}"


def reference_command_anchor(name: str) -> str:
    return f"refcmd-{label_slug(name)}"


def dependency_command_anchor(name: str) -> str:
    return f"depcmd-{label_slug(name)}"


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


def inferred_usage(name: str, layer: str) -> str:
    if layer == "workflow":
        return f"usage: mmseqs {name} <inputFileOrDB> <outputPrefixOrFile> <tmpDir> [options]"
    if layer == "high_level_api":
        return f"usage: mmseqs {name} <inputDB> <targetOrResultDB> <outputDB> [tmpDir] [options]"
    if layer == "mid_level_api":
        return f"usage: mmseqs {name} <inputDB(s)> <outputDB> [options]"
    return f"usage: mmseqs {name} <DB> [args] [options]"


def role_paragraph(meta: dict) -> str:
    layer = meta["layer"]
    if layer == "workflow":
        return "Execution role: workflow entrypoint that coordinates lower-level modules rather than acting as a single compute kernel."
    if layer == "high_level_api":
        return "Execution role: high-level API command that exposes a complete task path over MMseqs2 databases."
    if layer == "mid_level_api":
        return "Execution role: core compute module typically called by workflows and advanced custom pipelines."
    return "Execution role: low-level command used for DB management, conversion, and pipeline composition."


def design_paragraph(meta: dict) -> str:
    group = meta["primary_group"]
    calls = len(meta["calls"])
    called_by = len(meta["called_by"])
    return sentence(
        f"{GROUP_DESIGN_NOTES[group]} The current dependency map records {called_by} upstream caller(s) and {calls} downstream call(s), which indicates how broadly parameter changes can propagate"
    )


def use_case_paragraph(name: str, meta: dict) -> str:
    group = meta["primary_group"]
    if group == "search_workflows":
        return "Typical use case: choose this command when you need explicit control over search sensitivity, filtering, and alignment behavior for DB-to-DB runs."
    if group == "clustering":
        return "Typical use case: choose this command when constructing, refining, or updating cluster assignments while preserving explicit coverage/identity criteria."
    if group == "prefiltering":
        return "Typical use case: choose this command in custom pipelines that must expose candidate-generation behavior before alignment stages."
    if group == "database":
        return "Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts."
    if group == "result_handling":
        return "Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream."
    return (
        "Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults."
    )


def write_command_page(name: str, meta: dict) -> bool:
    help_file = HELP_DIR / f"{name}.txt"
    has_help = help_file.exists()
    help_text = help_file.read_text() if has_help else ""
    usage, options = parse_usage_and_options(help_text)

    lines = []
    lines.append(f"### `{name}` {{#{reference_command_anchor(name)}}}")
    lines.append("")
    if meta.get("description"):
        lines.append(sentence(meta["description"]))
    else:
        lines.append("This command is visible in the MMseqs2 command registry and documented here from source-level metadata.")
    lines.append("")

    lines.append(role_paragraph(meta))
    lines.append("")
    lines.append(design_paragraph(meta))
    lines.append("")
    lines.append(use_case_paragraph(name, meta))
    lines.append("")

    lines.append(
        f"Dependency entry: [Open in map](#{dependency_command_anchor(name)}); "
        f"functional module: [`{meta['primary_group']}`](#{module_anchor(meta['primary_group'])})."
    )
    lines.append("")

    lines.append("**Usage**")
    lines.append("")
    if usage:
        lines.append(f"`{usage}`")
    else:
        lines.append(f"`{inferred_usage(name, meta['layer'])}`")
        lines.append("")
        lines.append(
            f"The syntax line above is source-derived from command layer/category metadata. "
            f"Run `mmseqs {name}` locally for exact positional arguments in your build."
        )
    lines.append("")

    lines.append("**Key Options**")
    lines.append("")
    if options:
        lines.append("| Option | Purpose |")
        lines.append("| :--- | :--- |")
        for flag, desc in options[:12]:
            lines.append(f"| `{flag}` | {desc} |")
    else:
        lines.append(
            "Local CLI option snapshots are not available for this command. Use the dependency entry and calling workflow source files to recover parameter bundles for your runtime path."
        )
    lines.append("")

    lines.append("**Full CLI Help Snapshot**")
    lines.append("")
    if has_help:
        lines.append("```text")
        lines.append(help_text.rstrip())
        lines.append("```")
    else:
        lines.extend(
            typst_callout(
                "note",
                "This page keeps a source-derived summary because no local help snapshot was found for this command.",
            )
        )

    out = REF_DIR / f"{name}.md"
    out.write_text("\n".join(lines) + "\n")
    return has_help


def write_index(dep_map: dict[str, dict], has_help_map: dict[str, bool]) -> None:
    grouped: dict[str, list[str]] = defaultdict(list)
    for cmd, meta in dep_map.items():
        grouped[meta["primary_group"]].append(cmd)

    missing_help = sorted([c for c, has_help in has_help_map.items() if not has_help])

    lines = []
    lines.append("# MMseqs2 Command Reference Index {#sec-command-reference}")
    lines.append("")
    lines.append(
        "This index is generated from command metadata, dependency topology, and local CLI help snapshots where available. "
        "Use it to move quickly from command name to functional placement and detailed page content."
    )
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("| :--- | :--- |")
    lines.append(f"| Total visible commands | `{len(dep_map)}` |")
    lines.append(f"| Commands with help snapshots | `{sum(has_help_map.values())}` |")
    lines.append(f"| Commands with source-derived fallback pages | `{len(missing_help)}` |")
    lines.append("")

    if missing_help:
        lines.extend(
            typst_callout(
                "note",
                "Some commands currently use source-derived fallback text because local help snapshots were not present in `mmseqs_help_output`.",
            )
        )
        lines.append("| Command | Snapshot status |")
        lines.append("| :--- | :--- |")
        for cmd in missing_help:
            lines.append(f"| `{cmd}` | source-derived fallback |")
        lines.append("")

    lines.append("Primary topology view: [Dependency map](#sec-dependency-map).")
    lines.append("")

    lines.append("## Command Group Map {#sec-command-group-map}")
    lines.append("")
    lines.append("| Group | Command count | Commands |")
    lines.append("| :--- | :--- | :--- |")
    for group in GROUP_ORDER:
        cmds = sorted(grouped.get(group, []))
        if not cmds:
            continue
        cmd_links = ", ".join([f"[`{cmd}`](#{reference_command_anchor(cmd)})" for cmd in cmds])
        lines.append(f"| `{group}` | `{len(cmds)}` | {cmd_links} |")
    lines.append("")

    lines.append("## Command Pages {#sec-command-pages}")
    lines.append("")
    lines.append(
        "Full command pages follow below. Each page keeps local usage/options snapshots plus dependency links."
    )
    lines.append("")

    INDEX_MD.write_text("\n".join(lines) + "\n")


def main() -> None:
    dep_map = json.loads(DEP_JSON.read_text())
    has_help_map: dict[str, bool] = {}

    for cmd in sorted(dep_map):
        has_help_map[cmd] = write_command_page(cmd, dep_map[cmd])

    write_index(dep_map, has_help_map)

    print(f"Wrote command pages under {REF_DIR}")
    print(f"Wrote {INDEX_MD}")


if __name__ == "__main__":
    main()
