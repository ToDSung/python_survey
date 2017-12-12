# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:58:43 2017

@author: wlunareve
"""

import numpy as np

a = np.array([[1,2],[3,4]])
sum0 = np.sum(a, axis=0)
sum1 = np.sum(a, axis=1)

print (sum0)
print (sum1)