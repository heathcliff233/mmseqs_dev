# Appendix B: Developer Reference {#sec-appendix-developer}

Developer maintenance should start from generated artifacts, then fall back to narrative chapters when additional context is needed.

| Maintenance Need | Primary Artifact |
| :--- | :--- |
| Canonical architecture and performance foundations | [System Map](#sec-system-map), [Performance Foundations](#sec-performance-foundations) |
| Command topology and cascade edges | [Dependency Map](#sec-dependency-map) |
| Command catalog and snapshot coverage | [Command Reference Index](#sec-command-reference) |
| Dependency extraction logic | `scripts/build_dependency_graph.py` |
| Command page generation | `scripts/generate_command_reference.py` |
| Functional module generation | `scripts/generate_module_docs.py` |
| Structural consistency checks | `scripts/validate_docs.py` |

Legacy developer-oriented prose is preserved in `developer_manual.md`.
