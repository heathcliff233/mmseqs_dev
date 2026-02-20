### `fwbw` {#refcmd-fwbw}

Forward Backward Alignment.

Execution role: core compute module typically called by workflows and advanced custom pipelines.

This command family computes pair quality and coordinates and usually dominates per-pair compute cost after prefiltering. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-fwbw); functional module: [`alignment`](#mod-alignment).

**Usage**

`usage: mmseqs fwbw <inputDB(s)> <outputDB> [options]`

The syntax line above is source-derived from command layer/category metadata. Run `mmseqs fwbw` locally for exact positional arguments in your build.

**Key Options**

Local CLI option snapshots are not available for this command. Use the dependency entry and calling workflow source files to recover parameter bundles for your runtime path.

**Full CLI Help Snapshot**

```{=typst}
#doc_note[
This page keeps a source-derived summary because no local help snapshot was found for this command.
]
```

