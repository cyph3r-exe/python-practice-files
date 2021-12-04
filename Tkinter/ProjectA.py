#Making the Diabetes project

#Required will be a bit of ML and alot of Tkinter 

#importing tkinter files 
from tkinter import * 


def choice1():
        
    #intitialising tkinter file loop
    root = Tk()

    #first header of the software 
    myHeader = Label(root, text="Welcome to Diabetes Checker.", foreground="#ff0000")
    myHeader.pack()



    #taking initial entry from the user. 
    myEntry1 = Entry(root, text="Enter your glucose concentration: ")
    myEntry1.pack()

    #making the working ML tree 

    glucose_conc = myEntry1.get()

    if glucose_conc < 100:
        myEntry2 = Entry(root, text="Enter your BMI: ")
        myEntry2.pack()
        bMi = myEntry2.get()
        if bMi < 30:
            myEntry3 = Entry(root, text="Enter your Age: ")
            myEntry3.pack()
            Age = myEntry3.get()
            if Age < 31:
                if glucose_conc < 137:
                    myLabel2 = Label(root, text="Patient is not diabetic.")
                    myLabel2.pack()
                else:
                    myEntry3 = Entry(root, text="Enter your Blood Pressure: ")
                    blood_presure = myEntry3.get()
                    if blood_presure >=61:
                        myLabel4 = Label(root, text="Patient is diabetic.")
                        myLabel4.pack()
                    else:
                        myLabel5 = Label(root, text="Patient is not diabetic.")
                        myLabel5.pack()
            else:
                myEntry4 = Entry(root, text="Enter your diabetes pedigree:")
                myEntry4.pack()
                diab_pedi = myEntry4.get() 
                if diab_pedi <1:
                    if Age > 49:
                        myEntry5 = Entry(root, text="Enter your skin thickness: ")
                        myEntry5.pack()
                        skin_thicc = myEntry5.get()
                        if skin_thicc > 27:
                            myLabel5 = Label(root, text="Patient is diabetic.")
                            myLabel5.pack()
                        else:
                            myLabel6 = Label(root, text="Patient is not diabetic.")
                            myLabel6.pack()
                    else:
                        myLabel7 = Label(root, text="Patient is not diabetic.")
                        myLabel7.pack()
                else:
                    myLabel8 = Label(root, text="Patient is diabetic.")
                    myLabel8.pack()

    #second tree using elif

    elif glucose_conc < 167:
        myLabel9 = Label(root, text="Patient is diabetic.")
        myLabel9.pack()
    else:
        myEntry6 = Entry(root, text="Enter the number of times admitted: ")
        myEntry6.pack()
        no_of_times_admiited = myEntry6.get()

        if no_of_times_admiited > 0:
            myLabel9 = Label(root, text="Patient is diabetic.")
            myLabel9.pack()
        else:
            myEntry7 = Entry(root, text="Enter number of mLs of 2hr Serum insulin taken:")
            myEntry7.pack()
            hr2_serum_ins = myEntry7.get()
            if hr2_serum_ins > 138:
                myEntry2 = Entry(root, text="Enter your BMI: ")
                myEntry2.pack()
                bMi = myEntry2.get()
            
                if bMi < 31:
                    myLabel11 = Label(root, text="Patient is diabetic.")
                    myLabel11.pack()
                else:
                    myLabel12 = Label(root, text="Patient is not diabetic.")
                    myLabel12.pack()
            else:
                myLabel12 = Label(root, text="Patient is not diabetic.")
                myLabel12.pack()

    #running the loop
    root.mainloop()

def choice2():
    """
    Python program to determine whether someone 
    has diabetes or not. 
    """
    #taking inputs

    glucose_conc = int(input("Enter your glucose concentration: "))

    #main working tree
    if glucose_conc < 100:
        bMi = int(input("Enter your BMI: "))
        if bMi < 30:
            Age = int(input("Enter your Age: "))
            if Age < 31:
                if glucose_conc < 127:
                    print("Patient is not diabetic")
                else:
                    blood_pressure = int(input("Enter blood pressure: "))
                    if blood_pressure >= 61:
                        print("Patient is diabetic")
                    else:
                        print("Patient is not Diabetic")
            else:
                diab_pedi = int(input("Enter your diabetes pedigree: "))
                if diab_pedi <1:
                    if Age > 49:
                        skin_thik = int(input("Enter your skin thickness: "))
                        if skin_thik > 27:
                            print("Patient is diabetic.")
                        else:
                            print("Pateint is not diabetic")
                    else:
                        print("Patient is not diabetic")
                else:
                    print("Paitent is diabetic")
    elif glucose_conc > 167:
        print("Patient is diabetic")
    else:
        no_of_times_admiited = int("Enter the number of times admitted: ")
        if no_of_times_admiited > 0:
            print("Patient is diabetic")
        else:
            hr2_serum_ins = int(input("Enter number of mLs taken: "))
            if hr2_serum_ins > 138:
                bMi = int(input("Enter your BMI: "))
                if bMi > 31:
                    print("Patient is diabetics")
                else:
                    print("Patient is not diabetic")    
            else:
                print("Patient is not diabetic")

main_choice = input("Enter 1 for GUI version, 2 for CLI version")
if main_choice == 1:
    choice1()
else:
    choice2()
