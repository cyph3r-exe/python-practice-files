from tkinter import *

root = Tk()
root.title("Learning Radio Buttons")


def clicked(somevalue):
    myLabel = Label(root, text=somevalue)
    myLabel.pack()

modes = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]
pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

myButton = Button(root, text="Confirm Booking",command=lambda: clicked(pizza.get()))
myButton.pack()

#!Radiobutton(root, text="First Option", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#!Radiobutton(root, text="Second Option", variable=r, value=2, command=lambda: clicked(r.get())).pack()

root.mainloop()