#!/bin/bash
# Build Foldseek documentation as a static HTML site.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS_DIR="${ROOT_DIR}/foldseek_docs"
OUT_DIR="${ROOT_DIR}/public/foldseek"
SHELL_BEFORE_FILE="${ROOT_DIR}/site/templates/docs_shell_before.html"
SHELL_AFTER_FILE="${ROOT_DIR}/site/templates/docs_shell_after.html"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is required to build web docs." >&2
  exit 1
fi

mkdir -p "${OUT_DIR}" "${ROOT_DIR}/public/assets"

pandoc \
  -f markdown-yaml_metadata_block \
  -t html5 \
  --standalone \
  --section-divs \
  --toc \
  --toc-depth=4 \
  --metadata title="Foldseek Documentation" \
  --css ../assets/style.css \
  --include-before-body="${SHELL_BEFORE_FILE}" \
  --include-after-body="${SHELL_AFTER_FILE}" \
  "${DOCS_DIR}/introduction.md" \
  "${DOCS_DIR}/wiki.md" \
  "${DOCS_DIR}/manual.md" \
  "${DOCS_DIR}/submodules/easy_workflows.md" \
  "${DOCS_DIR}/submodules/structure_search.md" \
  "${DOCS_DIR}/submodules/structure_clustering.md" \
  "${DOCS_DIR}/submodules/multimer.md" \
  "${DOCS_DIR}/submodules/structure_manipulation.md" \
  "${DOCS_DIR}/submodules/databases.md" \
  "${DOCS_DIR}/expert_manual.md" \
  "${DOCS_DIR}/developer_manual.md" \
  -o "${OUT_DIR}/index.html"

echo "Foldseek web documentation built: ${OUT_DIR}/index.html"
