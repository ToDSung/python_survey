# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:20:39 2017

@author: wlunareve
"""

"""
物件導向設計的基本邏輯是為了要省去重複撰寫的麻煩將設備有很多種
我們可以讓不同的設備，諸如汽車、機車、飛機，同樣去繼承Vehicle父類別

透過物件導向程式設計，__name、__engine的用法
能把變數隱藏起來，無法建立物件再外呼叫父類別的屬性
"""
class Vehicle:
    def __init__(self,name,engine):
        self.__name=name
        self.__engine=engine
    
    def getName(self):
        return self.__name
    
    def getEngine(self):
        return self.__engine
    
    def setEngine(self,engine):
        self.__engine=engine
        
class Car(Vehicle):
    
    def __init__(self,name,engine,electric):
        super().__init__(name,engine)
        self.__electric=electric
    
    def getCarName(self):
        print("名字:"+self.getName())
        print("引擎:"+self.getEngine())
        print("電力:"+self.__electric)
        
    def getAuto(self):
        print("自動駕駛車")

myCar=Car("特斯拉","磁電引擎","電力")
myCar.getCarName()

myCar.setEngine("汽油引擎")
myCar.getCarName()
myCar.getAuto()
