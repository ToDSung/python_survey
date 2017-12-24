# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 00:10:51 2017

@author: wlunareve
"""
from pymongo import MongoClient
import pandas
import pandas_datareader.data as web

#data=web.DataReader('AAPL','yahoo',start='2017/1/1')
conn = MongoClient("mongodb://localhost:27017/")
db = conn.MongoDB_Practice
collection = db.AAPL

collection.delete_many({})

print(data)

data_dict=data.to_dict('record')
print(data_dict)
collection.insert_many(data_dict)