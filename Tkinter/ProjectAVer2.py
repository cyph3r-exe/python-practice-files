"""
Version 2 of the same diabetese project 
but without the CLI version. 
Only machine learning will be implemented
as the backend of the GUI which will run in the CLI. 
"""

#importing tkinter
from tkinter import *

root = Tk()

#glucose Label
glucoseLabel = Label(root, text="Enter your glucose concentration: ")

#glucose entry point 
entry1 = Entry(root, text="Enter your glucose concentration: ")
glucose_conc = entry1.get()
#styling 
glucoseLabel.grid(row=0, column=0)
entry1.grid(row=0, column=1)

#BMI entry point
bmiLabel = Label(root, text="Enter your BMI: ")
entry2 = Entry(root, text="Enter your BMI: ")
bMi = entry2.get()

#bmi styling
bmiLabel.grid(row=1, column=0)
entry2.grid(row=1, column=1)

#Age entry point
agelabel = Label(root, text="Enter you age: ")
ageEntry = Entry(root, text="Enter your age: ")
Age = ageEntry.get()

#Age styling
agelabel.grid(row=2,column=0)
ageEntry.grid(row=2,column=1)

#! blood pressure entry point
bp_label = Label(root, text="Enter your blood pressure: ")
bp_Entry = Entry(root, text="Enter your blood pressure: ")
bp_Entry.get()

#! blood pressure styling 
bp_label.grid(row=3, column=0)
bp_Entry.grid(row=3, column=1)

#TODO Diabetes pedigree
#! Diabetes pedigreee entry point
diab_pediLabel = Label(root, text="Enter  your diabetes pedigree: ")
diab_pediEntry = Entry(root, text="Enter your diabetes pedigree: ")
diab_pedi = diab_pediEntry.get()

#! diabetes pedigree styling 
diab_pediLabel.grid(row=4, column=0)
diab_pediEntry.grid(row=4, column=1)

#TODO: Skin Thickness


"""TODO: Number of times admitted to the hospital for sugar
related cases.
"""

#TODO NUmber of doses for 2hr Serum insulin taken.

#running the loop
root.mainloop()