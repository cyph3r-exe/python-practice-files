#WAP to accept a string and check whether it is a palindrome or not.

def isPalindrome(someString):
    return someString == someString[::-1]
 
 
# Driver code
someString = str(input("Enter anything: "))
answer = isPalindrome(someString)
 
if answer:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")