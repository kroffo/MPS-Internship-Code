###            Plot the propagation diagram for a given profile.             ###
################################################################################

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import matplotlib.patches as patches

n = int(sys.argv[1])

mode = 'r'

if len(sys.argv) > 2:
    mode = sys.argv[2]

R0 = 6.955e10
fileName = "../profile{}.data".format(n)
vmax, Dnu = np.loadtxt(fname="Data/vfactors/vfactors{}.txt".format(n),
                  usecols=[2,3],unpack=True,skiprows=1)

r, m, c, bv = np.loadtxt(fname=fileName,usecols=[23,61,14,97],
                         unpack=True,skiprows=6)
R = r[0]

t,l = np.genfromtxt(fname="Data/MALTR.dat",unpack=True,usecols=[3,2],skip_header=1)

for i in range(len(l)):
    l[i] = math.log10(l[i])

plt.subplot(212)
plt.gca().invert_xaxis()

plt.plot(t,l,'.')
plt.plot(t[int(n)-1],l[int(n)-1],'ro')
plt.xlabel("log(T$_\mathrm{eff}$/K)")
plt.ylabel("log(L/L$_☉$)")


profiles, rads, mas = np.loadtxt(fname="Data/Discontinuity.dat",usecols=[0,1,4],
                                    unpack=True,skiprows=1)
for i in range(len(profiles)):
    if profiles[i] == n:
        discont_rad = rads[i]
        discont_mass = mas[i]
        break

S = []

# Calculate Lamb Frequency and put it and brunt vasala frequency into microHz
for i in range(len(r)):
    S.append((((c[i]**2/((r[i]*R0)**2)*(1*(1+1))))**0.5)/(2*math.pi) * (10**6))

for i in range(len(bv)):
    bv[i] = (bv[i]**0.5) * (10**6) / (2*math.pi)

if mode.lower() in [ 'm', 'mass' ]:
    plt.subplot(211).axhline(
        vmax,ls='dashed',color='k',label=r"$\nu_{\mathrm{max}}$")
    plt.axvline(discont_rad,ls='dotted',color='k',label="Discontinuity")
    
    plt.plot(m,S,'-')
    plt.plot(m,bv,'-')
    plt.xlabel("Fractional Mass")
    plt.ylabel("Lamb Frequency")
    plt.subplot(211).set_yscale('log')
    #plt.subplot(211).set_xscale('log')
    plt.subplots_adjust(hspace=0.3)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),loc=3,mode='expand',ncol=2)
else:
    plt.subplot(211).axhline(
        vmax,ls='dashed',color='k',label=r"$\nu_{\mathrm{max}}$")
    plt.axvline(discont_rad,ls='dotted',color='k',label="Discontinuity")
    plt.subplot(211).add_patch(patches.Rectangle(
            (0.00001, vmax-2*Dnu), 1, 4*Dnu, alpha = 0.2
            ))
    plt.plot(r/R,S,'-',label='S$_{1}$/2$\pi$')
    plt.plot(r/R,bv,'-',label='N/2$\pi$')
    plt.xlabel("Fractional Radius")
    plt.ylabel("Lamb Frequency")
    plt.subplot(211).set_yscale('log')
    plt.subplot(211).set_xscale('log')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),loc=3,mode='expand',ncol=4)
    plt.subplot(211).set_xlim([10**-3,10**0])
    plt.subplot(211).set_ylim([10**1,10**7])

plt.subplots_adjust(hspace=0.3)

plt.savefig("Plots/PropagationDiagrams/PropagationDiagram{0:04.0f}".format(n))
