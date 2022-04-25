#Debangshu  Roy 
# XII - B 
# 40

#Write a program to count the number of vowels in a text file named 
#Myfile.txt. 

def enterData(Data):
    F = open("MyFile.txt", 'a+')
    F.writelines(Data)
    F.close()

def readData():
    F = open("MyFile.txt", 'r+')
    count = 0
    try:
        while (F):
            x = F.read()
            for i in x:
                if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                    count += 1
                    print(f"This file has {count} vowels.")
                else:
                    continue
    except:
        print("End of File")
 
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


            


