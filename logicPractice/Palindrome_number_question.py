# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:33:12 2017

@author: wlunareve
"""
"""
Determine whether an integer is a palindrome. Do this without extra space.
「迴文」在中文當中是指倒正著念和反著念都相同的句子，前後對稱，例如「上海自來水來自海上」。
在英文當中是指正著看和反著看都相同的單字，例如「 madam 」。
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    print(str(x))
    print(str(x)[::-1])
    
    if str(x) == str(x)[::-1]:
        return 1
    else:
        return 0
    
print(isPalindrome('abcba'))
print(isPalindrome('123456'))