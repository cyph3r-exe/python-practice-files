#Debangshu  Roy 
# XII - B 
# 40

#Write a menu driven program to accept, modify, delete. display (selective and complete) 
# data using a list. The Record structure is as follows 

#patient ID int 0
#patient name str 1
#Date of testing str 2
#rtpcr result str 3

import os 


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
        #! Function Call for writing in CSv file 

        x = str(input("Do you wish to continue ? Y / N: "))

    elif choice1 == 2:
        checkId = int(input("Enter ID of patient: "))
        #! Function Call 

    elif choice1 == 3:
        print("What do you want to Modify? ")
        print("1) Patient name")
        print("2) Patient date of Testing")
        print("3) Patient RTPCR Result")
        choice2 = int(input("Enter your choice: "))
        if choice2 == 1:
            new_name = str(input("Enter new name: "))
            #! Function Call
        
        elif choice2 == 2:
            new_date = str(input("Enter new Date: "))
            #! Function Call

        elif choice2 == 3:
            print("Enter 1 if it's +ve to -ve ")
            print("Enter 2 if it's -ve to +ve ")
            choice3 = int(input("Enter your choice: "))
            #! Function Call
            

    elif choice1 == 6:
        os._exit()


        

