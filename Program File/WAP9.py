#Debangshu Roy 
#WAP to accept 10 numbers from the user and display the sum of only even positive numbers 
#and odd positive numbers 

#Taking Values from the user
num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
num3 = int(input("Enter any number: "))
num4 = int(input("Enter any number: "))
num5 = int(input("Enter any number: "))
num6 = int(input("Enter any number: "))
num7 = int(input("Enter any number: "))
num8 = int(input("Enter any number: "))
num9 = int(input("Enter any number: "))
num10 = int(input("Enter any number: "))

#definging the Class 
class Sumofnumbers:
    #Defining the Function 
    def posSum(self, list):

        #intiating Loop
        pos_even_sum = 0
        pos_odd_sum = 0
        for num in list:
            num = int(num)
            if(num >= 0):
                if(num % 2 == 0):
                    pos_even_sum += num
                else:
                    pos_odd_sum += num
  
        print("Sum of even positive numbers is ",
              pos_even_sum)
  
        print("Sum of odd positive numbers is ",
              pos_odd_sum)

"""
I have used OOP because I could not get any other idea to make this program. 
Please don't scold. 
Sorry
"""
list_num = [num1,  num2, num3, num4, num5, num6, num7, num8, num9, num10]
obj = Sumofnumbers()
obj.posSum(list_num)