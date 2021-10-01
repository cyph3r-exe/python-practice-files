"""
Write a program with UDF to print the number
after increasing it to the power 
accepted from the user. 
"""
#Declaring Variables
x = int(input("Enter a number: "))
y = int(input("Enter it's power: "))

#Defining the Function
def main(num1, num2):
    calc = num1 ** num2
    print(f"The power of {num1} when it is raised by {num2} is {calc}")
    
#Calling the Function
main(x, y)
