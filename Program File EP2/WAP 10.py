#Debangshu Roy 
#XII - B 

#Write a function that takes a dictionary as an argument and forms a queue that stores 
# only name in the same order 
#in which the dictionary is created. Write the code to print the queue. 

x = "y"
queue = []

def main(ranDict):
    queue.append(ranDict["name"])
    #after storing name you print the data inside 

while (x):
    #creating the dictionary
    firDict = {"name": "", "dob": ""}
    #taking data
    enterName = input("Enter Name: ")
    enterDob = input("Enter Date of Birth: ")
    #updating data into dictionary
    firDict.update({"name": enterName})
    firDict.update({"dob": enterDob})
    #function call
    main(firDict)
    #continuation call 
    x = input("Do you want to continue? Y / N")
    if x == "y": 
        continue
    else:
        break

#prints all the names taken from the dictionary
for i in queue:
    print(i)