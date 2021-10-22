"""
Write a Python program to check whether a 
specified value is contained in a group of values
"""

#declaring values
values = [1,5,7,3,9,4,11,13,18,34,31,75,36,98,74,]
x = int(input("Enter the value you want to check: "))

#defining the loop
for i in values:
    #test 
    if i == x:
        print("The number you entered is present in the database")
    else:
        print("The number you entered is not present in the database")
