from tkinter import *

root = Tk()

def printName():
    print("yo hello")

button1 = Button(root, text="Print", command=printName)
button1.pack()
