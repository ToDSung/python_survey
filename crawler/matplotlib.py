# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:28:05 2017

@author: wlunareve
"""

#畫圖函式庫
#mpt is a customize object name
#mpt 是一個自定義物件名稱
import matplotlib.pyplot as mpt

month1=[1,2,3,4,5,8,10,12]
month2=[1,3,4,5,6,7,11,12]

sale1=[20000,40000,60000,80000,100000,120000,140000,160000]
sale2=[100000,20000,30000,150000,120000,50000,10000,180000]

mpt.figure(1) #圖1
mpt.plot(month1,sale1,lw=2,label='Ivy Lin')
mpt.plot(month2,sale2,lw=2,label='johnny Wu')
mpt.xlabel('month')
mpt.ylabel('Dollars')
mpt.legend()#顯示標記
mpt.title('mpt example')




mpt.figure(2) #圖2
mpt.plot([1,2,3,4],[1,4,9,16])

mpt.show()

#mpt.cla()中斷目前繪圖