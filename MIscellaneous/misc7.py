"""
ABC School has allotted unique token IDs from (1 to 
600) to all the parents for facilitating a lucky draw 
on the day of their Annual day function. The winner 
would receive a special prize. Write a program using 
Python that helps to automate the task.
"""
from random import *

while end_choice == 'y' or end_choice == 'Y':

    print("Annual day Lucky Draw")

    main_choice = input("Would you like to draw? Enter Y for Yes and N for No")

    def test():
        x = randrange(1,601)
        return x

    if main_choice == 'y' or main_choice == 'Y':
        lucky = test()
        print(f"The lcky number winning the prize is {lucky}")
    else:
        end_choice = input("Would you like to continue? Enter Y for Yes and N for No")
        if end_choice == 'y' or end_choice == 'Y':
            continue
        else:
            break