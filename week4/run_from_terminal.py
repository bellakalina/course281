'''
run_from_terminal.py 10/1/26 alk
demonstrates that python can be run from the linux terminal
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(-10, 10, 300)
y = x**3 + x**2 + x + 1

plt.plot(x, y, label = '$x^3 + x^2 + x + 1$')

plt.legend()
plt.xlabel('x', fontsize = 15)
plt.ylabel('y', fontsize = 15)
plt.title('Run from terminal, quadratic plot', fontsize = 20)

plt.savefig('run_from_terminal_plot.png')
plt.show()