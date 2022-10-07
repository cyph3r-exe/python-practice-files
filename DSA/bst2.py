#learning selection sort algorithm. 
def selection_Sort(list2):
    flag = 1 
    n=len(list2)
    for i in range(n): 
        min = i
        for j in range(i + 1, len(list2)):
            if list2[j] < list2[min]: 
                min = j
                flag = 1
            if flag == 1 : 
                list2[min], list2[i] = list2[i], list2[min]
                
numList = [8, 7, 13, 1, -9, 4]
selection_Sort(numList)
print("The sorted list is :")
for i in range(len(numList)):
    print(numList[i], end=" ")
