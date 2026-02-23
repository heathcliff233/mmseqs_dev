#!/bin/bash
# Build MMseqs2 documentation as a static HTML site.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS_DIR="${ROOT_DIR}/mmseqs2_docs"
OUT_DIR="${ROOT_DIR}/public/mmseqs"
SHELL_BEFORE_FILE="${ROOT_DIR}/site/templates/docs_shell_before_mmseqs.html"
SHELL_AFTER_FILE="${ROOT_DIR}/site/templates/docs_shell_after.html"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is required to build web docs." >&2
  exit 1
fi

mkdir -p "${OUT_DIR}" "${ROOT_DIR}/public/assets"

reference_pages=()
while IFS= read -r page; do
  reference_pages+=("${page}")
done < <(find "${DOCS_DIR}/reference" -maxdepth 1 -type f -name "*.md" ! -name "index.md" ! -name "dependency_map.md" | sort)

pandoc \
  -f markdown-yaml_metadata_block \
  -t html5 \
  --standalone \
  --section-divs \
  --toc \
  --toc-depth=4 \
  --metadata title="MMseqs2 Documentation" \
  --css ../assets/style.css \
  --include-before-body="${SHELL_BEFORE_FILE}" \
  --include-after-body="${SHELL_AFTER_FILE}" \
  "${DOCS_DIR}/introduction.md" \
  "${DOCS_DIR}/foundations.md" \
  "${DOCS_DIR}/system_map.md" \
  "${DOCS_DIR}/manual.md" \
  "${DOCS_DIR}/submodules/easy_workflows.md" \
  "${DOCS_DIR}/submodules/search.md" \
  "${DOCS_DIR}/submodules/clustering.md" \
  "${DOCS_DIR}/submodules/prefiltering.md" \
  "${DOCS_DIR}/submodules/alignment.md" \
  "${DOCS_DIR}/submodules/profiles.md" \
  "${DOCS_DIR}/submodules/database.md" \
  "${DOCS_DIR}/submodules/sequence_manipulation.md" \
  "${DOCS_DIR}/submodules/result_handling.md" \
  "${DOCS_DIR}/submodules/multi_hit.md" \
  "${DOCS_DIR}/submodules/taxonomy.md" \
  "${DOCS_DIR}/submodules/utilities.md" \
  "${DOCS_DIR}/expert_manual.md" \
  "${DOCS_DIR}/developer_manual.md" \
  "${DOCS_DIR}/wiki.md" \
  "${DOCS_DIR}/reference/index.md" \
  "${reference_pages[@]}" \
  "${DOCS_DIR}/reference/dependency_map.md" \
  -o "${OUT_DIR}/index.html"

if [[ -f "${DOCS_DIR}/mmseqs2_doc.pdf" ]]; then
  cp "${DOCS_DIR}/mmseqs2_doc.pdf" "${OUT_DIR}/mmseqs2_doc.pdf"
fi

echo "MMseqs2 web documentation built: ${OUT_DIR}/index.html"
