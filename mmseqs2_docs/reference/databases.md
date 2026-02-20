### `databases` {#refcmd-databases}

List and download databases.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family enforces DB contracts and storage/index integrity used by all workflows. The current dependency map records 0 upstream caller(s) and 8 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when preparing or restructuring DB artifacts to satisfy downstream module contracts.

Dependency entry: [Open in map](#depcmd-databases); functional module: [`database`](#mod-database).

**Usage**

`usage: mmseqs databases <DB> [args] [options]`

The syntax line above is source-derived from command layer/category metadata. Run `mmseqs databases` locally for exact positional arguments in your build.

**Key Options**

Local CLI option snapshots are not available for this command. Use the dependency entry and calling workflow source files to recover parameter bundles for your runtime path.

**Full CLI Help Snapshot**

```{=typst}
#doc_note[
This page keeps a source-derived summary because no local help snapshot was found for this command.
]
```

