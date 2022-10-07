#Debangshu  Roy 
# XII - B 
# 40

#To read a file A.txt and copy only three lettered words to another file, B.txt. Display the content and 
#size of B.txt

x = "Y"

while x == "Y":
    sentence = input("Enter a sentence: ")
    F = open("A.txt", 'a')
    F.writelines(sentence)
    F.close()
    x = input("Do you wish to continue? Y / N?")

def mainframe():
    F = open("A.txt", 'r')
    F1 = open("B.txt", 'a')
    A = F.readlines()
    for i in A:
        x = i.split()
        for y in x:
            if len(y) == 3:
                print(y)
                F1.write(i, F1)
            else:
                continue
    F1.close()
    F.close()
    B = open("B.txt", 'r')
    d = B.readlines()
    s = B.tell()
    print(d)
    print(s)
    
mainframe()

"""
Enter a sentence: aaj jaan ni jaan menu dena photo de kone de ch 
Do you wish to continue? Y / N?N
aaj
"""