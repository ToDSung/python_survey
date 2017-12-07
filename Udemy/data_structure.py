# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:33:59 2017

@author: wlunareve
"""

#串列 先進先出 list

list1=['a','b','c','d','e']
print(list1)
#['a', 'b', 'c', 'd', 'e']

#count()數量
print(list1.count('b'))
#1

#index()索引位置
print(list1.index('d'))
#3

#reverse()前後換
list1.reverse()
print(list1)
#['e', 'd', 'c', 'b', 'a']

#append()加在後面
list1.append('2')
print(list1)
#['e', 'd', 'c', 'b', 'a', 2]

#sort()排序
list1.sort()
print(list1)
#['2', 'a', 'b', 'c', 'd', 'e']

#pop()拿掉最後面 屬於堆疊的操作

#堆疊 先進後出 stack

stack1=[3,4,5]
stack1.append(6)
#stack=[3,4,5,6]
stack1.append(7)
#stack=[3,4,5,6,7]
stack1.pop()
#7
stack1.pop()
#6
stack1

#佇列 先進先出 queue

from collections import deque

queue1=deque(['阿呆','Eric','John','Michael'])
print(queue1)
#deque(['阿呆', 'Eric', 'John', 'Michael'])

queue1.append('Terry')
print(queue1)
#deque(['阿呆', 'Eric', 'John', 'Michael', 'Terry'])

#popleft() 先進先出
queue1.popleft()
print(queue1)
#dequedeque(['Eric', 'John', 'Michael', 'Terry'])

#---------------------------------------------------------------------#
#list 串列[]
#tuple 數組 固定元素()
tp1=()
print(tp1)
#()
tp2=(1,2,3,4,5,6,7,8)
print(tp2)
#(1, 2, 3, 4, 5, 6, 7, 8)
print(sum(tp2))
#36
print(tp2[2:5])
#(3,4,5)
print(tp2[-1])
#8

tp3=tuple([2**x for x in range(1,8)])
print(tp3)
#(2, 4, 8, 16, 32, 64, 128)

tp4=tuple('Ivy Lin')
print(tp4)
#('I', 'v', 'y', ' ', 'L', 'i', 'n')
tp5=('John','小寶','曉雯')
print(tp5)
#('John', '小寶', '曉雯')
print(tp4+tp5)
#('I', 'v', 'y', ' ', 'L', 'i', 'n', 'John', '小寶', '曉雯')

tp6=tuple([1,5,6,3,2,4,7,9,8])
print(tp6)
#(1, 5, 6, 3, 2, 4, 7, 9, 8)
print(max(tp6))
#9
print(min(tp6))
#1

#數組轉串列 tuple to list

listFromTuple=list(tp6)
print(listFromTuple)
#[1, 5, 6, 3, 2, 4, 7, 9, 8] 

#sort()會直接修改原始的list並排序完成
listFromTuple.sort()
print(listFromTuple)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

tp8=tuple(listFromTuple)
tp9=tuple(listFromTuple)
print(tp8==tp9)
#True

#set 集合 沒有順序、重複 {}
set1=set()
set2=set(['a','b','c','d','e'])
print(set2)
#{'a', 'c', 'd', 'e', 'b'}
set2.add('f')
print(set2)
#{'a', 'c', 'f', 'd', 'e', 'b'}
set2.remove('e')
print(set2)
#{'a', 'c', 'f', 'd', 'b'}

set3={'g','e','t','s','a'}
#union() 聯集 set2,set3有的元素
print(set2.union(set3))
#{'a', 'g', 'c', 't', 'f', 'd', 's', 'e', 'b'}

#intersection() 交集 set2,set3 皆有元素
print(set2.intersection(set3))
#{'a'}

#difference set2有 set3沒有
print(set2.difference(set3))
#{'c', 'f', 'b', 'd'}


#dict 字典:集合加上索引{索引:值}

tel={'Justin':'0920909872','Ivy':'0922876895'}
tel['Johnny']='0920885356'
print(tel)
#{'Justin': '0920909872', 'Ivy': '0922876895', 'Johnny': '0920885356'}
print(tel['Ivy'])
#0922876895
del tel['Johnny']
tel['Mary']='0987878787'
print(tel)
#{'Justin': '0920909872', 'Ivy': '0922876895', 'Mary': '0987878787'}
print(list(tel.keys()))
#['Justin', 'Ivy', 'Mary']
print(sorted(tel.keys()))
#['Justin', 'Ivy', 'Mary']
print('Ivy' in tel)
#True
print('Johnny' in tel)
#False
