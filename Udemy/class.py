# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:43:34 2017

@author: wlunareve
"""

class MyClass:
    i=12345

print(MyClass.i)

class complex:
    
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
    def __del__(self):
        print("object deleted")
x=complex(3.0,-4.5)

print(x.r,x.i)

x=None

class MyClass2:
    
    i=12345
    def f():
        return "Hello World!"
y=MyClass2
print(y.i)
print(y.f())    

        