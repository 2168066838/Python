from tkinter import *
import random
root = Tk()
root.title('小东西')
root.geometry('800x400+500+200')

aa = random.randint(1, 100)
bb = random.randint(1, 100)
aaa = random.randint(1, 100)
bbb = random.randint(1, 100)
aaaa = random.randint(1, 100)
bbbb = random.randint(1, 100)
aaaaa = random.randint(1, 100)
bbbba = random.randint(1, 100)
entry = Entry(root)
entry.grid(row=1, column=2)
text = StringVar()
xin=0
m = 0
i=0
def ee():
    l=['+','-','*','/']
    xx=random.choice(l)
    aaaaa = random.randint(1, 100)
    bbbbb = random.randint(1, 100)
    t = str(aaaaa)+xx+str(bbbbb)
    label1.configure(text=t)
def pp():
    global xin
    if xin==0:
        btn3.grid(row=0, column=3)
        btn4.grid(row=0, column=4)
        btn5.grid(row=0, column=5)
        btn6.grid(row=0, column=6)
        btn7.grid(row=0, column=7)
        xin=1
    elif xin==1:
        btn3.grid_forget()
        btn4.grid_forget()
        btn5.grid_forget()
        btn6.grid_forget()
        btn7.grid_forget()
        xin=0
def annu():
    global a,b,i
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    i=a+b
    t = str(a)+'+'+str(b)
    label1.configure(text=t)
def annu1():
    global aa,bb,i
    aa = random.randint(1, 100)
    bb = random.randint(1, 100)
    i=aa-bb
    t = str(aa)+'-'+str(bb)
    label1.configure(text=t)
def annu2():
    global aaa,bbb,i
    aaa = random.randint(1, 100)
    bbb = random.randint(1, 100)
    i=aaa*bbb
    t = str(aaa)+'*'+str(bbb)
    label1.configure(text=t)
def annu3():
    global aaaa,bbbb,i
    aaaa = random.randint(1, 100)
    bbbb = random.randint(1, 100)
    i=aaaa/bbbb
    t = str(aaaa)+'/'+str(bbbb)
    label1.configure(text=t)
def u():
    global m
    d = entry.get()
    d = int(d)
    m = int(m)
    if d == i:
        q = '对了'
        m += 10
        m = str(m)
        label.configure(text='分数:'+m)
    else:
        q = '错了'
        m -= 10
        m = str(m)
        label.configure(text='分数:'+m)

    
    
    
    
    
    
    
    
    text.set(q)
    annu()


#定义按钮
btn = Button(root, text='   确定   ', command=u)
btn2 = Button(root, text='开始出题 ', command=pp)
btn3 = Button(root, text='   +   ',command=annu)
btn4 = Button(root, text='   -   ',command=annu1)
btn5 = Button(root, text='   *   ',command=annu2)
btn6 = Button(root, text='   /   ',command=annu3)
btn7 = Button(root, text='   全部   ',command=ee)
#指定按钮的位置
btn.grid(row=1, column=4)
btn2.grid(row=0, column=0)
label = Label(root, text='分数：0')
label.grid(row=0, column=1, columnspan=1)
label1 = Label(root, text='?+?')
label1.grid(row=1, column=1, columnspan=1)
label2 = Label(root, text='题目：')
label2.grid(row=1, column=0, columnspan=1)
label3 = Label(root, textvariable=text)
label3.grid(row=3, column=1, columnspan=1)

root.mainloop()
