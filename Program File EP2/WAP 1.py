#Debangshu  Roy 
# XII - B 
# 40

#Write a programe to calculate simple using try and except block

ch = "Y"
#user looping 
while (ch):
    #try block
    try:
        #taking inputs
        x = int(input("Enter the principle amount: "))
        y = int(input("Enter Rate: "))
        z = int(input("Enter time (in years): "))
        calc = x * (y / 100) * z #calculations
        print(f"Your simple interest is: {calc}") #output

        gh = input("Program ended. Would you like to continue? Y / N: ")
        #check for continuation
        if gh == "Y" or gh == "y":
            continue
        else:
            break

    #except block
    except:
        print("Your program encountered an error.\n Press Y to try again. \n Press any other key to exit")
        bh = input("Continue? Y / N: ")
        #check for continuation
        if bh == "Y" or bh == "y":
            continue
        else:
            break  

#TEST OUTPUT 
#Enter the principle amount: 10000
#Enter Rate: 2
#Enter time (in years): 4
#Your simple interest is: 800.0
#Program ended. Would you like to continue? Y / N: Y
#Enter the principle amount: 100000
#Enter Rate: 3
#Enter time (in years): 3
#Your simple interest is: 9000.0
#Program ended. Would you like to continue? Y / N: 