#Write a python program to input 10 numbers in a list. Then print the numbers,
#sum and average.

a = []
n = 0

while n < 11:
    b = int(input("Enter a number: "))
    a.append(b)
    n = n + 1

c = a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] + a[9]
d = c/10

print("The sum of the number in the list is: ", c)
print("The average of the number in the list is: ", d)

