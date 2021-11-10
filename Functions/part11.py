"""
Write a program that contains user defined 
functions to calculate area, perimeter or surface 
area whichever is applicable for various shapes 
like square, rectangle, triangle, circle and cylinder. 
The user defined functions should accept the values 
for calculation as parameters and the calculated 
value should be returned. Import the module and 
use the appropriate functions.
"""

def square():
    side = int(input("Enter the value of the side of the square. (in cms): "))
    sq_choice = int(input("""Here is your menu. Type the number
    associated with the kind of value you want to see.
    1 -> Perimeter
    2 -> Area 
    3 -> Volume 
    4 -> Surface Area """))

    if sq_choice == 1:
        a = 4 * side
        print(f"The perimeter is of value {a} cms")
    elif sq_choice == 2:
        b = side * side
        print(f"The area is of value {b} cms^2")
    elif sq_choice == 3:
        c = side*side*side
        print(f"The volume is of value {c} cms^3")
    elif sq_choice == 4:
        d = 6*side*side
        print(f"The surface area is of value {d}")
    else:
        print("Please re-run the program.")

def rectangle():
    length = int(input("Enter the length of your rectangle: "))
    breadth = int(input("Enter the breadth of your rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    rec_choice = int(input("""Here is your menu. Type the number
    associated with the kind of value you want to see.
    1 -> Perimeter
    2 -> Area 
    3 -> Volume 
    4 -> Surface Area """))


