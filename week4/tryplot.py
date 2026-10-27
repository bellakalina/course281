'''
tryplot.py 9/28/26 alk
try out plotting.
'''

import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt

xs = np.linspace(-10,10,300)
ys = cos(xs)

plt.plot(xs, ys)
# plt.show()

y2s = sin(xs)
plt.plot(xs,y2s)
plt.xlabel('$\\pi\\Delta\\delta$')
plt.ylabel('$\\cos(x)$')
plt.show()