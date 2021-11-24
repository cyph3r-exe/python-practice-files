"""
 WAP to accept item name, price and category. 
 Assign discount ( in percentage) according o the category given in the table.  
 Thereafter display the total amount after subtracting the discount 
 percentage from price of the item. 
 The program should continue as long as user wishes to. 
"""

while x == 1:
    item = input("Enter the name of item you want to buy: ")
    price = int(input("Enter the price: "))
    category = int(input("""Enter the number of the category 
    you wish to put this in. 
    1 -> Electronics
    2 -> Kitchen 
    3 -> Furniture"""))

    if category == 1: 
        discprice = price - ((5/100) * price)
        print(f"The disocounted price for your {item} is {discprice}")
    elif category == 2:
        discprice = price - ((10/100) * price)
        print(f"The disocounted price for your {item} is {discprice}")
    elif category == 3:
        discprice = price - ((5/100) * price)
        print(f"The disocounted price for your {item} is {discprice}")
    else:
        print("Thank you for using our service")
        x = input("Enter 1 if you would like to continue, or enter any other button to exit: ")
        if x == 1:
            continue
        else:
            break   