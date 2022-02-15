#Debangshu Roy 
#WAP to check whether a number is a prime number or not. 
#The program should continue as long as the user wishes to.

x = "Y"

while x == "Y" or x == "y":
    number = int(input("Enter a number "))
    for x in range(2, number):
        if number % x == 0:
            print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")
        x = input("Would You like to continue ? Type Y / N ")
        if x == "Y" or x == "y":
            continue
        else:
            break
        