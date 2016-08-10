#!/bin/bash

cd Data
if [ -d vfactors ]; then
    rm -rf vfactors;
fi
mkdir vfactors
cd ..

N=$(ls ../profile*.data | wc -l)

# Find vfactors for each profile in parallel to drastically reduce time.
for i in $(seq 1 $N); do
    ./maybe_sub.sh python findVfactors.py $i
done
