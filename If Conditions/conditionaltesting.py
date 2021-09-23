"""
This program tests whether the weather is hot 
cold or normal according to the temperature the user 
inputs. 
"""

#Decalring variables 
hot_temp = "The day is hot. \n Drink lots of water"
cold_temp = "The day is cold. \n Use a heater at home"
normal = "The temperature is moderate. \n No need to do anything"
#Asking for temperature 
is_temp = float(input("What is the temperature today? :"))

#User enters temperature

#Code for checking and printing
while is_temp == is_temp:
    if is_temp > 30:
        print(hot_temp)
    elif is_temp < 10:
        print(cold_temp)
    elif is_temp > 11 and is_temp < 29:
        print(normal) 