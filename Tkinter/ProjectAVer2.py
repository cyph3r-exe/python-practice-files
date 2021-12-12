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

#styling 
glucoseLabel.grid(row=0, column=0)
entry1.grid(row=0, column=1)

#BMI entry point
bmiLabel = Label(root, text="Enter your BMI: ")
entry2 = Entry(root, text="Enter your BMI: ")

#bmi styling
bmiLabel.grid(row=1, column=0)
entry2.grid(row=1, column=1)

#Age entry point
agelabel = Label(root, text="Enter you age: ")
ageEntry = Entry(root, text="Enter your age: ")


#Age styling
agelabel.grid(row=2,column=0)
ageEntry.grid(row=2,column=1)

#! blood pressure entry point
bp_label = Label(root, text="Enter your blood pressure: ")
bp_Entry = Entry(root, text="Enter your blood pressure: ")


#! blood pressure styling 
bp_label.grid(row=3, column=0)
bp_Entry.grid(row=3, column=1)

#TODO Diabetes pedigree
#! Diabetes pedigreee entry point
diab_pediLabel = Label(root, text="Enter  your diabetes pedigree: ")
diab_pediEntry = Entry(root, text="Enter your diabetes pedigree: ")


#! diabetes pedigree styling 
diab_pediLabel.grid(row=4, column=0)
diab_pediEntry.grid(row=4, column=1)

#TODO: Skin Thickness
skinLabel = Label(root, text="Enter your skin thickness: ")
skinEntry = Entry(root, text="Enter your skin thickness: ")

#! Skin thickness styling
skinLabel.grid(row=5,column=0)
skinEntry.grid(row=5, column=1)

"""TODO: Number of times admitted to the hospital for sugar
related cases.
"""
hospitalLabel = Label(root, text="Enter the number of times admitted in the hospital for diabetese related issues: ")

hospitalEntry = Entry(root, text="Enter the number of times admitted in the hospital for diabetese related issues: ")

#! Hospital entry styling
hospitalLabel.grid(row=6,column=0)
hospitalEntry.grid(row=6, column=1)

#TODO NUmber of doses for 2hr Serum insulin taken.
insulinLabel = Label(root, text="Enter the number of times 2hr Serum Insulin taken: ")
insulingEntry = Entry(root, text="Enter the number of times 2hr Serum insulin taken: ")


#Defining the function for the button
def machinebackend():

    #getting all entry data
    glucose_conc = entry1.get()
    blood_pressure = bp_Entry.get()
    bMi = entry2.get()
    Age = ageEntry.get()
    diab_pedi = diab_pediEntry.get()
    skin_thicc = skinEntry.get()
    no_of_times_admiited = hospitalEntry.get()
    hr2_serum_ins = insulingEntry.get()

    #working ML Tree
    if glucose_conc < 100:
        if bMi < 30:
            if Age < 31:
                if glucose_conc < 127:
                    finalLabel1 = Label(root, text="The patient is not diabetic")
                    finalLabel1.grid(row=9, column=0)
                else:
                    if blood_pressure >= 61:
                        finalLabel2 = Label(root, text="The patient is diabetic")
                        finalLabel2.grid(row=9, column=0)
                    else:
                        finalLabel1 = Label(root, text="The patient is not diabetic")
                        finalLabel1.grid(row=9, column=0)
            else:
                if diab_pedi <1:
                    if Age > 49:
                        if skin_thicc > 27:
                            finalLabel2 = Label(root, text="The patient is diabetic")
                            finalLabel2.grid(row=9, column=0)
                        else:
                            finalLabel1 = Label(root, text="The patient is not diabetic")
                            finalLabel1.grid(row=9, column=0)
                    else:
                        finalLabel1 = Label(root, text="The patient is not diabetic")
                        finalLabel1.grid(row=9, column=0)
                else:
                    finalLabel2 = Label(root, text="The patient is diabetic")
                    finalLabel2.grid(row=9, column=0)
    elif glucose_conc > 167:
        finalLabel2 = Label(root, text="The patient is diabetic")
        finalLabel2.grid(row=9, column=0)
        if no_of_times_admiited > 0:
            finalLabel2 = Label(root, text="The patient is diabetic")
            finalLabel2.grid(row=9, column=0)
        else:
            if hr2_serum_ins > 138:
                if bMi > 31:
                    finalLabel2 = Label(root, text="The patient is diabetic")
                    finalLabel2.grid(row=9, column=0)
                else:
                    finalLabel1 = Label(root, text="The patient is not diabetic")
                    finalLabel1.grid(row=9, column=0)    
            else:
                finalLabel1 = Label(root, text="The patient is not diabetic")
                finalLabel1.grid(row=9, column=0)


#? The button should have some texture
employedButton = Button(root, text="Press to calculate", command=machinebackend)
employedButton.grid(row=7, column=0)

#running the loop
root.mainloop()