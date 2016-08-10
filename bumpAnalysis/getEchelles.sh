#!/bin/bash

# Runs echelle.py on every profile for this track.
# Plots stored in Plots/EchelleDiagrams
# Passes the first command line argument as the max
# l mode to plot on the echelle diagrams.

N=$(ls adipls-frequencies/profile*-freqs.dat | wc -l)

cd Plots
if [ -d EchelleDiagrams ]; then
    rm -rf EchelleDiagrams
fi
mkdir EchelleDiagrams
cd ..

i="1"
while [ $i -le $N ]; do
    ./maybe_sub.sh python plotEchelle.py $i $1
    i=$[$i+1]
done