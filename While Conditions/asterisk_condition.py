"""
Code to make the asterisk on the left side 
according to the number of lines the user wants.
"""

#Declaring Variables 
x = 1 

#Asking for number of lines 
lines = int(input("What is the number of lines you want: "))

#Initiating loop 
while x <= lines:
    print('*' * x)
    x = x + 1

#Stating end of Loop 
print("The loop has ended")