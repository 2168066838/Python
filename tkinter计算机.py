from tkinter import *
root = Tk()
root.title('小东西')
root.geometry('800x400+500+200')
entry1 = Entry(root)
entry1.grid(row=0, column=1)
entry2 = Entry(root)
entry2.grid(row=1, column=1)
entry3 = Entry(root)
entry3.grid(row=2, column=1)
text = StringVar()


def annu():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    a = float(a)
    c = float(c)
    if b == '+':
        q = (a+c)
    if b == '-':
        q = (a-c)
    if b == '*':
        q = (a*c)
    if b == '/':
        q = (a/c)
    text.set(q)


#定义按钮
btn = Button(root, text='   确定   ', command=annu)
#指定按钮的位置
btn.grid(row=3, column=0)
label = Label(root, text='第一个数字')
label.grid(row=0, column=0, columnspan=1)
label = Label(root, text='符号')
label.grid(row=1, column=0, columnspan=1)
label = Label(root, text='第二个数字')
label.grid(row=2, column=0, columnspan=1)
label = Label(root, textvariable=text)
label.grid(row=3, column=1, columnspan=1)


root.mainloop()
