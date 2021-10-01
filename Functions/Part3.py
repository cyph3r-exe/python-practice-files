"""
Write a program to create a user defined 
function to display how many number of times
a character is there in a string, both of which are
taken from the user.
"""
#Declaring variables 
x = str(input("Enter a string: "))
y = input("Enter a character: ")

#Defiing the function
def main(sitring, charac):
    z = 0
    for v in sitring:
        if v == charac:
            z += 1
        print(z)

#Calling the function
main(x, y)        