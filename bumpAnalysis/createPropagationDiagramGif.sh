#!/bin/bash

# Creates a gif from the $1th profile to the $2th profile of Propagation
# Diagrams labeled Plots/Propagation$1-$2.gif
#
# Note: This submits jobs to the cluster, and waits for there to be no more jobs
#       on the cluster from the user to continue (you may have to change the
#       user). Being so, it will not continue if you have other jobs running.
#       This could be done more efficiently, but it's not worth the time
#       for me to figure that out.

START=$1
END=$2

cd Plots
if [ -d PropagationDiagrams ]; then
    echo "Removing old propagation diagrams..."
    rm -rf PropagationDiagrams
fi
mkdir PropagationDiagrams
cd ..

echo "Creating plots..."

for i in $(seq $START $END); do
    ./maybe_sub.sh python plotPropagationDiagram.py $i
done

echo "Waiting for jobs to finish..."

while [ true ]; do
    if [ $(condor_q roffo | wc -l) = 6 ]; then
        echo "Jobs finished."
        break
    fi
    sleep 3
done

echo "Creating gif..."

cd Plots/PropagationDiagrams

convert *.png Propagation$START-$END.gif

mv Propagation$START-$END.gif ..

cd ../..

echo "Finished."