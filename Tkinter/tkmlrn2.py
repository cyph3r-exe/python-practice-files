#second tkinter file 

#learning to use the grid system of tkinter

from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My Name is Debangshu Roy")

myLabel1.grid(row=1, column=0)
myLabel2.grid(row=2, column=0)

root.mainloop()