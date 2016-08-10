### Uses scaling relations to calculate numax and Dnu for each profile       ###
################################################################################

import numpy as np
import sys

profile_num=sys.argv[1]

print("Finding vfactors for profile {}...".format(profile_num))

m, t, r = np.genfromtxt(fname="../profile{}.data".format(profile_num),
                        usecols=[17,6,8],skip_header=2,max_rows=1)

m_sun = 1
r_sun = 1
t_sun = 5772
vmax_sun = 3050

vmax = ((m/m_sun)*((r_sun/r)**2)*((t_sun/t)**0.5))*vmax_sun

vac = 1.8*vmax

deltav_sun = 135.1

deltav = (((m/m_sun)*(r_sun/r)**3)**0.5)*deltav_sun

with open("Data/vfactors/vfactors{}.txt".format(profile_num), "w") as f:
    f.write("lower_bound\tupper_bound\tv_max\t\tdelta_v\n")
    f.write(str(vmax-5*deltav))
    f.write("\t")
    f.write(str(vmax+5*deltav))
    f.write("\t")
    f.write(str(vmax))
    f.write("\t")
    f.write(str(deltav))
