#if else questions 
a = input("Enter your data: ")
print(a)

"""
This program tests whether the weather is hot 
cold or normal according to the temperature the user 
inputs. 

Hot = Greater than 50
Cold = Less than 10
Normal = Between 10 and 50
"""

a = int(input("Enter the temperature: "))

if a > 50:
    print("It is hot")
elif a < 10:
    print("It is cold")
else:
    print("It is normal")


"""
Test whether the number is even or odd
whichever the user inputs.
"""

a = int(input("Enter the number: "))
if a % 2 == 0:
    print("It is even")
else:
    print("It is odd")

"""
If the name is less than 3 characters then the name is 
shorter than usual. If the name is of more than 20 characters 
it is longer than usual.
"""

a = input("Enter your name: ")
if len(a) < 3:
    print("The name is shorter than usual")
elif len(a) > 20:
    print("The name is longer than usual")
else:
    print("The name is normal")