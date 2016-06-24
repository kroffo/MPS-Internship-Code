import matplotlib.pyplot as plt
import numpy as np

# Plots the luminosity amplitude ratio versus the mass using the data of stars
# generated using vary_masses.sh and analyzed by analyzeStars.sh

luminosityRatio = []
mass = []

lowest_mass = 0.8
highest_mass = 2.2
step = 0.1

for i in np.arange(lowest_mass, highest_mass + step, step):
    # May need to change {:0X.Xf} to account for directory names
    t, l = np.loadtxt(fname="mass/{:03.1f}/LOGS/Analysis/critPoints.dat".format(i), unpack=True, usecols=(0,1), skiprows=1)
    luminosityRatio.append( (10**l[0]) / (10**l[1]) )
    mass.append(i)

plt.plot(mass,luminosityRatio)
#plt.title("Luminosity Amplitude Ratio versus Mass in the RGB Bump")
plt.xlim((lowest_mass, highest_mass))
plt.xlabel("Mass M/M$_☉$")
plt.ylabel("Luminosity Ratio L$_\mathrm{max}$/L$_\mathrm{min}$")
plt.subplot().minorticks_on()
plt.savefig("JCDFig3Plot.png")
