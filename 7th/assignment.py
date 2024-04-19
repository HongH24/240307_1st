# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:20:08 2024

@author: honghee
"""


#%% 2  ## Find and correct 2 errors in the method

## --------------------------------------------------------------------Question
class Car:
    color = ""
    speed = 0
    
    def upSpeed(value):
        speed += value

## ----------------------------------------------------------------------Answer
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value): ## self 추가
        self.speed += value   ## self 추가
        
        

#%% 4 ## Reset the speed value "50"

## --------------------------------------------------------------------Question
class Horse:
    speed = 0
    
    ###################
    #                 #
    #                 #
    ###################
    
    
## ----------------------------------------------------------------------Answer
class Horse:
    speed = 0
    
    def __init__(self):
        self.speed = 50
        
    def get(self):
        return self.speed

h_speed = Horse()
print(h_speed.get()) ## reset the speed value "50"
    


#%% 6  Select the corresponding execution result

## --------------------------------------------------------------------Question
class Car:
    def method(self):
        print("슈퍼클래스")

class Sedan(Car):
    def method(self):
        print("서브클래스")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

## ----------------------------------------------------------------------Answer
## 3.슈퍼클래스 서브클래스

#%% 7  Fill in the blanks

## --------------------------------------------------------------------Question
class Car:
    speed = 0
    
    def upSpeed(self, value):
        self.speed = self.speed + value
    
##____________## :
    seatNum = 0
    
    def getSeatNum(self):
        return self.seatNum
    
## ----------------------------------------------------------------------Answer
class Car:
    speed = 0
    
    def upSpeed(self, value):
        self.speed = self.speed + value
    
class RVCar(Car): ## 추가
    seatNum = 0
    
    def getSeatNum(self):
        return self.seatNum