#WAP to accept a string and a character and display the position of character in the string.

#taking the inputs from the user
randomString = str(input("Enter anything: "))
ranChar = str(input("Enter a character: "))

for i in randomString:
    j = 0
    if ranChar == i:
        print(j)
    else:
        j += 1

