'''oop.py 10/8/26 alk
try out object oriented programming.
'''

import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
import pandas as pd

# mylist = [1, 2, 3]
# mylist.append('foo')
# print(mylist)

class Spammer:
    # init is automatically called, self is passed to all class methods first
    def __init__(self, x):
        self.x = x # saves x so that other methods can use it

    def pr(self, n):
        print(n*self.x)

n = 3

hah = Spammer('hah ')
hee = Spammer('hee ')

# hah.pr(n)
# hee.pr(n)

# print(hah.x)
# print(hee.x)

# class inheritance
class Eggs(Spammer):
    '''eggs is a subclass of spammer'''
    def __init__(self):
        super().__init__('Eggs! ') # call the init of the super class
    def pr(self, n):
        super().pr(n)
        print('That\'s all')

egg = Eggs()
egg.pr(5)

class Part:
    '''represents a partcle at position x,y'''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y