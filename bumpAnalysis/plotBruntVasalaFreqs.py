### Plots the glitch in the Brunt Vasala Frequency for a given profile.      ###
### Indicates the location of the profile on a plot of the Period Separation ###
### versus model number.                                                     ###
################################################################################

import pylab
import numpy as np
import math
import sys

n = len(sys.argv)

profiles, pi_1 = np.genfromtxt(fname='Data/DPi_1.dat',unpack=True,skip_header=1)

s, e = np.genfromtxt(fname='Data/critPoints.dat',unpack=True,skip_header=1)
start_pro = int(s)
end_pro = int(e)

fig = pylab.figure()

ax = fig.add_subplot(2,1,1)
ax.minorticks_on()
ax.plot(profiles, pi_1, ',')
ax.axvline(start_pro,ls='dashed',color='k')
ax.axvline(end_pro,ls='dashed',color='k')
ax.set_xlabel("Model Number")
ax.set_ylabel("$\Delta\Pi_1$")
start,end = ax.get_ylim()
ax.set_yticks(np.arange(start, end, (end-start)/5))
ax.yaxis.tick_right()
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')

bx = 0
cx = 0

colors = ['r','g','y','m','c','k']

cx = fig.add_subplot(2,1,2)
cx.set_ylabel("Brunt-Vasala Frequency N/$\mu$Hz",position=(0,0.5,0))
cx.minorticks_on()
cx.yaxis.tick_right()
cx.set_xlabel("Radius r/R")

for i in range(1, len(sys.argv)):
    profile_number = int(sys.argv[i])

    ax.plot(profiles[profile_number-1],pi_1[profile_number-1],colors[i-1]+'.')

    rawr, rawbvf = np.genfromtxt(fname="../profile{}.data".format(profile_number),
                           unpack=True, usecols=[4,97], skip_header=6)

    r = []
    bvf = []
    for j in range(len(rawbvf)):
        if (rawbvf[j] > 0.1):
            r.append(rawr[j])
            bvf.append(rawbvf[j])
    bvf = [ x**0.5 for x in bvf ]

    cx.plot(r/r[0],bvf,colors[i-1]+'-')

fig.subplots_adjust(hspace=0)

pylab.show()#savefig("Plots/PiVsModel")
