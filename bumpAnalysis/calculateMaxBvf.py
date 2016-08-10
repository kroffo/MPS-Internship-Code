### Reads in the brunt vasala frequencies from the MESA profiles, and takes  ###
### the max value for each profile to write to a file.                       ###
################################################################################

import numpy as np

profiles = np.loadtxt(fname="Data/filteredProfileNumbers.dat")

maxbvf = []

for profile_number in range(1,len(profiles)+1):
                           
    bvf = np.genfromtxt(
        fname="../profile{}.data".format(profile_number),
        usecols=[97], skip_header=6)

    max = 0
    for f in bvf:
        if (f > max):
            max = f

    maxbvf.append(max**0.5)

def smooth(arr):
    smoothed = [arr[0], arr[1]]
    for i in range(2,len(arr)-2):
        smoothed.append((arr[i-2] + arr[i-1] + arr[i] + arr[i+1] + arr[i+2])/5)
    smoothed.append(arr[len(arr)-2])
    smoothed.append(arr[len(arr)-1])
    return smoothed

#maxbvf = smooth(maxbvf)
with open("Data/MaxBvf.dat", "w") as file:
    file.write("Model_Number\tBrunt_Vasala_Frequency\n")
    for i in range(len(maxbvf)):
        file.write(str(int(profiles[i])) + "\t\t" + str(maxbvf[i]) + "\n")
