### `pickconsensusrep` {#refcmd-pickconsensusrep}

Select new representatives for each cluster based on consensus.

Execution role: core compute module typically called by workflows and advanced custom pipelines.

This command family controls graph construction and cluster assignment behavior, so early filter decisions strongly affect downstream structure. The current dependency map records 0 upstream caller(s) and 7 downstream call(s), which indicates how broadly parameter changes can propagate.

Typical use case: choose this command when constructing, refining, or updating cluster assignments while preserving explicit coverage/identity criteria.

Dependency entry: [Open in map](#depcmd-pickconsensusrep); functional module: [`clustering`](#mod-clustering).

**Usage**

`usage: mmseqs pickconsensusrep <inputDB(s)> <outputDB> [options]`

The syntax line above is source-derived from command layer/category metadata. Run `mmseqs pickconsensusrep` locally for exact positional arguments in your build.

**Key Options**

Local CLI option snapshots are not available for this command. Use the dependency entry and calling workflow source files to recover parameter bundles for your runtime path.

**Full CLI Help Snapshot**

```{=typst}
#doc_note[
This page keeps a source-derived summary because no local help snapshot was found for this command.
]
```

