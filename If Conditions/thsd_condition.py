"""
Write a Python program to test whether 
a number is within 100 of 1000 or 2000.
"""

#declaring the variable
x = int(input("Enter any number: "))

#code logic
if x < 100: 
    print(x, " is below 100. ")
elif x >= 100 and x < 1000:
    print(x, " is more than 100 less than 1000. ")
elif x >= 1000 and x < 2000: 
    print(x, " is larger than 1000 and less than 2000")