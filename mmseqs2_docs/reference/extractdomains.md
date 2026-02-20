### `extractdomains` {#refcmd-extractdomains}

Extract highest scoring alignment regions for each sequence from BLAST-tab file.

Execution role: low-level command used for DB management, conversion, and pipeline composition.

This command family reshapes and exports outputs; interpretation must remain consistent with upstream scoring modes. The current dependency map records 0 upstream caller(s) and 0 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when transforming or exporting result DBs after scoring decisions are already fixed upstream.

Dependency entry: [Open in map](#depcmd-extractdomains); functional module: [`result_handling`](#mod-result-handling).

**Usage**

`usage: mmseqs extractdomains <DB> [args] [options]`

The syntax line above is source-derived from command layer/category metadata. Run `mmseqs extractdomains` locally for exact positional arguments in your build.

**Key Options**

Local CLI option snapshots are not available for this command. Use the dependency entry and calling workflow source files to recover parameter bundles for your runtime path.

**Full CLI Help Snapshot**

```{=typst}
#doc_note[
This page keeps a source-derived summary because no local help snapshot was found for this command.
]
```

