### `aggregatetaxweights` {#refcmd-aggregatetaxweights}

Aggregate multiple taxon labels to a single label.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family maps sequence evidence into taxonomy labels and reports under explicit aggregation rules. The current dependency map records 1 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when you need explicit control of this stage instead of relying on workflow defaults.

Dependency entry: [Open in map](#depcmd-aggregatetaxweights); functional module: [`taxonomy`](#mod-taxonomy).

**Usage**

`usage: mmseqs aggregatetaxweights <DB> [args] [options]`

The syntax line above is source-derived from command layer/category metadata. Run `mmseqs aggregatetaxweights` locally for exact positional arguments in your build.

**Key Options**

Local CLI option snapshots are not available for this command. Use the dependency entry and calling workflow source files to recover parameter bundles for your runtime path.

**Full CLI Help Snapshot**

```{=typst}
#doc_note[
This page keeps a source-derived summary because no local help snapshot was found for this command.
]
```

