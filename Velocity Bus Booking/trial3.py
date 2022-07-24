import os
import csv
from tkinter import *
   
root = Tk()
root.title('VBB Sign_In')
root.geometry("800x500")
    
name_label = Label(root, text="Enter your First name: ")
name_label.grid(row=0, column=0)
name_label_entry = Entry(root)
name_label_entry.grid(row=0, column=1)

secondname = Label(root, text="Enter your Second name: ")
secondname.grid(row=1,column=0)
secondname_entry = Entry(root)
secondname_entry.grid(row=1, column=1)

email = Label(root, text="Enter your Email: ")
email.grid(row=2,column=0)
email_entry = Entry(root)
email_entry.grid(row=2, column=1)

username = Label(root, text="Enter your username: ")
username.grid(row=3, column=0)
username_entry = Entry(root)
username_entry.grid(row=3, column=1)

userpassword = Label(root, text="Enter your password: ")
userpassword.grid(row=4, column=0)
userpassword_entry = Entry(root)
userpassword_entry.grid(row=4, column=1)

passwordconf = Label(root, text="Confirm your password: ")
passwordconf.grid(row=5, column=0)
passwordconf_entry = Entry(root)
passwordconf_entry.grid(row=5, column=1)

root.mainloop()