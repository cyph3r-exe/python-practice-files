"""
Write a program that takes two numbers 
as arguments and displays their sum
"""
#Declaring Variables 
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

#Defininf the function
def main(num1, num2):
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

#Calling the function 
main(x,y)