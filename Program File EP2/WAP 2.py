#Debangshu  Roy 
# XII - B 
# 40

#Write a program to count the number of vowels in a text file named 
#Myfile.txt. 

def enterData(Data):
    F = open("MyFile.txt", 'a+')
    F.writelines(Data)
    F.close()

count = 0
def readData():
    F = open("MyFile.txt", 'r+')
    global count
    x = F.read()
    for i in x:
        for j in ['a', 'e', 'i', 'o', 'u']:
            if i == j:
                count += 1
            else:
                continue
        else:
            continue

    print(count)
        
choice = "Y"
while (choice):
    x = input("Enter the string of your choice: ")
    enterData(x)
    choice = input("Do you want to continue? Y / N")
    if choice == "Y" or choice == "y":
        continue
    else:
        readData()  
        break
"""
TEST OUTPUT 1
Enter the string of your choice: hola mi tale tale ooo om nom nom bhrim krim prem challl
Do you want to continue? Y / NN
17

TEST OUTPUT 2 (SAME FILE)
Enter the string of your choice: idk tum batao araam aata hai dinar se tere mit jaate hai saare ghum 
Do you want to continue? Y / NN
45
"""