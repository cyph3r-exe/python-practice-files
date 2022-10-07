#Deivangh Grover 
#XII - B 
from random import *
import csv
from datetime import *

print("Welcome to Hotel Transylvania")

guest1 = 500
perday = 400
dbac = 1000
withasb = 2000
wadb = 3000
wihtoutasb = 4000

def booker():
    ranList = []
    cost = 0
    F = open("bookingrecords.csv", 'a', newline='')
    write = csv.writer(F)
    name = input("Enter your first name: ")
    surname = input("Enter your sur name: ")
    date = input("Enter date of booking - DD/MM/YYYY: ")
    refID = name[:3:1]
    print("") #roomtype
    print("Enter preferred room type. \n1) Double Bed AC \n2) With AC Single Bed \n3) Without AC Double Bed \n4) Without AC Single Bed")
    seat = input("Write selection: ")
    roomnom = randint(1, 100)
    if seat == 1:
        cost = cost + dbac
    elif seat == 2:
        cost = cost + withasb
    elif seat == 3: 
        cost += wadb
    elif seat == 4: 
        cost += wihtoutasb

    daysstaying = int(input("Enter the number of staying days: "))
    a = daysstaying * perday
    totalguests = int(input("Enter total number room guests: "))
    b = guest1 * totalguests

    total_cost = a*b*cost
    day = datetime.today()

    ranList = [name, surname, date, refID, day, seat, roomnom, daysstaying, totalguests, total_cost]
    write.writerow(ranList)
    F.close()

booker()
#def completecheckbooking():
#    F = open("")


    
    



    


    
    