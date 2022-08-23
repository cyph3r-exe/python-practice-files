#anirudh project 
#add modify delete
#beauty parlour employee data

import pickle
import os

#Main Menu
def mainmenu():
    print("1: Add Employee Data for Beauty Parlour")
    print("2: Show Employee Data for every employee")
    print("3: Show Employee data for one particular Employee")
    print("4: Modify Employee particulars")
    print("5: Delete Employee details")
    print("6: Exit")
    choice = input("Enter your choice: ")
    if choice == 1:
        addEmployeedata()
    elif choice == 2:
        showcollectively()
    elif choice == 3:
        showparticularData()
    elif choice == 4:
        modify()
    elif choice == 5:
        deletedata()
    elif choice == 6:
        os._exit()

#function to add employee details 
def addEmployeedata():
    F = open("empdata.dat", 'ab')
    y = "y"
    while (y):
        empID = input("Enter Employee ID: ")
        empName = input("Enter Employee full name: ")
        empContact  = input("Enter Phone Number: ")
        empwork = input("Enter work title: ")
        empsal  = input("Enter monthly salary: ")
        varList = [empID, empName, empContact, empwork, empsal]
        pickle.dump(varList, F)
        choice1 = input("Do you wish to enter again? ")
        if choice1 == 'y':
            continue
        else:
            F.close()
            mainmenu()

#function to display selectively
def showparticularData():
    y = "y"
    while (y):
        F = open("empdata.dat",'rb')
        totalD = pickle.load(F)
        askID = input("Enter Employee ID: ")
        for i in totalD:
            if i[0] == askID:
                print(f"Employee Name: {i[1]}")
                print(f"Employee Phone Number: {i[2]}")
                print(f"Employee Work Title: {i[3]}")
                print(f"Employee Salary: {i[4]}")
                choice1 = input("If you wish to try again?, press y, or else press n.")
                if choice1 == 'y':
                    continue
                else:
                    F.close()
                    mainmenu()
            else:
                choice1 = input("If you wish to try again?, press y, or else press n.")
                if choice1 == 'y':
                    continue
                else:
                    F.close()
                    mainmenu()

#function to display collectively. 
def showcollectively():
    F = open("empdata.dat", 'rb')
    totalData = pickle.load(F)
    for i in totalData:
        print(f"Employee ID: {i[0]}")
        print(f"Employee Name: {i[1]}")
        print(f"Employee Phone Number: {i[2]}")
        print(f"Employee Work Title: {i[3]}")
        print(f"Employee Salary: {i[4]}")
    F.close()
    mainmenu()

#function to modify one particular detail at a time
def modify():
    F = open("empdata.dat", 'rb')
    F1 = open("temp.dat", 'wb')
    totaldd = pickle.load(F)

    def editID():
        askId = input("Enter employee ID: ")
        for i in totaldd:
            if i[0] != askId:
                pickle.dump(i, F1)
            else:
                newId = input("Enter New ID: ")
                i[0] = newId
                pickle.dump(i, F1)
                print("Sucessfully Edited. Returning to main menu")
        F.close()
        F1.close()
        os.remove("empdata.dat")
        os.rename("temp.dat", "empdata.dat")
        mainmenu()

    def editName():
        askname = input("Enter employee Name: ")
        for i in totaldd:
            if i[0] != askname:
                pickle.dump(i, F1)
            else:
                newname = input("Enter New Name: ")
                i[0] = newname
                pickle.dump(i, F1)
                print("Sucessfully Edited. Returning to main menu")
        F.close()
        F1.close()
        os.remove("empdata.dat")
        os.rename("temp.dat", "empdata.dat")
        mainmenu()
        
    def editphone():
        askphone = input("Enter employee phone: ")
        for i in totaldd:
            if i[0] != askphone:
                pickle.dump(i, F1)
            else:
                newphone = input("Enter New Phone: ")
                i[0] = newphone
                pickle.dump(i, F1)
                print("Sucessfully Edited. Returning to main menu")
        F.close()
        F1.close()
        os.remove("empdata.dat")
        os.rename("temp.dat", "empdata.dat")
        mainmenu()

    def editwork():
        askwork = input("Enter employee Work Title: ")
        for i in totaldd:
            if i[0] != askwork:
                pickle.dump(i, F1)
            else:
                newwork = input("Enter New Work Title: ")
                i[0] = newwork
                pickle.dump(i, F1)
                print("Sucessfully Edited. Returning to main menu")
        F.close()
        F1.close()
        os.remove("empdata.dat")
        os.rename("temp.dat", "empdata.dat")
        mainmenu()
    
    def editSalary():
        asksalary = input("Enter employee salary: ")
        for i in totaldd:
            if i[0] != asksalary:
                pickle.dump(i, F1)
            else:
                newsalary = input("Enter New salary: ")
                i[0] = newsalary
                pickle.dump(i, F1)
                print("Sucessfully Edited. Returning to main menu")
        F.close()
        F1.close()
        os.remove("empdata.dat")
        os.rename("temp.dat", "empdata.dat")
        mainmenu()

    modchoice = int(input("""What do you Want to modify? 
    1: Employee ID
    2: Employee Name: 
    3: Employee Phone Number: 
    4: Employee Work Title: 
    5: Employee Salary: 
    6: Return to Main Menu"""))
    if modchoice == 1:
        editID()
    elif modchoice == 2:
        editName()
    elif modchoice == 3:
        editphone
    elif modchoice == 4:
        editwork()
    elif modchoice == 5:
        editSalary()
    elif modchoice == 6:
        mainmenu()
    
#function to delete employee details 
def deletedata():
    F = open("empdata.dat", 'rb')
    F1 = open("temp.dat", 'wb')
    read = pickle.load(F)
    askID = input("Enter ID of employee you want to delete. ")
    for i in read:
        if i[0] != askID:
            pickle.dump(i, F1)
        else:
            continue
    mainmenu()      
    F.close()
    F1.close()
    os.remove("empdata.dat")
    os.rename("temp.dat", "empdata.dat")

