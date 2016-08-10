import matplotlib.pyplot as plt
import numpy as np
import math

def get_max(arr):
    max = arr[0]
    for v in arr:
        if v > max:
            max = v
    return max

def index_of(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

model_numbers, convective_depths = np.genfromtxt(fname="../history.data",
                              usecols=[0,9],
                              unpack=True,
                              skip_header=6
                              )
offset = model_numbers[0] - 1

profiles = [ int(x - offset) for x in model_numbers ]

discont_models, discont_depth = np.genfromtxt(
    fname="Data/Discontinuity.dat",
    usecols=[0,1],
    unpack=True,
    skip_header=1
    )

radii = []
discontinuity_depths = []
lums = []
temps = []

for n in profiles:
    dis_dep = discont_depth[ index_of(discont_models, n) ]
    r, l, t = np.genfromtxt(fname="../profile{}.data".format(n),
                            usecols=[8,7,6],
                            skip_header=2,
                            max_rows=1
                            )
    lums.append(math.log10(l))
    temps.append(t)
    radii.append(r)
    discontinuity_depths.append(dis_dep)

max_r = get_max(radii)

radii = [ x/max_r for x in radii ]
for i in range(len(radii)):
    discontinuity_depths[i] = discontinuity_depths[i]*radii[i]
    convective_depths[i] = convective_depths[i]*radii[i]

with open("Data/Depths.dat", "w") as file:
    file.write("Radius\t\tConv_Depth\tDis_Depth\tTemperature\tlog(L)\n")
    for i in range(len(lums)):
        file.write(str(radii[i]) + '\t' + 
                str(convective_depths[i]) + '\t' + 
                str(discontinuity_depths[i]) + '\t' +
                str(temps[i]) + '\t' + 
                str(lums[i]) + '\n')

for n in range(len(radii)):
    print("    Plotting... {}%".format(int(n/(len(radii)-1)*100)),end='\r')
    plt.subplot(211)
    plt.plot(temps,lums)
    plt.plot(temps[n],lums[n],'ro')
    plt.xlabel("Temperature T$_{\mathrm{eff}}$/K")
    plt.ylabel("Luminosity log(L/L$_☉$)")
    plt.gca().invert_xaxis()
    
    plt.subplot(212)
    circle1 = plt.Circle((0, 0), radii[n], fill=False, color='r')
    circle2 = plt.Circle((0, 0), convective_depths[n], fill=False, color='g')
    circle3 = plt.Circle((0, 0), discontinuity_depths[n], fill=False, color='b')
    fig = plt.gcf()
    ax = fig.gca()
    
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)
    
    
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    plt.savefig(".DepthPlots/{0:04.0f}".format(n))
    plt.clf()
print("Plotting finsihed.                                    ")
