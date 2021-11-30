"""
Write a function to print the table of a given number. 
The number has to be entered by the user
"""

#taking inputs
x = int(input("Enter any number: "))
y = int(input("Enter the number till which you want o see the multiplication: "))

#defining the function
def test(a, b):
    tbm = 1

    #intialising while loop
    while tbm <= b:
        print(f"{a} * {tbm} = {a * tbm}")
        tbm = tbm + 1

#calling the function
test(x,y)