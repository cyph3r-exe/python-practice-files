"""
Write a program that creates a GK quiz consisting 
of any five questions of your choice. The questions 
should be displayed randomly. Create a user defined 
function score() to calculate the score of the quiz and 
another user defined function remark (scorevalue) 
that accepts the final score to display remarks as 
follows:

5 Outstanding
4 Excellent
3 Good
2 Read more to score more
1 Needs to take interest
0 General knowledge will always help you. Take it seriously.
"""

import random

#function containing question 1
def question1():

    x = int(input("""Q) Who is the father of our nation? 
    1) Dr. Rajendra Prasad
    2) Mahatma Gandhi
    3) Jawaharlal Nehru
    4) Netaji Subhash Chandra Bose
    Enter your answer number here: """))
    return x

#function containing question 2
def question2():
    x = int(input(""" Q) Gidda is the fold dance of which indian state? 
    1) Assam
    2) Punjab
    3) Kerela
    4) Gujurat
    Enter your answer number here: """))
    return x  

#function containing question 3
def question3():
    x = int(input("""Q) Who invented the telephone? 
    1) Alexander Graham Bell 
    2) Alexander The Great 
    3) Alexander Fleming
    4) Johannes Gutenberg
    Enter your answer number here: 
    """))

#function containing question 4
def question4():
    x = int(input("""What is the largest moon of the saturn
    1) Titan
    2) Neptune
    3) Jupiter
    4) Nebula 
    Enter your answer number here: 
    """))

#function containing question 5
def question5():
    x = int(input("""Q) Who invented the computer? 
    1) Alexander Graham Bell
    2) Mahatma Gandhi
    3) Johannes Gutenberg
    4) Charles Babbage
    Enter your answer number here:
    """))

index = 0
starter = input("Would you like to start the quiz? Enter Y for Yes, and N for No")
if starter == 'y' or starter == 'Y':
    print("Lets get started. Here is your first question.")
    
    #intitiating while loop
    while random < 6:
        random = random.randrange(1, 5)
        if random == 1:
            answer = question1()
            if answer == 2:
                index += 1
            else:
                continue
        elif random == 2:
            answer = question2()
            if answer == 3:
                index += 1
            else:
                continue
        elif random == 3:
            answer = question3()
            if answer == 1:
                index += 1
            else:
                continue
        elif random == 4:
            answer = question4()
            if answer == 1:
                index += 1
            else:
                continue
        elif random == 5:
            answer = question5()
            if answer == 2:
                index += 1
            else:
                continue
            