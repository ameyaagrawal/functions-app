from tkinter import *

master = Tk()

e = Entry(master, width=12)
e.pack()

def callback():
    print(e.get())

b = Button(master, text="print", width=10, command=callback)
b.pack()

