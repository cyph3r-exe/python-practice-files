#Debangshu  Roy 
# XII - B 
# 40

#Write a program to display only three lettered words 
#from a text file named 'Three.txt'. Also return the count 
#of such words returned. 

def insertData(Data):
    F = open("Three.txt", 'a+')
    F.writelines(Data)
    F.close()

num = 0 
def finalDataReading():
    F = open("Three.txt", 'r+')
    x = F.readlines()
    global num
    for i in x:
        y = i.split()
        for g in y:
            if len(g) == 3:
                num += 1
            else:
                continue

choice = "Y"
while (choice):
    x = input("Enter the string of your choice: ")
    insertData(x)
    choice = input("Do you want to continue? Y / N")
    if choice == "Y" or choice == "y":
        continue
    else:
        finalDataReading()
        print(f"Number of three lettered words: {num}")
        break

#TEST OUTPUTS 
