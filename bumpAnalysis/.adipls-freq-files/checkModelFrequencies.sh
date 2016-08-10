#!/bin/bash

if [ -e errors.txt ]; then
    rm errors.txt
fi

for i in $(seq 1 1622); do
    python checkFrequencies.py profile$i-freqs.dat
done

if [ -s errors.txt ]; then
    echo "No errors! Congrats!" >> errors.txt
fi