#WAP to create a simple calculator performing only four basic operations.
#Importing Time module to stop execution of the prgram to make it feel more realistic
import time

#Declare Variables 

first_value = float(input("Enter a number "))
second_value = float(input("Enter the second number "))
print("Processing ...")
time.sleep(2)                   # Stops execution of the program for 2 seconds    

print("Enter any one of the four operators you want to operate the given numbers with ")
op = (input("Choose an operator: +, -, /, *, %, //"))

#Programe for the Calculator 
if op == "+":                   # Operation of Addition 
    print("Computing please wait")
    time.sleep(2)
    print("The result is ", first_value + second_value)
elif op == "-":                 # Operation of Subtraction 
    if first_value > second_value:
        print("Error, the answer may come in negatives.")
    else:
        print("We are computing please wait")
        time.sleep(2)
        print("The result is ", first_value - second_value)
elif op == "*":                 #Operation of multiplication
    print("We are computing please wait")
    time.sleep(2) 
    print("The result is ", first_value * second_value)
elif op == "/":                     #Operation of Division 
    if first_value or second_value == 0:
        print("Division with 0 is not possible")
    else:
        print("We are computiing please wait")
        time.sleep(2)
        print("The result is ", first_value / second_value)
elif op == "%":
    print("We are computing please wait")
    time.sleep(2)
    print("Your result is ", first_value % second_value)
elif op == "//":
    if first_value or second_value == 0:
        print('Sorry but floor division for 0 is not possible')
    else:
        print("We are computing please wait")
        time.sleep(2)
        print("Your result is ", first_value//second_value)
else:
    print("You have entered the wrong choice. Please run the program again")
