### Plots the Radius versus Age, and depth of convective envelope versus Age ###
################################################################################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


profile_models = []

file_name = "../history.data"
# Read mass, age, luminosity, temp, radius, convective depth
m, a, l, t, r, cd = np.loadtxt(fname=file_name,usecols=(2,1,36,34,37,9),unpack=True,skiprows=6)

mn = []

for i in range(len(r)):
    mn.append(i+1)
    r[i] = 10**r[i]
    a[i] = a[i]/(1e9)
    l[i] = 10**l[i]

plt.plot([1,2])
plt.subplot(121).minorticks_on()

plt.xlabel("Model Number")
plt.ylabel("Radius R/R$_☉$")

plt.plot(mn,r,',')

plt.subplot(122).plot(mn,cd,',')

plt.xlabel("Model Number")
plt.ylabel("Convective Depth r/R")
plt.subplot(122).minorticks_on()

plt.subplots_adjust(wspace=0.4)

plt.savefig("RadiusAndConvectiveDepth")
