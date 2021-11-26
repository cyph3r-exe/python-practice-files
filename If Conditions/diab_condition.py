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