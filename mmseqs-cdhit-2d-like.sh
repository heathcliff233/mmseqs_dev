#!/bin/sh -e
# This script implements a CD-HIT 2D-like workflow using MMSeqs2.
# It searches new sequences against old representative sequences,
# outputs remaining sequences as FASTA and assignments as TSV.
# The input arguments require oldSequenceDB, newSequenceDB, oldClusteringDB, outputFasta, outputTsv, tmpDir.

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

abspath() {
    if [ -d "$1" ]; then
        (cd "$1"; pwd)
    elif [ -f "$1" ]; then
        if [ -z "${1##*/*}" ]; then
            echo "$(cd "${1%/*}"; pwd)/${1##*/}"
        else
            echo "$(pwd)/$1"
        fi
    elif [ -d "$(dirname "$1")" ]; then
        echo "$(cd "$(dirname "$1")"; pwd)/$(basename "$1")"
    fi
}

# --- Input Validation ---
[ "$#" -ne 6 ] && echo "Usage: <i:oldSequenceDB> <i:newSequenceDB> <i:oldClusteringDB> <o:outputFasta> <o:outputTsv> <o:tmpDir>" && exit 1
[ ! -f "$1.dbtype" ] && fail "$1.dbtype not found!"
[ ! -f "$2.dbtype" ] && fail "$2.dbtype not found!"
[ ! -f "$3.dbtype" ] && fail "$3.dbtype not found!"
[   -f "$4" ] && fail "$4 already exists!"
[   -f "$5" ] && fail "$5 already exists!"
[ ! -d "$6" ] && echo "tmp directory $6 not found, creating it." && mkdir -p "$6"

LINSEARCH_PAR="--min-seq-id 0.3 -c 0.8"

# --- Variable Setup ---
OLD_SEQ_DB="$1"
NEW_SEQ_DB="$2"
OLD_CLUST_DB="$3"
OUTPUT_FASTA="$4"
OUTPUT_TSV="$5"
TMP_PATH="$6"
MMSEQS="${MMSEQS:-mmseqs}"

# --- Workflow ---

# 1. Create a key map for the new sequences and re-key the new sequence database and its header database.
if notExists "${TMP_PATH}/key_map.tsv"; then
    log "Creating a key map for new sequences"
    # Get the largest key from the old index
    OFFSET="$(awk '$1 > max { max = $1 } END { print max }' "${OLD_SEQ_DB}.index")"
    awk -v offset="$OFFSET" '{print $1"\t"offset + $1 + 1}' "${NEW_SEQ_DB}.index" > "${TMP_PATH}/key_map.tsv"
fi

if notExists "${TMP_PATH}/query_seqs.dbtype"; then
    log "Re-keying the new sequence database and headers"
    "$MMSEQS" renamedbkeys "${TMP_PATH}/key_map.tsv" "$NEW_SEQ_DB" "${TMP_PATH}/query_seqs" ${VERBOSITY_PAR} --subdb-mode 1 || fail "renamedbkeys died"
    "$MMSEQS" renamedbkeys "${TMP_PATH}/key_map.tsv" "${NEW_SEQ_DB}_h" "${TMP_PATH}/query_seqs_h" ${VERBOSITY_PAR} || fail "renamedbkeys for headers died"
fi

# 2. Extract representative sequences from the old clustering.
if notExists "${TMP_PATH}/old_reps.dbtype"; then
    log "Extracting representative sequences from old clusters"
    "$MMSEQS" result2repseq "$OLD_SEQ_DB" "$OLD_CLUST_DB" "${TMP_PATH}/old_reps" ${RESULT2REPSEQ_PAR} \
        || fail "result2repseq died"
fi

# 3. Create linindex for old representatives.
if notExists "${TMP_PATH}/old_reps.linidx"; then
    log "Creating linindex for old representatives"
    "$MMSEQS" createlinindex "${TMP_PATH}/old_reps" "${TMP_PATH}/index_tmp" ${CREATELININDEX_PAR} \
        || fail "createlinindex died"
fi

# 4. Linsearch for new sequences against old representatives.
if notExists "${TMP_PATH}/linoverlap.dbtype"; then
    log "Linsearch for new sequences against old representatives"
    "$MMSEQS" linsearch "${TMP_PATH}/query_seqs" "${TMP_PATH}/old_reps" "${TMP_PATH}/linoverlap" "${TMP_PATH}/linsearch_tmp" ${LINSEARCH_PAR} \
        || fail "linsearch died"
fi

# 5. Get the best assignment for each new sequence from the LINOVERLAP matches.
if notExists "${TMP_PATH}/new_assignments.dbtype"; then
    log "Filtering for best assignments from rescored matches"
    "$MMSEQS" filterdb "${TMP_PATH}/linoverlap" "${TMP_PATH}/new_hit_top1" --extract-lines 1 ${THREADS_PAR} \
        || fail "filter result for top1 died"
    "$MMSEQS" swapdb "${TMP_PATH}/new_hit_top1" "${TMP_PATH}/new_assignments" ${THREADS_PAR} \
        || fail "swap search result died"
fi

# 6. Extract new sequences that were not assigned to any old cluster.
if notExists "${TMP_PATH}/unassigned_seqs.dbtype"; then
    log "Extracting unassigned new sequences"
    awk '{print $1}' "${TMP_PATH}/new_assignments.index" > "${TMP_PATH}/assigned_keys.list"
    "$MMSEQS" filterdb "${TMP_PATH}/query_seqs" "${TMP_PATH}/unassigned_seqs" --filter-file "${TMP_PATH}/assigned_keys.list" --positive-filter 0 ${VERBOSITY_PAR} \
        || fail "filterdb for unassigned sequences died"
    "$MMSEQS" filterdb "${TMP_PATH}/query_seqs_h" "${TMP_PATH}/unassigned_seqs_h" --filter-file "${TMP_PATH}/assigned_keys.list" --positive-filter 0 ${VERBOSITY_PAR} \
        || fail "filterdb for unassigned sequences header died"
fi

# 7. Convert unassigned sequences to FASTA format
if notExists "${OUTPUT_FASTA}"; then
    log "Converting unassigned sequences to FASTA"
    "$MMSEQS" convert2fasta "${TMP_PATH}/unassigned_seqs" "${OUTPUT_FASTA}" ${VERBOSITY_PAR} \
        || fail "convert2fasta died"
fi

# 8. Convert assignments to TSV format
if notExists "${OUTPUT_TSV}"; then
    log "Converting assignments to TSV"
    "$MMSEQS" createtsv "${TMP_PATH}/query_seqs" "${TMP_PATH}/old_reps" "${TMP_PATH}/new_assignments" "${OUTPUT_TSV}" ${VERBOSITY_PAR} \
        || fail "createtsv died"
fi

log "CD-HIT 2D-like workflow complete. Results in ${OUTPUT_FASTA} and ${OUTPUT_TSV}"