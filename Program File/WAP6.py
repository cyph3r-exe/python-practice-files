#Debangshu Roy 
# WAP to accept three numbers and display the larget number

x = int(input("Enter your number "))
y = int(input("Enter your second number "))
z = int(input("Enter your third number "))

if x>y and x>z:
    print("X is the greatest number")
if y>z and y>x:
    print("Y is the greatest number")
if z>y and z>x:
    print("Z is the greatest number")
            