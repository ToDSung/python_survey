# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:45:56 2017

@author: wlunareve
"""

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
http://www.runoob.com/python3/python3-string.html
字符串呼叫擷取
#!/usr/bin/python3
 
var1 = 'Hello World!'
var2 = "Runoob"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

var1[0]:  H
var2[1:5]:  unoo
"""
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
# =============================================================================
#     subStringList=[]
#     for i in range(len(s)):
#         subStringList.append((s[i]))
#         print (subStringList)
# =============================================================================
    start = 0
    maxLength = 0
    usedChar = {}
    
    for i in range(len(s)):

        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i
        
        print (usedChar[s[i]],end=' ')
        print (s[i],end=' ')
        print (start,end=' ')
        print (maxLength)

    return [maxLength]
    
    
print(lengthOfLongestSubstring('aaabbcdefe'))