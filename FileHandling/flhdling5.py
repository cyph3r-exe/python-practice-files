"""
Consider a csv file , emp.csv , containing details of employees ( employee no, 
name, DOB , salary). Write a function that reads the contents of the file and 
displays the records of only those employees whose salary is between 50000 
to 80000 (both inclusive)
"""

import csv 

def testfun():
    F = open("emp.csv", 'r')
    r = csv.reader(F)
    for i in r:
        if i[3] < 50000 and i[3] > 80000:
            print(i)
        else:
            continue
    F.close()

