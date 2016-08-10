### Calculates the frequency output by ADIPLS closest to numax (of the l=0   ###
### modes) for each profile, and writes out.                                 ###
################################################################################

import numpy as np
import sys

profiles = np.loadtxt(fname="Data/filteredProfileNumbers.dat")

v_max = []
v_closest = []

for i in range(len(profiles)):
    p = int(profiles[i])
    print(" {}% Complete...         ".format(int(i/len(profiles)*100)),end="\r")
    
    input_file = "adipls-frequencies/profile{0}-freqs.dat".format(p)

    data = np.loadtxt(fname=input_file,unpack=True)

    frequencies = []
    l = 0
    
    for j in range(len(data[0])):
        if (data[0][j] > l):
            break
        frequencies.append(data[2][j])
    
    vmax = np.genfromtxt(fname="Data/vfactors/vfactors{}.txt".format(p),
                         usecols=[2],skip_header=1)
    
    vclosest = -1000
    
    for f in frequencies:
        if (abs(f-vmax) < abs(vclosest-vmax)):
            vclosest = f

    v_max.append(vmax)
    v_closest.append(vclosest)

print(" Writing results...    ",end='\r')

with open("Data/vClosestToVmax.dat", "w") as file:
    file.write("Model_Number\tv_max\t\t\tv_closest\n")
    for i in range(len(v_max)):
        file.write(str(int(profiles[i])) + "\t\t" + str(v_max[i]) + "\t\t" + str(v_closest[i]) + "\n")

print(" Calculations complete.        ")
