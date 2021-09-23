"""
IF the name is less than 3 characters then the name is 
shorter than usual. If the name is of more than 50 characters 
it is longer than usual.
"""

#Taking name from the user 
name = str(input("Please enter your full name: "))

#Evaluating the name 
if len(name) < 3:
    print("The name that you have put is too short")
elif len(name) > 50:
    print("The name that you have put is too long")
else:
    print("The name you have entered is just perfect")
        