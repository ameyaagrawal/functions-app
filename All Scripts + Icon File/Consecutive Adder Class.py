from tkinter import *
from tkinter import messagebox

class Consecutive:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.label1 = Label(frame, text="This adds every number  upto the entered number.")
        self.label1.grid()

        self.entry1 = Entry(frame, width=6)
        self.entry1.grid(row=1, columnspan=2)
        
        self.button1 = Button(frame, text="Calculate", command=self.callback)
        self.button1.grid(row=2, columnspan=2)

    def callback(self):
        sum1 = 0
        for y in range(1,(int(self.entry1.get()))+1):
           sum1 += y
        message = messagebox.showinfo("Result" , "Result = "+str(sum1))




root = Tk()
root.title("Consecutive Number Adder")
b = Consecutive(root)
