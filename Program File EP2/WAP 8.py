#Debangshu  Roy 
# XII - B 
# 40

#Rishi has list of his friends. He went to pass the list as argument 
#to a function that forms stack of names which begin with a vowel. 
#write the function 

#variables
x = 'y'
stkList = []
varList = []

#mainnet fucntion
def rishi(fullList):
    for i in fullList:
        if i[0] == 'aeiou':
            stkList.append(i)

#loop to enter names (main loop)
while (x):
    name = input("Enter name: ")
    varList.append(name)
    rishi(varList)
    conf = input("Do you wish to continue?: y / n")

#loop to display final stack
for j in reversed(stkList):
    print(f"Names starting with Vowel are: {j}")
