#Debangshu  Roy 
# XII - B 
# 40

#WAP to add, modify, delete, and display (selective or complete) data from a binary file. 
#The records are stored using a list and are as follows 
#BID - int 0
#arrival - str 1
#destination - str 2
#doj - str 3
#fare - float 4

import os
import pickle

def addData(data):
    F = open("Database.dat", 'ab+')
    pickle.dump(data, F)
    F.close()

def deleteData(iD):
    F = open("Database.dat", 'rb')
    F1 = open("temp.dat", 'wb')
    try:
        while (F):
            a = pickle.load(F)
            for i in a:
                if i[0] != iD:
                    pickle.dump(i, F1)
                else:
                    continue
    except EOFError:
        print("File Completed")
    
    finally:
        os.remove("Database.dat")
        os.rename("temp.dat", "Database.dat")

def modArrivalData(iD, new_data):
    F = open("Database.dat", 'rb')
    F1 = open("temp.dat", 'wb')
    try:
        while (F):
            a = pickle.load(F)
            for i in a:
                if i[0] == iD:
                    i[1] = new_data
                    pickle.dump(i, F1)
                else:
                    pickle.dump(i, F1)
                    continue
        
    except EOFError:
        print("End of File. ")

    finally:
        os.remove("Database.dat")
        os.rename("temp.dat", "Database.dat")
 

def modDestinationData(iD, new_data):
    F = open("Database.dat", 'rb')
    F1 = open("temp.dat", 'wb')
    try:
        while (F):
            a = pickle.load(F)
            for i in a:
                if i[0] == iD:
                    i[2] = new_data
                    pickle.dump(i, F1)
                else:
                    pickle.dump(i, F1)
                    continue
        
    except EOFError:
        print("End of File. ")

    finally:
        os.remove("Database.dat")
        os.rename("temp.dat", "Database.dat")

def modDateofJourneyData(iD, new_data):
    F = open("Database.dat", 'rb')
    F1 = open("temp.dat", 'wb')
    try:
        while (F):
            a = pickle.load(F)
            for i in a:
                if i[0] == iD:
                    i[3] = new_data
                    pickle.dump(i, F1)
                else:
                    pickle.dump(i, F1)
                    continue
        
    except EOFError:
        print("End of File. ")

    finally:
        os.remove("Database.dat")
        os.rename("temp.dat", "Database.dat")

def modFare(iD, new_data):
    F = open("Database.dat", 'rb')
    F1 = open("temp.dat", 'wb')
    try:
        while (F):
            a = pickle.load(F)
            for i in a:
                if i[0] == iD:
                    i[4] = new_data
                    pickle.dump(i, F1)
                else:
                    pickle.dump(i, F1)
                    continue
        
    except EOFError:
        print("End of File. ")

    finally:
        os.remove("Database.dat")
        os.rename("temp.dat", "Database.dat")

def selectiveDataDisplay (iD):
    F = open("Database.dat", 'rb')
    try:
        while (F):
            a = pickle.load(F)
            for i in a:
                if i[0] == iD:
                    print("Your Booking details are as follows.")
                    print(f"Arrival - {i[1]}")
                    print(f"Destination - {i[2]}")
                    print(f"Date of Journey - {i[3]}")
                    print(f"Fare - {i[4]}")
                else:
                    print("Given ID was not found please try again.")
    except:
        print("End of File. ")
    F.close()

def completeDisplay():
    F = open("Database.dat", 'rb')
    try:
        while (F):
            a = pickle.load(F)
            for i in a:
                print(f"Booking ID - {i[0]}")
                print(f"Arrival - {i[1]}")
                print(f"Destination - {i[2]}")
                print(f"Date of Journey - {i[3]}")
                print(f"Fare - {i[4]}")
                print()
                print("---------------------------------")
                print()
    except:
        print("End of File.")
    F.close()


bID = 0 
ch = "y"
while (ch):
    print("Welcome to Plane")
    print("Please select what you want to do: ")
    print("1) Add Data to Database \n 2) Delete data from Database. \n 3) Selectively Modify data in a database. ")
    print("4) Display Selective or complete data from a databse ")
    first_ch = int(input("Enter your choice: "))   

    if first_ch == 1:
        temp_list = []
        bID += 1
        temp_list.append(bID)
        arrival = str(input("Enter Arrival Location Code [for eg New Delhi - NDL]: "))
        temp_list.append(arrival)
        dest = str(input("Enter Destination Location Code [for eg Ranchi - IXR]: "))
        temp_list.append(dest)
        doj = str(input("Enter Date of Journey [DD/MM/YYYY]: "))
        temp_list.append(doj)
        fr = int(input("Enter fare: "))
        print(f"Your Booking ID is {bID}. Please remember it access your record.")
        temp_list.append(fr)
        addData(temp_list)
        temp_list.clear()
        ch = str(input("Do you wish to continue ? Y / N: "))

    elif first_ch == 2:
        ch_bID = int(input("Enter your Booking ID: "))
        print("What do you want to edit: \n 1) Arrival Location Code \n 2) Dstination Location Code ")
        print("3) Date of Journey \n 4) Fare ")
        i_ochoice = int(input("Enter your choice: "))
        if i_ochoice == 1:
            new_Arrival = str(input("Enter new Arrival Location Code: "))
            modArrivalData(ch_bID, new_Arrival)
            print("Operation completed successfully")
            ch = str(input("Do you wish to continue ? Y / N: "))

        elif i_ochoice == 2:
            new_dest = str(input("Enter new Destination Location Code: "))
            modDestinationData(ch_bID, new_dest)

            print("Operation completed successfully")
            ch = str(input("Do you wish to continue ? Y / N: "))
        elif i_ochoice == 3:
            new_DOJ = str(input("Enter new Date of Journey: "))
            modDateofJourneyData(ch_bID, new_DOJ)

            print("Operation completed successfully")
            ch = str(input("Do you wish to continue ? Y / N: "))
        elif i_ochoice == 4:
            new_fare = float(input("Enter new fare: "))
            modFare(ch_bID, new_fare)

            print("Operation completed successfully")
            ch = str(input("Do you wish to continue ? Y / N: "))
    elif first_ch == 3:
        print("Do you want to view \n 1) Selective Data \n 2) Complete Data")
        o_ochoice = int(input("Enter your choice: "))
        if o_ochoice == 1:
            ch_bID = int(input("Enter your Booking ID: "))
            selectiveDataDisplay(ch_bID)
            ch = str(input("Do you wish to continue ? Y / N: "))
        elif o_ochoice == 2:
            completeDisplay()
            ch = str(input("Do you wish to continue ? Y / N: "))