### Calculates the Large and Small02 and Small01 Frequency Separations which ###
### occur for each model.                                                    ###
###                                                                          ###
### Writes results in Data/Separations                                       ###
################################################################################

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math

import sys

n = sys.argv[1]

plt.plot([1,2])
plt.subplot(321)

t, l = np.loadtxt(fname="Data/MALTR.dat",usecols=[3,2],unpack=True,skiprows=1)

for i in range(len(l)):
    l[i] = math.log10(l[i])

plt.gca().invert_xaxis()

plt.plot(t,l,'.')
plt.plot(t[int(n)-1],l[int(n)-1],'o')
plt.xlabel("T$_\mathrm{eff}$/K")
plt.ylabel("log(L/L$_☉$)")
start,end = plt.ylim()
plt.yticks(np.arange(start, end,(end-start)/4))

start,end = plt.xlim()
plt.xticks(np.arange(start, end, (end-start)/4))

input_file = "adipls-frequencies/profile{0}-freqs.dat".format(n)

data = np.loadtxt(fname=input_file,unpack=True)

frequencies = []
mode_inertias = []
frequencies.append([])
mode_inertias.append([])
l = 0

for j in range(1,len(data[0])):
    if (data[0][j] > l):
        frequencies.append([])
        mode_inertias.append([])
        l = l + 1
    frequencies[l].append(data[2][j])
    mode_inertias[l].append(data[3][j])

lfs_freqs = []
lfs = []
sfs = []
inertias = []
freqs = []
inertia_freqs = []

for i in range(len(frequencies[0])):
    i = int(i)
    freq = frequencies[0][i]
    lofreq = 0
    if (i > 0):
        lofreq = frequencies[0][i-1]
        lfs.append(abs(frequencies[0][i] - frequencies[0][i-1]))
        lfs_freqs.append(frequencies[0][i])
    smallest_f = 0
    smallest_inertia = 100000
    for j in range(len(frequencies[2])):
        j = int(j)
        frequency = frequencies[2][j]
        inertia = mode_inertias[2][j]
        if (freq > frequency) and (lofreq < frequency) and (
            inertia < smallest_inertia):
            smallest_inertia = inertia
            smallest_f = frequency
    if (smallest_f > 0):
        sfs.append(abs(freq - smallest_f))
        freqs.append(freq)
        inertias.append(smallest_inertia)
        inertia_freqs.append(smallest_f)


# Earl and I decided to cut the last one out because it sometimes becomes
# what we believe to be an outlier, causing jumps in the separations.
with open("Data/Separations/lfs{}.dat".format(n), "w") as file:
    file.write("Frequency\tLarge_Frequency_Separation\n")
    for i in range(len(lfs)-1):
        file.write(str(lfs_freqs[i]) + "\t\t" + str(lfs[i]) + "\n")

with open("Data/Separations/sfs{}.dat".format(n), "w") as file:
    file.write("Frequency\tSmall_Frequency_Separation\n")
    for i in range(len(sfs)-1):
        file.write(str(freqs[i]) + "\t\t" + str(sfs[i]) + "\n")

plt.subplot(322).plot(lfs_freqs,lfs,".")
plt.xlabel(r'Frequency $\nu$/$\mu$Hz')
plt.ylabel(r'$\Delta\nu$/$\mu$Hz')
start,end = plt.ylim()
plt.yticks(np.arange(start, end,(end-start)/4))

plt.subplot(324).plot(freqs,sfs,".")
plt.xlabel(r'Frequency $\nu$/$\mu$Hz')
plt.ylabel(r'$\delta\nu_{02}$/$\mu$Hz')
start,end = plt.ylim()
plt.yticks(np.arange(start, end,(end-start)/4))

plt.subplot(323).plot(frequencies[0],mode_inertias[0],".")
plt.subplot(323).plot(frequencies[2],mode_inertias[2],".")
plt.subplot(323).plot(inertia_freqs,inertias,".")
plt.subplot(323).set_yscale('log')
start,end = plt.ylim()
start = math.log10(start)
end = math.log10(end)
plt.yticks(10**np.arange(start, end,(end-start)/4))
plt.subplots_adjust(wspace=0.6)
plt.subplots_adjust(hspace=0.6)

plt.ylabel("Mode inertia")
plt.xlabel(r"Frequency $\nu$/$\mu$Hz")


input_file = "adipls-frequencies/profile{0}-freqs.dat".format(n)

data = np.loadtxt(fname=input_file,unpack=True)

frequencies = []
mode_inertias = []
frequencies.append([])
mode_inertias.append([])
l = 0

for j in range(1,len(data[0])):
    if (data[0][j] > l):
        frequencies.append([])
        mode_inertias.append([])
        l = l + 1
    frequencies[l].append(data[2][j])
    mode_inertias[l].append(data[3][j])

lfs_freqs = []
lfs = []
L1_sfs = []
inertias = []
freqs = []
inertia_freqs = []

for i in range(len(frequencies[0])-1):
    i = int(i)
    freq = frequencies[0][i]
    high_freq = frequencies[0][i+1]
    smallest_f = 0
    smallest_inertia = 100000
    for j in range(len(frequencies[1])):
        j = int(j)
        frequency = frequencies[1][j]
        inertia = mode_inertias[1][j]
        if (freq < frequency) and (high_freq > frequency) and (
            inertia < smallest_inertia):
            smallest_inertia = inertia
            smallest_f = frequency
    if (smallest_f > 0):
        L1_sfs.append(abs(0.5*(freq - 2*smallest_f + high_freq)))
        freqs.append(freq)
        inertias.append(smallest_inertia)
        inertia_freqs.append(smallest_f)

with open("Data/Separations/L1_sfs{}.dat".format(n), "w") as file:
    file.write("Frequency\tSmall_Frequency_Separation_01\n")
    for i in range(len(L1_sfs)-1):
        file.write(str(freqs[i]) + "\t\t" + str(L1_sfs[i]) + "\n")


plt.subplot(325).plot(frequencies[0],mode_inertias[0],".")
plt.plot(frequencies[1],mode_inertias[1],".")
plt.plot(inertia_freqs,inertias,".")
plt.subplot(325).set_yscale('log')
start,end = plt.ylim()
start = math.log10(start)
end = math.log10(end)
plt.yticks(10**np.arange(start, end,(end-start)/4))

plt.ylabel("Mode inertia")
plt.xlabel(r"Frequency $\nu$/$\mu$Hz")

plt.subplot(326).plot(freqs,L1_sfs,".")
plt.xlabel(r'Frequency $\nu$/$\mu$Hz')
plt.ylabel(r'$\delta\nu_{01}$/$\mu$Hz')

# plt.clf()
# plt.plot(frequencies[0],mode_inertias[0],".")
# plt.plot(frequencies[1],mode_inertias[1],".")
# plt.plot(inertia_freqs,inertias,".")
# plt.subplot().set_yscale('log')
# start,end = plt.ylim()
# start = math.log10(start)
# end = math.log10(end)
# plt.yticks(10**np.arange(start, end,(end-start)/4))

# plt.ylabel("Mode inertia")
# plt.xlabel(r"Frequency $\nu$/$\mu$Hz")

# plt.show()

plt.savefig("Plots/Separations/Separations{0:04.0f}".format(int(n)))
