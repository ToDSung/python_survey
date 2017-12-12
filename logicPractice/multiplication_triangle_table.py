# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:50:55 2017

@author: wlunareve
"""


for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%2d'%(i,j,i*j),end=' ')
    print()

print()

#左上三角格式输出九九乘法表

for i in range(1,10):
    for j in range(i,10):
        print('%d*%d=%2d'%(i,j,i*j),end=' ')
    print()
    
print()

#右上三角格式输出九九乘法表

for i in range(1,10):
    for k in range(1,i):
        print (end='       ')
    for j in range(i,10):
        print('%d*%d=%2d'%(i,j,i*j),end=' ')
    print()

print()

#左下三角格式输出九九乘法表
    
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2d'%(i,j,i*j),end=' ')
    print()

print()

#右下三角格式输出九九乘法表
for i in range(1,10):
    for k in range(1,10-i):
        print(end="       ")
    for j in range(1,i+1):
        product=i*j
        print("%d*%d=%2d" % (i,j,product),end=" ")
    print (" ")
