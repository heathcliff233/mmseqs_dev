#!/bin/bash
# Build PDF documentation for MMseqs2
set -euo pipefail

# Always run from the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

pick_pdf_engine() {
  local help_text
  help_text="$(pandoc --help 2>/dev/null || true)"

  if command -v typst >/dev/null 2>&1; then
    echo "typst"
    return
  fi
  if command -v xelatex >/dev/null 2>&1; then
    echo "xelatex"
    return
  fi
  if command -v pdflatex >/dev/null 2>&1; then
    echo "pdflatex"
    return
  fi
  echo ""
}

PDF_ENGINE="$(pick_pdf_engine)"
if [ -z "$PDF_ENGINE" ]; then
  echo "Error: no supported PDF engine found (typst/xelatex/pdflatex)." >&2
  exit 1
fi

if [ "$PDF_ENGINE" != "typst" ]; then
  echo "Warning: typst engine not available in this environment; falling back to '$PDF_ENGINE'." >&2
fi

# Order:
# cover -> intro -> sharp bits -> system map -> foundations -> functional manual/submodules -> expert
# -> appendices/reference indexes
pandoc \
  -f markdown-yaml_metadata_block \
  --pdf-engine="$PDF_ENGINE" \
  --lua-filter=fix-rule.lua \
  cover.md \
  numbering.md \
  toc.md \
  introduction.md \
  sharp_bits.md \
  system_map.md \
  foundations.md \
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
  appendix_wiki_reference.md \
  appendix_developer.md \
  reference/index.md \
  reference/dependency_map.md \
  -o mmseqs2_doc.pdf

echo "MMseqs2 PDF documentation built successfully: mmseqs2_doc.pdf"
