#!/bin/bash

cd mass

for i in $(ls mass); do
    echo "Analyzing $i..."
    cd $i/LOGS/Analysis
    if [ -d "gyre" ]; then
        cd gyre
        find *.FGONG -name . -o -prune | head -1 | xargs -i bash -c "echo start {}; maybe_sub.sh fgong2freqs-gyre.sh {}; echo end {}"
        cd ..
    fi
    cd ../../..
done

cd ..