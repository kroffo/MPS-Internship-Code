#!/bin/bash

# Runs plotPropagationDiagram.py on every profile for this track.
# Plots stored in Plots/PropagationDiagrams
# Passes the first command line argument as the x-axis variable to the program
#     (Either r or m for fractional radius or mass)

N=$(ls adipls-frequencies/profile*-freqs.dat | wc -l)

cd Plots
if [ -d PropagationDiagrams ]; then
    rm -rf PropagationDiagrams
fi
mkdir PropagationDiagrams
cd ..

i="1"
while [ $i -le $N ]; do
    ./maybe_sub.sh python plotPropagationDiagram.py $i $1
    i=$[$i+1]
done