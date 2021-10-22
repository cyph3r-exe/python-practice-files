"""
Write a Python program which accepts the user's first and last name 
and print them in reverse order with a space between them
"""

#Declaring variables 
x = str(input("Enter your first name: "))
y = str(input("Enter your last name: "))

#Defining the function 
def main(b, a):
    print(f"Your reversed name is {a} {b}")
    
#calling the function
main(x, y)