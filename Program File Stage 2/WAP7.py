# WAP to create a user defined function named calc() which takes marks as an argument. 
# The function should calculate percentage and grade. Assume MM are 50. 
# The grade will be assigned as per the following table: 
#      >=80..................A 
#        >=60 and <80.......B 
#       <60...........C 

#function to calculate and print output
def calc(marks):
    mm = 50
    perc = (marks / mm)*100
    print(f"Your percentage is {perc}")
    if perc >= 80:
        print(f"You acheived A grade")
    elif perc >= 60:
        print(f"You achieved B grade")
    elif perc < 60:
        print("You achieved C grade")

#taking the input
numEntry = int(input("Enter your marks: "))

#calling the function
calc(numEntry)