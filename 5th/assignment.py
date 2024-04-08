# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:09:37 2024

@author: hhkim
"""

#%% Q3

from tkinter import *
window = Tk()
window.geometry("210x210")

def rdo_change():
    if var.get() == 1:
        label1.configure(text='벤츠')
    else:
        label1.configure(text='포르쉐')
        
var = IntVar()
rdo1 = Radiobutton(window, text = "벤츠", variable = var, value = 1, command = rdo_change)
rdo2 = Radiobutton(window, text = "포르쉐", variable = var, value = 2, command = rdo_change)
label1 = Label(window, text="선택한 차량", fg="red")

rdo1.pack()
rdo2.pack()
label1.pack()

window.mainloop()


#%% Q4
#%% Q4
from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

## NOTICE : upper letter ##
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

window.mainloop()

#%% Q4
from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

## NOTICE : upper letter ##
button1.pack(side=RIGHT)
button2.pack(side=RIGHT)
button3.pack(side=RIGHT)

window.mainloop()

#%% Q4
from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

## NOTICE : upper letter ##
button1.pack(side=TOP)
button2.pack(side=TOP)
button3.pack(side=TOP)

window.mainloop()

#%% Q4
from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

## NOTICE : upper letter ##
button1.pack(side=BOTTOM)
button2.pack(side=BOTTOM)
button3.pack(side=BOTTOM)

window.mainloop()




# =============================================================================
# from tkinter import *
# window = Tk()
# 
# btnList = [None] * 3
# 
# for i in range(3):
#     btnList[i] = Button(window, text="버튼"+str(i+1))
#     
# for btn in btnList:
#     btn.pack(side=RIGHT)
#     
# window.mainloop()
# =============================================================================


#%% Q5

from tkinter import *
from time import *

fnameList = ["jeju1.gif","jeju2.gif","jeju3.gif","jeju4.gif","jeju5.gif",\
             "jeju6.gif","jeju7.gif","jeju8.gif","jeju9.gif"]
num = 0

def clickNext():
    
    global num    
    num += 1
    
    if num > len(fnameList)-1:
        num = 0
    
    pLabel.configure(text=fnameList[num])
    
    
    
def clickPrev():
    
    global num
    num -= 1
    if num < 0:
        num = len(fnameList)-1
        
    pLabel.configure(text=fnameList[num])
    

window = Tk()
window.geometry("500x100")
window.title = "tk"

btnPrev = Button(window, text="<< 이전", command = clickPrev)
btnNext = Button(window, text="다음 >>", command = clickNext)
pLabel  = Label(window, text = fnameList[0])

btnPrev.place(x = 100, y = 10)
btnNext.place(x = 300, y = 10)
pLabel.place(x = 200, y = 10)


window.mainloop()


#%% Self Study 10-2 (p.19-20)

# =============================================================================
# =============================================================================
# # #%% Ref. Code 10-11.py
# # 
# # from tkinter import *
# # 
# # gifpath    = "C:/Users/nayeon/Desktop/홍희/24-1_i-SEEDprogramming/source/GIF/"
# # btnList    = [""]*9
# # fnameList  = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", \
# #               "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", \
# #               "pie.gif"]
# # photoList  = [None] * 9
# # i, k       = 0, 0
# # xPos, yPos = 0, 0
# # num        = 0
# # 
# # ## 메인 코드 부분 ##
# # window = Tk()
# # window.geometry("210x210")
# # 
# # for i in range(0, 9) :
# #     photoList[i] = PhotoImage(file = gifpath + fnameList[i])
# #     btnList[i] = Button(window, image = photoList[i])  
# # 
# # for i in range(0, 3) :
# #     for k in range(0, 3) :
# #         btnList[num].place(x = xPos, y = yPos)
# #         num += 1
# #         xPos += 70
# #     xPos = 0
# #     yPos += 70
# # 
# # window.mainloop()
# =============================================================================
# =============================================================================

## Self Study 10-2 (p.19-20)
## use: import random, and then function shuffle
from tkinter import *
from random import *

gifpath    = "C:/Users/nayeon/Desktop/홍희/24-1_i-SEEDprogramming/source/GIF/"
btnList    = [""]*9
fnameList  = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", \
              "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", \
              "pie.gif"]
photoList  = [None] * 9
i, k       = 0, 0
xPos, yPos = 0, 0
num        = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

shuffle(fnameList)

for i in range(len(fnameList)) :
    photoList[i] = PhotoImage(file = gifpath + fnameList[i])
    btnList[i]   = Button(window, image=photoList[i])  

for i in range(3) :
    for k in range(3) :
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()



#%% Self Study 10-5 p.35

# =============================================================================
# =============================================================================
# # #%% Ref. Code 10-22.py
# # 
# # from tkinter import *
# # from tkinter.filedialog import *
# # 
# # gifpath    = "C:/Users/nayeon/Desktop/홍희/24-1_i-SEEDprogramming/source/GIF/"
# # 
# # def func_open() :
# #     filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "pic*.gif"), ("모든 파일", "*.*")))
# #     photo = PhotoImage(file = filename)
# #     pLabel.configure(image = photo)
# #     pLabel.image = photo
# # 
# # def func_exit() :
# #     window.quit()
# #     window.destroy()
# # 
# # window = Tk()
# # window.geometry("500x500")
# # window.title("명화 감상하기")
# # 
# # photo = PhotoImage()
# # pLabel = Label(window, image = photo)
# # pLabel.pack(expand=1, anchor = CENTER)
# # 
# # mainMenu = Menu(window)
# # window.config(menu = mainMenu)
# # fileMenu = Menu(mainMenu)
# # mainMenu.add_cascade(label = "파일", menu = fileMenu)
# # fileMenu.add_command(label = "파일 열기", command = func_open)
# # fileMenu.add_separator()
# # fileMenu.add_command(label = "프로그램 종료", command = func_exit)
# # 
# # window.mainloop()
# =============================================================================
# =============================================================================


## Self Study 10-5 p.35
## photo.put("#%02x%02x%02x" % (grey, grey, grey), (x, y))

from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

gifpath    = "C:/Users/nayeon/Desktop/홍희/24-1_i-SEEDprogramming/source/GIF/"

def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "pic*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)

    width = photo.width()
    height = photo.height()

    for ny in range(height) :
        for nx in range(width) :
            r, g, b = photo.get(nx, ny)
            grey = int((r+g+b)/3)
            photo.put("#%02x%02x%02x" % (grey, grey, grey), (nx, ny))

    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()


## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기(흑백)")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)


window.mainloop()
