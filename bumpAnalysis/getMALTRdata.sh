#!/bin/bash

cd ..

# This is necessary if getMALTRdata.sh was previously stopped before completion
# Without deleting first, the file will be appended to, thus leaving it's
# bad contents.
if [ -e MALTR.dat ]; then
    rm MALTR.dat
fi

touch MALTR.dat
N=$(ls profile*.data | wc -l)
echo -e "Mass\t\t\tAge\t\t\tLuminosity\t\tTeff\t\t\tRadius" >> MALTR.dat
for i in $(seq 1 $N); do
    less profile$i.data | awk '{ print $18"\t"$5"\t"$8"\t"$7"\t"$9 }' | sed -n 3p >> MALTR.dat
done
mv MALTR.dat Analysis/Data
cd Analysis
