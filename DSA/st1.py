 #Sooraj has a list of names. He wants to create a stack which has only those names 
 # which start with a vowel. 

A = [] #given list
B = [] #stack 

def test(s):
    for i in s:
        c = i.split()
        for j in c:
            d = "aeiou"
            e = "AEIOU"
            if j[0] in d or j[0] in e:
                B.append(i)
            else:
                continue

x = "Y"
count = 1 
while x == "Y" or x == "y":
    n = int(input("Enter the number of times you want to enter names: "))
    while count <= n:
        f = str(input("Enter any name: "))
        A.append(f)
        count += 1
    x = str(input("DO you wish to continue? Y / N ?: "))

test(A)
print(B)
    