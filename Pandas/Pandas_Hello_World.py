# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:28:42 2017

@author: wlunareve
"""

from pandas import Series,DataFrame
import pandas as pd
'''
pandas 有兩種自己的資料結構

Series 是一種一維的資料類型，其中的每個元素都有各自的標籤
DataFrame 是一個二維的、表格型的資料結構，可以把它當作一個 Series 的字典。
'''
#可以建立豎起來的list
s=Series([100,'python','Soochow','Qiwsir'])
print(s)

#可以自定義屬性名稱
s2=Series([100,'python','Soochow','Qiwsir'], index=['mark','title','university','name'])
print(s2)
'''
s2.index
Out[]:Index(['mark', 'title', 'university', 'name'], dtype='object')
s.values
Out[]: array([100, 'python', 'Soochow', 'Qiwsir'], dtype=object)
s.index
Out[]: RangeIndex(start=0, stop=4, step=1)
'''

s3=Series([3,9,4,7], index=['a','b','c','d'])
print(s3)
#可以做簡易計算
print(s3[s3>5])
'''
b    9
d    7
dtype: int64
'''
print(s3*8)
'''
a    24
b    72
c    32
d    56
dtype: int64
'''
#可以建立矩陣
d=DataFrame( {"name":["yahoo","google","facebook"], "marks":[200,400,800], "price":[9, 3, 7]})
print(d)
'''
   marks      name  price
0    200     yahoo      9
1    400    google      3
2    800  facebook      7
'''