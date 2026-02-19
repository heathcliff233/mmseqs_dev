#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

"${SCRIPT_DIR}/build_dependency_graph.py"
"${SCRIPT_DIR}/generate_command_reference.py"
"${SCRIPT_DIR}/generate_module_docs.py"
"${SCRIPT_DIR}/validate_docs.py"

cd "${DOCS_DIR}"
./build_pdf.sh

echo "Documentation refresh complete."
