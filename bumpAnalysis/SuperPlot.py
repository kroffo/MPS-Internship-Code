### This script can be edited and run to plot as configured. By default, it  ###
### will show the plot. However, this script can be called with parameters:  ###
###                                                                          ###
###     python SuperPlot.py <xvar> <point-type> <save-name> <list>           ###
###                                                                          ###
###       xvar: The variable to plot on the x-axis (see below)               ###
### point-type: type of points to plot                                       ###
###  save-name: if "show", show the plot. else, save in Plots/<save-name>    ###
###       list: A list of what to plot. Ex: "DPi dnu/Dnu T L R"              ###
###             It is possible to plot ratios as well.                       ###
###             To do so, simply put a '/' between the two variables.        ###
###                                                                          ###
### Available variables for plotting are as follows:                         ###
###                                                                          ###
###    Period Separation (DPi)                                               ###
###    Luminosity (L)                                                        ###
###    Temperature (T)                                                       ###
###    Radius (R)                                                            ###
###    Small Frequency Separation 02 (dnu02)                                 ###
###    Large Frequency Separation (Dnu)                                      ###
###    Small Frequency Separation 01 (dnu01)                                 ###
###    nu closest to numax (vclose)                                          ###
###    Age (A)                                                               ###
###    Age difference between profiles (dA)                                  ###
###    Max Brunt Vasala Frequency (maxbvf)                                   ###
###    Discontinuity Fractional Radius (disr)                                ###
###    Discontinuity Absolute Radius (disR)                                  ###
###    Discontinuity Mass (dism)                                             ###
###                                                                          ###
### See the function get_data() for alternate reference names which can be   ###
### used as parameters to the script.                                        ###
###                                                                          ###
###                            Happy Plotting!                               ###
################################################################################

import matplotlib.pyplot as plt
import numpy as np
import math
import sys

profiles, pi_1 = np.genfromtxt(fname='Data/DPi_1.dat',unpack=True,skip_header=1)

t, l, r, a = np.genfromtxt(
    fname="Data/filteredMALTR.dat",usecols=[3,2,4,1],unpack=True,skip_header=1)

dAge = [a[1] - a[0]]
for i in range(1,len(a)):
    dAge.append(a[i] - a[i-1])

for i in range(len(l)):
    l[i] = math.log10(l[i])

models, sfs = np.genfromtxt(fname="Data/SFS.dat",unpack=True,skip_header=1)
lfs = np.genfromtxt(fname="Data/LFS.dat",usecols=[1],skip_header=1)
sfs1 = np.genfromtxt(fname="Data/SFS01.dat",usecols=[1],skip_header=1)
bvfMax = np.genfromtxt(fname="Data/MaxBvf.dat",usecols=[1],skip_header=1)
disr, dism, disR = np.loadtxt(fname="Data/Discontinuity.dat",
                        usecols=[1,4,2],unpack=True,skiprows=1)

s, e = np.genfromtxt(fname='Data/critPoints.dat',unpack=True,skip_header=1)
start_pro = int(s)
end_pro = int(e)

vclose = np.genfromtxt(
    fname="Data/vClosestToVmax.dat",usecols=[2],skip_header=1)

def get_data(name):
    if (name.lower() in [ 'dpi', 'deltapi' ]):
        return pi_1
    elif (name.lower() in [ 'l', 'lum', 'luminosity' ]):
        return l
    elif (name.lower() in [ 't', 'temp', 'temperature']):
        return t
    elif (name.lower() in [ 'r','rad', 'radius']):
        return r
    elif (name in [ 'dnu', 'dnu02', 'deltanu', 'deltanu02', 'sfs', 'SFS' ]):
        return sfs
    elif (name in [ 'Dnu', 'Deltanu', 'lfs', 'LFS' ]):
        return lfs
    elif (name in [ 'dnu01', 'deltanu01', 'sfs01', 'SFS01' ]):
        return sfs1
    elif (name.lower() in [ 'vclose', 'vclosevmax', 'vclosestvmax', 'vclosesttovmax' ]):
        return vclose
    elif (name.lower() in [ 'age', 'a' ]):
        return a
    elif (name.lower() in [ 'da', 'dage' ]):
        return dAge
    elif (name.lower() in [ 'maxbvf', 'bvf', 'maxb', 'mb' ]):
        return bvfMax
    elif (name in [ 'disr', 'Disr', 'DISr' ]):
        return disr
    elif (name in [ 'dism', 'Dism', 'DISm' ]):
        return dism
    elif (name in [ 'disR', 'DisR', 'DISR' ]):
        return disR
    else:
        return []

