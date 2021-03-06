﻿#coding=utf-8

import zxxk, time, json
from Tkinter import *

app = Tk()
app.geometry('200x200')
app.title("学习网")

def view():
	
	fp = file('config.json')
	s = json.load(fp)
	for key in s.keys():
		username = key
		passwd = s[key]
	
	try:
		zxxk.Login(e.get(), username, passwd)
		m.set(zxxk.getInfo())
	except:
		m.set('你输入的验证码有误，请重新输入！')
		zxxk.checkCode()
		time.sleep(1)
		global imgt
		imgt = PhotoImage(file='yzm.png')
		aLable['image'] = imgt
		aLable.grid(row=0,column=0)

def downfile():
	zxxk.downFile(id.get())



zxxk.checkCode()

topLable = Label(app,text="请输入以下验证码登录")
topLable.pack()

aFrame = Frame(app)
aFrame.pack()

img = PhotoImage(file='yzm.png')
aLable = Label(aFrame)
aLable['image'] = img
aLable.grid(row=0, column=0)


e = StringVar()
aEntry = Entry(aFrame, width=8, textvariable=e)
aEntry.grid(row=0,column=1)

aButton = Button(aFrame,text="登录",command=view)
aButton.grid(row=0,column=3)

m = StringVar()
aMessage = Message(aFrame,textvariable=m)
aMessage.grid(rowspan=3,columnspan=3)


bFrame = Frame(app)
bFrame.pack()

bLabel = Label(bFrame, text='请输入编码ID：')
bLabel.grid(row=0,column=0)

id = StringVar()
bEntry = Entry(bFrame,width=10,textvariable=id)
bEntry.grid(row=0,column=1)

downButton = Button(bFrame,text="下载",command=downfile)
downButton.grid(row=1,column=0)

quitButton = Button(bFrame,text="退出",command=app.quit)
quitButton.grid(row=1,column=1)



app.mainloop()





