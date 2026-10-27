'''subplots.py 10/6/26 alk
try out subplots.
'''

import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
import pandas as pd

# going to make a plot w/ 4 subplots showing x**n for n = 1, 2, 3, 4

xs = np.linspace(-1, 1, 300)

for i in range(1, 5):
    plt.subplot(220+i) # 2 cols, 2 rows, plot 1
    plt.plot(xs, xs**i)

plt.show()