#!/bin/bash
# Build and preview docs website locally.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${1:-8000}"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 is required for local preview." >&2
  exit 1
fi

"${ROOT_DIR}/scripts/build_docs_web.sh"
cd "${ROOT_DIR}/public"
echo "Serving docs at http://localhost:${PORT}"
python3 -m http.server "${PORT}"
