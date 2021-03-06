from Tkinter import *
import tkMessageBox
import random

class MainMenu:    
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        
        self.label1 = Label(self.frame, text="Select an option below to get started:", font='Arial 18 bold')
        self.label1.pack(pady=5, padx=5)
        self.label1.update_idletasks()
        
        self.button1 = Button(self.frame, text="Consecutive Number Adder", command=self.consecutiveWin)
        self.button1.pack(padx=3, pady=1)
        self.button1.update_idletasks()

        self.button2 = Button(self.frame, text="Text Reverser", command=self.textWin)
        self.button2.pack(padx=3, pady=1)
        self.button2.update_idletasks()
        
        self.button3 = Button(self.frame, text="Compound Interest", command=self.compoundWin)
        self.button3.pack(padx=3, pady=1)
        self.button3.update_idletasks()
        
        self.button4 = Button(self.frame, text="Mass Converter", command=self.weightWin)
        self.button4.pack(padx=3, pady=1)
        self.button4.update_idletasks()

        self.button5 = Button(self.frame, text="Coin Flip", command=self.coinWin)
        self.button5.pack(padx=3, pady=1)
        self.button5.update_idletasks()

        self.button6 = Button(self.frame, text="Factorial", command=self.factorialWin)
        self.button6.pack(padx=3, pady=1)
        self.button6.update_idletasks()

        self.button7 = Button(self.frame, text="Dice Roll", command=self.diceWin)
        self.button7.pack(padx=3, pady=1)
        self.button7.update_idletasks()

        self.button8 = Button(self.frame, text="Upper/Lowercase", command=self.upperlowerWin)
        self.button8.pack(padx=3, pady=1)
        self.button8.update_idletasks()

        self.button9 = Button(self.frame, text="Digit Sum", command=self.digitWin)
        self.button9.pack(padx=3, pady=1)
        self.button9.update_idletasks()

        self.label2 = Label(self.frame, text="By Ameya Agrawal, 2018")
        self.label2.pack(side=BOTTOM, padx=2, pady=20)
        self.label2.update_idletasks()

        print("success")
                
    def consecutiveWin(self):
        a=Tk()
        a.title("Consecutive Number Adder")
        b=Consecutive(a)
        

    def textWin(self):
        a=Tk()
        a.title("Text Reverser")
        b=Reverse(a)

    def compoundWin(self):
        a=Tk()
        a.title("Compound Interest")
        b=Compound(a)

    def weightWin(self):
        a=Tk()
        a.title("Mass Converter")
        b=Weight(a)

    def coinWin(self):
        a=Tk()
        a.title("Coin Flip")
        b=Coin(a)

    def factorialWin(self):
        a=Tk()
        a.title("Factorial")
        b=Factorial(a)

    def diceWin(self):
        a=Tk()
        a.title("Dice Roll")
        b=Dice(a)

    def upperlowerWin(self):
        a=Tk()
        a.title("Uppercase and Lowercase Converter")
        b=UpperLower(a)

    def digitWin(self):
        a=Tk()
        a.title("Digit Sum")
        b=digitSum(a)
        

class Consecutive:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        
        self.label1 = Label(self.frame, text="This adds every number upto the entered number.", font='Arial 15 bold')
        self.label1.pack()
        self.label1.update_idletasks()

        self.entry1 = Entry(self.frame, width=6)
        self.entry1.pack()
        self.entry1.update_idletasks()
                
        self.button1 = Button(self.frame, text="Calculate", command=self.callback)
        self.button1.pack()
        self.button1.update_idletasks()

        self.entry1.bind('<Return>', self.enterkey)

    def callback(self):
        if self.entry1.get().isdigit():
            sum1 = 0
            for y in range(1,(int(self.entry1.get()))+1):
               sum1 += y
            message = tkMessageBox.showinfo("Result" , "Result = "+str(sum1))
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def enterkey(self, event):
            self.callback()

