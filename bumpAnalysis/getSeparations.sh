#!/bin/bash

N=$(ls adipls-frequencies/profile*-freqs.dat | wc -l)

echo "Creating Separations directories for results..."
cd Data
if [ -d Separations ]; then
    rm -rf Separations
fi
mkdir Separations
cd ../Plots
if [ -d Separations ]; then
    rm -rf Separations
fi
mkdir Separations
cd ..

echo "Submitting jobs..."

i="1"
while [ $i -le $N ]; do
    ./maybe_sub.sh python calculateSeparations.py $i
    i=$[$i+1]
done

echo "Done."