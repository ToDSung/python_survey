# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:41:09 2017

@author: wlunareve
"""
#try to create regular triangle
def regularTriangleByMyself(number):
    for i in range(1,number):
        if i%2==1: #忽視偶數行生成
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
"""
regularTriangleByMyself(judgeInput(1))
regularTriangleByMyself(judgeInput(2))
regularTriangleByMyself(judgeInput(3))
regularTriangleByMyself(judgeInput(4))
regularTriangleByMyself(judgeInput(5))
"""
#輸入數字出現指定層數的等腰三角形

def createRegularTriangle(number):
    for i in range(1,number):
        for x in range (1,number-i):
            print(' ',end='')
        for j in range (1,i*2):
            print('+',end='')
        print()
        
createRegularTriangle(10)