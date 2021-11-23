"""
Make the following programs using user defined functions 
( write down in your notebook and then try them on the system ) …
 also pass arguments and return values in at least one question 
(1) Fibonacci series 
(2) Return reverse of a number 
(3) Count the ni of spaces in a string
"""

def fibonacci():

    nterms = int(input("How many terms? "))
    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < nterms:
       print(n1)
       nth = n1 + n2   
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

def strspaces():
    string = input("Enter any sentence of your choice: ")
    numcount = 0
    for i in string:
        if i == ' ':
            numcount =+ 1
        else:
            continue
    print(f"Number of spaces in your string are: {numcount}")

while choice_main < 4:
    choice_main = int(input("""
    What would you like to use in this program. 
    Please type the value associated with the 
    same. Thank you for co-operating. 
    1 -> Fibonacci till n Terms 
    2 -> Reverse of a number. 
    3 -> Number of spaces in a string. 

    Enter number here : 
    """))

    if choice_main == 1:
        fibonacci()
    elif choice_main == 2:
        reverse()
    elif choice_main == 3:
        strspaces()
    else: 
        print("Please try again")