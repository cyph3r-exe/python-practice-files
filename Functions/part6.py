"""
WAP using UDF to return the position of an 
character in the given string. 
"""

#Defining the function
def test(x,y):
    a = 0
    b = 0
    for i in x:
        if y == i:
            a += 1 
        elif y != i:
            continue
        else:
            return b
    return a

string = input("Enter a string: ")
char = input("Enter a character: ")

z = test(string, char)
print(f"The number of character in your string are {z}")