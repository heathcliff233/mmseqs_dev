#!/usr/bin/env python3
"""Generate command reference markdown pages from dependency map + help snapshots."""

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


def reference_group_anchor(group: str) -> str:
    return f"refgroup-{label_slug(group)}"


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


def write_command_page(name: str, meta: dict) -> bool:
    help_file = HELP_DIR / f"{name}.txt"
    has_help = help_file.exists()
    help_text = help_file.read_text() if has_help else ""
    usage, options = parse_usage_and_options(help_text)

    lines = []
    lines.append(f"## `{name}` {{#{reference_command_anchor(name)}}}")
    lines.append("")
    if meta.get("description"):
        lines.append(sentence(meta["description"]))
        lines.append("")

    lines.append("### Classification")
    lines.append("")
    lines.append("| Aspect | Value |")
    lines.append("| :--- | :--- |")
    lines.append(f"| API layer | `{meta['layer']}` |")
    lines.append(
        f"| Primary functional group | [`{meta['primary_group']}`](#{module_anchor(meta['primary_group'])}) |"
    )
    lines.append(f"| Category flags | `{meta['category']}` |")
    lines.append("")

    lines.append("### Topology")
    lines.append("")
    lines.append("| Aspect | Value |")
    lines.append("| :--- | :--- |")
    lines.append(f"| Upstream command count | `{len(meta['called_by'])}` |")
    lines.append(f"| Downstream command count | `{len(meta['calls'])}` |")
    lines.append(f"| Workflow script count | `{len(meta['workflow_scripts'])}` |")
    lines.append(f"| Detailed dependency entry | [Open in map](#{dependency_command_anchor(name)}) |")
    lines.append("")

    lines.append("### Usage")
    lines.append("")
    if usage:
        lines.append(f"`{usage}`")
    else:
        lines.append("No local help snapshot usage line is available.")
    lines.append("")

    lines.append("### Key Options")
    lines.append("")
    if options:
        lines.append("| Option | Purpose |")
        lines.append("| :--- | :--- |")
        for flag, desc in options[:12]:
            lines.append(f"| `{flag}` | {desc} |")
    else:
        lines.append("No parsed options are available for this command.")
    lines.append("")

    lines.append("### Full CLI Help Snapshot")
    lines.append("")
    if has_help:
        lines.append("```text")
        lines.append(help_text.rstrip())
        lines.append("```")
    else:
        lines.extend(
            typst_callout(
                "warning",
                "Help snapshot missing in mmseqs_help_output. Refresh local snapshots before relying on exact options/defaults.",
            )
        )

    lines.append("### Cross References")
    lines.append("")
    lines.append(
        f"See [Dependency map section](#sec-dependency-map), [dependency entry](#{dependency_command_anchor(name)}), "
        + "[command reference index](#sec-command-reference), and "
        + f"[functional module page](#{module_anchor(meta['primary_group'])})."
    )
    lines.append("")

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
    lines.append("This reference is generated from source metadata and local help snapshots.")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("| :--- | :--- |")
    lines.append(f"| Total visible commands | `{len(dep_map)}` |")
    lines.append(f"| Commands with help snapshots | `{sum(has_help_map.values())}` |")
    lines.append(f"| Commands missing snapshots | `{len(missing_help)}` |")
    lines.append("")

    if missing_help:
        lines.extend(
            typst_callout(
                "warning",
                "Some visible commands do not have local help snapshots. Use `generate_mmseqs_docs.sh` to refresh before publishing final CLI defaults.",
            )
        )
        lines.append("| Command | Snapshot status |")
        lines.append("| :--- | :--- |")
        for cmd in missing_help:
            lines.append(f"| `{cmd}` | missing |")
        lines.append("")

    lines.append("Primary maps: [Dependency map](#sec-dependency-map).")
    lines.append("")

    for group in GROUP_ORDER:
        cmds = sorted(grouped.get(group, []))
        if not cmds:
            continue
        lines.append(f"## {group.replace('_', ' ').title()} {{#{reference_group_anchor(group)}}}")
        lines.append("")
        lines.append("| Command | Layer | Snapshot |")
        lines.append("| :--- | :--- | :--- |")
        for cmd in cmds:
            status = "help" if has_help_map.get(cmd, False) else "missing-help"
            lines.append(f"| [`{cmd}`](#{reference_command_anchor(cmd)}) | `{dep_map[cmd]['layer']}` | `{status}` |")
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
