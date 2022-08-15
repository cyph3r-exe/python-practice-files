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