# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:45:13 2017

@author: wlunareve
"""

import matplotlib.pyplot as plt
import numpy as np

A = np.random.rand(5, 5)
plt.figure(1)
plt.imshow(A, interpolation='nearest')
plt.grid(True)

plt.figure(2)
plt.imshow(A, interpolation='bilinear')
plt.grid(True)

plt.figure(3)
plt.imshow(A, interpolation='bicubic')
plt.grid(True)

plt.show()