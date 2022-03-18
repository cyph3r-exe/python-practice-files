#Wap to check whether number when divided by two is odd or even 

#count variable
c = 1
while c > 0 and c < 10000:
    #taking inputs
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    #defining the function
    def main(a, b):
        try:
            global c
            c = a // b 
            if c % 2 == 0:
                print(c)
                c = c - c 
            else:
                print("The number obtained is Odd")
                break 
                #another method to close the loop - c = c - c 
        except ZeroDivisionError:
            print("Please try again")

main(a, b)
        
        
