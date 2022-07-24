import csv 
import os

def selective(pid):
    F = open("data.csv", 'r')
    a = csv.reader(F)
    for x in a:
        if x[0] == pid:
            print("Success")
        else:
            continue
    
    F.close()

choice = input("daal na: ")
selective(choice)