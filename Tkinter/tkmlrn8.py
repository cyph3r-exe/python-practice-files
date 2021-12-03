#Defining buttons in tkintor and coloring them 
#also using UDF to print a message on the screen. 

#importing tkinter 
from tkinter import * 

#intitialising loop
root = Tk()

#defining te fucntion  
def myWriting():
    myLabel1 = Label(root, text="Here is my text")
    myLabel1.pack()

#defining the buttons
#bg for background, fg for foreground.
         
myButton = Button(root, text="Click me", bg="#187563", fg="#39f6d0" ,command=myWriting)
myButton.pack()

root.mainloop()