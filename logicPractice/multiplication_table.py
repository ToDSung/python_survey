# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:38:56 2017

@author: wlunareve
"""

def MultiplicationTable(number):
    for i in range(number):
        i=i+1
        for j in range(number):            
            j=j+1
            print ('%s*%s=%s \t' % (i,j,i*j), end='')
        print()
        
MultiplicationTable(9)