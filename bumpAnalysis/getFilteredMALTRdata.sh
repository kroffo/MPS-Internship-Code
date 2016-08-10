#!/bin/bash

cd ..
# These files shouldn't exist, but can if the script was prviously stopped early
# If they do, they must be deleted, else the new writes will be appended.
if [ -e filteredMALTR.dat ]; then
    rm filteredMALTR.dat
fi
if [ -e filteredProfileNumbers.dat ]; then
    rm filteredProfileNumbers.dat
fi
touch filteredMALTR.dat
touch filteredProfileNumbers.dat
N=$(ls profile*.data | wc -l)
echo -e "Mass\t\t\tAge\t\t\tLuminosity\t\tTeff\t\t\tRadius" >> filteredMALTR.dat
for i in $(seq 1 $N ); do
    if [ ! $(wc -l Analysis/adipls-frequencies/profile$i-freqs.dat | awk '{ print $1 }') = 0 ]; then
        less profile$i.data | awk '{ print $18"\t"$5"\t"$8"\t"$7"\t"$9 }' | sed -n 3p >> filteredMALTR.dat
        echo $i >> filteredProfileNumbers.dat
    fi
done
mv filteredMALTR.dat Analysis/Data
mv filteredProfileNumbers.dat Analysis/Data
cd Analysis