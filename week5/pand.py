'''pand.py 10/6/26 alk
try out pandas.
'''

import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('week5/data_files/gl2.xlsx')

xs = df['x'].to_numpy()
ys = df['y'].to_numpy()

plt.plot(xs, ys, 'bo-')
plt.show()