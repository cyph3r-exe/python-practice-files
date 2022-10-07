#Debangshu Roy 
#XII - B
#40 

#Write a program to do selection sorting 

ranLiist = []
numofelements= int(input("How many elements would you like to add: "))
for i in range(0,numofelements):
    count = int(input("Enter a number: "))
    ranLiist.append(count)
print()
print("OriginaL List: ",ranLiist)
    
def sorting(ranLiist):
    for i in range(0,len(ranLiist)-1):
        b = i
        for x in range(i+1,len(ranLiist)):
            if ranLiist[x]<ranLiist[b]:
                b = x
        ranLiist[i],ranLiist[b] = ranLiist[b],ranLiist[i]
        
sorting(ranLiist)
print("Sorted List: ",ranLiist)


"""
TEST OUTPUT
How many elements would you like to add: 8
Enter a number: 47
Enter a number: 98
Enter a number: 32
Enter a number: 348
Enter a number: 3
Enter a number: 4
Enter a number: 73 
Enter a number: 21

OriginaL List:  [47, 98, 32, 348, 3, 4, 73, 21]
Sorted List:  [3, 4, 21, 32, 47, 73, 98, 348]
"""