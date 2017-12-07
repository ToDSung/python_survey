# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 00:41:12 2017

@author: wlunareve
"""
"""
fp=open('檔案名稱','檔案開啟模式')
r讀
w寫
a從檔案尾寫入
r+開啟讀寫的檔案
w+清除檔案後讀寫內容
a+從檔案尾讀寫
"""

fp=open('file.txt','w+')

if fp!=None:
    print("檔案開啟成功")
    fp.write("小白")
    
fp.close()
fp=open('file.txt','r')
if fp!=None:
    fileRead=fp.readlines()
    print(fileRead)
fp.close()