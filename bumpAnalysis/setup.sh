#!/bin/bash

# Initialize Data directory, where calculated values should be stored.
if [ -d Data ]; then
    rm -rf Data
fi
mkdir Data
cd Data

# Write the number of profiles to a file for other scripts to read
echo $(ls ../../profile*.data | wc -l) >> number_of_profiles.dat

cd ..

# Initialize Plots directory, where plots should be stored
if [ -d Plots ]; then
    rm -rf Plots
fi
mkdir Plots

### Grab some data ###

echo "Setting up MALTR.dat..."
./getMALTRdata.sh

echo "Locating bump..."
python locateBump.py
mv critPoints.dat Data/critPoints.dat

python HRplot.py

echo "Done."