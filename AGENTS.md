# AGENTS.md

This is the meta agent guide for this repository.  
Use it to decide whether to follow `AGENTS_mmseqs.md`, `AGENTS_foldseek.md`, or both.

## Routing Rules

Use `AGENTS_mmseqs.md` when the task primarily targets:

- `MMseqs2/`
- `mmseqs2_docs/`
- `mmseqs_help_output/`
- `generate_mmseqs_docs.sh`

Use `AGENTS_foldseek.md` when the task primarily targets:

- `foldseek/`
- `foldseek_docs/`
- `foldseek_help_output/`
- `generate_foldseek_docs.sh`

Use both guides when the task spans both systems (for example shared design, cross-tool comparison, or synchronized documentation updates).

## Switching Protocol

1. Identify target scope by files and user intent.
2. Load only the relevant guide(s):
   - MMseqs-only: `AGENTS_mmseqs.md`
   - Foldseek-only: `AGENTS_foldseek.md`
   - Mixed scope: both
3. Keep boundaries explicit in the output:
   - clearly label MMseqs changes vs Foldseek changes
   - avoid mixing command semantics between tools
4. If policies conflict, prefer the guide that matches the file you are editing.

## Submodule Note

`MMseqs2/` and `foldseek/` are upstream git submodules.  
If code directories are missing after clone, initialize them with:

```bash
git submodule update --init --recursive
```

## Quick Intent Map

- “MMseqs docs/manual/reference update” -> `AGENTS_mmseqs.md`
- “Foldseek docs/manual/reference update” -> `AGENTS_foldseek.md`
- “Keep both manuals aligned” -> both guides
