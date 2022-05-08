# -*- coding: utf-8 -*-
"""
Created on Sun May  8 03:32:24 2022

@author: Flo Strich
"""

import numpy as np
from matplotlib import pyplot as plt

x = np.array((13, 35, 1, 20, 43, 1.37, 18, 37, 1.26, 42, 55, 2.06, 39, 44, 1.94, 84, 104, 4.31)).reshape((-1, 3)).T



# y = np.array([x[0] / x[1], x[2] / x[1]])

# y.sort(1)

# plt.plot(*y)


z = x[:2] / x[2]

#z.sort(1)

plt.plot(*z, "o")
