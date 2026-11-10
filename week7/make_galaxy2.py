""" make_galaxy2.py  10/23/26  D. Candela
Make 3D coordinates of stars in an imaginary galaxy then make 3D scatter plot of the
stars and optionally write star coordinates to a file.
(Modified from make_galaxy.py 10/23/26 - this program leaves the galaxy flat)
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import cos,sin,arctan2,sqrt,cross,eye
from scipy import linalg

STARS = 5000   # stars in main disk
STARSB = 3300  # stars in central bulge
RR = 10.       # radius of disk, kpc
RRB = 3.3      # radius of central bulge, kpc
ARMN = 5       # number of spiral arms
ARMEPS = 0.7   # arm density modulation strength, dimensionless
ARMTT = 3.0    # arm twist rate, dimensionless

# Make 2D array of sprial disk star coordinates.
rng = np.random.default_rng()
xs = RR*rng.normal(size=STARS)
ys = RR*rng.normal(size=STARS)
zs = np.zeros(STARS)   # start with stars gaussian-distributed in xy plane
rs = sqrt(xs**2 + ys**2)
thets = arctan2(ys,xs)   # convert to polar coordinates
# Add spiral arms by modifying theta.
thet2s = thets + (ARMEPS/ARMN)*sin(ARMN*thets) + ARMTT * rs/RR
x2s = rs*cos(thet2s)
y2s = rs*sin(thet2s)   # convert back to cartesian
disk = np.stack((x2s,y2s,zs),axis=1)  # stack x,y,z as columns of 2D array

# Make 2D array of bulge star coordinates
xbs = RRB*rng.normal(size=STARSB)
ybs = RRB*rng.normal(size=STARSB)
zbs = RRB*rng.normal(size=STARSB)           # make the bulge stars
bulge = np.stack((xbs,ybs,zbs),axis=1)  # stack x,y,z as columns of 2D array

galaxy = np.concatenate((disk,bulge)) # combine disk and bulge to give galaxy

# preliminaries to plotting
xalls = galaxy[:,0]
yalls = galaxy[:,1]
zalls = galaxy[:,2]   # slice into columns for x, y, z
nall = len(xalls)     # how many stars

# make the scatter plot
plt.figure(figsize=(10,10))
plt.rc('font', size=12)
ax = plt.axes(projection='3d')            # get some 3D axes
ax.scatter(xalls,yalls,zalls,s=1,c="m")  # do the scatter plot
psize = 25.0                      # size of plotting box
ax.set_xlim(-psize, psize)
ax.set_ylim(-psize, psize)
ax.set_zlim(-psize, psize)
ax.set_xlabel("x(kpc)")
ax.set_ylabel("y(kpc)")
ax.set_zlabel("z(kpc)")
plt.title ("Imaginary Galaxy with %d stars"%nall)
plt.show()

# Write the data to a file
np.savetxt("galaxy2.txt",galaxy,newline="\r\n",fmt="%10.6f",
           header="%10s %10s %10s"%("x(kpc)","y(kpc)","z(kpc)"),
           comments="")
