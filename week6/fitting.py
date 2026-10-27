'''fitting.py 10/13/26 alk
fit excel files to data'''

import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
import pandas as pd
from dfit import Dfit

# read data file and list columns
data1 = pd.read_excel('week6/data1.xlsx')
print(list(data1))

# extract to arrays
c0,c1,c3 = list(data1)    # get the column names
xs1 = data1[c0].to_numpy()
ys1 = data1[c1].to_numpy()
yerrs1 = data1[c3].to_numpy()
plt.errorbar(xs1, ys1, yerrs1, fmt = 'o b')
plt.ylabel(c1)
plt.show()

def lin_eq(x, a, b):
    '''linear equation'''
    return a * x + b

# use dfit to fit the data
lin_fit = Dfit(lin_eq, xs1, ys1, yerrs1)
lin_fit.printfit()
lin_fit.plotfit()