#WAP to accept two strings and display the characters that are present in both the strings.

string1 = str(input("Enter the first String: "))
string2 = str(input("Enter the second string: "))

for i in string1:
    for j in string2:
        if i == j:
            print(i)
        else:
            continue
