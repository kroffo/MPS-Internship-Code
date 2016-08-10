#!/bin/bash

# A script that takes a command as an argument and applys to all masses

cd mass

for m in $(ls); do
    cd $m/bumpTrack/LOGS/Analysis
    $1
    cd ../../../..
done

cd ..