#!/bin/sh -e
# This script implements incremental clustering using MMSeqs2 linsearch and linclust.
# The input arguments require oldSequenceDB, newSequenceDB, oldClusteringDB, newClusteringDB, combSequenceDB, tmpDir.
# We will 
# - re-index newSequenceDB
# - run linsearch to remove new sequences that can be assigned in the old clustering
# - substract the remaining sequences and do linclust on them
# - combine the old and new clusters as well as the sequence databases

# --- Utility Functions ---
fail() {
    echo "Error: $1"
    exit 1
}

notExists() {
    [ ! -f "$1" ]
}

log() {
    echo "=== $1"
}

# --- Input Validation ---
[ "$#" -ne 6 ] && echo "Usage: <i:oldSequenceDB> <i:newSequenceDB> <i:oldClusteringDB> <o:newClusteringDB> <o:combSequenceDB> <o:tmpDir>" && exit 1
[ ! -f "$1.dbtype" ] && fail "$1.dbtype not found!"
[ ! -f "$2.dbtype" ] && fail "$2.dbtype not found!"
[ ! -f "$3.dbtype" ] && fail "$3.dbtype not found!"
[   -f "$4.dbtype" ] && fail "$4.dbtype already exists!"
[   -f "$5.dbtype" ] && fail "$5.dbtype already exists!"
[ ! -d "$6" ] && echo "tmp directory $6 not found, creating it." && mkdir -p "$6"

LINSEARCH_PAR="--min-seq-id 0.3 -c 0.8"
LINCLUST_PAR="--min-seq-id 0.3 -c 0.8"

# --- Variable Setup ---
OLD_SEQ_DB="$1"
NEW_SEQ_DB="$2"
OLD_CLUST_DB="$3"
NEW_CLUST_DB="$4"
COMB_SEQ_DB="$5"
TMP_PATH="$6"
MMSEQS="${MMSEQS:-mmseqs}"

# --- Workflow ---

# 1. Create a key map for the new sequences and re-key the new sequence database and its header database.
if notExists "${TMP_PATH}/key_map.tsv"; then
    log "Creating a key map for new sequences"
    # (LEGACY) Get the last key from the index as the true offset.
    # OFFSET=$(awk 'END{print $1}' "${OLD_SEQ_DB}.index" || echo 0)
    # awk -v offset="$OFFSET" '{print $1"\t"offset + $1}' "${NEW_SEQ_DB}.index" > "${TMP_PATH}/key_map.tsv"
    # (UPDATE) Get the largest key from the index
    OFFSET="$(awk '$1 > max { max = $1 } END { print max }' "${OLD_SEQ_DB}.index")"
    awk -v offset="$OFFSET" '{print $1"\t"offset + $1 + 1}' "${NEW_SEQ_DB}.index" > "${TMP_PATH}/key_map.tsv"
fi

if notExists "${TMP_PATH}/query_seqs.dbtype"; then
    log "Re-keying the new sequence database and headers"
    "$MMSEQS" renamedbkeys "${TMP_PATH}/key_map.tsv" "$NEW_SEQ_DB" "${TMP_PATH}/query_seqs" ${VERBOSITY_PAR} --subdb-mode 1 || fail "renamedbkeys died"
    # 
    # "$MMSEQS" renamedbkeys "${TMP_PATH}/key_map.tsv" "${NEW_SEQ_DB}_h" "${TMP_PATH}/query_seqs_h" ${VERBOSITY_PAR} || fail "renamedbkeys for headers died"
fi

# 2. Unify the sequence space.
# This critical first step creates a single master database containing all sequences,
# which resolves all key and offset conflicts upfront.
if notExists "${COMB_SEQ_DB}.dbtype"; then
    log "Unifying old and new sequence databases"
    "$MMSEQS" concatdbs "$OLD_SEQ_DB" "${TMP_PATH}/query_seqs" "${COMB_SEQ_DB}" --preserve-keys --threads 1 \
        || fail "concatdbs for master DB died"
    "$MMSEQS" concatdbs "${OLD_SEQ_DB}_h" "${TMP_PATH}/query_seqs_h" "${COMB_SEQ_DB}_h" --preserve-keys --threads 1 \
        || fail "concatdbs header for master DB died"
fi
MASTER_SEQ_DB="${COMB_SEQ_DB}"

# 3. Extract representative sequences from the old clustering.
# The unified MASTER_SEQ_DB is used as the context.
if notExists "${TMP_PATH}/old_reps.dbtype"; then
    log "Extracting representative sequences from old clusters"
    "$MMSEQS" result2repseq "$MASTER_SEQ_DB" "$OLD_CLUST_DB" "${TMP_PATH}/old_reps" ${RESULT2REPSEQ_PAR} \
        || fail "result2repseq died"
