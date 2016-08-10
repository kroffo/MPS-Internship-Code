#!/bin/bash

mkdir plots

for i in $(ls mass); do
    cp mass/$i/LOGS/Analysis/bump.png plots/"$i"bump.png
    cp mass/$i/LOGS/Analysis/HRWithBump.png plots/"$i"HR.png
done