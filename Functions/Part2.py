"""
Write a program to accept to number two numbers 
display quotient and remainder
"""

#Declaring Variables 
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

#Defining the function
def main(num1, num2):
    rem = num1 % num2
    quote = num1 / num2
    print(f"The quotient is {quote} and the remainder is {rem}")

#Calling the function
main(x,y)
