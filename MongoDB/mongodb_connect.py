# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:09:22 2017

@author: wlunareve
"""

from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017/")
'''
如果你只想連本機端的server你可以忽略，
遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，
請務必記得把腳括號的內容代換成自己的資料
'''
'''

SQL	NOSQL
server	server
database	database
table	collection
row	dictionary

'''

#MongoDB_Practice 是 SQL中的 database
db = conn.MongoDB_Practice
#collection = SQL 中的table
collection = db.FirstTrying
stats=collection.stats

print(stats)

'''
delete(刪除)
'''

#刪除全部資料
collection.delete_many({})


'''
insert(插入)
'''
#插入一個值
collection.insert_one({'name':'jerry'})
#document = SQL 中的一筆資料
document=({
    'name':'Anna',
    'phoneNumber':'0912345678',
    'age':'18',
    'gender':'woman'
    })
collection.insert_one(document)

#插入多個值
collection.insert_many([{'name':'Anna'},
                        {'name':'kitty'}])
'''
find(查詢)
'''
#查詢出屬性
cursor = collection.find_one({'name':'Anna'})
'''
cursor = collection.find_one({'_id': ObjectId('<id_string>')}) 
如果你在意速度的話用Id尋找會比用內容尋找快很多喔!
'''
for data in cursor:
    print(data,end =' ')
print()
print()
#查詢全部資料
cursor1 = collection.find()

for data1 in cursor1:
    print (data1)
print()
#查詢指定資料的全部內容    
cursor2 =collection.find({'name':'Anna'})

for data2 in cursor2:
    print(data2)