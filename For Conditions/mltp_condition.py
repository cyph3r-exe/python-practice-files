"""
Make the following programs using user defined functions 
( write down in your notebook and then try them on the system ) …
 also pass arguments and return values in at least one question 
(1) Fibonacci series 
(2) Return reverse of a number 
(3) Count the ni of spaces in a string
"""

choice_main = int(input("""
What would you like to use in this program. 
Please type the value associated with the 
same. Thank you for co-operating. 
1 -> Fibonacci till n Terms 
2 -> Reverse of a number. 
3 -> Number of spaces in a string. 

Enter number here : 
"""))

def fibonacci():
    # Program to display the Fibonacci sequence up to n-th term
    nterms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
    while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
    
def reverse():
    num = 1234
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    print("Reversed Number: " + str(reversed_num))

