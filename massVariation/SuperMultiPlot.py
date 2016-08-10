# This script can be edited and run to plot as configured. It will save in
# Plots/SuperPlot.png
#
# However, this script can be called with parameters:
#
#     python SuperPlot.py <xvar> <point-type> <save-name> <list>
#
#       xvar: model or temperature
# point-type: type of points to plot
#  save-name: if "show" will show the plot. Otherwise, will save in Plots/<list>
#       list: A list of what to plot. Ex: "DPi dnu T L R"

import matplotlib.pyplot as plt
import numpy as np
import math
import sys

connect_ends = True

profiles = []
pi_1 = []
l, t, r = [], [], []
sfs, lfs, sfs1, vclose = [], [], [], []
bump_starts_x = []
bump_ends_x = []
bump_starts_y = []
bump_ends_y = []
start_index, end_index = 0, 0

def get_data(name):
    if (name in [ 'dpi', 'DPi', 'deltapi', 'deltaPi', 'DeltaPi', 'Deltapi' ]):
        return pi_1
    elif (name in [ 'l', 'L', 'lum', 'Lum', 'luminosity', 'Luminosity' ]):
        return l
    elif (name in [ 't', 'T', 'temp', 'Temp', 'temperature', 'Temperature' ]):
        return t
    elif (name in [ 'r', 'R', 'rad', 'Rad', 'radius', 'Radius' ]):
        return r
    elif (name in [ 'dnu', 'dnu02', 'deltanu', 'deltanu02', 'sfs', 'SFS' ]):
        return sfs
    elif (name in [ 'Dnu', 'Deltanu', 'lfs', 'LFS' ]):
        return lfs
    elif (name in [ 'dnu01', 'deltanu01', 'sfs01', 'SFS01' ]):
        return sfs1
    elif (name in [ 'vclose', 'vclosevmax', 'vclosestvmax', 'vclosesttovmax' ]):
        return vclose
    else:
        return []

def get_label(name):
    if (name in [ 'dpi', 'DPi', 'deltapi', 'deltaPi', 'DeltaPi', 'Deltapi' ]):
        return r'$\Delta\Pi_{01}$'
    elif (name in [ 'l', 'L', 'lum', 'Lum', 'luminosity', 'Luminosity' ]):
        return r'$\log(L)$'
    elif (name in [ 't', 'T', 'temp', 'Temp', 'temperature', 'Temperature' ]):
        return r'T$_{\mathrm{eff}}$'
    elif (name in [ 'r', 'R', 'rad', 'Rad', 'radius', 'Radius' ]):
        return r'R'
    elif (name in [ 'dnu', 'dnu02', 'deltanu', 'deltanu02', 'sfs', 'SFS' ]):
        return r'$\delta\nu_{02}$'
    elif (name in [ 'Dnu', 'Deltanu', 'lfs', 'LFS' ]):
        return r'$\Delta\nu$'
    elif (name in [ 'dnu01', 'deltanu01', 'sfs01', 'SFS01' ]):
        return r'$\delta\nu_{01}$'
    elif (name in [ 'vclose', 'vclosevmax', 'vclosestvmax', 'vclosesttovmax' ]):
        return r'$\nu_{\mathrm{closest}}\nu_{\mathrm{max}}$'

def add_plot(name,plot_num,plot_type):
    plt.subplot(plot_num).minorticks_on()
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
    bump_starts_x[(plot_num % 10) - 1].append(x_values[start_index])
    bump_starts_y[(plot_num % 10) - 1].append(y_values[start_index])
    bump_ends_x[(plot_num % 10) - 1].append(x_values[end_index])
    bump_ends_y[(plot_num % 10) - 1].append(y_values[end_index])
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

for i in to_plot:
    bump_starts_x.append([])
    bump_ends_x.append([])
    bump_starts_y.append([])
    bump_ends_y.append([])

plot_type = '-'
if len(sys.argv) > 2:
    plot_type = sys.argv[2]

for i in range(7, 23):
    path = "mass/{:03.1f}/bumpTrack/LOGS/Analysis/".format(i/10)

    profiles, pi_1 = np.genfromtxt(fname=path+'Data/DPi_1.dat',
                                   unpack=True,skip_header=1)

    t, l, r = np.genfromtxt(fname=path+"Data/filteredMALTR.dat",
                            usecols=[3,2,4],unpack=True,skip_header=1)

    for i in range(len(l)):
        l[i] = math.log10(l[i])

    models, sfs = np.genfromtxt(fname=path+"Data/SFS.dat",unpack=True,skip_header=1)
    lfs = np.genfromtxt(fname=path+"Data/LFS.dat",usecols=[1],skip_header=1)
    sfs1 = np.genfromtxt(fname=path+"Data/SFS01.dat",usecols=[1],skip_header=1)

    s, e = np.genfromtxt(fname=path+'Data/critPoints.dat',unpack=True,skip_header=1)
    start_index = int(s)
    end_index = int(e)
    for i in range(len(models)):
        if (int(models[i]) == start_index):
            start_index = i
            break
    for i in range(len(models)):
        if (int(models[i]) == end_index):
            end_index = i
            break
    

    vclose = np.genfromtxt(
        fname=path+"Data/vClosestToVmax.dat",usecols=[2],skip_header=1)

    x_values = models
    xlabel = "Model Number"
    if len(sys.argv) > 1:
        x_values = get_data(sys.argv[1])
        if (len(x_values) == 0):
            x_values = models
        else:
            xlabel = get_label(sys.argv[1])

    base_subplot_number = 100*len(to_plot) + 11

    for j in range(len(to_plot)):
        plot_number = base_subplot_number + j
        add_plot(to_plot[j],plot_number,plot_type)

for i in range(base_subplot_number,base_subplot_number+len(to_plot)):
    if (connect_ends):
        plt.subplot(i).plot(bump_starts_x[(i % 10) - 1],bump_starts_y[(i % 10) - 1],'k-')
        plt.subplot(i).plot(bump_ends_x[(i % 10) - 1],bump_ends_y[(i % 10) - 1],'k-')
    plt.subplot(i).yaxis.tick_right()
    if (xlabel == get_label("temp")):
        plt.subplot(i).invert_xaxis()

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

