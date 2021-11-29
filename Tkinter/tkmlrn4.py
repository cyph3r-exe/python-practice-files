#File to show another type 
#of using the grid system 

#importing tkinter
from tkinter import * 

#initialsing GUI loop
root = Tk()

#content 
myLabel1 = Label(root, text="This could be the day I die for you").grid(row=0, column=0)
myLabel2 = Label(root, text="Don't let it be the day").grid(row=1, column=0)

#running GUI loop
root.mainloop()
