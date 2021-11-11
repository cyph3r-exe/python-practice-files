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
    while sq_choice < 5:
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
    while rec_choice < 5:
        length = int(input("Enter the length of your rectangle: "))
        breadth = int(input("Enter the breadth of your rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        rec_choice = int(input("""Here is your menu. Type the number
        associated with the kind of value you want to see.
        1 -> Perimeter
        2 -> Area 
        3 -> Volume 
        4 -> Surface Area """))

        if rec_choice == 1:
            a1 = 2 * (length + breadth)
            print(f"The perimeter of you rectangle is of {a1} cms.")
        elif rec_choice == 2:
            b1 = length * breadth
            print(f"The area of your rectangle is {b1} cms^2")
        elif rec_choice == 3:
            c1 = length * breadth * height
            print(f"The volume of your rectangle is {c1}")
        elif rec_choice == 4:
            d1 = 2 ((length * breadth) + (breadth * height) + (height * length))
            print(f"The surface area of your rectangle is {d1}")
        else:
            print("Please try again")

def triangle():
    tr_base = int(input("Enter the value of the base of the triangle: "))
    tr_side1 = int(input("Enter the value of one side of the triangle: "))
    tr_side2 = int(input("Enter the value of the other side of the triangle: "))

while main_choice < 6:
        main_choice = int(input("""
        Welcome.... 
        This is a menu driven program to help you 
        calculate stuff about shapes. 
        Please choose the number associated with the 
        values of the shape you want to see. 
        1 -> Square
        2 -> Rectangle
        3 -> Triangle
        4 -> Circle
        5 -> Cylinder
        Enter number here: """))
        if main_choice == 1:
            square()
        elif main_choice == 2:
            rectangle()