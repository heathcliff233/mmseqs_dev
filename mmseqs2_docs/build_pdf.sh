#!/bin/bash
# Build PDF documentation for MMseqs2
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
  submodules/search.md \
  submodules/clustering.md \
  submodules/prefiltering.md \
  submodules/alignment.md \
  submodules/profiles.md \
  submodules/database.md \
  submodules/sequence_manipulation.md \
  submodules/result_handling.md \
  submodules/multi_hit.md \
  submodules/taxonomy.md \
  submodules/utilities.md \
  expert_manual.md \
  developer_manual.md \
  -o mmseqs2_doc.pdf

echo "MMseqs2 PDF documentation built successfully: mmseqs2_doc.pdf"
