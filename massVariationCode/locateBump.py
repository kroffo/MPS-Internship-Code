import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# How many neighboring points to check for max or min (5 neighbors on each side)
crit_tolerance = 3

# The farthest apart the max and min of the bump should be.
# If a max and min are found, but not this close, they are rejected
temp_tolerance = 0.02

# The number of points to skip in the beginning of the data.
# Initial points may include several maxes and mins which are close together
# so they should be skipped over.
skip_points = 100

plt.gca().invert_xaxis()

def main():
    m, a, l, t, r = np.loadtxt(fname="MALTR.dat",unpack=True,skiprows=1)
    
    mass = list(m)[0]
    a = list(a)
    l = list(l)
    t = list(t)
    r = list(r)

    crits = find_min_max(t, l, skip_points)
    
    min_index = crits[0][0]
    max_index = crits[0][1]
    midpoints = min_index - max_index
    tmin, tmax, lmin, lmax, rmin, rmax, amax, amin = t[min_index], t[
        max_index], l[min_index], l[max_index], r[min_index], r[
        max_index], a[max_index], a[min_index]
    
    create_hrbump_plot(t, l, crits[1], crits[2], mass)

    # Cut out data sufficiently far from the bump
    for i in range(min_index + midpoints,len(a)):
        del a[-1]
        del l[-1]
        del t[-1]
        del r[-1]

    a = list(reversed(a))
    l = list(reversed(l))
    t = list(reversed(t))
    r = list(reversed(r))

    for i in range(max_index - midpoints):
        del a[-1]
        del l[-1]
        del t[-1]
        del r[-1]
        
    a = list(reversed(a))
    l = list(reversed(l))
    t = list(reversed(t))
    r = list(reversed(r))

    f = open('trimmedMALTR.dat', 'w')
    f.write("Mass\tAge\tLuminosity\tTemperature\tRadius\n")
    for i in range(len(t)):
        f.write("%f\t%f\t%f\t%f\t%f\n"%(mass,a[i],l[i],t[i],r[i]))
    f.close()

    f = open('critPoints.dat', 'w')
    f.write("Temperature\tLuminosity\tRadius\tAge\n")
    f.write("%f\t%f\t%f\t%f\n"%(tmax,lmax,rmax,amax))
    f.write("%f\t%f\t%f\t%f\n"%(tmin,lmin,rmin,amin))
    f.close()

    plt.plot(t,l,"b.")
    plt.plot(crits[1],crits[2],"ro")
    plt.subplot().minorticks_on()
    #plt.title("Bump of {:04.2f} M$_☉$ Star".format(mass))
    plt.xlabel(r"Effective Temperature log(T$_{\mathrm{eff}}$/K)")
    plt.ylabel(r"Luminosity log(L/L$_☉$)")

    plt.savefig("bump.png")

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
