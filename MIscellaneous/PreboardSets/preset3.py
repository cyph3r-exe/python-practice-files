"""
1.Write a function in Python PUSH(Lst), 
where Lst is a list of numbers. 
From this list push all numbers not divisible by 6 into a stack implemented by using a list. 
Display the stack if it has at least one element, otherwise display appropriate error message.
"""

mainstack = [35, 66, 24, 73, 21, 36, ]
newstack = []
def PUSH(Lst):
    for i in Lst:
        if i % 6 != 0:
            newstack.insert(len(newstack), i)
        else:
            continue

PUSH(mainstack)
print(newstack)

if len(newstack) > 1:
    for i in newstack[::-1]:
        print(i)
        newstack.pop(0)
else:
    print("Error hai bhai")
 