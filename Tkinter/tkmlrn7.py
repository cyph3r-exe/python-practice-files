#Learning to use functions using buttons in tkinter

from tkinter import *

root = Tk()

def call():
    myLabel = Label(root, text="Called a function.")
    myLabel.pack()

myButton = Button(root, text="Press Here.", command=call)
myButton.pack()

root.mainloop()
