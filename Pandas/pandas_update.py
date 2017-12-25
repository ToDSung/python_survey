# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:27:30 2017

@author: wlunareve
"""

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import os

finance=pd.read_csv('.\\out\\BABA.csv')

'''更新多個欄位
# 指派一個值會讓索引到的每一個值，都被指派為新值
df.loc[df['Sex']=='male', 'Sex'] = 1
df.loc[df['Sex']=='female', 'Sex'] = 0

# 指派一個list
std = df['Age'].std()  #算出標準差
mean = df['Age'].mean()  #算出平均數
size = len(df[pd.isnull(df['Age'])])  #算出null值的長度
age_null_random_list = np.random.randint(mean - std, mean + std, size=size)  #產生一個屆在一個標準差之內的隨機整數
df.loc[pd.isnull(df['Age']), 'Age'] = age_null_random_list  # 將隨機整數指派給null值
'''
