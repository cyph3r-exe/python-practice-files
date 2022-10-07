#Debangshu  Roy 
# XII - B 
# 40

#Arjun is working on a list of numbers. Out of the numbers, he wants to store only 
#prime number to the stack. Help him form the stack and then display all elements of 
#the stack. If the stack is empty, display the message "over"

stack = []
varStack = []
x = "Y"

while x == "Y":
    askforNum = int(input("Enter a number: "))
    varStack.append(askforNum)
    x = input("Do you wish to continue? Y / N?")

def primeCheck(L):
    for i in L:
        if i % 2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0:
            continue
        else:
            stack.append(i)

def display():
    for i in reversed(stack):
        print(i)
        stack.pop()
    print("over")

primeCheck(varStack)
display() 

"""
TEST OUTPUT
Enter a number: 13
Do you wish to continue? Y / N?Y
Enter a number: 90
Do you wish to continue? Y / N?Y
Enter a number: 57
Do you wish to continue? Y / N?Y
Enter a number: 43
Do you wish to continue? Y / N?Y
Enter a number: 8
Do you wish to continue? Y / N?Y
Enter a number: 7
Do you wish to continue? Y / N?Y
Enter a number: 17
Do you wish to continue? Y / N?Y
Enter a number: 2
Do you wish to continue? Y / N?N
17
43
13
"""