"""
Generate list of coordinates 
using nested loops
"""
def main(x, y):
    for i in range(x):
        for u in range(y):
            print(f"{x}, {y}")

num1 = int(input("Enter a single digit number: "))