class Reverse:
    def __init__(self, master):

        self.label1 = Label(master, text="This reverses your text (window can be expanded for more space)", font='Arial 15 bold')
        self.label1.pack()
        self.label1.update_idletasks()

        self.entry1 = Text(master, highlightbackground='blue', font='Verdana 13', padx=5, pady=5, bd=1, highlightcolor='blue')
        self.entry1.pack(expand = True, fill = 'both', padx=10, pady=2)
        self.entry1.update_idletasks()

        self.button1 = Button(master, text="Reverse", command=self.callback)
        self.button1.pack()
        self.button1.update_idletasks()

    def callback(self):
        given = self.entry1.get("1.0", END)
        if len(given)>0:
            finaltext = ""
            index = len(given)-1
            while index >= 0:
              finaltext += given[index]
              index -= 1
            message = tkMessageBox.showinfo("Result", finaltext)
        else:
            error = tkMessageBox.showinfo("ERROR", "Empty Box!!")

class Compound:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.frame.update_idletasks()
        
        self.label1 = Label(self.frame, text="Please provide the following information", font='Arial 15 bold')
        self.label1.grid(row=0, columnspan=2, pady=5)
        self.label1.update_idletasks()
        
        self.label2 = Label(self.frame, text="**A rate of 13% should be entered as 1.13 \n A rate of 7% should be entered as 1.07**")
        self.label2.grid(row=6, columnspan=2)
        self.label2.update_idletasks()
        
        self.startLabel = Label(self.frame, text="Starting Amount")
        self.startLabel.grid(row=2, column=0, sticky=E)
        self.startLabel.update_idletasks()
        
        self.startEntry = Entry(self.frame, width=15)
        self.startEntry.grid(row=2, column=1)
        self.startEntry.update_idletasks()

        self.yearsLabel = Label(self.frame, text="Years")
        self.yearsLabel.grid(row=3, column=0, sticky=E)
        self.yearsLabel.update_idletasks()
        
        self.yearsEntry = Entry(self.frame, width=15)
        self.yearsEntry.grid(row=3, column=1)
        self.yearsEntry.update_idletasks()
        
        self.rateLabel = Label(self.frame, text="Interest Rate")
        self.rateLabel.grid(row=4, column=0, sticky=E)
        self.rateLabel.update_idletasks()
        
        self.rateEntry = Entry(self.frame, width=15)
        self.rateEntry.grid(row=4, column=1)
        self.rateEntry.update_idletasks()
        
        self.button1 = Button(self.frame, text="Calculate", command=self.callback)
        self.button1.grid(row=5, columnspan=2)
        self.button1.update_idletasks()

    def callback(self):
        amount = float(self.startEntry.get())
        years = float(self.yearsEntry.get())
        rate = float(self.rateEntry.get())

        total = amount*(rate**years)
        total = round(total, 4)
        message = tkMessageBox.showinfo("Result in " + str(round(years)) + " Years", total)

