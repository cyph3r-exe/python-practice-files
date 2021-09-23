"""
The correct number will be 9
The user has 3 attempts to make 
the correct guess.
"""

#Declaring Variables 
correct_guess = 9
guess_number = 0
tries = 3
taken_trials = 3

#Initiating the loop
while guess_number <= tries:
    print("You have", taken_trials," tries")
    Guess = int(input("Guess the number: "))
    guess_number += 1
    taken_trials -= 1
    if Guess == correct_guess:
        print("YOu guessed it correctly")
        break
else:
    print("Sorry you failed")
     