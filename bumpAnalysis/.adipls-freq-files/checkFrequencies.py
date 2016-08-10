import numpy as np

import sys

inputFileName = sys.argv[1]

#print("Analyzing",inputFileName)

l, n, f = np.loadtxt(fname=inputFileName,usecols=(0,1,2),unpack=True)

previous = 0
current_l = 0

with open("errors.txt", "a") as errorFile:

    for i in range(len(f)):
        if l[i] > current_l:
            current_l = l[i]
        elif f[i] < previous:
            errorFile.write(
                "ERROR: \t {} \t l =".format(inputFileName),l[i]," n =",n[i])
            print("ERROR: \t {} \t l =".format(inputFileName),l[i]," n =",n[i])
        previous = f[i]
