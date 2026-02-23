#!/bin/bash
# Build both MMseqs2 and Foldseek static websites for GitHub Pages.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PUBLIC_DIR="${ROOT_DIR}/public"
ASSET_SRC_DIR="${ROOT_DIR}/site/assets"
ASSET_DST_DIR="${PUBLIC_DIR}/assets"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is required to build web docs." >&2
  exit 1
fi

rm -rf "${PUBLIC_DIR}"
mkdir -p "${ASSET_DST_DIR}" "${PUBLIC_DIR}/mmseqs" "${PUBLIC_DIR}/foldseek"

cp -R "${ASSET_SRC_DIR}/." "${ASSET_DST_DIR}/"

"${ROOT_DIR}/scripts/build_mmseqs_web.sh"
"${ROOT_DIR}/scripts/build_foldseek_web.sh"

cat > "${PUBLIC_DIR}/index.html" <<'EOF'
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>MMseqs2 and Foldseek Documentation</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header class="docs-header">
    <div class="docs-header-inner">
      <a class="home-link" href="index.html">Docs Home</a>
      <nav class="product-nav">
        <a href="mmseqs/index.html">MMseqs2 Docs</a>
        <a href="foldseek/index.html">Foldseek Docs</a>
      </nav>
    </div>
  </header>

  <main class="landing">
    <h1>Documentation Sites</h1>
    <p>This repository publishes independent static documentation websites for MMseqs2 and Foldseek.</p>
    <div class="card-grid">
      <a class="doc-card" href="mmseqs/index.html">
        <h2>MMseqs2</h2>
        <p>Sequence-search and clustering documentation, module manual, and command reference.</p>
      </a>
      <a class="doc-card" href="foldseek/index.html">
        <h2>Foldseek</h2>
        <p>Structure-search and multimer documentation with workflow and developer references.</p>
      </a>
    </div>
  </main>
</body>
</html>
EOF

# Avoid Jekyll processing on GitHub Pages.
touch "${PUBLIC_DIR}/.nojekyll"

echo "Static websites built under: ${PUBLIC_DIR}"