def get_label(name):
    if (name.lower() in [ 'dpi', 'deltapi' ]):
        return r'$\Delta\Pi_{01}$'
    elif (name.lower() in [ 'l', 'lum', 'luminosity' ]):
        return r'$\log(L)$'
    elif (name.lower() in [ 't', 'temp', 'temperature']):
        return r'T$_{\mathrm{eff}}$'
    elif (name.lower() in [ 'r','rad', 'radius']):
        return r'R'
    elif (name in [ 'dnu', 'dnu02', 'deltanu', 'deltanu02', 'sfs', 'SFS' ]):
        return r'$\delta\nu_{02}$'
    elif (name in [ 'Dnu', 'Deltanu', 'lfs', 'LFS' ]):
        return r'$\Delta\nu$'
    elif (name in [ 'dnu01', 'deltanu01', 'sfs01', 'SFS01' ]):
        return r'$\delta\nu_{01}$'
    elif (name.lower() in [ 'vclose', 'vclosevmax', 'vclosestvmax', 'vclosesttovmax' ]):
        return r'$\nu_{\mathrm{closest}}\nu_{\mathrm{max}}$'
    elif (name.lower() in [ 'age', 'a' ]):
        return r'Age'
    elif (name.lower() in [ 'da', 'dage' ]):
        return r'$\Delta$Age'
    elif (name.lower() in [ 'maxbvf', 'bvf', 'maxb', 'mb' ]):
        return r'$N_{\mathrm{max}}$'
    elif (name in [ 'disr', 'Disr', 'DISr' ]):
        return "r$_{dis}$/R"
    elif (name in [ 'dism', 'Dism', 'DISm' ]):
        return "m$_{dis}$/M"
    elif (name in [ 'disR', 'DisR', 'DISR' ]):
        return "R$_{dis}$ $(R_☉)$"
    


x_values = models
xlabel = "Model Number"
if len(sys.argv) > 1:
    x_values = get_data(sys.argv[1])
    if (len(x_values) == 0):
        x_values = models
    else:
        for i in range(len(models)):
            if models[i] == start_pro:
                start_pro = i
                break
        for i in range(len(models)):
            if models[i] == end_pro:
                end_pro = i
                break
        xlabel = get_label(sys.argv[1])
        start_pro = x_values[start_pro]
        end_pro = x_values[end_pro]


def add_plot(name,plot_num,plot_type):
    plt.subplot(plot_num).minorticks_on()
    plt.axvline(start_pro,ls='dashed',color='k')
    plt.axvline(end_pro,ls='dashed',color='k')
    y_values = []
    ylabel = ''
    if "/" in name:
        name = name.split("/")
        y_values = [y0/y1 for y0,y1 in zip(get_data(name[0]),get_data(name[1]))]
        ylabel = '{}/{}'.format(get_label(name[0]),get_label(name[1]))
    else:
        y_values = get_data(name)
        ylabel = get_label(name)
    plt.plot(x_values,y_values,plot_type)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    start,end = plt.ylim()
    plt.yticks(np.arange(start, end, (end-start)/4))
    

to_plot = []
to_plot.append('DPi')
to_plot.append('L')
to_plot.append('T')
to_plot.append('R')
to_plot.append('Dnu/dnu')
to_plot.append('dnu')
to_plot.append('Dnu')
to_plot.append('dnu01')
to_plot.append('vclose')

if len(sys.argv) > 4:
    to_plot = sys.argv[4].split(' ')

base_subplot_number = 100*len(to_plot) + 11

plot_type = '-'
if len(sys.argv) > 2:
    plot_type = sys.argv[2]

for i in range(len(to_plot)):
    plot_number = base_subplot_number + i
    add_plot(to_plot[i],plot_number,plot_type)

for i in range(base_subplot_number,base_subplot_number+len(to_plot)):
    plt.subplot(i).yaxis.tick_right()

for i in range(base_subplot_number,base_subplot_number+len(to_plot)-1):
    labels = plt.subplot(i).get_xticklabels()
    for label in labels:
        label.set_visible(False)

plt.subplots_adjust(hspace=0)

if len(sys.argv) > 3:
    if (sys.argv[3] in ['Show', 'show', 's', 'S']):
        plt.show()
    else:
        plt.savefig("Plots/{}".format(sys.argv[3]))
else:    
    plt.show()

