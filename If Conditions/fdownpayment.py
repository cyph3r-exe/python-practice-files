"""
This code here should print out the down payment 
of a house based on the credit score os a user. 
"""

#Declaring variables and taking in values and inputs from the user. 
credit_score  = float(input("Please enter your credit score : ")) #Taking Credit Score 
dollar_sign, price_of_house = '$', 1000000

#Calculations done to get the value credit score 

#Good Credit score calculation 
bad_credit = (price_of_house/100)*30
bad_downpayment = bad_credit

#Bad credit score calculation 
good_credit = (price_of_house/100)*20
good_downpayment = good_credit

#Final Printing 
if credit_score > 500:
    print("Your credit score is good. \nThe downpayment you need to pay is ", dollar_sign, good_downpayment)
else:
    print("Your credit score is a bit on the lesser side.\nYour downpayment will be", dollar_sign, bad_downpayment)