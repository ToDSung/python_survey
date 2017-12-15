# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 01:12:30 2017

@author: wlunareve
"""

"""
Given an array of integers, 
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

example
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


"""
.format() 來格式化字串
>>> '{0} is {1}!!'.format('Justin', 'caterpillar')
'Justin is caterpillar!!'
>>> '{real} is {nick}!!'.format(real = 'Justin', nick = 'caterpillar')
'Justin is caterpillar!!'
>>> '{real} is {nick}!!'.format(nick = 'caterpillar', real = 'Justin')
'Justin is caterpillar!!'
>>> '{0} is {nick}!!'.format('Justin', nick = 'caterpillar')
'Justin is caterpillar!!'
>>> '{name} is {age} years old!'.format(name = 'Justin', age = 35)
'Justin is 35 years old!'
>>>

"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target == nums[i]+nums[j]:
                print('question nums :  {0}'.format(nums))
                print('target : {0}'.format(target))
                print('location : {0} and answer : {1} '.format([i,j],[nums[i],nums[j]]))
                
twoSum([2,7,11,15],26)
