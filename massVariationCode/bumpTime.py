import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Plots the luminosity amplitude ratio versus the mass using the data of stars
# generated using vary_masses.sh and analyzed by analyzeStars.sh

bumpDuration = []
mass = []

lowest_mass = 0.8
highest_mass = 2.2
step = 0.1

for i in np.arange(lowest_mass, highest_mass + step, step):
    # May need to change {:0X.Xf} to account for directory names
    t, l, r, a = np.loadtxt(fname="mass/{:03.1f}/LOGS/Analysis/critPoints.dat".format(i), unpack=True, skiprows=1)
    bumpDuration.append( (a[1] - a[0])/1000000 )
    mass.append(i)

plt.plot(mass,bumpDuration)
#plt.title("Luminosity Amplitude Ratio versus Mass in the RGB Bump")
plt.xlim((lowest_mass, highest_mass))
plt.xlabel("Mass M/M$_☉$")
plt.ylabel("Bump Duration (Myr)")
plt.subplot().minorticks_on()
plt.savefig("bumpDuration.png")

