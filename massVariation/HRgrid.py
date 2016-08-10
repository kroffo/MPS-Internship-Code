import matplotlib.pyplot as plt
import numpy as np
import math

t = []
l = []

for i in range(7, 23):
    name="mass/{:03.1f}/bumpTrack/LOGS/Analysis/Data/MALTR.dat".format(i/10)
    temp, lum = np.genfromtxt(fname=name,usecols=[3,2],unpack=True,skip_header=1)
    t.append(temp)
    l.append([ math.log10(x) for x in lum ])

for i in range(len(t)):
    plt.plot(t[i],l[i],'k,')

plt.gca().invert_xaxis()
plt.show()
