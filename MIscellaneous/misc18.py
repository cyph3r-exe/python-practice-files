#Debangshu Roy 
#XII - B 
#40

#Write a program to enter the following data into a new text file. 

print("Write the 4 lines given in the question.")
for i in range(4):
    F = open("ab.txt", 'a')
    x = input("Enter the sentence: ")
    y = x + '\n'
    F.writelines(y)
    F.close()

def replacer():
    F = open("ab.txt", 'r')
    x = F.readlines()
    y = ""
    for i in x:
        for j in i:
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                y = y + '*'
            else:
                y = y + j
    print(y)

def counter():
    F = open("ab.txt", 'r')
    x = F.readlines()
    count = 0
    for i in x:
        if i[0] != 'aeiouAEIOU':
            count += 1
        else:
            pass
    print(count)

replacer()
counter()