"""
Write a program to accept a character from 
the user and display whether it is a special character, 
digit or an alphabet. The program should continue 
as long as the juser wishes to.
"""

x = "Y"

while x == "y":
    check = input("Enter a character: ")

    if check >= 'a' and check <= 'z' or check >= 'A' and check <= 'Z':
        print("It is an alphabet")
    elif check >= '0' and check <= '9':
        print("It is a digit")
    else:
        print("It is a special character")
    x = input("Do you wish to continue? Y / N ?")
    if x == "y" or x == "Y":
        continue
    else:
        print("Thank you for using our program. ")
        break