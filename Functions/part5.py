"""
WAP using UDF to display the reverse 
of a number. 
"""
#Defining the function
def reverse(num):
    sum = 0
    while num > 0:
            x = num % 10 
            sum = sum * 10 + x
            num = num // 10
            print(sum)

#Declaring Variables 
var = int(input("Enter a number: "))

#calling the function
reverse(var) 