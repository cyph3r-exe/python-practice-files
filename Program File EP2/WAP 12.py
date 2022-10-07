#Debangshu Roy 
#XII - B
#40

# WAP to binary sort

ranList=[]
def listsorter():
    ab=int(input("Enter no. of elements : "))
    for x in range(ab):
        bd=int(input("Enter numbers:"))
        ranList.append(bd)
    print("Original: ",ranList)
    ranList.sort()
    print("Sorted: ",ranList)

def search():
    num = int(input("Enter a number: "))
    i = 0
    z = len(ranList)-1
    while i<=z:
        m = (i+z)//2
        if num == ranList[m]:
            print()
            print(f"{num} is found at position: {m+1}")
            break
        elif num>ranList[m]:
            i = m+1
        elif num<ranList[m]:
            z = m-1
        else:
            print(num,"not found in list",ranList)

listsorter()
search()

"""
Enter no. of elements : 3
Enter numbers:98
Enter numbers:23
Enter numbers:21
Original:  [98, 23, 21]
Sorted:  [21, 23, 98]
"""