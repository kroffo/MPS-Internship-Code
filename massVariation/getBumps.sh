#!/bin/bash

cd mass

for i in $(ls); do

    cd $i/bumpTrack/LOGS

    if [ ! -d Analysis ]; then
        mkdir Analysis
    fi

    cd Analysis
    cp ../../../../../HRplot.py .
    python HRplot.py
    cp HRdiagram.png ../../../../../plots/"$i"bumpZoom.png
    cd ../../../..

done

cd ..