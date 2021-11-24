"""
 WAP to accept item name, price and category. 
 Assign discount ( in percentage) according o the category given in the table.  
 Thereafter display the total amount after subtracting the discount 
 percentage from price of the item. 
 The program should continue as long as user wishes to. 
"""

item = input("Enter the name of item you want to buy: ")
price = int(input("Enter the price: "))
category = int(input("""Enter the number of the category 
you wish to put this in. 
1 -> """))