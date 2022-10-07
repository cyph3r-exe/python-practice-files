#learning bubble sort. 

newList = [7,8,13,1,-9,4]

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

bubble_sort(newList)
print("The sorted list is: ")
for i in range(len(newList)):
    print(newList[i], end=' ')
