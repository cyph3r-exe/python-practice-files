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
        if i[:1] == 'a' or i[:1] == 'e' or i[:1] == 'i' or i[:1] == 'o' or i[:1] == 'u':
            stkList.append(i)

def printlist():
    ab = reversed(stkList)
    for j in ab:
        print(f"Names starting with Vowel are: {j}")
#loop to enter names (main loop)
while (x):
    name = input("Enter name: ")
    varList.append(name)
    rishi(varList)
    x = input("Do you wish to continue?: y / n")
    if x == 'y' or x == 'Y':
        continue
    elif x == 'n' or x == 'N':
        printlist()
        break

#loop to display final stack
"""
Enter name: anushka
Do you wish to continue?: y / ny
Enter name: debangshu
Do you wish to continue?: y / ny
Enter name: esha
Do you wish to continue?: y / ny
Enter name: deivangh
Do you wish to continue?: y / nn
Names starting with Vowel are: esha   
Names starting with Vowel are: anushka
"""