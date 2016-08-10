import numpy as np
import matplotlib.pyplot as plt

def get_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

num_points = 4

differences = []
masses = []

lowest_mass = 0.8
highest_mass = 2.2
step = 0.1

for i in np.arange(lowest_mass, highest_mass + step/2, step):
    # May need to change {:0X.Xf} to account for directory names
    s,e = np.loadtxt(
        fname="mass/{:03.1f}/bumpTrack/LOGS/Analysis/Data/critPoints.dat".format(i),
        unpack=True, skiprows=1)
    start = int(s)
    end = int(e)
    profiles, sfs01 = np.loadtxt(
        fname="mass/{:03.1f}/bumpTrack/LOGS/Analysis/Data/SFS01.dat".format(i),
        unpack=True, skiprows=1)
    
    sum = sfs01[get_index(profiles,start)]
    count = 1
    for j in range(1,num_points+1):
        sum += sfs01[get_index(profiles,start) + i]
        sum += sfs01[get_index(profiles,start) - i]
        count += 2
    sdnu  = sum / count

    sum = sfs01[get_index(profiles,end)]
    count = 0
    for j in range(1,num_points+1):
        sum += sfs01[get_index(profiles,end) + i]
        sum += sfs01[get_index(profiles,end) - i]
        count += 2
    ednu = sum / count

    differences.append(ednu - sdnu)
    masses.append(i)

plt.plot(masses,differences)
plt.xlabel("Mass M/M$_☉$")
plt.ylabel(r"Difference In $\delta\nu_{01}$ Across The Bump")
plt.savefig("dnu01Difference")
