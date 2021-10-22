"""
Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20
"""

#declaring variables 
x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))

a = x + y

def main(z):
    if z >= 15 and z <= 20:
        return 20
    else:
        print(z)

store = main(a)
print(store)