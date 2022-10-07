#Debangshu Roy 
#XII - B 
#40

L = []
A= int(input("How many elements would you like to add: "))
for x in range(A):
    A = int(input("Enter a number: "))
    L.append(A)

print("Original List: ",L)

for x in range(0,len(L)-1):
    for i in range(0,len(L)-1):
        if L[i]>L[i+1]:
            L[i],L[i+1] = L[i+1],L[i]

print("Sorted List: ",L)

"""
TEST OUTPUT 
How many elements would you like to add: 4 
Enter a number: 23
Enter a number: 34
Enter a number: 54
Enter a number: 1
Original List:  [23, 34, 54, 1]
Sorted List:  [1, 23, 34, 54]
"""