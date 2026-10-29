'''ints.py 10/27/26 alk
numerical integration'''

import numpy as np
from numpy import sin, cos

def trap(f, a, b, nn):
    '''trapezoid-rule integration of f from a to b with nn slices'''
    h = (b - a)/nn
    wts = np.ones(nn + 1)
    wts[0] = 0.5
    wts[-1] = 0.5
    xs = np.linspace(a, b, nn + 1)
    fs = f(xs)
    return h * np.sum(fs * wts)

def igrnd(x):
    '''defines an integrand'''
    return sin(x)

a = 0
b = np.pi
print(f'exact: {1 - cos(b)}')

# try different slices for integral
for nn in (5, 10, 20, 50, 100):
    print(f'int({a:.2f}, {b:.2f}) w/ {nn} slices: {trap(igrnd, a, b, nn)}')