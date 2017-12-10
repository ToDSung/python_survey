# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:28:05 2017

@author: wlunareve
"""

#畫圖函式庫
#mpt is a customize object name
#mpt 是一個自定義物件名稱
import matplotlib.pyplot as plt
import numpy as np

month1=[1,2,3,4,5,8,10,12]
month2=[1,3,4,5,6,7,11,12]

sale1=[20000,40000,60000,80000,100000,120000,140000,160000]
sale2=[100000,20000,30000,150000,120000,50000,10000,180000]

plt.figure(1) #圖1
plt.plot(month1,sale1,lw=2,label='Ivy Lin')
plt.plot(month2,sale2,lw=2,label='johnny Wu')
plt.xlabel('month')
plt.ylabel('Dollars')
plt.legend()#顯示標記
plt.title('mpt example')

plt.figure(2) #圖2
#plot()第三個參數是格式字串點
plt.plot([1,2,3,4],[1,4,9,16],'ro')

#mpt.cla()中斷目前繪圖
plt.figure(3)
# 0 to 5 range 0.2
t=np.arange(0.,5.,0.2)
#'r--'紅色虛線,'bs'藍色矩形,'g^'綠色三角形
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show