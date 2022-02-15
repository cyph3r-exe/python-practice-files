#Debangshu Roy 
#WAP to accept a number and display the corresponding weekday

x = int(input("Enter the number of the weekday: "))

if x == 0:
    print("There is no corresponding weekday")
elif x < 0:
    print("Enter a positive number and try again")
elif x < 8:
    print("Enter a number between 1 and 7 ")
elif x == 1:
    print("The corresponding day is Monday")
elif x == 2:
    print("The corresponding day is Tuesday")
elif x == 3:
    print("The corresponding day is Wednesday")
elif x == 4:
    print("The corresponding day is Thursday")
elif x == 5: 
    print("The corresponding day is Friday")
elif x == 6:
    print("The corresponding day is Saturday")
elif x == 7:
    print("The corresponding day is Sunday")
