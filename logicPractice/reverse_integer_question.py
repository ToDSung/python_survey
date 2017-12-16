# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:39:43 2017

@author: wlunareve
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers 
within the 32-bit signed integer range. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows. 


"""
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x>0:
        strX=str(x)
        reverseStrX=[]
        for i in range(len(strX)):
            reverseStrX.append(strX[i])
        reverseStrX.reverse()
        anwser = ''.join(reverseStrX)
        return int(anwser)
    else:
        strX=str(x)
        reverseStrX=[]
        for i in range(1,len(strX)):
            reverseStrX.append(strX[i])
        reverseStrX.reverse()
        anwser =  '-' + ''.join(reverseStrX)
        return int(anwser)
    
print(reverse(-56789))