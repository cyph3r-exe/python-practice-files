#Arjun wala problem 

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