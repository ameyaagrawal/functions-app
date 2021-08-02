from tkinter import *

root = Tk()

label1 = Label(root, text="yes", bg="green")
label1.pack(fill=X,side="top")

label2 = Label(root, text="no", bg="yellow")
label2.pack(fill=Y,side="right")

label3 = Label(root, text="maybe", bg="blue")
label3.pack(fill=Y,side="left")

label4 = Label(root, text="maybe not", bg="red")
label4.pack(fill=X,side="bottom")

root.mainloop()

