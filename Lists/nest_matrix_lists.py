"""
Using nested loops to iterate over
all the items in a matrix list
"""

#Defining a matrix list
matrix = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

#This loop will iterate over all the items inside the matrix list
for row in matrix:
    for index in row:
        print(index)

