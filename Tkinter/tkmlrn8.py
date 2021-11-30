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
myButton = Button(root, text="Click me", bg="#ff0000", command=myWriting)
myButton.pack()

root.mainloop()

