#LEarning to use buttons in tkinter

from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello There !!")
myBUtton = Button(root, text="Click me Now")

myLabel.grid(row="0", column="0")
myBUtton.grid(row="1", column="0")

root.mainloop()
