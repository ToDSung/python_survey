# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:41:09 2017

@author: wlunareve
"""
#try to create regular triangle
def regularTriangleByMyself(number):
    for i in range(1,number):
        if i%2==1:
            for x in range (1,number-int(i/2)):
                print (' ',end='')
            for j in range(0,i):
                print('+',end='')
            print()
    print()            

def judgeInput(number):
    if number%2==1:
        return number+1
    else:
        return number
regularTriangleByMyself(judgeInput(1))
regularTriangleByMyself(judgeInput(2))
regularTriangleByMyself(judgeInput(3))
regularTriangleByMyself(judgeInput(4))
regularTriangleByMyself(judgeInput(5))

