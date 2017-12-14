# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:41:09 2017

@author: wlunareve
"""
#try to create regular triangle
def regularTriangleByMyself(number):
    for layer in range(1,number):
        if layer%2==1: #忽視偶數行生成
            for blank in range (1,number-int(layer/2)):
                print (' ',end='')
            for stars in range(0,layer):
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

def initializeTotalStars():
    global TotalStars
    TotalStars=0

def countTotalStars(inputstars=0):
    global TotalStars
    TotalStars = TotalStars+inputstars
    return TotalStars

def showTotalStarsAndDeleteVariable():
    global TotalStars
    print('Totally star number is :' + repr(TotalStars))
    del TotalStars

def createRegularTriangle(number):
    initializeTotalStars()
    for layer in range(1,number):
        for blank in range (1,number-layer):
            print(' ',end='')
        for stars in range (1,layer*2):
            print('+',end='')
        countTotalStars(stars)
        print()
    showTotalStarsAndDeleteVariable()
    

createRegularTriangle(20)