class Weight:
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()
        self.frame.update_idletasks()
        
        self.label1 = Label(self.frame, text="Please enter the chosen field, then click the corresponding button.", font='Arial 15 bold')
        self.label1.grid(row=0, columnspan=3)
        self.label1.update_idletasks()
      
        self.entry6 = Entry(self.frame, width=15)
        self.entry6.grid(row=1, column=0, padx=2, pady=2)
        self.entry6.update_idletasks()
        self.entry6.bind('<Return>', self.enter6)
        self.a6 = Label(self.frame, text="???")
        self.a6.grid(row=1, column=1, padx=2, pady=2)
        self.button6 = Button(self.frame, text="Milligrams to Grams", command=self.mgtog)
        self.button6.grid(row=1, column=2, padx=2, pady=2)
        self.button6.update_idletasks()        
        
        self.entry5 = Entry(self.frame, width=15)
        self.entry5.grid(row=2, column=0, padx=2, pady=2)
        self.entry5.update_idletasks()
        self.entry5.bind('<Return>', self.enter5)  
        self.a5 = Label(self.frame, text="???")
        self.a5.grid(row=2, column=1, padx=2, pady=2) 
        self.button5 = Button(self.frame, text="Grams to Milligrams", command=self.gtomg)
        self.button5.grid(row=2, column=2, padx=2, pady=2)
        self.button5.update_idletasks()

        self.entry1 = Entry(self.frame, width=15)
        self.entry1.grid(row=3, column=0, padx=2, pady=2)
        self.entry1.update_idletasks()
        self.entry1.bind('<Return>', self.enter1)
        self.a1 = Label(self.frame, text="???")
        self.a1.grid(row=3, column=1, padx=2, pady=2)
        self.button1 = Button(self.frame, text="Kilograms to Grams", command=self.kgtog)
        self.button1.grid(row=3, column=2, padx=2, pady=2)
        self.button1.update_idletasks()
        
        self.entry2 = Entry(self.frame, width=15)
        self.entry2.grid(row=4, column=0, padx=2, pady=2)
        self.entry2.update_idletasks()
        self.entry2.bind('<Return>', self.enter2)
        self.a2 = Label(self.frame, text="???")
        self.a2.grid(row=4, column=1, padx=2, pady=2)
        self.button2 = Button(self.frame, text="Grams to Kilograms", command=self.gtokg)
        self.button2.grid(row=4, column=2, padx=2, pady=2)
        self.button2.update_idletasks()

        self.entry3 = Entry(self.frame, width=15)
        self.entry3.grid(row=5, column=0, padx=2, pady=2)
        self.entry3.update_idletasks()
        self.entry3.bind('<Return>', self.enter3)        
        self.a3 = Label(self.frame, text="???")
        self.a3.grid(row=5, column=1, padx=25, pady=2)
        self.button3 = Button(self.frame, text="Kilograms to Tonnes", command=self.kgtoton)
        self.button3.grid(row=5, column=2, padx=2, pady=2)
        self.button3.update_idletasks()

        self.entry4 = Entry(self.frame, width=15)
        self.entry4.grid(row=6, column=0, padx=2, pady=2)
        self.entry4.update_idletasks()
        self.entry4.bind('<Return>', self.enter4)
        self.a4 = Label(self.frame, text="???")
        self.a4.grid(row=6, column=1, padx=25, pady=2)
        self.button4 = Button(self.frame, text="Tonnes to Kilograms", command=self.tontokg)
        self.button4.grid(row=6, column=2, padx=2, pady=2)
        self.button4.update_idletasks()

        self.entry7 = Entry(self.frame, width=15)
        self.entry7.grid(row=7, column=0, padx=2, pady=2)
        self.entry7.update_idletasks()
        self.entry7.bind('<Return>', self.enter7)
        self.a7 = Label(self.frame, text="???")
        self.a7.grid(row=7, column=1, padx=25, pady=2)
        self.button7 = Button(self.frame, text="Pounds to Ounces", command=self.lbtooz)
        self.button7.grid(row=7, column=2, padx=2, pady=2)
        self.button7.update_idletasks()

        self.entry8 = Entry(self.frame, width=15)
        self.entry8.grid(row=8, column=0, padx=2, pady=2)
        self.entry8.update_idletasks()
        self.entry8.bind('<Return>', self.enter8)
        self.a8 = Label(self.frame, text="???")
        self.a8.grid(row=8, column=1, padx=25, pady=2)
        self.button8 = Button(self.frame, text="Ounces to Pounds", command=self.oztolb)
        self.button8.grid(row=8, column=2, padx=2, pady=2)
        self.button8.update_idletasks()

        self.entry9 = Entry(self.frame, width=15)
        self.entry9.grid(row=9, column=0, padx=2, pady=2)
        self.entry9.update_idletasks()
        self.entry9.bind('<Return>', self.enter9)
        self.a9 = Label(self.frame, text="???")
        self.a9.grid(row=9, column=1, padx=25, pady=2)
        self.button9 = Button(self.frame, text="Pounds to Kilograms", command=self.lbtokg)
        self.button9.grid(row=9, column=2, padx=2, pady=2)
        self.button9.update_idletasks()

        self.entry10 = Entry(self.frame, width=15)
        self.entry10.grid(row=10, column=0, padx=2, pady=2)
        self.entry10.update_idletasks()
        self.entry10.bind('<Return>', self.enter10)
        self.a10 = Label(self.frame, text="???")
        self.a10.grid(row=10, column=1, padx=25, pady=2)
        self.button10 = Button(self.frame, text="Kilograms to Pounds", command=self.kgtolb)
        self.button10.grid(row=10, column=2, padx=2, pady=2)
        self.button10.update_idletasks()
        
    def kgtog(self):
        if self.entry1.get().isdigit():
            amt = float(self.entry1.get())
            final = amt*1000
            result = tkMessageBox.showinfo("Result", str(amt)+"kg = "+ str(final)+"g")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!") 

    def gtokg(self):
        if self.entry2.get().isdigit():
            amt = float(self.entry2.get())
            final = amt/1000
            result = tkMessageBox.showinfo("Result", str(amt)+"g = "+ str(final)+"kg")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def kgtoton(self):
        if self.entry3.get().isdigit():
            amt = float(self.entry3.get())
            final = amt/1000
            result = tkMessageBox.showinfo("Result", str(amt)+"kg = "+ str(final)+" tonne(s)")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def tontokg(self):
        if self.entry4.get().isdigit():
            amt = float(self.entry4.get())
            final = amt*1000
            result = tkMessageBox.showinfo("Result", str(amt)+" tonne(s) = "+ str(final)+"kg")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def mgtog(self):
        if self.entry6.get().isdigit():
            amt = float(self.entry6.get())
            final = amt/1000
            result = tkMessageBox.showinfo("Result", str(amt)+"mg = "+ str(final)+"g")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def gtomg(self):
        if self.entry5.get().isdigit():
            amt = float(self.entry5.get())
            final = amt*1000
            result = tkMessageBox.showinfo("Result", str(amt)+"g = "+ str(final)+"mg")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def lbtooz(self):
        if self.entry7.get().isdigit():
            amt = float(self.entry7.get())
            final = amt*16
            result = tkMessageBox.showinfo("Result", str(amt)+"lb = "+ str(final)+"oz")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def oztolb(self):
        if self.entry8.get().isdigit():
            amt = float(self.entry8.get())
            final = amt/16
            result = tkMessageBox.showinfo("Result", str(amt)+"oz = "+ str(final)+"lb")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def lbtokg(self):
        if self.entry9.get().isdigit():
            amt = float(self.entry9.get())
            final = round((amt/2.20462), 4)
            result = tkMessageBox.showinfo("Result", str(amt)+"lb = "+ str(final)+"kg")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def kgtolb(self):
        if self.entry10.get().isdigit():
            amt = float(self.entry10.get())
            final = round((amt*2.20462), 4)
            result = tkMessageBox.showinfo("Result", str(amt)+"kg = "+ str(final)+"lb")
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def enter6(self, event):
        self.mgtog()
    def enter5(self, event):
        self.gtomg()
    def enter1(self, event):
        self.kgtog()
    def enter2(self, event):
        self.gtokg()
    def enter3(self, event):
        self.kgtoton()
    def enter4(self, event):
        self.tontokg()
    def enter7(self, event):
        self.lbtooz()
    def enter8(self, event):
        self.oztolb()
    def enter9(self, event):
        self.lbtokg()
    def enter10(self, event):
        self.kgtolb()

