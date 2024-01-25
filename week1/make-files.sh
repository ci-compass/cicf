#!/bin/bash

# Sample shell script
#
# Usage:
#   make-files.sh [file prefix] [number of files]
#
# Make files takes a prefix and a positive integer N. It then creates a bunch of
# files named prefix-1, prefix-2, prefix-3, ..., prefix-N


# Are there two arguments?
if [ $# -ne 2 ]; then
    echo "need two arguments"
    exit 0
fi
# is the second argument a number between 1 and 100?
if (( $2 < 1 || $2 > 100 )); then
    echo "$2 needs to be an integer between 1 and 100"
    exit 1
fi

for i in $(seq $2); do
    echo $i > "$1-$i.txt"
done

