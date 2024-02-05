from random import *
from tkinter import *
b = randint(1, 100)
root = Tk()
root.title('猜数字')
root.geometry('800x400+500+200')
entry1 = Entry(root)
entry1.grid(row=1, column=1)
text = StringVar()


def chongzhi():
    global b  # 将局部变量设为全局变量
    b = randint(1, 100)


def annu():
    a = int(entry1.get())

    if a <= b:
        q = '小了'
    if a >= b:
        q = '大了'
    if a == b:
        q = '对了'

    text.set(q)


#定义按钮
btn = Button(root, text='   确定   ', command=annu)
btn2 = Button(root, text='   重置   ', command=chongzhi)
#指定按钮的位置
btn.grid(row=3, column=0)
btn2.grid(row=4, column=0)

label = Label(root, text='游戏规则：从1-100之间猜数字')
label.grid(row=0, column=0, columnspan=1)
label = Label(root, text='请输入答案:')
label.grid(row=1, column=0, columnspan=1)
label = Label(root, textvariable=text)
label.grid(row=4, column=1, columnspan=1)


root.mainloop()
