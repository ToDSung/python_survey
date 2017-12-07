# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 00:03:24 2017

@author: wlunareve
"""
"""多型polymorphism，先RUN子類別的函數"""
class Vehicle:
    def __init__(self,name,engine):
        self.__name=name
        self.__engine=engine
    
    def getName(self):
        return self.__name
    """父類別getEngine函數不會繼承"""
    def getEngine(self):
        return self.__engine

class Car(Vehicle):
    
    def __init__(self,name,engine,electric):
        super().__init__(name,engine)
        self.__electric=electric
    
    def getCarName(self):
        print("名字:"+self.getName())
        print("引擎:"+self.getEngine())
        print("電力:"+self.__electric)
        
    def getEngine(self):
        return ("我來亂的")
        
    def getAuto(self):
        print("自動駕駛車")
        
myCar=Car("特斯拉","磁電引擎","電力")
myCar.getCarName()

myCar.getAuto()

"""多型，先RUN子類別的函數"""
myCar.getEngine()
myCar.getCarName()