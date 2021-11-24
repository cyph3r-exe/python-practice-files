"""
WAP to accept a number and display sum of squares of its digits. 
"""
print 
try:
    num = int(input("Enter a number: "))
    temp = num
    mix = 0
    while temp != 0:
        hi = temp % 10
        low = hi * hi
        mix = mix + low
        temp = int(temp /10 )
    print(f"\n Sum of square of digits of num{num} = {mix}")

except ValueError:
    print("\n Wrong input") 
