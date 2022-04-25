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

def finalDataReading():
    F = open("Three.txt", 'r+')
    x = F.readlines()
    num = 0 
    try: 
        while (F):
            for i in x:
                y = i.split()
                for g in y:
                    if len(g) == 3:
                        num += 1
                        print(g)
                    else:
                        continue
    except:
        print("End of File")

choice = "Y"
while (choice):
    x = input("Enter the string of your choice: ")
    insertData(x)
    choice = input("Do you want to continue? Y / N")
    if choice == "Y" or choice == "y":
        continue
    else:
        finalDataReading()
        break