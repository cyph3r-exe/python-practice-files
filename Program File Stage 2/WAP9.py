#WAP to accept the following data in a dictionary: 
#Item_Name, CP, SP 
#Displaying 
#Item_Name, Profit or Loss 
#The program should continue as long as the user wishes to. 

itemInt = int(input("Enter number of items to be stored: "))
x = "y" 
shopping = dict()

while x == "y" or x == "Y":
    Item_name = input("Enter the Item Name: ")
    cp = int(input("Enter the Cost Price: "))
    sp = int(input("Enter the Selling price: "))
    shopping[Item_name] = [cp, sp, sp-cp]
    print("\n\nITEM_NAME\tCOST_PRICE\tSELLING_PRICE\tPROFIT_or_LOSS")

    for k in shopping:
        print(k,'\t\t', shopping[k])
    
    UserChoice = str(input("Would you like to continue?: Y or N"))
    if UserChoice == "y" or UserChoice == "Y":
        continue
    else:
        break



