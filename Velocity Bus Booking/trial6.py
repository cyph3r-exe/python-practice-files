import csv

F = open("locationdata.csv", 'r')
rd = list(csv.reader(F))

print(rd[1][1])
