#WAP to accept two strings and display the characters that are present in both the strings.

#accepting the strings
string1 = str(input("Enter the first String: "))
string2 = str(input("Enter the second string: "))

#loops for printing the characters 
for i in string1:   #First loop to take out a single char
    for j in string2:   #Second loop to take a single char
        if i == j:  #check
            print(i)    
        else:
            continue
