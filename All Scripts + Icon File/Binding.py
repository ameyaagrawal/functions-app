from tkinter import *

root = Tk()

def left(event): #event is anything a user can do like click, move, etc.
    print("Left")

def right(event):
    print("Right")

frame = Frame(root, width=300, height = 300)
frame.bind("<Button-1>", left) #"Button-1" is left click
frame.bind("<Button-2>", right) #"Button-2" is right click
frame.pack()
