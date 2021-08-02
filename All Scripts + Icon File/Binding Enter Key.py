from tkinter import *
from tkinter import messagebox

class MainMenu:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button1 = Button(frame, text="Consecutive Number Adder", command=self.consecutiveWin)
        self.button1.grid(row=0, column=0)


    def consecutiveWin(self):
         a=Tk()
         a.title("Consecutive Number Adder")
         b = Consecutive(a)

class Consecutive:
    def __init__(self, master):
        self.label1 = Label(master, text="This adds every number upto the entered number.")
        self.label1.grid()

        self.entry1 = Entry(master, width=6)
        self.entry1.grid(row=1, columnspan=2)
                
        self.button1 = Button(master, text="Calculate", command=self.callback)
        self.button1.grid(row=2, columnspan=2)

        master.bind('<Return>', self.enterkey)

    def enterkey(self, event):
            self.callback()

    def callback(self):
        if self.entry1.get().isdigit():
            sum1 = 0
            for y in range(1,(int(self.entry1.get()))+1):
               sum1 += y
            message = messagebox.showinfo("Result" , "Result = "+str(sum1))
        else:
            error = messagebox.showinfo("ERROR", "That is not a number!!")

    


mainMenu = Tk()
mainMenu.title("Good Stuff")
c = MainMenu(mainMenu)
