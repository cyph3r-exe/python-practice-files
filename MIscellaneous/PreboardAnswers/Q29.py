#Write a function Lshift(Arr, n) in python, which acceps a list Arr of numbers
#and n is a numeric value by which all elements of the list are shifted 
#to the left. 
Arr = [10, 20, 30, 40, 12, 11]
def Lshift(Arr, n):
    for i in range(n):
        a = Arr[0]
        Arr.pop(0)
        Arr.append(a)

#or use insertion sort method