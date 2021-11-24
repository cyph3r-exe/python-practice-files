"""
WAP to accept a character and display the following 
pattern according to the number of lines entered.     
"""

x = input("Enter any character: ")

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print(x, end=" ")
    print("\n")