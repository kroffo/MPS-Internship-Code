import matplotlib.pyplot as plt
import numpy as np
import math
import os.path
import sys
import shutil

end_ages = np.genfromtxt(fname="trimmedMALTR.dat",usecols=[1],skip_header=1)
min_age = end_ages[1]
max_age = end_ages[len(end_ages)-1]
model_not_grabbed = True
bump_temps, bump_ages = np.genfromtxt(fname="critPoints.dat",usecols=[0,3],unpack=True,skip_header=1)
bump_min_temp = bump_temps[0]
bump_max_temp = bump_temps[1]
bump_max_age = bump_ages[1]
bump_model_not_grabbed = True
zoom_age_max_not_found = True

t = []
l = []
tmax = 0
tmin = 0
lmax = 0
lmin = 0

print("    Grabbing bump profiles:")

for i in range(1,int(sys.argv[1])):
    profile = "../profile%d.data"%(i)
    if os.path.isfile(profile):
        age, temp, lum = np.genfromtxt(fname=profile,usecols=[4,6,7],skip_header=2,max_rows=1)
        if age <= max_age and age >= min_age:
            print("      profile%d.data"%(i))
            temp = math.log10(temp)
            lum = math.log10(lum)
            t.append(temp)
            l.append(lum)
            shutil.copyfile("../profile%d.data"%(i),"gyre/profile%d.data"%(i))
            if model_not_grabbed:
                shutil.copyfile("../profile%d.mod"%(i-1),"bumpTrack/bumpStart.mod")
                model_not_grabbed = False
                f = open("bumpTrack/maxAge.dat",'w')
                f.write(str(max_age))
                f.close()
            if (temp < bump_max_temp) and (bump_model_not_grabbed):
                bump_model_not_grabbed = False
                tmin = temp
                lmin = lum
                shutil.copyfile("../profile%d.mod"%(i-1),"bumpTrack/zoomStart.mod")
            if (temp < bump_min_temp) and (not bump_model_not_grabbed) and (
                  zoom_age_max_not_found) and (age > bump_max_age):
                f = open("bumpTrack/zoomMaxAge.dat",'w')
                tmax = temp
                lmax = lum
                end_age = np.genfromtxt(fname="../profile%d.data"%(i+2),usecols=[4],skip_header=2,max_rows=1)
                f.write(str(end_age))
                f.close()
                zoom_age_max_not_found = False
                
#plt.plot(t,l,'b.')
#plt.plot(tmin,lmin,'ro')
#plt.plot(tmax,lmax,'ro')
#plt.gca().invert_xaxis()

#plt.show()