class Coin:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        
        self.label1 = Label(self.frame, text="Click the button to flip a coin!", font='Arial 15 bold')
        self.label1.grid(row=0, columnspan=2)
        self.label1.update_idletasks()

        self.button1 = Button(self.frame, text="Flip!", command=self.flip)
        self.button1.grid(row=1, columnspan=2)
        self.button1.update_idletasks()

        master.bind('<Return>', self.enterkey)

    def enterkey(self, event):
        self.flip()

    def flip(self):
        choices = ['Heads!','Tails!']
        selected = random.choice(choices)
        result = tkMessageBox.showinfo("Result", selected)

class Factorial:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        
        self.label1 = Label(self.frame, text="This will find the factorial of the entered value!", font='Arial 15 bold')
        self.label1.grid(row=0, columnspan=2)
        self.label1.update_idletasks()

        self.entry1 = Entry(self.frame, width = 15)
        self.entry1.grid(row=1, columnspan=2)
        self.entry1.update_idletasks()

        self.button1 = Button(self.frame, text="Calculate", command=self.callback)
        self.button1.grid(row=2, columnspan=2)
        self.button1.update_idletasks()

        self.entry1.bind('<Return>', self.enterkey)

    def callback(self):
        if self.entry1.get().isdigit():
            x = int(self.entry1.get())
            final = 1
            for n in range(1,x+1):
                final *= n
            final = float(final)
            result = tkMessageBox.showinfo("Result", final)
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def enterkey(self, event):
        self.callback()
            
