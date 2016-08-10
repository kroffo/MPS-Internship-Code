### Locates the radius at which the discontinuity occurrs for each profile.  ###
###                                                                          ###
### Done by reading in the Hydrogen abundancy at decreasing radii until a    ###
### sudden decrease occurrs after at least 10 zones have the same value.     ###
################################################################################

import numpy as np

discontinuity_radii = []
star_R = []
discontinuity_masses = []

profiles = np.loadtxt(fname="Data/filteredProfileNumbers.dat")

for n in range(len(profiles)):
    print(" Calculating... {}%".format(int(n/len(profiles)*100)),end='\r')
    fileName = "../profile{}.data".format(int(profiles[n]))

    m, r, X = np.loadtxt(fname=fileName,usecols=[61,23,33],
                         unpack=True,skiprows=6)
    R = r[0]

    discont_rad = 0
    discont_m = 0
    count = 0
    flag = False
    for i in range(1,len(X)):
        delta = abs(X[i] - X[i-1])
        if delta == 0:
            count += 1
            if count > 10:
                flag = True
        elif delta > 0.01 and flag:
            discont_rad = r[i]
            discont_m = m[i]
            break
        else:
            count = 0

    discontinuity_radii.append(discont_rad)
    discontinuity_masses.append(discont_m)
    star_R.append(R)

with open("Data/Discontinuity.dat", "w") as file:
    file.write("Model_Number\tFractional_Radius\tDiscontinuity_Radius\tStellar_Radius\tFractional_Mass\n")
    for i in range(len(profiles)):
        file.write(str(int(profiles[i])) + "\t\t" +
                   str(discontinuity_radii[i]/star_R[i]) + "\t\t" +
                   str(discontinuity_radii[i]) + "\t\t" + 
                   str(star_R[i]) + "\t" + 
                   str(discontinuity_masses[i]) + "\n")
