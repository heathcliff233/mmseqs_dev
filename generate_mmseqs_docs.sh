#!/bin/bash

set -euo pipefail

# Check if the mmseqs executable path is provided
if [ -z "${1:-}" ]; then
    echo "Usage: $0 <path_to_mmseqs_executable>"
    exit 1
fi

MMSEQS_EXEC="$1"
if [ ! -x "$MMSEQS_EXEC" ]; then
    echo "Error: '$MMSEQS_EXEC' is not executable"
    exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_CPP="$ROOT_DIR/MMseqs2/src/MMseqsBase.cpp"
OUT_DIR="$ROOT_DIR/mmseqs_help_output"

# Create output directory
mkdir -p "$OUT_DIR"

TMP_CMDS="$(mktemp)"
trap 'rm -f "$TMP_CMDS"' EXIT

# Extract visible (non-hidden) command names from MMseqsBase.cpp
python - "$BASE_CPP" > "$TMP_CMDS" <<'PY'
import re
import sys
from pathlib import Path

text = Path(sys.argv[1]).read_text()
pattern = re.compile(
    r'\{\s*"([^"]+)"\s*,\s*[A-Za-z0-9_]+\s*,\s*&par\.[^,]+,\s*([^,\n]+),',
    re.S,
)
cmds = []
for name, category in pattern.findall(text):
    if "COMMAND_HIDDEN" in category:
        continue
    cmds.append(name)

# `apply` is wrapped in a preprocessor branch and may be skipped by the regex.
# It is visible on non-cygwin builds.
cmds.append("apply")

for cmd in sorted(set(cmds)):
    print(cmd)
PY

TOTAL="$(wc -l < "$TMP_CMDS" | tr -d ' ')"
CUR=0

while IFS= read -r module; do
    CUR=$((CUR + 1))
    out_file="$OUT_DIR/${module}.txt"
    echo "[$CUR/$TOTAL] Getting help for: mmseqs $module"
    if "$MMSEQS_EXEC" "$module" -h > "$out_file" 2>&1; then
        :
    else
        echo "Warning: failed to get help for '$module' (see $out_file)"
    fi
done < "$TMP_CMDS"

echo "All visible-command help outputs saved to '$OUT_DIR'."
