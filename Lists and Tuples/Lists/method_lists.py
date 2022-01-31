"""
Using List methods to remove 
add or dsiplay all the numbrs in a list.
"""

#Declaring a list 
check_numbers = [3, 5, 7, 1, 4, 2, 9, 8]

#Using pop to remove the last digit or 
#any other digit from the list. 
check_numbers.pop()
print(check_numbers)

#Using insert to insert a 
# a digit at a specific point. 
check_numbers.insert(2, 10)
print(check_numbers)

#Using a sort to sort a list
check_numbers.sort()
print(check_numbers)

#using reverse true sort to 
#sort in reverse 
check_numbers.sort(reverse=True)
print(check_numbers)

#Using copy to create a copy of our 
#first list 
a = check_numbers.copy()
print(check_numbers)  
print(a)

