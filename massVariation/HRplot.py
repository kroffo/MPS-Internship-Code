import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Plots the HR Diagram for a star using MALT.dat

#MALT.dat contains Mass, Age, Luminosity and Temperature data
#m, l, t = np.loadtxt(fname="MALTR.dat",unpack=True,usecols=(0,2,3),skiprows=1)
m, a, l, t, r, cd = np.loadtxt(fname="../history.data",usecols=(2,1,36,34,37,9),unpack=True,skiprows=6)

plt.plot(t, l, 'b-')
#plt.plot(t, l, 'b.')

plt.gca().invert_xaxis()
plt.subplot().minorticks_on()
#plt.title("HR Diagram for a Star of {:04.2f} M$_☉$".format(m[0]))
plt.xlabel(r"Effective Temperature log(T$_{\mathrm{eff}}$/K)")
plt.ylabel(r"Luminosity log(L/L$_☉$)")

plt.savefig("HRdiagram")
