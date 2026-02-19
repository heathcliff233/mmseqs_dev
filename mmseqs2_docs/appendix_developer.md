# Appendix B: Developer Reference

Developer maintenance should start from generated artifacts, then fall back to narrative chapters when additional context is needed.

| Maintenance Need | Primary Artifact |
| :--- | :--- |
| Canonical architecture and performance foundations | `system_map.md`, `foundations.md` |
| Command topology and cascade edges | `reference/dependency_map.md` |
| Command catalog and snapshot coverage | `reference/index.md` |
| Dependency extraction logic | `scripts/build_dependency_graph.py` |
| Command page generation | `scripts/generate_command_reference.py` |
| Functional module generation | `scripts/generate_module_docs.py` |
| Structural consistency checks | `scripts/validate_docs.py` |

Legacy developer-oriented prose is preserved in `developer_manual.md`.
