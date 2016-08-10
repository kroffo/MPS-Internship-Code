### Locates the bump in the track and outputs the model numbers of the start ###
### and end of it in a file called critPoints.dat (located in Data)          ###
################################################################################

import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math

import sys

number_profiles = int(np.loadtxt(fname='Data/number_of_profiles.dat'))

# How many neighboring points to check for max or min (5 neighbors on each side)
crit_tolerance = 3

# The farthest apart the max and min of the bump should be.
# If a max and min are found, but not this close, they are rejected
temp_tolerance = 0.02

# The number of points to skip in the beginning of the data.
# Initial points may include several maxes and mins which are close together
# so they should be skipped over.
skip_points = 0

plt.gca().invert_xaxis()

def main():

    m, a, l, t, r = np.genfromtxt(
        fname="Data/MALTR.dat",unpack=True,skip_header=1)
    
    mass = list(m)[0]
    a = list(a)
    l = list(l)
    t = [ math.log10(x) for x in list(t) ]
    r = list(r)

    crits = find_min_max(t, l, skip_points)
    
    min_index = crits[0][0]
    max_index = crits[0][1]
    midpoints = min_index - max_index
    tmin, tmax, lmin, lmax, rmin, rmax, amax, amin = t[min_index], t[
        max_index], l[min_index], l[max_index], r[min_index], r[
        max_index], a[max_index], a[min_index]
    
#    create_hrbump_plot(t, l, crits[1], crits[2], mass)

    for i in range(min_index, len(a)):
        # Go about for the uncertainty (2sigma)
        if t[i] < t[max_index] - 100/(10**t[max_index]):
            a = a[:i]
            l = l[:i]
            t = t[:i]
            r = r[:i]
            break

    for i in range(max_index, 0, -1):
        if t[i] > t[min_index] + 100/(10**t[min_index]):
            a = a[i:]
            l = l[i:]
            t = t[i:]
            r = r[i:]
            break

    f = open('critPoints.dat', 'w')
    f.write("BumpStart\tBumpEnd\n")
    f.write("%d\t\t%d"%(max_index,min_index))
    f.close()

    plt.plot(t,l,"b.")
    plt.plot(crits[1],crits[2],"ro")
    plt.subplot().minorticks_on()
    #plt.title("Bump of {:04.2f} M$_☉$ Star".format(mass))
    plt.xlabel(r"Effective Temperature log(T$_{\mathrm{eff}}$/K)")
    plt.ylabel(r"Luminosity log(L/L$_☉$)")

   # plt.show()#savefig("bump.png")

# finds the min and max of the bump by finding the first local max and min
# within temp_tolerance log(K) of each other
def find_min_max(t,l, start_index):
    max_l, min_l, max_t, max_l = 0, 0, 0, 0
    max_index, min_index = 0, 0
    for i in range(start_index + crit_tolerance,len(l) - crit_tolerance):
        if is_local_max(i,l):
            max_l = l[i]
            max_t = t[i]
            max_index = i
            break
    for i in range(max_index+crit_tolerance,len(l)-crit_tolerance):
        if is_local_min(i,l):
            min_l = l[i]
            min_t = t[i]
            min_index = i
            break
    if t[max_index] - t[min_index] > temp_tolerance:
        return find_min_max(t, l, max_index)
    return [[min_index, max_index], [min_t, max_t], [min_l, max_l]]

# returns whether a point is a local max
def is_local_max(index,l):
    for i in range(1,crit_tolerance):
        if l[index] < l[index - i] or l[index] < l[index + i]:
            return False
    return True

# returns whether a point is a local min
def is_local_min(index,l):
    for i in range(1,crit_tolerance):
        if l[index] > l[index - i] or l[index] > l[index + i]:
            return False
    return True

# Creates the hr diagram with two red points signifying the bump
def create_hrbump_plot(t, l, tc, lc, m):
    plt.plot(t, l, 'b-')
    
    if tc[0] != 0 and tc[1] != 0:
        plt.plot(tc, lc, 'r.')
    
#    plt.title("HR Diagram for a Star of {:04.2f} M$_☉$".format(m))
    plt.xlabel(r"Effective Temperature log(T$_{\mathrm{eff}}$/K)")
    plt.ylabel(r"Luminosity log(L/L$_☉$)")
    plt.subplot().minorticks_on()
    plt.savefig("HRWithBump")
    plt.cla()

main()
