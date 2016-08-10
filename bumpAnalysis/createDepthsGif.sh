#!/bin/bash

### Creates a gif showing how the radius, convective depth, and discontinuity
### move across the track

mkdir .DepthPlots

echo "Creating plots..."
python .plotDepthsPlots.py

echo "Creating gif..."
cd .DepthPlots
convert *.png Depths.gif
mv Depths.gif ..
cd ..

echo "Cleaning up..."

rm -rf .DepthPlots

echo "Finished."