# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:02:59 2017

@author: wlunareve
"""

def square(number):
    for i in range(1,number):
        for j in range(1,number):
            print ('+',end='')
        print()
    print()
square(10)

"""
+
++
+++
++++
+++++
++++++
+++++++
++++++++
+++++++++
"""
def setFirstQuadrantTriangle(number):
    for i in range(1,number):
        for j in range (1,i+1):
            print('+',end='')
        print()
    print()

setFirstQuadrantTriangle(10)

"""
         +
        ++
       +++
      ++++
     +++++
    ++++++
   +++++++
  ++++++++
 +++++++++
"""
def setSecondQuadrantTriangle(number):
    for i in range(1,number):
        for k in range(i+1,number):
            print(' ',end='')
        for j in range(1,i+1):
            print('+',end='')
        print()
    print()
setSecondQuadrantTriangle(10)

"""
 +++++++++
  ++++++++
   +++++++
    ++++++
     +++++
      ++++
       +++
        ++
         +
"""
def setThirdQuadrantTriangle(number):
    for i in range(1,number):
        for k in range(1,i):
            print(' ',end='')
        for j in range(i,number):
            print('+',end='')
        print()
    print()
setThirdQuadrantTriangle(10)

"""
++++++++++
+++++++++
++++++++
+++++++
++++++
+++++
++++
+++
++
+

"""
def setFourthQuadrantTriangle(number):
    for i in range(1,number):
        for j in range(i,number):
            print ('+',end='')
        print()
    print()
setFourthQuadrantTriangle(10)
