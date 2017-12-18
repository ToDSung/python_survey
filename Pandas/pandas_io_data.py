# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 00:08:19 2017

@author: wlunareve
"""

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import os

'''
不要連續下載資料，會有錯誤
#finance= web.DataReader('BABA','yahoo', start='2017/1/1')
'''
print (finance.tail(3))

#finance.index 是日期
print (finance.index)
#x軸 finance.index y軸 finance 的索引 Open 中的值
plt.plot(finance.index, finance['Open'])
plt.xlabel('Date-Month')
plt.ylabel('dollars')
plt.show
'''
os.mkdir('.\\out')
finance.to_csv('.\\out\\BABA.csv')
'''