fi

# 4. Create linindex for old representatives.
if notExists "${TMP_PATH}/old_reps.linidx"; then
    # shellcheck disable=SC2086
    "$MMSEQS" createlinindex "${TMP_PATH}/old_reps" "${TMP_PATH}/index_tmp" ${CREATELININDEX_PAR} \
        || fail "createlinindex died"
fi

# 5. Linsearch for new sequences against old representatives.
if notExists "${TMP_PATH}/linoverlap.dbtype"; then
    log "Linsearch for new sequences against old representatives"
    "$MMSEQS" linsearch "${TMP_PATH}/query_seqs" "${TMP_PATH}/old_reps" "${TMP_PATH}/linoverlap" "${TMP_PATH}/linsearch_tmp" ${LINSEARCH_PAR} \
        || fail "linsearch died"
fi

# 6. Get the best assignment for each new sequence from the LINOVERLAP matches.
if notExists "${TMP_PATH}/new_assignments.dbtype"; then
    log "Filtering for best assignments from rescored matches"
    "$MMSEQS" filterdb "${TMP_PATH}/linoverlap" "${TMP_PATH}/new_hit_top1" --extract-lines 1 ${THREADS_PAR} \
        || fail "filter result for top1 died"
    "$MMSEQS" swapdb "${TMP_PATH}/new_hit_top1" "${TMP_PATH}/new_assignments" ${THREADS_PAR} \
        || fail "swap search result died"
    # "$MMSEQS" filterdb "${TMP_PATH}/linoverlap" "${TMP_PATH}/new_assignments" --trim-to-one-column ${THREADS_PAR} \
    #     || fail "filterdb for assignments died"
fi

# 7. Merge the new assignments into the old clustering DB.
# We use the unified MASTER_SEQ_DB as the first argument, ensuring all keys are found.
UPDATED_CLUST_DB="${TMP_PATH}/updated_clustering.db"
if [ -f "${TMP_PATH}/new_assignments.index" ] && [ -s "${TMP_PATH}/new_assignments.index" ]; then
    if notExists "${UPDATED_CLUST_DB}.dbtype"; then
        log "Merging assigned sequences into the old clustering"
        "$MMSEQS" mergedbs "$OLD_CLUST_DB" "${UPDATED_CLUST_DB}" "$OLD_CLUST_DB" "${TMP_PATH}/new_assignments" ${VERBOSITY_PAR} \
            || fail "mergedbs died"
    fi
else
    UPDATED_CLUST_DB="$OLD_CLUST_DB"
fi

# 8. Extract new sequences that were not assigned to any old cluster.
if notExists "${TMP_PATH}/unassigned_seqs.dbtype"; then
    log "Extracting unassigned new sequences"
    awk '{print $1}' "${TMP_PATH}/new_assignments.index" > "${TMP_PATH}/assigned_keys.list"
    "$MMSEQS" filterdb "${TMP_PATH}/query_seqs" "${TMP_PATH}/unassigned_seqs" --filter-file "${TMP_PATH}/assigned_keys.list" --positive-filter 0 ${VERBOSITY_PAR} \
        || fail "filterdb for unassigned sequences died"
    "$MMSEQS" filterdb "${TMP_PATH}/query_seqs_h" "${TMP_PATH}/unassigned_seqs_h" --filter-file "${TMP_PATH}/assigned_keys.list" --positive-filter 0 ${VERBOSITY_PAR} \
        || fail "filterdb for unassigned sequences header died"
fi

# 9. Cluster the unassigned sequences separately using linclust.
if notExists "${TMP_PATH}/new_clusters.dbtype" && [ -s "${TMP_PATH}/unassigned_seqs.index" ]; then
    log "Clustering unassigned sequences with linclust"
    "$MMSEQS" linclust "${TMP_PATH}/unassigned_seqs" "${TMP_PATH}/new_clusters" "${TMP_PATH}/cluster_tmp" ${LINCLUST_PAR} \
        || fail "linclust for new sequences died"
fi

# 10. Combine the updated old clusters with the newly formed clusters.
if [ -f "${TMP_PATH}/new_clusters.dbtype" ]; then
    if notExists "${NEW_CLUST_DB}.dbtype"; then
        log "Merging updated clustering with new clusters"
        "$MMSEQS" concatdbs "${UPDATED_CLUST_DB}" "${TMP_PATH}/new_clusters" "$NEW_CLUST_DB" --preserve-keys ${THREADS_PAR} \
            || fail "concatdbs died"
    fi
else
    log "No new clusters formed. Final result is the updated clustering."
    "$MMSEQS" mvdb "${UPDATED_CLUST_DB}" "$NEW_CLUST_DB"
fi

echo "Expansion complete. Final clustering is in ${NEW_CLUST_DB}"
