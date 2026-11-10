'''odes.py 11/10/26 alk
practice integrating odes'''

import numpy as np
from numpy import cos, sin, exp, sqrt, log
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp

# problem: dy/dt = -y^3 + sin(t)
# for t in [0, 10] s.t. y(0) = 0

# define the ode
def prob1(t, y):
    '''derivative function: dy/dt = -y^3 + sin(t)'''
    dydt = -1 * y**3 + sin(t)
    return dydt

# domain
ta = 0.
tb = 10.

# inital condition
y_0 = [0.]   # using a list for solve_ivp (vector initial condition)

# solve using solve_ivp
nn_ivp = 300
ts = np.linspace(ta, tb, nn_ivp)
t_span = ts[0], ts[-1]
sol = solve_ivp(prob1, t_span, y_0, t_eval = ts)
ys = sol.y[0] # solution is 1st and only row

# solve with euler
nn = 100
h = (tb - ta) / (nn - 1)
ts_eul = np.linspace(ta, tb, nn)
ys_eul = np.zeros_like(ts_eul)
ys_eul[0] = y_0[0]

for j in range(nn - 1):
    tj = ts_eul[j]
    yj = ys_eul[j]
    ys_eul[j + 1] = yj + h * prob1(tj, yj)

# solve with RK2
ts_rk2 = np.linspace(ta, tb, nn)
ys_rk2 = np.zeros_like(ts_rk2)
ys_rk2[0] = y_0[0]

for j in range(nn - 1):
    tj = ts_rk2[j]
    yj = ys_rk2[j]
    k1 = h * prob1(tj, yj)
    k2 = h * prob1(tj + h/2, yj + k1 / 2)
    ys_rk2[j + 1] = yj + k2

plt.title(f'Using {nn} points')
plt.plot(ts_eul, ys_eul, 'b.', label = "Euler's")
plt.plot(ts, ys, label = 'solve_ivp', color = 'k')
plt.plot(ts_rk2, ys_rk2, 'r.', label = "RK2")
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()