from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Consecutive Number Adder")

label1 = Label(root, text="This adds every number upto the entered number.")
label1.grid()

entry1 = Entry(root, width=6)
entry1.grid(row=1, columnspan=2)

def callback():
    sum1 = 0
    for y in range(1,(int(entry1.get()))+1):
       sum1 += y
    message = messagebox.showinfo("Result" , "Result = "+str(sum1))


button1 = Button(root, text="Calculate", command=callback)
button1.grid(row=2, columnspan=2)
