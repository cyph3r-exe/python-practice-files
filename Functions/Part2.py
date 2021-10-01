"""
Write a program to accept to number two numbers 
display quotient and remainder
"""

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

def main(num1, num2):
    rem = num1 % num2
    quote = num1 / num2
    print(f"The quotient is {quote} and the remainder is {rem}")

main(x,y)
