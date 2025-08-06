#!/bin/bash

# CICF Week 1 Exercise 2
#
# Redirection
#
# Make a file `source.txt` that consists of 100 random numbers.
# Then sort the numbers into a second file named `sorted.txt`

# create the source file
for i in $(seq 100); do
    echo $RANDOM
done > source.txt

# now sort the file into `sorted.txt`

# replace this line
cp source.txt sorted.txt