class Dice:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        
        self.label1 = Label(self.frame, text="Please select an option below \n Results of 10 rolls will be displayed.", font='Arial 15 bold')
        self.label1.pack(padx=2, pady=2)
        self.label1.update_idletasks()

        self.button1 = Button(master, text="4-sided", command=self.s4dice)
        self.button1.pack(padx=2, pady=2)
        self.button1.update_idletasks()

        self.button2 = Button(master, text="6-sided", command=self.s6dice)
        self.button2.pack(padx=2, pady=2)
        self.button2.update_idletasks()

        self.button3 = Button(master, text="8-sided", command=self.s8dice)
        self.button3.pack(padx=2, pady=2)
        self.button3.update_idletasks()

        self.button4 = Button(master, text="10-sided", command=self.s10dice)
        self.button4.pack(padx=2, pady=2)
        self.button4.update_idletasks()

        self.button5 = Button(master, text="12-sided", command=self.s12dice)
        self.button5.pack(padx=2, pady=2)
        self.button5.update_idletasks()

        self.button6 = Button(master, text="20-sided", command=self.s20dice)
        self.button6.pack(padx=2, pady=2)
        self.button6.update_idletasks()

    def s4dice(self):
        lst1 = []
        for x in range(1, 11):
            x=random.randint(1,4)
            lst1.append(x)
        result = tkMessageBox.showinfo("Result",
                                     "1st Roll: "+str(lst1[0])+\
                                     "\n2nd Roll: "+ str(lst1[1])+\
                                     "\n3rd Roll: "+ str(lst1[2])+\
                                     "\n4th Roll: "+ str(lst1[3])+\
                                     "\n5th Roll: "+ str(lst1[4])+\
                                     "\n6th Roll: "+ str(lst1[5])+\
                                     "\n7th Roll: "+ str(lst1[6])+\
                                     "\n8th Roll: "+ str(lst1[7])+\
                                     "\n9th Roll: "+ str(lst1[8])+\
                                     "\n10th Roll: "+ str(lst1[9]))


    def s6dice(self):
        lst1 = []
        for x in range(1, 11):
            x=random.randint(1,6)
            lst1.append(x)
        result = tkMessageBox.showinfo("Result",
                                     "1st Roll: "+str(lst1[0])+\
                                     "\n2nd Roll: "+ str(lst1[1])+\
                                     "\n3rd Roll: "+ str(lst1[2])+\
                                     "\n4th Roll: "+ str(lst1[3])+\
                                     "\n5th Roll: "+ str(lst1[4])+\
                                     "\n6th Roll: "+ str(lst1[5])+\
                                     "\n7th Roll: "+ str(lst1[6])+\
                                     "\n8th Roll: "+ str(lst1[7])+\
                                     "\n9th Roll: "+ str(lst1[8])+\
                                     "\n10th Roll: "+ str(lst1[9]))

    def s8dice(self):
        lst1 = []
        for x in range(1, 11):
            x=random.randint(1,8)
            lst1.append(x)
        result = tkMessageBox.showinfo("Result",
                                     "1st Roll: "+str(lst1[0])+\
                                     "\n2nd Roll: "+ str(lst1[1])+\
                                     "\n3rd Roll: "+ str(lst1[2])+\
                                     "\n4th Roll: "+ str(lst1[3])+\
                                     "\n5th Roll: "+ str(lst1[4])+\
                                     "\n6th Roll: "+ str(lst1[5])+\
                                     "\n7th Roll: "+ str(lst1[6])+\
                                     "\n8th Roll: "+ str(lst1[7])+\
                                     "\n9th Roll: "+ str(lst1[8])+\
                                     "\n10th Roll: "+ str(lst1[9]))

    def s10dice(self):
        lst1 = []
        for x in range(1, 11):
            x=random.randint(1,10)
            lst1.append(x)
        result = tkMessageBox.showinfo("Result",
                                     "1st Roll: "+str(lst1[0])+\
                                     "\n2nd Roll: "+ str(lst1[1])+\
                                     "\n3rd Roll: "+ str(lst1[2])+\
                                     "\n4th Roll: "+ str(lst1[3])+\
                                     "\n5th Roll: "+ str(lst1[4])+\
                                     "\n6th Roll: "+ str(lst1[5])+\
                                     "\n7th Roll: "+ str(lst1[6])+\
                                     "\n8th Roll: "+ str(lst1[7])+\
                                     "\n9th Roll: "+ str(lst1[8])+\
                                     "\n10th Roll: "+ str(lst1[9]))

    def s12dice(self):
        lst1 = []
        for x in range(1, 11):
            x=random.randint(1,12)
            lst1.append(x)
        result = tkMessageBox.showinfo("Result",
                                     "1st Roll: "+str(lst1[0])+\
                                     "\n2nd Roll: "+ str(lst1[1])+\
                                     "\n3rd Roll: "+ str(lst1[2])+\
                                     "\n4th Roll: "+ str(lst1[3])+\
                                     "\n5th Roll: "+ str(lst1[4])+\
                                     "\n6th Roll: "+ str(lst1[5])+\
                                     "\n7th Roll: "+ str(lst1[6])+\
                                     "\n8th Roll: "+ str(lst1[7])+\
                                     "\n9th Roll: "+ str(lst1[8])+\
                                     "\n10th Roll: "+ str(lst1[9]))

    def s20dice(self):
        lst1 = []
        for x in range(1, 11):
            x=random.randint(1,20)
            lst1.append(x)
        result = tkMessageBox.showinfo("Result",
                                     "1st Roll: "+str(lst1[0])+\
                                     "\n2nd Roll: "+ str(lst1[1])+\
                                     "\n3rd Roll: "+ str(lst1[2])+\
                                     "\n4th Roll: "+ str(lst1[3])+\
                                     "\n5th Roll: "+ str(lst1[4])+\
                                     "\n6th Roll: "+ str(lst1[5])+\
                                     "\n7th Roll: "+ str(lst1[6])+\
                                     "\n8th Roll: "+ str(lst1[7])+\
                                     "\n9th Roll: "+ str(lst1[8])+\
                                     "\n10th Roll: "+ str(lst1[9]))

