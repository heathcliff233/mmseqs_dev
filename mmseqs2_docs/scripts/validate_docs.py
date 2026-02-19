#!/usr/bin/env python3
"""Validate structural consistency of MMseqs2 docs."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "mmseqs2_docs"
REF = DOCS / "reference"
SUB = DOCS / "submodules"
DEP_JSON = REF / "dependency_map.json"
HELP = ROOT / "mmseqs_help_output"


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)


def warn(msg: str, warnings: list[str]) -> None:
    warnings.append(msg)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not DEP_JSON.exists():
        fail(f"Missing dependency map: {DEP_JSON}", errors)
        print("\n".join(errors))
        return 1

    dep_map = json.loads(DEP_JSON.read_text())

    # Reference coverage
    for cmd in dep_map:
        page = REF / f"{cmd}.md"
        if not page.exists():
            fail(f"Missing command reference page: {page}", errors)

    if not (REF / "index.md").exists():
        fail("Missing reference index: mmseqs2_docs/reference/index.md", errors)
    if not (REF / "dependency_map.md").exists():
        fail("Missing dependency map markdown: mmseqs2_docs/reference/dependency_map.md", errors)

    # Help snapshot coverage (warning-level)
    missing_help = sorted([cmd for cmd in dep_map if not (HELP / f"{cmd}.txt").exists()])
    if missing_help:
        warn(
            "Missing help snapshots for visible commands: " + ", ".join(missing_help),
            warnings,
        )

    # Submodule command headings
    all_headings = []
    for path in sorted(SUB.glob("*.md")):
        text = path.read_text()
        headings = re.findall(r"^## `([^`]+)`", text, re.M)
        dup = [x for x, c in Counter(headings).items() if c > 1]
        if dup:
            fail(f"Duplicate command headings in {path.name}: {', '.join(dup)}", errors)
        for cmd in headings:
            all_headings.append((cmd, path.name))

        # basic cross-reference link check
        for ref_cmd in re.findall(r"\[Full CLI\]\(\.\./reference/([^)]+)\.md\)", text):
            if not (REF / f"{ref_cmd}.md").exists():
                fail(f"Broken Full CLI link in {path.name}: {ref_cmd}", errors)

    # command appears in one submodule page
    by_cmd = Counter(cmd for cmd, _ in all_headings)
    multi = sorted([cmd for cmd, n in by_cmd.items() if n > 1])
    if multi:
        fail("Commands appearing in multiple submodule pages: " + ", ".join(multi), errors)

    missing_in_submodules = sorted([cmd for cmd in dep_map if cmd not in by_cmd])
    if missing_in_submodules:
        fail(
            "Visible commands missing from submodule docs: " + ", ".join(missing_in_submodules),
            errors,
        )

    print("Validation summary")
    print(f"- visible commands: {len(dep_map)}")
    print(f"- submodule command entries: {len(all_headings)}")
    print(f"- missing help snapshots: {len(missing_help)}")
    print(f"- warnings: {len(warnings)}")
    print(f"- errors: {len(errors)}")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"- {w}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"- {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
