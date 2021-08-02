from tkinter import *
from tkinter import messagebox

class MainMenu:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button1 = Button(frame, text="Consecutive Number Adder", command=self.consecutiveWin)
        self.button1.grid(row=0, column=0)

        self.button2 = Button(frame, text="Text Reverser", command=self.text)
        self.button2.grid(row=2, column=0)

    def consecutiveWin(self):
        a=Tk()
        a.title("Consecutive Number Adder")
        b = Consecutive(a)

    def text(self):
        a=Tk()
        a.title("Text Reverser")
        b = Reverse(a)

class Consecutive:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.label1 = Label(frame, text="This adds every number upto the entered number.")
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

class Reverse:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.label1 = Label(frame, text="This reverses your text")
        self.label1.pack()

        self.entry1 = Entry(frame, width=40)
        self.entry1.pack()
        
        self.button1 = Button(frame, text="Reverse", command=self.callback)
        self.button1.pack()

    def callback(self):
        finaltext = ""
        text = self.entry1.get()
        index = len(str(text))-1
        while index >= 0:
          finaltext += text[index]
          index -= 1
        message = messagebox.showinfo("Result", finaltext)

mainMenu = Tk()
mainMenu.title("Good Stuff")
c = MainMenu(mainMenu)
