#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:23:36 2018

@author: mingcheien
"""

import scrapy
from bs4 import BeautifulSoup
from firstScrapy.items import firstScrapyItem

class AppleCrawler(scrapy.Spider):
    name='apple'
    start_urls = ('https://tw.appledaily.com/new/realtime', )
    def parse(self,response):
        
        self.logger.info('A response from %s just arrived!', response.url)
        
        res=BeautifulSoup(response.body,'lxml')
        for news in res.select('.rtddt'):
            #print(news)
            newsDetailHtml=news.select('a')[0]['href']
            yield scrapy.Request(newsDetailHtml,self.parse_detail)
    
    def parse_detail(self,response):
        res2=BeautifulSoup(response.body,'lxml')
        items=[]
        for article in res2.select('.ndArticle_leftColumn'):
            #print(article)
            item=firstScrapyItem()
            title = article.find_all('h1')[0].text
            date = article.select('.ndArticle_creat')[0].text.split('出版時間：')[1]
            url=response.url
            print(title)
            print(date)
            print(url)
            item['title']=title
            item['date']=date
            item['url']=url
            items.append(item)
            
        return items