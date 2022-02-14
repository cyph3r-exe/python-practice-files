# ANIRUDH PRATAP SINGH
# 11-B
# AIR FORCE GOLDEN JUBILLE INSTITUTE
# 
from datetime import datetime

print( "                          WELCOME TO SAPNA BEAUTY PARLOUR                         ")
print("For online booking for your seat complete you registration by")
Name= input("Enter your name :  ")
Phone = int(input("Enter your Phone no. :  "))
BookingDate=(input("Enter Date DD/MM/YYYY : "))
BookingTime  = (input("Enter time : "))
print("Registration Complete")
print()
print("This is our menu")

print("*****************************************************************************************************************")
def menu():
    print("                      MENU")
    print()
    print("                      1. Rate Chart")
    print("                      2. Bill")
    print("                      3. EDIT-Generate New Bill")
    print("                      4. Exit SAPNA BEAUTY PARLOUR")
    print("************************************************************************************************************")
    
choice=1
while choice>=1:
    menu()
    choice = int(input("Enter your choice : "))
    sum=0
    Total=0
    D={"Eyerows":100, "Fore Head": 200, "Upper Lips": 100, "Full Face" : 800 , "                                                                .":".", "Normal Manicure":200,"Spa Manicure": 200, "Polishing Manicure": 250,"                                                            .":".", "Boy Cut":150, "V Cut": 125, "U Cut": 120, "Ironing":80,"                                                                             .":".", "Full Arms":100, "Half Arms": 100, "Full Legs": 100, "Half Legs" : 100 ,"Under Arms":100, "Full Body":1000,"                                      .":".", "Herbal":300, "Fruit": 400, "Gold": 450,  "Insta Glow" : 600 ,"                                                                            .":".", "Head Massage":300, "Foot Massage": 400, "Full Body Massage": 3000,"                                                              . ":".", "Normal Pedicure":200,"Spa Pedicure": 200, "Polishing Pedicure": 250,"                                                           .":".", "Light Makeup":800, "Party Makeup": 1200, "Bridal Makeup": 2000,}
    list = (D.keys())
    if choice == 1:
        print("           THREADING                           HAIR CUT                      ")
        print(" Eyerows              100/-          Boy Cut              150/-")
        print(" Fore Head            200/-          U Cut                120/-")                                 
        print(" Upper Lips           100/-          V Cut                125/-")
        print(" Full Face            800/-          Ironing              80/-",end= '\n')
        print()
        print("           WAXING                              FACIAL                       ")                           
        print(" Full Arms            100/-          Herbal               300/-")
        print(" Half Arms            100/-          Fruit                400/-")
        print(" Full Legs            100/-          Gold                 450/-")
        print(" Half Legs            100/-          Insta Glow           600/-")
        print(" Under Arms           100/-")        
        print(" Full Body            1000/-",end= '\n') 
        print()
        print("           MANI CURE                            PEDI CURE                     ")
        print(" Normal Manicure      200/-          Normal Pedicure      200/-")
        print(" Spa Manicure         200/-          Spa Pedicure         200/-")
        print(" Polishing Manicure   250/-          Polishing Pedicure   250/-",end= '\n')
        print()
        print("           BODY SPA                             MAKE UP                       ")                                                                   
        print(" Head Massage         300/-          Light Makeup         800/-")
        print(" Foot Massage         400/-          Party Makeup         1200/-")
        print(" Full Body Massage    3000/-         Bridal Makeup        2000/-",end= '\n')
        print()
        print("           MEHANDI")
        print(" Depends on Designs (But not included in bill)",end= '\n\n\n')
    elif choice == 2:
        while True:
            print()
            order = input("Enter your order / type 'Exit' if you are done : ")
            #print("Cost is",D[order])
            if order in list:
                sum= sum + D[order]
                GST= sum*18/100
                Total =sum + GST
            elif order =="Exit":
                break
            else:
                print("Enter right item")
            print("Your Bill is ",sum,"/-")
            
        print("***********************************************************************************************************")    
        print("                                    Sapna Beauty Parlour              ")
        print("                                                         ",datetime.now())
        print("         Booking Date-:",BookingDate)                           
        print("         Booking Time-:",BookingTime)
        print("         Customer name:",Name)
        print("         Customer Mobile No.:",Phone)                                    
        print(         )
        print()
        print("                  Your Total Bill is ",sum,"/-")
        print("                            GST 18%: ",GST)
        print("             Total Amount to be paid ",Total,"/-")
        print()
        print()
        print("                                   Thank You For Visiting Us")
        print("***********************************************************************************************************")
            
    elif choice == 3:
        while True:
            print()
            order = input("Enter your order : ")
            if order in list:
                sum= sum + D[order]
            elif order =="Exit":
                break
            else:
                print("Enter right item")
            print("Your Bill is ",sum,"/-")

        print("***********************************************************************************************************")    
        print("                                    Sapna Beauty Parlour              ")
        print("                                                         ",datetime.now())
        print("         Booking Date-:",BookingDate)                           
        print("         Booking Time-:",BookingTime)
        print("         Customer name:",Name)
        print("         Customer Mobile No.:",Phone)                                    
        print(         )
        print()
        print("                  Your Total Bill is ",sum,"/-")
        print("                            GST 18%: ",GST)
        print("             Total Amount to be paid ",Total,"/-")
        print()
        print()
        print("                                   Thank You For Visiting Us")
        print("***********************************************************************************************************")
            
    elif choice == 4:
        break