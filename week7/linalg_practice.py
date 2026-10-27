'''linalg_practice.py 10/20/26 alk
try out fitting w/ scipy linalg'''

import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
from scipy import linalg

# # make two vectors and compute the various products
# a = np.array((1, 2, 3), float)
# b = np.array((4, 5, 6), float)
# print(f'a = {a}, b = {b}')

# # numpy product, multiplies component by component
# print(f'a * b = {a * b}')

# # dot product
# print(f'a @ b = {a @ b}')

# # cross product
# print(f'a cross b = {np.cross(a,b)}')

# make two arrays and compute the product
aa = np.array(((1, 2, 3), (4, 5, 6)), float)
bb = np.array(((5, 6), (7, 8), (9, 10)), float)
print(f'aa = {aa}, bb = {bb}')

# numpy product, multiplies component by component
# print(f'aa * bb = {aa ** bb}') # gives an error, only one row OR column can be expanded at one time

# dot product
print(f'aa @ bb = {aa @ bb}')

# matrix multiplication
print(f'matmul(aa, bb) = {np.matmul(aa, bb)}')