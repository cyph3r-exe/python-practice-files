#Samriddhi Code 

ch =  "y"
while (ch):
    num = int(input("Enter a number: "))
    s = 1
    for i in range(num,0,-1):
        s = s* i 
    print(s)
    ch = input("Do you wish to continue? y/n")
    if ch == 'y' or ch == 'Y':
        continue
    else:
        break
