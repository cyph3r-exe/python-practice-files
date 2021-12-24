# Using the root title function to change the title 
# of the GUI

#? importing the tkinter files
from tkinter import *

#initialising the root window
root = Tk()

#using the title function to change the title
root.title("Simple Title ")

#A simple label
myLabel1 = Label(root, text="This the lable of the GUI")
myLabel1.pack()

#running he main GUi loop
root.mainloop()
