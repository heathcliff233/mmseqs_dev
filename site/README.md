# Documentation Website Build

This repository can publish static HTML documentation for both products:

- `public/mmseqs/index.html`
- `public/foldseek/index.html`

Build commands:

```bash
bash scripts/build_mmseqs_web.sh
bash scripts/build_foldseek_web.sh
bash scripts/build_docs_web.sh
```

Local preview:

```bash
bash scripts/preview_docs_web.sh 8000
```

Deployment is handled by `.github/workflows/deploy-docs-pages.yml` via GitHub Pages.
