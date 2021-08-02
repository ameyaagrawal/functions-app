from tkinter import *
from tkinter import messagebox

class Consecutive:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack(side=TOP)
        
        self.label1 = Label(frame, text="This adds every number upto the entered number.")
        self.label1.pack()

        self.entry1 = Entry(frame, width=6)
        self.entry1.pack()
                
        self.button1 = Button(frame, text="Calculate", command=self.callback)
        self.button1.pack(side="left")

        self.quit = Button(frame, text="Quit", command=self.quitframe)
        self.quit.pack(side="left")

    def callback(self):
        sum1 = 0
        for y in range(1,(int(self.entry1.get()))+1):
           sum1 += y
        message = messagebox.showinfo("Result" , "Result = "+str(sum1))

    def quitframe(self):
        exit()

class Reverse:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.label1 = Label(frame, text="This reverses your text")
        self.label1.pack()

        self.entry1 = Entry(frame, width=40)
        self.entry1.pack()
        
        self.button1 = Button(frame, text="Reverse", command=self.callback)
        self.button1.pack(side="left", anchor = "center")

        self.quit = Button(frame, text="Quit", command=self.quitframe)
        self.quit.pack(side="left", anchor = "center")

    def callback(self):
        finaltext = ""
        text = self.entry1.get()
        index = len(str(text))-1
        while index >= 0:
          finaltext += text[index]
          index -= 1
        message = messagebox.showinfo("Result", finaltext)

    def quitframe(self):
        exit()

root = Tk()
root.title("Consecutive Number Adder")
a = Consecutive(root)

window2 = Tk()
window2.title("Text Reverser")
b = Reverse(window2)
