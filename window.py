import tkinter
from tkinter import ttk
from selenium import webdriver
import time
import requests
import json
from openpyxl import Workbook
import hashlib
import os
import datetime

win = tkinter.Tk()
win.title("热点新闻抽取")
win.geometry("600x400")

# welcome image
canvas = tkinter.Canvas(win, height=200, width=500)#画布
image_file = tkinter.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.place(x=80,y=0)

# 文字表述
tkinter.Label(win, text='请您选择要浏览的新闻类型: ').place(x=100, y= 140)
tkinter.Label(win, text='请您输入新闻页面下拉次数(建议取值10-80): ').place(x=100, y= 200)


cv= tkinter.StringVar()
cv.set('下拉选择新闻类型')
com=ttk.Combobox(win,textvariable=cv, width = 40, height =10)#长度
com.place(x=100,y=170)



#设置下拉数据
com["value"]=("财经","体育","科技","热点","娱乐","游戏","搞笑","汽车")
#设置默认值
com.current()


# 文本框
name = tkinter.StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = ttk.Entry(win, width=42,textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
nameEntered.place(x=100,y=230)      # 设置其在界面中出现的位置  column代表列   row 代表行
nameEntered.focus()     # 当程序运行时,光标默认会出现在该文本框中


def catch_start():
    global newstype
    global newsnumber
    newstype=com.get()
    newsnumber=nameEntered.get()
    print('您所选择的新闻类型：'+newstype+"类")
    print('您所输入的新闻页面下滑次数：'+newsnumber+"次")
    btn_login.configure(text='正在启动浏览器···' )     # 设置button显示的内容
    btn_login.configure(state='disabled')      # 将按钮设置为灰色状态，不可使用状态
    os.system("python cccctoutiao.py %s %s" % (newstype,newsnumber))

# 按键
btn_login = tkinter.Button(win, text='开 始', command=catch_start, width =13)
btn_login.place(x=240, y=280)

win.mainloop()




