# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:30:06 2017

@author: wlunareve
"""

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import os

finance=pd.read_csv('.\\out\\BABA.csv')
'''
#根據row index索引 0~2XX
df.loc[<indices_list>, <columns_list>]
'''
#輸出最後三筆
print(finance.tail(3))
'''
           Date        Open        High         Low       Close   Adj Close    Volume  
239  2017-12-13  175.190002  177.699997  174.300003  176.470001  176.470001   18653400  
240  2017-12-14  173.110001  173.389999  169.610001  171.750000  171.750000   32629400  
241  2017-12-18  174.600006  174.699997  172.369995  174.309998  174.309998    8519413  
'''

#從csv中讀取以後才有0~25X 的索引
print(finance.loc[0])
'''
Date         2017-01-03
Open                 89
High                 89
Low               88.08
Close              88.6
Adj Close          88.6
Volume          8789400
Name: 0, dtype: object
'''
print(finance.loc[len(finance)-1])
'''
Date         2017-12-18
Open              174.6
High              174.7
Low              172.37
Close            174.31
Adj Close        174.31
Volume          8519413
Name: 241, dtype: object
'''
print(finance['Date'])
'''
0      2017-01-03
1      2017-01-04
2      2017-01-05
3      2017-01-06
4      2017-01-09
5      XXXX-XX-XX
......
......
......
'''
#兩個中括號
print(finance.loc[[2,3,5]])
'''
         Date       Open       High        Low      Close  Adj Close    Volume
2  2017-01-05  91.910004  94.809998  91.639999  94.370003  94.370003  16821500
3  2017-01-06  94.400002  94.500000  93.000000  93.889999  93.889999   7639800
5  2017-01-10  96.400002  97.903999  95.550003  96.750000  96.750000  14780600
'''
print(finance[['Date','Volume']])
'''
           Date    Volume
0    2017-01-03   8789400
1    2017-01-04  11490200
2    2017-01-05  16821500
3    2017-01-06   7639800
4    2017-01-09  10792900
'''

print(finance.loc[0,'Date'])
'''
2017-01-03
'''
print(finance.loc[[0,1,2],'Date'])
'''
0    2017-01-03
1    2017-01-04
2    2017-01-05
Name: Date, dtype: object
'''
print(finance.loc[range(3),['Date','Open']])
'''
         Date       Open
0  2017-01-03  89.000000
1  2017-01-04  88.985001
2  2017-01-05  91.910004
'''
# 找出指定資料的用法
print(finance.loc[finance['Date']=='2017-12-05'])
'''
           Date        Open        High     Low       Close   Adj Close    Volume  
233  2017-12-05  165.279999  172.960007  164.25  168.960007  168.960007  31609900  
'''
print(finance.loc[finance['Volume']>50000000,['Date','Volume']])
'''
           Date    Volume
108  2017-06-08  80936900
109  2017-06-09  54367400
157  2017-08-17  56840300
'''

