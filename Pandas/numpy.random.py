# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:38:40 2017

@author: wlunareve
"""

import numpy as np

#隨機取5個0~1之間的float
x=np.random.rand(5)
#隨機取5個-1~1之間的float
y=np.random.randn(5)
#隨機取整數5~15
z=np.random.randint(5,15)

#取0~1之間 2 * 3 的矩陣
v=np.random.rand(2,3)

#取0~19間的整數
w=np.random.randint(19)

print(x)
print(y)
print(z)
print(v)
print(w)