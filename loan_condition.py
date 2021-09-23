"""
If the applicant has good income and
has a good credit score then he is 
applicable to apply for a loan. 
"""

#Taking Values of income and credit 

income = float(input("What is your income in Indian Rupee: "))
credit_score = float(input("What is your credit score: "))

#Checking 
if credit_score > 500 and income > 100000:
    
    #Printing according to the values entered by the user
    print('You have are applicable for applying for a loan,')
else:
    print("You are not applicable to apply for a loan. Please try again later.")
