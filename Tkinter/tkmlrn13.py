from tkinter import *

root = Tk()
root.title("Simple App")

#icon
root.iconbitmap('D:/New folder/Backup/User/Documents/GitHub/python-practice-files/Tkinter/logo.png')

frame = LabelFrame(root, text = "This is my frame..... ", padx =5, pady =5)
frame.pack(padx = 10, pady = 10)
 
b = Button(frame, text = "This is my frame..... ")
b.pack()

#running to loop
root.mainloop()