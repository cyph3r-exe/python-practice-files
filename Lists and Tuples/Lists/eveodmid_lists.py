#Write a function in python that takes a list as an argument and displays the square of even numbers and square roots of 
#odd numbers separately 


import math as mt
#defining the function 
myList = [9, 10, 12, 11, 14, 15, 19, 16]
oddList = []
evenList = []
def myListSorter(a):
    for i in a:
        if i %2 == 0:
            b = mt.pow(i,2)
            evenList.append(b)
        elif i % 2 != 0:
            c = mt.sqrt(i)
            oddList.append(c)
    
    print("Square of even numbers are : ")
    for j in evenList:
        print(j)

    print('Square root of odd numbers are :')
    for g in oddList:
        print(g)
        