#WAP to accept 10 numbers in a tuple and then display the largest and the smallest number.

x = 1
emptyTuple = ()

while x <=10:
    ranInt = int(input("Enter any Number: "))
    emptyTuple = emptyTuple + (ranInt, )
    x =+ 1
    print(min(emptyTuple))
    print(max(emptyTuple))
