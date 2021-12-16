#! string concatenation in python 

#! importing the module
from tkinter import *

#initialising the root window
root = Tk()

#Name label 
nameLabel = Label(root, text="Enter your name here: ")
nameLabel.grid(row=0, column=0)

#Namee label entry field 
nameEntry = Entry(root, text = "Name")
nameEntry.grid(row = 0, column =1)

#defining the function call 
def myCall():
    myLabel1 = Label(root, text=f"My name is {nameEntry.get()}")
    myLabel1.grid(row=2, column=0)

#defining the button
initButton = Button(root, text="Press me", command = myCall)
initButton.grid(row=1, column=0)

#running the root window loop 
root.mainloop()
    