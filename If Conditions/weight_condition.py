"""
The user weight and choses to convert the weight 
entered either in Kilos or into Pounds
"""

#Taking the weight from the user. 
weight = float(input("Enter your weight: "))

#Calculating the weight 
KeJee =  float(weight/2.205)

#Calculating the weight in lbs 
ElbeS = float(weight/2.205)

#Asking from convert from where to where 
choice = str(input("Enter [L] for Lbs to Kgs conversion\n Enter [K] for Kgs to Lbs conversion."))

#Checking for L or Kg. 
if choice == ['l', 'L']:
    print("Your converted weight is: ", ElbeS)
elif choice == ['kg', 'KG', 'Kg', 'kG']:
    print("You converted weight is: ", KeJee)

