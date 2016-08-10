#!/bin/bash

for i in $(ls mass); do
    cp mass/$i/bumpTrack/LOGS/Analysis/Plots/superPlot.png superPlots/"$i".png
done