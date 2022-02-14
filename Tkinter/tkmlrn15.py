from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")

def popup():
    messagebox.showinfo("This is my title", "Hello World")

Button(root, text="Popup", command=popup).pack()

root.mainloop()