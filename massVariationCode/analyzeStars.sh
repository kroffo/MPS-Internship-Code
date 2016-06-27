#!/bin/bash

cd mass

for i in $(ls); do
    echo "Analyzing $i..."
    cd $i/LOGS
    if [ -d "Analysis" ]; then
        rm -rf Analysis
    fi
    mkdir Analysis
    cd Analysis
    less ../history.data | awk '{ print $3"\t"$2"\t"$37"\t"$35"\t"$38 }' |
    sed -e '1,5d' > MALTR.dat
    cp ../../../../HRplot.py .
    cp ../../../../locateBump.py .
    python locateBump.py
    python HRplot.py
    cd ../../..
done
cd ..
if [ -d "plots" ]; then
    rm -rf plots
fi
./grabPlots.sh
