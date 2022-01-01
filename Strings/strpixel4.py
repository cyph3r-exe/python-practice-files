"""
Write a program that accepts a string containing digits 
and then displays the sum of these digits.
"""

def findSum(str1):
    temporaryString = "0"
    TSum = 0
    for characNumber in str1:
        if (characNumber.isdigit()):
            temporaryString += characNumber
        else:
            TSum += int(temporaryString)
            temporaryString = "0"
    return TSum + int(temporaryString)

str1 = input(str("Enter any alphanumeric string"))
 
# Function call
print(findSum(str1))