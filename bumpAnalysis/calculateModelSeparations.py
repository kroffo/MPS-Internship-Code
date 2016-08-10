### Uses a gaussian to take a weighted average of the various values for the ###
### frequency separations to use as single values for each profile. Centered ###
### around numax, with width set by full-width at half-maximum.              ###
###                                                                          ###
### The num_points closest points to numax are used for the average.         ###
################################################################################

import math
import numpy as np
import sys
import os.path as op

number_profiles = int(np.loadtxt(fname="Data/number_of_profiles.dat"))

# Number points to use for the average
num_points = 5

# Earl gave me this to calculate the width of the Gaussians.
fwhm_conversion = (2*(2*np.log(2))**0.5)

def gaussian(x,mean,stddev):
    y = (2*math.pi*(stddev**2))**(-0.5)*math.exp(-((x-mean)**2)/(2*stddev**2))
    return y

def calculateAverage(arr,mean,stddev):
    sum = 0
    weight_sum = 0
    for x in arr:
        y = gaussian(x,mean,stddev)
        sum = sum + y*x
        weight_sum = weight_sum + y
    return sum/weight_sum

def getNClosest(arr,value,N):
    closest = [ ]
    for i in range(N):
        closest.append(0)
    for v in arr:
        if abs(value - v) < abs(value - closest[N-1]):
            closest[N-1] = v
            for i in range(N-1):
                if abs(value - v) < abs(value - closest[N-2-i]):
                    closest[N-1-i] = closest[N-2-i]
                    closest[N-2-i] = v
                else:
                    break
    return closest

lfs = []
sfs = []
sfs1 = []
models = []

for profile_number in range(1,number_profiles+1):
    print(" Calculating... {}%".format(int(profile_number/number_profiles*100)),end="\r")
    numax = np.genfromtxt(fname='Data/vfactors/vfactors{}.txt'.format(profile_number),usecols=[2],skip_header=1)
    mean = numax
    stddev = 0.66*(numax**0.88)/fwhm_conversion
    if op.isfile('Data/Separations/sfs{}.dat'.format(profile_number)):
        ss = np.genfromtxt(
            fname='Data/Separations/sfs{}.dat'.format(profile_number),
            usecols=[1],
            skip_header=1
            )
        ls = np.genfromtxt(
            fname='Data/Separations/lfs{}.dat'.format(profile_number),
            usecols=[1],
            skip_header=1
            )
        ss1 = np.genfromtxt(
            fname='Data/Separations/L1_sfs{}.dat'.format(profile_number),
            usecols=[1],
            skip_header=1
            )
        ss = getNClosest(ss,numax,num_points)
        ls = getNClosest(ls,numax,num_points)
        ss1 = getNClosest(ss1,numax,num_points)
        sfs.append(calculateAverage(ss,mean,stddev))
        lfs.append(calculateAverage(ls,mean,stddev))
        sfs1.append(calculateAverage(ss1,mean,stddev))
        models.append(profile_number)
print()
with open("Data/LFS.dat", "w") as file:
    file.write("Model_Number\tLarge_Frequency_Separation\n")
    for i in range(len(models)):
        file.write(str(models[i]) + "\t\t" + str(lfs[i]) + "\n")

with open("Data/SFS.dat", "w") as file:
    file.write("Model_Number\tSmall_Frequency_Separation\n")
    for i in range(len(models)):
        file.write(str(models[i]) + "\t\t" + str(sfs[i]) + "\n")

with open("Data/SFS01.dat", "w") as file:
    file.write("Model_Number\tSmall_Frequency_Separation_01\n")
    for i in range(len(models)):
        file.write(str(models[i]) + "\t\t" + str(sfs1[i]) + "\n")
