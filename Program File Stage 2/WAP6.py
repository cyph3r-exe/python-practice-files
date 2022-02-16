#WAP to accept three numbers into a tuple an display square of each number. 

#initialising tuple
numTuples = ()

#intialising variables 
x = 0

#loop to accept data
while x < 3:
    ranNum = int(input("Enter a random number: "))
    numTuples = numTuples + (ranNum, )
    x += 1

#loop to display the squares
for i in numTuples:
    print(f"Your squared value is {i*i}")
