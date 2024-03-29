#%% Q5
print('[ assignment1-Q5 ]')
ss = "Python"
for i in range(0,len(ss)):
    print(ss[i]+'$', end='')
    

#%% Q11
print('[ assignment1-Q11 ]')
inStr  = "파이썬 ### CookBook $$$ @@@ 열공중 123"
outStr = ""

for i in range(len(inStr)):
                
    if not inStr[i].isspace() \
        and not inStr[i].isdigit() \
        and inStr[i] not in "#$@":
        outStr += inStr[i]
        
print("기존 문자열 --> %s"%inStr)
print("한글, 영문자만 남김 --> %s"%outStr)


#%% Q9
print('[ assignment1-Q9 ]')
inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(0, strLen):
    outStr += inStr[len(inStr) - (i+1)]
    
print("내용을 거꾸로 출력 --> %s"%outStr)


#%% Q13
print('[ assignment1-Q13 ]')

import turtle
import random
from tkinter.simpledialog import *
import math

inStr = ""
swidth, sheight = 500, 500
tx, ty, txtsize = 0, 0, 20

inStr = askstring('문자열입력','거북이 쓸 문자열 입력')

radius = 200
rotations = 2 ## 회전수
angle = 360 * rotations / len(inStr)
radian = 3.14 * angle / 180

turtle.title('거북이가 나선모양으로 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth+50, height = sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()

for ch in inStr:
    tx = radius * math.cos(radian)
    ty = radius * math.sin(radian)
    r  = random.random()
    g  = random.random()
    b  = random.random()

    turtle.goto(tx, ty)
    
    turtle.pencolor( (r,g,b) )
    turtle.write(ch, font=('맑은고딕', txtsize, 'bold'))
    
    radius -= 3  # Increase (+)  // Decrease (-)
    radian += 3.14 * angle / 180
    
turtle.done()


