# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:50:42 2024

@author: hhkim
"""

#%% FileIO1 - 1
## in  : input(), read(), readline(), readlines()
## out : print(), write(), writeline()


#%% FileIO1 - 2
## 1. A 파일 열기 - C 파일 읽기 - B 파일 쓰기 - D 파일 닫기

#%% FileIO1 - 3
## 1. 쓰기모드가 아닌 "읽기모드"가 기본
## 6. t와 b는 겸용사용 안됨 (w+t = 텍스트 쓰기모드 같은경우 가능)

#%% FileIO1 - 4
## 1. open
## 2. readline
## 3. close

inFp = open("test.txt","r")
inStr = inFp.readline()
print(inStr, end="")
inFp.close()



#%% FileIO2 - 6
## 1. inFp.readlines()
## 2. outFp.writelines(inStr)

inFp = open("test.txt","r")
outFp = open("toto.txt","w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()

