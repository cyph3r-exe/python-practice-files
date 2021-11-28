#third tkinter file 
from tkinter import *

#give the following inputs
name = input("Enter the name: ")
line1 = input("Enter the message: ")

#initialising GUI loop
root = Tk()

#entering the text using string formatting
myLabel1 = Label(root, text=f"Hey there {name}" )
myLabel2 = Label(root, text=f"{line1}")
myLabel3 = Label(root, text="Just don't stop and believe in what you are doing")

#aligning and displaying 
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)

#running the GUI loop
root.mainloop()