### `countkmer` {#refcmd-countkmer}

Count k-mers.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family is the main acceleration gate that prunes candidate pairs before expensive alignment. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command in custom pipelines that must expose candidate-generation behavior before alignment stages.

Dependency entry: [Open in map](#depcmd-countkmer); functional module: [`prefiltering`](#mod-prefiltering).

**Usage**

`usage: mmseqs countkmer <DB> [args] [options]`

The syntax line above is source-derived from command layer/category metadata. Run `mmseqs countkmer` locally for exact positional arguments in your build.

**Key Options**

Local CLI option snapshots are not available for this command. Use the dependency entry and calling workflow source files to recover parameter bundles for your runtime path.

**Full CLI Help Snapshot**

```{=typst}
#doc_note[
This page keeps a source-derived summary because no local help snapshot was found for this command.
]
```

