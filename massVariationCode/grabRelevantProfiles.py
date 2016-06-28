import numpy as np
import os.path
import sys
import shutil

bump_ages = np.genfromtxt(fname="trimmedMALTR.dat",usecols=[1],skip_header=1)
min_age = bump_ages[1]
max_age = bump_ages[len(bump_ages)-1]
model_not_grabbed = True
print("    Grabbing bump profiles:")

for i in range(1,int(sys.argv[1])):
    profile = "../profile%d.data"%(i)
    if os.path.isfile(profile):
        age = np.genfromtxt(fname=profile,usecols=[4],skip_header=2,max_rows=1)
        if age <= max_age and age >= min_age:
            print("      profile%d.data"%(i))
            shutil.copyfile("../profile%d.data"%(i),"gyre/profile%d.data"%(i))
            if model_not_grabbed:
                shutil.copyfile("../profile%d.mod"%(i-1),"bumpTrack/bumpStart.mod")
                model_not_grabbed = False
                f = open("bumpTrack/maxAge.dat",'w')
                f.write(str(max_age))
                f.close()
