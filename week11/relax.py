'''relax.py 11/17/26 alk
relaxation method'''

import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

# IVP
ll = 1.0 # square edge length [m]
vvtop = 100.
vvbot = -100.
vvleft = -100.
vvright = 100. # voltages on edges [V]
nn = 100 # points on each edge


# make grid, set boundaries
vv = np.zeros((nn, nn))
vv[-1, :] = vvtop
vv[0, :] = vvbot
vv[:, 0] = vvleft
vv[:, -1] = vvright
# print(vv)

dvvmax = 0.001 # biggest change allowed
sweeps = 0
maxsweeps = 3000
start = perf_counter()

om = 0.9 # omega - overrelaxation parameter
# at om = 0, takes 7s to run; at om = 0.9, takes 1s to run

while sweeps < maxsweeps:
    dvvbig = 0. # biggest change this sweep
    for r in range(1, nn - 1):
        for c in range(1, nn - 1):
            vvav = 0.25 * (vv[r + 1, c] + vv[r - 1, c] + vv[r, c + 1] + vv[r, c - 1])
            dvv = (vvav - vv[r, c]) * (1 + om)
            dvvbig = max(dvvbig, abs(dvv))
            vv[r, c] += dvv
    sweeps += 1

    if dvvbig < dvvmax:
        break

end = perf_counter()
took = end - start

print(f'Time taken: {took:.5f}s')
print(f'Sweeps: {sweeps}')
print(f'dvvbig = {dvvbig}')

plt.imshow(vv, extent = (0, ll, 0, ll), origin = 'lower')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.colorbar()
plt.show()