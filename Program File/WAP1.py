#Debangshu Roy 
#WAP to accept Principal Interest, Rate and Time and display the output 

def interest(principle, rate, time):
    calc = int(principle*rate*time)
    calc2 = int(calc/100)
    print("Your total payable interest is ", calc2)

princple = int(input("Enter the value of your principle amount"))
rate = int(input("Enter the value of your rate"))
time = int(input("Enter the value of your time"))

interest(princple, rate, time)