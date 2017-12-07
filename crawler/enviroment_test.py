# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup

def getWebPage(url): #原始地址,
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取\n",
    resp = requests.get(
            url=url,
            cookies={"over18": "1"})
    if resp.status_code != 200:
        print("Invalid url:", resp.url)
        return resp.text
    else:
        return resp.text
    
def startAnalize(webpage):
    strSoup=BeautifulSoup(webpage,"lxml")
    print(strSoup)

webPage=getWebPage("https://www.ptt.cc/bbs/LoL/M.1512659037.A.F3E.html")
startAnalize(webPage)