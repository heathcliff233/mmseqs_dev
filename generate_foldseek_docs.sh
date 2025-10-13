#!/bin/bash

# Check if the foldseek executable path is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_foldseek_executable>"
    exit 1
fi

FOLDSEEK_EXEC="$1"

# Create a directory to store the help output
mkdir -p foldseek_help_output

# List of all user-facing Foldseek command-line modules
# Based strictly on the actual modules present in foldseek_help_output directory
MODULES=(
    # Easy workflow modules
    "easy-search"
    "easy-cluster"
    "easy-rbh"
    "easy-multimersearch"
    "easy-multimercluster"

    # Core workflow modules
    "search"
    "cluster"
    "rbh"
    "multimersearch"
    "multimercluster"

    # Database management modules
    "createdb"
    "databases"
    "createindex"
    "createclusearchdb"

    # Alignment modules
    "tmalign"
    "structurealign"
    "structurerescorediagonal"
    "aln2tmscore"
    "scoremultimer"

    # Utility modules
    "result2profile"
    "clust"
    "convertalis"
    "convert2pdb"
    "createmultimerreport"
    "expandmultimer"
    "compressca"
)

# Iterate through the modules and get their help output
for module in "${MODULES[@]}"; do
    echo "Getting help for: foldseek $module"
    # Execute the command and save output to a file
    "${FOLDSEEK_EXEC}" "$module" -h > "foldseek_help_output/${module}.txt" 2>&1
    if [ $? -ne 0 ]; then
        echo "Error getting help for $module. Check foldseek_help_output/${module}.txt for details."
    fi
done

echo "All help outputs saved to the 'foldseek_help_output' directory."