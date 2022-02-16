#WAP to accept a string and check whether it is a palindrome or not.

#Function to check wether the given string is a palindrome
def isPalindrome(someString):
    return someString == someString[::-1]
 
 
#initialisation
someString = str(input("Enter anything: "))
answer = isPalindrome(someString)

#printing the answers
if answer:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")