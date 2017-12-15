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

"""
位元 AND a & b
位元 OR  a | b
位元 XOR a ^ b
位元 NOT ~ a
"""


def hammingDistance(x,y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    print(bin(x))
    print(bin(y))
    
    return (bin(x^y).count('1'))

print(hammingDistance(255,8))

