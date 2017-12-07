# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 01:00:52 2017

@author: wlunareve
"""
i=10 #全域

def testFunction():
    i=78#區域
    print(i)
testFunction()
print(i)
i=45
testFunction()    
print(i)


#return 以及預先帶入參數
def test2Function(a,b=2):
    return a+b

try1=test2Function(2,3)
print(try1)
try2=test2Function(2)
print(try2)
