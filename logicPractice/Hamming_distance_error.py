# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 23:14:41 2017

@author: wlunareve
"""

'''zip function
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)
    >>> zipped
    [(1, 4), (2, 5), (3, 6)]
    >>> zip(a,c)
    [(1, 4), (2, 5), (3, 6)]
    >>> zip(*zipped)
    [(1, 2, 3), (4, 5, 6)]
'''

def hammingDistance(x,y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    listBinaryX=decimalToBinary(x)
    print(listBinaryX)
    listBinaryY=decimalToBinary(y)
    print(listBinaryY)    
    
    return sum([listBinaryX != listBinaryY for listBinaryX, listBinaryY in zip(listBinaryX, listBinaryY)])
    
def decimalToBinary(a,binary=[]):
    if a:
        decimalToBinary(floor(a/2))
        binary.append(int(a%2))
        return binary
    else:
        binary.clear()


print(hammingDistance(15,8))

