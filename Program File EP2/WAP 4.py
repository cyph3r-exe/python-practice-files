#Debangshu  Roy 
# XII - B 
# 40

#WAP to display only those sentences which that start with 
#"The" from the text file hello.txt

#function to add data to the file 
def addData(br):
    F = open("hello.txt", 'a+')
    F.writelines(br)
    F.close()

#function to display all the required data given in the question 
def displayData():
    F = open("hello.txt", 'r+')
    y = F.readlines()
    for i in y:
        j = i.split() #getting words separated
        if j[0] == 'The' or j[0] == 'THE':
            print(i)
        else:
            continue   
    F.close()

#menu 
ch = "Y"
while (ch):
    c = int(input("Choose what you want to do: \n 1 -> Add data to file. \n 2 -> Display final output."))
    if c == 1:
        ab = input("Enter any string you want: ")
        ab = ab + "\n"
        addData(ab)
        ch = input("Do you want to continue ? Y / N: ")
        if ch == "Y" or ch == "y":
            continue
        else:
            displayData()
            break

"""
TEST OUTPUT
Choose what you want to do: 
1 -> Add data to file.
2 -> Display final output.1
Enter any string you want: The sly fox was very sleepy
Do you want to continue ? Y / N: Y
Choose what you want to do: 
1 -> Add data to file.
2 -> Display final output.1
Enter any string you want: The hare was running around the goose. 
Do you want to continue ? Y / N: N
The sly fox was very sleepy
"""