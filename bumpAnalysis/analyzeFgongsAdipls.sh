#!/bin/bash

if [ -d adipls-frequencies ]; then
    echo "Removing old frequencies directory..."
    rm -rf adipls-frequencies
fi

echo "Setting up freqeuncies..."
mkdir adipls-frequencies
cp maybe_sub.sh adipls-frequencies
cp .adipls-freq-files/* adipls-frequencies
cd ..

echo "Submitting jobs..."
for i in $(ls profile*.data.FGONG); do
    cp $i Analysis/adipls-frequencies
    cd Analysis/adipls-frequencies
    PROFILE=$(echo $i | cut -f1 -d".")
    ./maybe_sub.sh ./analyzeProfileAdipls.sh $PROFILE
    cd ../..
done
