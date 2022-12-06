#Ramya has created a dictionary containing names and marks as key value pairs of 6 students 
#Write a program, with separate user defined functions to perform the following operations. 

#Push the keys (name of the student) of the dictionary into a stack, where the corrosponding marks is less than
#50

#Pop and display the contents of the stack. 

R = {"Joy" : 51, "Rancho" : 95, "Bebo" : 39, "Ali" : 65, "Simran" : 19, "Tom" : 72}
highStack = []
def pushKeys(ramDict):
    for i in ramDict:
        if R[i] <= 50:
            highStack.append(i)

def popKeys():
    a = highStack[::-1]
    for i in a:
        print(i)

    for j in a:
        a.pop()
    

pushKeys(R)
popKeys()