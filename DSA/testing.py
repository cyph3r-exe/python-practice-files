
from asyncore import read
import csv
from hashlib import new 

F = open("Database.csv", 'r', newline='')
r = csv.reader(F)
for i in r:
    print(i)