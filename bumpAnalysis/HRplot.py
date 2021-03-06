###               Plots the HR Diagram for a star using MALTR.dat            ###
################################################################################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

m, l, t = np.loadtxt(fname="Data/MALTR.dat",unpack=True,usecols=(0,2,3),skiprows=1)

plt.plot(t, l, 'b-')
plt.plot(t, l, 'b.')

plt.gca().invert_xaxis()
plt.subplot().minorticks_on()
plt.title("HR Diagram for a Star of {:04.2f} M$_☉$".format(m[0]))
plt.xlabel(r"Effective Temperature log(T$_{\mathrm{eff}}$/K)")
plt.ylabel(r"Luminosity log(L/L$_☉$)")

plt.savefig("Plots/HRdiagram")
