#!/usr/bin/env python3
"""Build a command dependency map for MMseqs2 docs.

Inputs:
- MMseqs2/src/MMseqsBase.cpp
- MMseqs2/data/workflow/*.sh
- mmseqs2_docs/submodules/*.md (current command grouping hints)

Outputs:
- mmseqs2_docs/reference/dependency_map.json
- mmseqs2_docs/reference/dependency_map.md
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "mmseqs2_docs"
SRC = ROOT / "MMseqs2"
OUT_JSON = DOCS / "reference" / "dependency_map.json"
OUT_MD = DOCS / "reference" / "dependency_map.md"

GROUP_FILE_TO_NAME = {
    "easy_workflows.md": "easy_workflows",
    "search.md": "search_workflows",
    "clustering.md": "clustering",
    "prefiltering.md": "prefiltering",
    "alignment.md": "alignment",
    "profiles.md": "profiles",
    "database.md": "database",
    "result_handling.md": "result_handling",
    "sequence_manipulation.md": "sequence_manipulation",
    "taxonomy.md": "taxonomy",
    "multi_hit.md": "multi_hit",
    "utilities.md": "utilities",
}

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

NO_EDGE_TEXT = "`n/a`"

SCRIPT_OWNERS = {
    "easysearch.sh": ["easy-search", "easy-linsearch"],
    "easycluster.sh": ["easy-cluster", "easy-linclust"],
    "easyrbh.sh": ["easy-rbh"],
    "easytaxonomy.sh": ["easy-taxonomy"],
    "blastp.sh": ["search"],
    "blastn.sh": ["search"],
    "blastpgp.sh": ["search"],
    "searchtargetprofile.sh": ["search"],
    "searchslicedtargetprofile.sh": ["search"],
    "translated_search.sh": ["search"],
    "iterativepp.sh": ["search"],
    "linsearch.sh": ["linsearch"],
    "map.sh": ["map"],
    "rbh.sh": ["rbh"],
    "linclust.sh": ["linclust"],
    "clustering.sh": ["cluster"],
    "cascaded_clustering.sh": ["cluster"],
    "nucleotide_clustering.sh": ["cluster"],
    "update_clustering.sh": ["clusterupdate"],
    "taxonomy.sh": ["taxonomy"],
    "taxpercontig.sh": ["taxonomy"],
    "createtaxdb.sh": ["createtaxdb"],
    "databases.sh": ["databases"],
    "createindex.sh": ["createindex", "createlinindex"],
    "multihitdb.sh": ["multihitdb"],
    "multihitsearch.sh": ["multihitsearch"],
    "pickconsensusrep.sh": ["pickconsensusrep"],
    "tsv2exprofiledb.sh": ["tsv2exprofiledb"],
}

WORKFLOW_CPP_OWNERS = {
    "Search.cpp": ["search"],
    "Linsearch.cpp": ["linsearch"],
    "Cluster.cpp": ["cluster"],
    "ClusterUpdate.cpp": ["clusterupdate"],
    "Linclust.cpp": ["linclust"],
    "Map.cpp": ["map"],
    "Rbh.cpp": ["rbh"],
    "Taxonomy.cpp": ["taxonomy"],
    "EasySearch.cpp": ["easy-search", "easy-linsearch"],
    "EasyCluster.cpp": ["easy-cluster"],
    "EasyLinclust.cpp": ["easy-linclust"],
    "EasyRbh.cpp": ["easy-rbh"],
    "EasyTaxonomy.cpp": ["easy-taxonomy"],
    "CreateIndex.cpp": ["createindex", "createlinindex"],
    "Databases.cpp": ["databases"],
    "PickConsensusRep.cpp": ["pickconsensusrep"],
}

GROUP_HINT_OVERRIDES = {
    "databases": "database",
    "linsearch": "search_workflows",
    "convert2fasta": "result_handling",
    "createtaxdb": "taxonomy",
    "createbintaxonomy": "taxonomy",
    "createdmptaxonomy": "taxonomy",
    "createbintaxmapping": "taxonomy",
    "addtaxonomy": "taxonomy",
    "taxonomyreport": "taxonomy",
    "filtertaxdb": "taxonomy",
    "filtertaxseqdb": "taxonomy",
    "aggregatetax": "taxonomy",
    "aggregatetaxweights": "taxonomy",
    "lcaalign": "taxonomy",
    "lca": "taxonomy",
    "majoritylca": "taxonomy",
    "pickconsensusrep": "clustering",
    "transitivealign": "alignment",
    "fwbw": "alignment",
    "rmdb": "database",
    "sequence2profile": "profiles",
    "profile2pssm": "profiles",
    "profile2neff": "profiles",
    "profile2consensus": "profiles",
    "profile2repseq": "profiles",
    "convertprofiledb": "profiles",
    "convertca3m": "profiles",
    "expand2profile": "profiles",
    "pairaln": "profiles",
    "diffseqdbs": "utilities",
    "summarizetabs": "utilities",
    "gff2db": "utilities",
    "maskbygff": "utilities",
    "convertkb": "utilities",
    "summarizeheaders": "result_handling",
    "nrtotaxmapping": "taxonomy",
    "extractdomains": "result_handling",
    "countkmer": "prefiltering",
}


def linked_command_list(items: list[str]) -> str:
    if not items:
        return NO_EDGE_TEXT
    return ", ".join(f"[`{x}`](./{x}.md)" for x in items)


def inline_script_list(items: list[str]) -> str:
    if not items:
        return NO_EDGE_TEXT
    return ", ".join(f"`{x}`" for x in items)


def parse_commands() -> dict[str, dict[str, str]]:
    mmseqs_base = (SRC / "src" / "MMseqsBase.cpp").read_text()
    # name, function, category, description
    pattern = re.compile(
        r'\{\s*"([^"]+)"\s*,\s*([A-Za-z0-9_]+)\s*,\s*&par\.[^,]+,\s*([^,\n]+),\s*(?:"([^"]*)"|NULL)',
        re.S,
    )
    commands = {}
    for name, func, category, description in pattern.findall(mmseqs_base):
        category = category.strip()
        if "COMMAND_HIDDEN" in category:
            continue
        commands[name] = {
            "name": name,
            "function": func,
            "category": category,
            "description": description.strip(),
        }

    # `apply` is guarded with a platform-specific preprocessor branch in MMseqsBase.cpp.
    # On non-cygwin builds it is visible as COMMAND_DB; ensure it is not dropped by regex parsing.
    if "apply" not in commands:
        commands["apply"] = {
            "name": "apply",
            "function": "apply",
            "category": "COMMAND_DB",
            "description": "Execute given program on each DB entry",
        }
    return commands


def parse_existing_group_hints() -> dict[str, str]:
    hints = {}
    submodules = DOCS / "submodules"
    for path in sorted(submodules.glob("*.md")):
        group = GROUP_FILE_TO_NAME.get(path.name)
        if not group:
            continue
        text = path.read_text()
        for cmd in re.findall(r"^## `([^`]+)`", text, re.M):
            hints[cmd] = group
    return hints


def category_to_layer(category: str) -> str:
    if "COMMAND_EASY" in category:
        return "workflow"
    if "COMMAND_MAIN" in category:
        return "high_level_api"
    if "COMMAND_PREFILTER" in category:
        return "mid_level_api"
    if "COMMAND_ALIGNMENT" in category:
        return "mid_level_api"
    if "COMMAND_CLUSTER" in category:
        return "mid_level_api"
    if "COMMAND_MULTIHIT" in category:
        return "high_level_api"
    if "COMMAND_TAXONOMY" in category and "COMMAND_MAIN" in category:
        return "high_level_api"
    if "COMMAND_PROFILE_PROFILE" in category:
        return "mid_level_api"
    return "low_level_api"


def infer_group(name: str, category: str, hints: dict[str, str]) -> str:
    if name in GROUP_HINT_OVERRIDES:
        return GROUP_HINT_OVERRIDES[name]
    if name in {"search", "linsearch", "map", "rbh"}:
        return "search_workflows"
    if name in hints:
        return hints[name]
    if "COMMAND_EASY" in category:
        return "easy_workflows"
    if "COMMAND_PREFILTER" in category:
        return "prefiltering"
    if "COMMAND_ALIGNMENT" in category:
        return "alignment"
    if "COMMAND_CLUSTER" in category or name in {"cluster", "linclust", "clusterupdate"}:
        return "clustering"
    if "COMMAND_PROFILE" in category or "COMMAND_PROFILE_PROFILE" in category:
        return "profiles"
    if "COMMAND_TAXONOMY" in category:
        return "taxonomy"
    if "COMMAND_MULTIHIT" in category:
        return "multi_hit"
    if "COMMAND_RESULT" in category or "COMMAND_FORMAT_CONVERSION" in category:
        return "result_handling"
    if "COMMAND_SEQUENCE" in category:
        return "sequence_manipulation"
    if "COMMAND_DATABASE_CREATION" in category or "COMMAND_SET" in category or "COMMAND_STORAGE" in category:
        return "database"
    return "utilities"


def parse_workflow_calls() -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    script_calls: dict[str, set[str]] = defaultdict(set)
    command_scripts: dict[str, set[str]] = defaultdict(set)

    workflow_dir = SRC / "data" / "workflow"
    cmd_pattern = re.compile(
        r"(?:\$RUNNER\s+)?[\"']?\$\{?MMSEQS\}?[\"']?\s+[\"']?([a-z0-9-]+)[\"']?",
        re.I,
    )

    for script in sorted(workflow_dir.glob("*.sh")):
        text = script.read_text()
        script_name = script.name
        called = set(cmd_pattern.findall(text))
        script_calls[script_name] = called
        for cmd in called:
            command_scripts[cmd].add(script_name)

    return script_calls, command_scripts


def parse_workflow_cpp_calls(commands: dict[str, dict[str, str]]) -> dict[str, set[str]]:
    owners_to_calls: dict[str, set[str]] = defaultdict(set)
    workflow_src = SRC / "src" / "workflow"
    cmd_names = set(commands.keys())

    create_param_pattern = re.compile(r"createParameterString\(par\.([A-Za-z0-9_]+)")
    quoted_literal_pattern = re.compile(r"addVariable\(\"[A-Z_]+\",\s*\"([a-z0-9-]+)\"\)", re.I)

    for file_name, owners in WORKFLOW_CPP_OWNERS.items():
        path = workflow_src / file_name
        if not path.exists():
            continue
        text = path.read_text()
        called = set()

        # Most workflow dependencies are exposed through parameter bundles.
        for par_name in create_param_pattern.findall(text):
            if par_name in cmd_names:
                called.add(par_name)

        # Some command names are passed as string literals (e.g. ALIGN_MODULE = "align").
        for cmd_literal in quoted_literal_pattern.findall(text):
            if cmd_literal in cmd_names:
                called.add(cmd_literal)

        for owner in owners:
            owners_to_calls[owner].update(called)

    return owners_to_calls


def build_map() -> dict[str, dict]:
    commands = parse_commands()
    hints = parse_existing_group_hints()
    script_calls, command_scripts = parse_workflow_calls()
    cpp_calls = parse_workflow_cpp_calls(commands)

    # owner command -> called commands
    owner_edges: dict[str, set[str]] = defaultdict(set)
    for script_name, owners in SCRIPT_OWNERS.items():
        called = script_calls.get(script_name, set())
        for owner in owners:
            owner_edges[owner].update(called)
    for owner, called in cpp_calls.items():
        owner_edges[owner].update(called)

    # inverse called-by
    called_by: dict[str, set[str]] = defaultdict(set)
    for owner, downstream in owner_edges.items():
        for cmd in downstream:
            called_by[cmd].add(owner)

    result: dict[str, dict] = {}
    for name, meta in commands.items():
        group = infer_group(name, meta["category"], hints)
        layer = category_to_layer(meta["category"])

        calls = sorted(c for c in owner_edges.get(name, set()) if c in commands)
        upstream = sorted(c for c in called_by.get(name, set()) if c in commands)

        result[name] = {
            "name": name,
            "description": meta["description"],
            "category": meta["category"],
            "layer": layer,
            "primary_group": group,
            "calls": calls,
            "called_by": upstream,
            "workflow_scripts": sorted(command_scripts.get(name, set())),
        }

    return result


def write_outputs(dep_map: dict[str, dict]) -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(dep_map, indent=2, sort_keys=True) + "\n")

    grouped: dict[str, list[str]] = defaultdict(list)
    for cmd, meta in dep_map.items():
        grouped[meta["primary_group"]].append(cmd)

    lines = []
    lines.append("# MMseqs2 Dependency Map")
    lines.append("")
    lines.append("This file is generated from `MMseqs2/src/MMseqsBase.cpp` and workflow scripts.")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("| :--- | :--- |")
    lines.append(f"| Total visible commands | `{len(dep_map)}` |")
    lines.append("")
    lines.append("`n/a` in connection fields means no direct edge was resolved by static extraction.")
    lines.append("")

    for group in GROUP_ORDER:
        commands = sorted(grouped.get(group, []))
        if not commands:
            continue
        lines.append(f"## {group.replace('_', ' ').title()}")
        lines.append("")
        for cmd in commands:
            meta = dep_map[cmd]
            anchor = f"cmd-{cmd.replace('-', '')}"
            lines.append(f"### `{cmd}` {{#{anchor}}}")
            lines.append("")
            if meta["description"]:
                lines.append(meta["description"] + ".")
                lines.append("")
            lines.append("| Aspect | Value |")
            lines.append("| :--- | :--- |")
            lines.append(f"| Layer | `{meta['layer']}` |")
            lines.append(f"| Category flags | `{meta['category']}` |")
            lines.append(f"| Calls | {linked_command_list(meta['calls'])} |")
            lines.append(f"| Called by | {linked_command_list(meta['called_by'])} |")
            lines.append(f"| Workflow scripts | {inline_script_list(meta['workflow_scripts'])} |")
            lines.append(f"| Command reference | [Open page](./{cmd}.md) |")
            lines.append("")

    OUT_MD.write_text("\n".join(lines) + "\n")


def main() -> None:
    dep_map = build_map()
    write_outputs(dep_map)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
