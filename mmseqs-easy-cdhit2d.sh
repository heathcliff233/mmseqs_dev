#!/bin/sh -e

# This script filters a query FASTA/DB file against a target FASTA/DB file.
# It removes any sequences from the query that are found to be similar to sequences in the target.
# It can output results as FASTA files or MMseqs2 databases.

# --- Utility Functions ---
fail() {
    echo "Error: $1"
    exit 1
}

log() {
    echo "--- $1 ---"
}

# --- Input Validation ---
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <target> <query> <filtered_output> <matches_basename>"
    echo "Inputs <target> and <query> can be FASTA files or MMseqs2 databases."
    echo "If both inputs are DBs, <filtered_output> will be a DB, and a matches DB will be created from <matches_basename>."
    echo "Otherwise, <filtered_output> will be a FASTA file."
    exit 1
fi

TARGET_INPUT="$1"
QUERY_INPUT="$2"
FILTERED_OUTPUT="$3"
MATCHES_BASENAME="$4"
MATCHES_TSV="${MATCHES_BASENAME}.tsv"

# --- Variable Setup ---
TMP_PATH=$(mktemp -d -t mmseqs-cdhit2d.XXXXXX)
MMSEQS="${MMSEQS:-mmseqs}"
trap 'rm -rf "${TMP_PATH}"' EXIT

# --- Workflow ---

# 1. Prepare input databases
log "Preparing databases"
IS_DB_INPUT=false
if [ -f "${TARGET_INPUT}.dbtype" ] && [ -f "${QUERY_INPUT}.dbtype" ]; then
    IS_DB_INPUT=true
fi

if [ "$IS_DB_INPUT" = true ]; then
    TARGET_DB_PATH="${TARGET_INPUT}"
    QUERY_DB_PATH="${QUERY_INPUT}"
else
    if [ -f "${TARGET_INPUT}.dbtype" ]; then
        TARGET_DB_PATH="${TARGET_INPUT}"
    else
        [ ! -f "$TARGET_INPUT" ] && fail "Target FASTA file not found: $TARGET_INPUT"
        TARGET_DB_PATH="${TMP_PATH}/target_db"
        "$MMSEQS" createdb "$TARGET_INPUT" "$TARGET_DB_PATH" ${CREATEDB_PAR} || fail "createdb for target failed"
    fi
    if [ -f "${QUERY_INPUT}.dbtype" ]; then
        QUERY_DB_PATH="${QUERY_INPUT}"
    else
        [ ! -f "$QUERY_INPUT" ] && fail "Query FASTA file not found: $QUERY_INPUT"
        QUERY_DB_PATH="${TMP_PATH}/query_db"
        "$MMSEQS" createdb "$QUERY_INPUT" "$QUERY_DB_PATH" ${CREATEDB_PAR} || fail "createdb for query failed"
    fi
fi

# 2. Create linear index for the target database
log "Creating index for target database"
# shellcheck disable=SC2086
"$MMSEQS" createlinindex "$TARGET_DB_PATH" "${TMP_PATH}/index_tmp" ${CREATELININDEX_PAR} \
    || fail "createlinindex died"

# 3. Search query against target
log "Searching for similar sequences using linsearch"
# shellcheck disable=SC2086
"$MMSEQS" linsearch "$QUERY_DB_PATH" "$TARGET_DB_PATH" "${TMP_PATH}/search_res" "${TMP_PATH}/tmp_search" ${LINSEARCH_PAR} \
    || fail "linsearch died"

# 4. Identify and filter out matched query sequences
log "Filtering out similar sequences"
if [ -s "${TMP_PATH}/search_res.index" ]; then
    if [ "$IS_DB_INPUT" = true ]; then
        log "Creating matches database from search result"
# shellcheck disable=SC2086
        "$MMSEQS" filterdb "${TMP_PATH}/search_res" "$MATCHES_BASENAME" --trim-to-one-column ${THREADS_PAR} \
            || fail "filterdb for matches failed"
        log "Matches DB written to $MATCHES_BASENAME"

        log "Creating matches TSV from matches DB"
# shellcheck disable=SC2086
        "$MMSEQS" createtsv "$QUERY_DB_PATH" "$TARGET_DB_PATH" "$MATCHES_BASENAME" "$MATCHES_TSV" ${THREADS_PAR} \
            || fail "createtsv for matches failed"

        awk '{print $1}' "${MATCHES_BASENAME}.index" > "${TMP_PATH}/assigned_keys.list"
    else
# shellcheck disable=SC2086
        "$MMSEQS" createtsv "$QUERY_DB_PATH" "$TARGET_DB_PATH" "${TMP_PATH}/search_res" "$MATCHES_TSV" ${THREADS_PAR} \
            || fail "createtsv died"
        cut -f1 "$MATCHES_TSV" | sort -u > "${TMP_PATH}/assigned_keys.list"
    fi
    log "Matches TSV written to $MATCHES_TSV"

# shellcheck disable=SC2086
    "$MMSEQS" filterdb "$QUERY_DB_PATH" "${TMP_PATH}/query_db_filtered" --filter-file "${TMP_PATH}/assigned_keys.list" --positive-filter 0 ${VERBOSITY_PAR} \
        || fail "filterdb for unassigned died"
    FILTERED_QUERY_DB="${TMP_PATH}/query_db_filtered"
else
    log "No similar sequences found. Keeping all query sequences."
    touch "$MATCHES_TSV"
    if [ "$IS_DB_INPUT" = true ]; then
        touch "${MATCHES_BASENAME}.dbtype"
    fi
    FILTERED_QUERY_DB="$QUERY_DB_PATH"
fi

# 5. Output the filtered query sequences
log "Writing filtered output to $FILTERED_OUTPUT"
if [ "$IS_DB_INPUT" = true ]; then
    if [ "$FILTERED_QUERY_DB" = "$QUERY_DB_PATH" ]; then
        "$MMSEQS" concatdbs "$QUERY_DB_PATH" "$FILTERED_OUTPUT" || fail "DB copy failed"
    else
        "$MMSEQS" mvdb "$FILTERED_QUERY_DB" "$FILTERED_OUTPUT" || fail "mvdb failed"
    fi
else
    if [ -s "${FILTERED_QUERY_DB}.index" ]; then
        "$MMSEQS" convert2fasta "$FILTERED_QUERY_DB" "$FILTERED_OUTPUT" || fail "convert2fasta died"
    else
        log "All query sequences were filtered out. Output file will be empty."
        touch "$FILTERED_OUTPUT"
    fi
fi

log "Done."