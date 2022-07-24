from tkinter import * 

root = Tk()

#creating a label
myLabel = Label(root, text="hello world")
myLabel2 = Label(root, text="My name is Debansghu Roy. ")
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()
