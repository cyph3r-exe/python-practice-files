"""Write a program that has a user defined function 
to accept the coefficients of a quadratic equation 
in variables and calculates its determinant. For 
example : if the coefficients are stored in the 
variables a,b,c then calculate determinant as 
b2-4ac. Write the appropriate condition to check 
determinants on positive, zero and negative and 
output appropriate result."""


import os
def test():
    a = int(input("Enter the first coeficient: "))
    b = int(input("Enter the second coefficient: "))
    c = int(input("Enter the third coefficient: "))

    calc = pow(b,2) - 4*(a*c)
    if calc > 0:
        print("The solution is positive")
    elif calc == 0:
        print("The solution is neutral")
    elif calc < 0:
        print("The solution is negative.")
    else:
        print("Plase try again.")

x = input("Do you want to start the program? Enter Y for Yes and N for No.")
if x == 'y' or x == 'Y':
    test()
elif x == 'N' or x == 'n':
    os.exit
else:
    os.exit