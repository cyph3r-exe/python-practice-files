#WAP to accept 10 numbers in a tuple and then display the largest and the smallest number.

#initialising variables 
x = 1
emptyTuple = ()

#loops to show the smallest and largest numbers
while x <=10:
    ranInt = int(input("Enter any Number: "))
    emptyTuple = emptyTuple + (ranInt, )
    x =+ 1
    print(min(emptyTuple))
    print(max(emptyTuple))