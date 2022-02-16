#Debangshu Roy 
#Fibonacci Series with while loop 

x = "yes"

while x =="yes" or x == "YES" or x == "YeS":
    n = int(input("Enter a number : "))
    if n == 0:
        print("Kindly enter a non-zero integer")
    elif n < 0:
        print("Kindly enter a positive integer")
    else: 
        a = 0
        b = 1 
        print(a)
        print(b)
    1 = 2
    while 1 < n:
        1 = 1 + 1 
        c = a + b 
        print(c)
        a = b
        b = c 
    x = input("Would you like to continue? Yes or No")
    if x == "Yes" or x == "YES":
        continue 
    else:
        break 