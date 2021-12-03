#Learning how to use input fields in tkinter 
#then implementing it to form a software later in 
#further files 

#importing tkinter
from tkinter import *

#intitialising tkinter file loop
root = Tk()

#taking inputs
#input properties include borderwidth, and background colour
myinput = Entry(root, text="Enter something here", width=20)
myinput.pack()

#defining the function
def call():
    mylabel = Label(root, text="Printed after clicking")
    mylabel.pack()

myButton = Button(root, text="Click me", command=call, width=20, bg="#000000", fg="#ff0000")
myButton.pack()

root.mainloop()
