#!/bin/bash
# Build PDF documentation for Foldseek
set -euo pipefail

# Always run from the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Build PDF from separate source files (no concatenation) with a TOC
# Order: cover → intro → user guide → manual → submodules → expert → developer
pandoc \
  -f markdown-yaml_metadata_block \
  --pdf-engine=typst \
  --lua-filter=fix-rule.lua \
  cover.md \
  numbering.md \
  toc.md \
  introduction.md \
  wiki.md \
  manual.md \
  submodules/easy_workflows.md \
  submodules/structure_search.md \
  submodules/structure_clustering.md \
  submodules/multimer.md \
  submodules/structure_manipulation.md \
  submodules/databases.md \
  expert_manual.md \
  developer_manual.md \
  -o foldseek_doc.pdf

echo "Foldseek PDF documentation built successfully: foldseek_doc.pdf"
