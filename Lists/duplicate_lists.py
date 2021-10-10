"""
Write a program to remove all
the duplicates in a list of numbers
"""

the_list = [5, 4, 3, 6, 5, 1, 3]

for i in the_list:
    if i in the_list:
        the_list.remove(i)
        print(the_list)
    else:
        continue


    

