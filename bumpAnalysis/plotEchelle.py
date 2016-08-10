###                            See getEchelles.sh                            ###
################################################################################

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math

import sys

n = int(sys.argv[1])

max_n = -1
if (len(sys.argv) > 2):
    max_n = int(sys.argv[2])

plt.plot([1,2])
plt.subplot(121)

t,l = np.genfromtxt(fname="Data/MALTR.dat",unpack=True,usecols=[3,2],skip_header=1)

for i in range(len(l)):
    l[i] = math.log10(l[i])

plt.gca().invert_xaxis()

plt.plot(t,l,'.')
plt.plot(t[int(n)-1],l[int(n)-1],'o')
plt.xlabel("log(T$_\mathrm{eff}$/K)")
plt.ylabel("log(L/L$_☉$)")

input_file = "adipls-frequencies/profile{0}-freqs.dat".format(n)

data = np.loadtxt(fname=input_file,unpack=True)

frequencies = []

frequencies.append([])
l = 0

for i in range(len(data[0])):
    if (data[0][i] > l):
        frequencies.append([])
        l = l + 1
    frequencies[l].append(data[2][i])

large_frequency_separation = (np.genfromtxt(
    fname="Data/LFS.dat",usecols=[1],skip_header=1))[n-1]

if (max_n > len(frequencies)) or (max_n == -1) :
    max_n = len(frequencies) - 1

for i in range(max_n+1):
    plt.subplot(122).plot(frequencies[i]%large_frequency_separation,frequencies[i],".")

plt.xlabel(r'Frequency modulo %f ($\mu$Hz)'%(large_frequency_separation))
plt.ylabel(r'Frequency ($\mu$Hz)')

plt.subplots_adjust(wspace=0.3)

plt.savefig("Plots/EchelleDiagrams/echelle{0:04.0f}".format(int(n)))
