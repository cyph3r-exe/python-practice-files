"""
Write a Python program to get the
volume of a sphere with radius 6.
"""

#defining the function
def main(r):
    vol = 1.33333333333 * 3.14 * r * r * r
    return vol

#declaring the variables
a = int(input("Enter the radius of your sphere: "))
b = main(a)

#output
print(f"the volume of your sphere is: {b}")