class UpperLower:
    def __init__(self, master):
        
        self.label1 = Label(master, text="Copy & Paste (???C and ???V) your text below, then click the desired operation", font='Arial 15 bold')
        self.label1.pack()
        self.label1.update_idletasks()

        self.entry1 = Text(master, highlightbackground='blue', font='Verdana 13', padx=5, pady=5, bd=1, highlightcolor='blue')
        self.entry1.pack(expand = True, fill = 'both', padx=10, pady=2)
        self.entry1.update_idletasks()

        self.button1 = Button(master, text="Lowercase", command=self.lower)
        self.button1.pack(side=LEFT, padx=50)
        self.button1.update_idletasks()

        self.button2 = Button(master, text="Uppercase", command=self.upper)
        self.button2.pack(side=RIGHT, padx=50)
        self.button2.update_idletasks()

    def lower(self):
        finalstr = self.entry1.get("1.0", END).lower()
        result = tkMessageBox.showinfo("Result", finalstr)

    def upper(self):
        finalstr = self.entry1.get("1.0", END).upper()
        result = tkMessageBox.showinfo("Result", finalstr)

class digitSum:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        
        self.label1 = Label(self.frame, text="This will add all the digits used in the entered number.", font='Arial 15 bold')
        self.label1.pack()
        self.label1.update_idletasks()
        
        self.entry1 = Entry(self.frame, width=15)
        self.entry1.pack()
        self.entry1.update_idletasks()

        self.button1 = Button(self.frame, text="Calculate", command=self.callback)
        self.button1.pack()
        self.button1.update_idletasks()

        self.entry1.bind('<Return>', self.enterkey)

    def callback(self):
        if self.entry1.get().isdigit():
            n = str(self.entry1.get())
            total = 0
            for x in n:
                total += int(x)
            result = tkMessageBox.showinfo("Result", "The digit sum of "+n+" is "+str(total))
        else:
            error = tkMessageBox.showinfo("ERROR", "Please enter a positive integer!!")

    def enterkey(self, event):
        self.callback()
        
menu = Tk()
menu.title("Utilities")
MainMenu(menu)
menu.mainloop()