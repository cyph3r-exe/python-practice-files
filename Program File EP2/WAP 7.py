#Debangshu  Roy 
# XII - B 
# 40

#Write a menu driven program to accept, modify, delete. display (selective and complete) 
# data using a list. The Record structure is as follows 

#patient ID int 0
#patient name str 1
#Date of testing str 2
#rtpcr result str 3

from hashlib import new
import os
import csv

#function to add data to CSV file. 

def addData(data):
    F = open("Database.csv", 'a', newline='')
    pointer = csv.writer(F)
    pointer.writerow(data)
    F.close()

def deleteData(iD):
    F = open("Database.csv", 'r')
    F1 = open("temp.csv", 'a', newline='')
    reader = csv.reader(F)
    writer = csv.writer(F1)
    for i in reader:
        if i[0] == iD:
            continue
        else:
            writer.writerow(i)
    F.close()
    F1.close()
    os.remove('Database.csv')
    os.rename("temp.csv", "Database.csv")

def modPatientName(iD, newName):
    F = open("Database.csv", 'r')
    F1 = open("temp.csv", 'w', newline='')
    reader = csv.reader(F)
    writer = csv.writer(F1)
    for i in reader:
        for j in i:
            if j[0] == iD:
                j[1] == newName
                writer.writerow(i)
            else:
                writer.writerow(i)
    F.close()
    F1.close()
    os.remove('Database.csv')
    os.rename("temp.csv", "Database.csv")

def modDateofTesting(iD, newDOT):
    F = open("Database.csv", 'r')
    F1 = open("temp.csv", 'w', newline='')
    reader = csv.reader(F)
    writer = csv.writer(F1)
    for i in reader:
        if i[0] == iD:
            i[1] == newDOT
            writer.writerow(i)
        else:
            writer.writerow(i)
    F.close()
    F1.close()
    os.remove('Database.csv')
    os.rename("temp.csv", "Database.csv")

def modResultPOStoNEG(iD):
    F = open("Database.csv", 'r')
    F1 = open("temp.csv", 'w', newline='')
    reader = csv.reader(F)
    writer = csv.writer(F1)
    for i in reader:
        if i[0] == iD:
            i[3] == "-"
            writer.writerow(i)
        else:
            writer.writerow(i)
    F.close()
    F1.close()
    os.remove('Database.csv')
    os.rename("temp.csv", "Database.csv")
    
def modResultNEGtoPOS(iD):
    F = open("Database.csv", 'r')
    F1 = open("temp.csv", 'w', newline='')
    reader = csv.reader(F)
    writer = csv.writer(F1)
    for i in reader:
        if i[0] == iD:
            i[3] == "+"
            writer.writerow(i)
        else:
            writer.writerow(i)
    F.close()
    F1.close()
    os.remove('Database.csv')
    os.rename("temp.csv", "Database.csv")

def seldisplay(name):
    F = open("Database.csv", 'r')
    p = csv.reader(F)
    for i in p:
        if i[1] == name:
            print(i)
        else:
            continue
    print("Patient Name not found.")
    F.close()

def comdisplay():
    F = open('Database.csv', 'r')
    p = csv.reader(F)
    for i in p: 
        print(f"Patient ID : {i[0]}")
        print(f"Patient Name : {i[1]}")
        print(f"Patient Test Date : {i[2]}")
        print(f"Patient Test Result {i[3]}")
        print()
    F.close()
x = "Y"
Pid = 0
while (x):

    print("Welcome to Corona Database. Please choose an action of your choice.")
    print("1) Add Data to the Database")
    print("2) Delete a record from the database")
    print("3) Modify Particulars of a record.")
    print("4) Display Particular record")
    print("5) Display All recards")
    print("6) Exit")
    choice1 = int(input("Choose your choice: "))
    if choice1 == 1:
        temp = []
        Pid += 1
        temp.append(Pid)
        Pname = str(input("Enter Patient Name [Full Name]: "))
        temp.append(Pname)
        Pdot = str(input("Enter Date of Testing [DD/MM/YYYY]: "))
        temp.append(Pdot)
        rtpcr = str(input("Enter Result [+/-]: "))
        temp.append(rtpcr)
        addData(temp)

        x = str(input("Do you wish to continue ? Y / N: "))

    elif choice1 == 2:
        checkId = int(input("Enter ID of patient: "))
        deleteData(checkId) 

    elif choice1 == 3:
        print("What do you want to Modify? ")
        print("1) Patient name")
        print("2) Patient date of Testing")
        print("3) Patient RTPCR Result")
        choice2 = int(input("Enter your choice: "))
        if choice2 == 1:
            checkId = int(input("Enter ID of patient: "))
            new_name = str(input("Enter new name: "))
            modPatientName(checkId, new_name)

            x = str(input("Do you wish to continue ? Y / N: "))
        
        elif choice2 == 2:
            checkId = int(input("Enter ID of patient: "))
            new_date = str(input("Enter new Date: "))
            modDateofTesting(checkId, new_date)
            x = str(input("Do you wish to continue ? Y / N: "))

        elif choice2 == 3:
            print("Enter 1 if it's +ve to -ve ")
            print("Enter 2 if it's -ve to +ve ")
            choice3 = int(input("Enter your choice: "))
            checkId = int(input("Enter ID of patient: "))
            if choice3 == 1:
                modResultPOStoNEG(checkId)
            else:
                modResultNEGtoPOS(checkId)

    elif choice1== 4:
        uName = input("Enter name of person: ")
        seldisplay(uName)


    elif choice1 == 5:
        comdisplay()

    elif choice1 == 6:
        os._exit()

"""
Welcome to Corona Database. Please choose an action of your choice.
1) Add Data to the Database
2) Delete a record from the database
3) Modify Particulars of a record.
4) Display Particular record
5) Display All recards
6) Exit
Choose your choice: 5
Patient ID : 1
Patient Name : Debangshu Roy
Patient Test Date : 27092022
Patient Test Result +
"""