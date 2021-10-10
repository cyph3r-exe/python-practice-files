"""
Generate list of coordinates 
using nested loops
"""

#Defining the function 
def main(x, y):
    for i in range(x):
        for u in range(y):
            print(f"{i}, {u}")

#Declaring Variables 
num1 = int(input("Enter a single digit number: "))
num2 = int(input("Enter another single digit number: "))

#Caling the function 
main(num1, num2)
