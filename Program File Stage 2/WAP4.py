#WAP to accept 10 numbers into a list and count the number of even multiples of 7.

#initialising vairables
blankList = []
x = 0
y = 0

#taking 10 inputs from the user
while x <= 10:
    ranInt = int(input("Enter a number: "))
    blankList.append(ranInt)

#loop for checking
for i in blankList:
    if i % 2 == 0:
        if i % 7 == 0:
            y =+ 1 

#output
print(y)