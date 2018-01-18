import sys
import requests
import urllib.parse
import time
from bs4 import BeautifulSoup
from selenium import webdriver


payload={'q':sys.argv[1],'site':'site:ptt.cc/'}
q1=urllib.parse.quote(payload['q']) #url編碼轉換
url='https://google.com.tw/search?q='+q1+'+'+payload['site']
print(url)
print(sys.argv[1])
"""
tStart=time.time()

driver=webdriver.PhantomJS(executable_path=r'E://phantomjs/bin/phantomjs') #模擬瀏覽器
x=sys.argv[1]
payload={'q':x,'site':'site:ptt.cc/'}
q1=urllib.parse.quote(payload['q']) #url編碼轉換
url='https://google.com.tw/search?q='+q1+'+'+payload['site']
print('目標網址',url)
driver.get(url)

page=1
for change in range(2,4):
    
    pageSource = driver.page_source #重新讀取當前頁面
    #print(pageSource)
    soup = BeautifulSoup (pageSource, "html5lib") #流入BeautifulSoup
    for item in soup.find_all('h3'):
        for item2 in item.find_all('a'):
            print (item2.text)
     
    a=repr(change)
    driver.find_element_by_link_text(a).click() #點擊下一頁
    print('此處頁數為第',page,'頁')
    page+=1
    print ("===============================================================================================================")

driver.close();
tEnd=time.time()
t=tEnd-tStart
print(t)
"""