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
import math as mt
import os

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
    while tr_choice < 5:
        tr_base_a = int(input("Enter the value of the base of the triangle: "))
        tr_side1_b = int(input("Enter the value of one side of the triangle: "))
        tr_side2_c = int(input("Enter the value of the other side of the triangle: "))
        if tr_base_a + tr_side1_b > tr_side2_c:
            if tr_side2_c + tr_side1_b > tr_base_a:
                if tr_base_a + tr_side2_c > tr_side1_b:
                    tr_choice = int(input("""Here is your menu. Type the number
                    associated with the kind of value you want to see.
                    1 -> Perimeter
                    2 -> Area 
                    3 -> Volume 
                    4 -> Surface Area: """))
                    #Using heron's formula to find the height of the triangle 
                    #given by the user. 
                    s = (tr_base_a + tr_side1_b + tr_side2_c) / 2
                    tr_area = mt.sqrt(s * (s - tr_base_a) * (s - tr_side1_b) * (s - tr_side2_c))
                    tr_height = (2 * s) / tr_base_a
                    if tr_choice == 1:
                        tr_perim = tr_base_a + tr_side1_b + tr_side2_c
                        print(f"The perimeter of your triabngle is {tr_perim}")
                    elif tr_choice == 2:
                        print(f"The area of your triangle is {tr_area}")
                    elif tr_choice == 3:
                        tr_volume = (tr_base_a * tr_side1_b * tr_height) / 3
                        print(f"The volume of your triangle is {tr_volume}")
                    elif tr_choice == 4:
                        print(f"the surface area of your triangle is {tr_area}")

def circle():
    while cs_choice < 5:
        cs_radius = int(input("Enter the radius of your circle: "))
        cs_choice = int(input("""Here is your menu. Type the number
                    associated with the kind of value you want to see.
                    1 -> Perimeter
                    2 -> Area 
                    3 -> Volume 
                    4 -> Surface Area: """))
        if cs_choice == 1:
            cs_perim = 2 * 3.14 * cs_radius
            print(f"The perimeter of your circle is {cs_perim}")
        elif cs_choice == 2:
            cs_area = 2 * 3.14 * (cs_radius * cs_radius)
            print(f"The area of your circle is {cs_area}")
        elif cs_choice == 3:
            cs_volume = 4/3(3.14 (cs_radius * cs_radius * cs_radius))
            print(f"The volume of your circle is {cs_volume}")
        elif cs_choice == 4:
            cs_surArea = 4/3(3.14 (cs_radius * cs_radius))
            print(f"The surface area of your circle is {cs_surArea}")
        else:
            print("Please try again")

def cylinder():
    while cy_choice < 5:
        cy_radius = int(input("Enter the radius of your cylinder: "))
        cy_height = int(input("Enter height of your cylinder: "))
        cy_choice = int(input("""Here is your menu. Type the number
                    associated with the kind of value you want to see. 
                    1 -> Volume 
                    2 -> Surface Area: """))
        if cy_choice == 1:
            cy_volume = 3.14 * (cy_radius * cy_radius) * cy_height
            print(f"The volume of the sphere is {cy_volume}")
        elif cy_choice == 2:
            cy_surArea = 2 * 3.14 * cy_radius * cy_height * (cy_radius + cy_height)
            print(f"The surface area of your cylinder is {cy_surArea}")
        
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
        elif main_choice == 3:
            triangle()
        elif main_choice == 4:
            circle()
        elif main_choice == 5:
            cylinder()
        else:
            x = int(input("""Whould you like ot continue? 
            If yes press 1
            if no, press 2: """))
            if x == 1:
                continue
            elif x == 2:
                os.exit
