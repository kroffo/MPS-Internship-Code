import matplotlib.pyplot as plt
import numpy as np
import sys

inputFileName = sys.argv[1]

l, n, f, m = np.loadtxt(fname=inputFileName,usecols=(0,1,2,3),unpack=True)
max_l = int(l[len(l)-1] + 1)

# # Load frequencies and mode inertias into frequencies array.
# # frequencies is an array of arrays corresponding to l modes
# # each l mode array holds an array corresponding to n modes
# # each n mode array holds the frequency, and the mode inertia
# frequencies = []
# frequencies.append([])
# l = 0
# for i in range(len(data[0])):
#     if (data[0][i] > l):
#         frequencies.append([])
#         l = l + 1
#     frequencies[l].append( [data[2][i], data[3][i] ])

l_modes = []
for i in range(max_l):
    l_modes.append([[],[]])

for i in range(len(l)):
    if (n[i] > 0):
        print(l[i])
        l_modes[int(l[i])][0].append(f[i])
        l_modes[int(l[i])][1].append(m[i])

for i in range(max_l):
    plt.plot(l_modes[i][0],l_modes[i][1],'.')

# for i in range(len(frequencies)):
#     l_modes.append([[],[]])
#     for j in range(len(frequencies[i])):
#         l_modes[i][0].append(frequencies[i][j][0])
#         l_modes[i][1].append(frequencies[i][j][1])
#     plt.plot(l_modes[i][0],l_modes[i][1],'.')

plt.axes().set_yscale('log')
plt.ylabel("Mode inertia")
plt.xlabel(r"Frequency $\nu$/Hz")
plt.savefig("ModeInertiasExample")
