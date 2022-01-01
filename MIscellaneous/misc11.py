a=["paracitamol","surfaz-sn","ondem-md-4","pantaford-dsr","tribs","avomine"]
b=[20,72.57,46.58,89,42,20]
c=[100,25,50,100,60,100]
d={"MEDICINE NAME":a,"PRICE":b,"QUANTITY":c}

print("WELCOME TO THIS MEDICINE MANAGEMENT SOFTWARE ,MADE BY RIDHI SHARMA CLASS XI 'SCIENCE' AFS CHANDAN NAGAR 9BRD PUNE")
while(True):

    print("""
             1=ADD MEDICINE
             2=SELL MEDICINE
             3=DETAILS OF OLD STOCK
             4=DELETE MEDICINE(NOTE:YOU CAN DELETE THOSE MEDICINES THAT ARE EXPIRED OR DAMAGED)
             5=EDIT MEDICINE DETAILS
             6=EXIT
     
    """)
    print( )
    e=int(input("ENTER YOUR CHOICE:"))
    if e==1:
        print("\n                                !!!!BEFORE ADDING THE MEDICINE TO THE STOCK PLEASE CHECK THE EXPIRY DATE OF IT!!!!")
        print( )
        
        f=str(input("ENTER THE MEDICINE NAME:"))
        if f in a:
            print("\n                               !!!!!MEDICINE ALREADY IN THE STOCK!!!!!!")
            z=a.index(f)
            i=str(input("\nDO YOU WANT TO UPDATE THE PRICE AND THE QUANTITY ? ( Y / N ):"))
            if i =="y":
                g=int(input("\nENTER THE PRICE:"))
                h=int(input("ENTER THE QUANTITY:"))
                b[z]=g
                c[z]+=h
                y=str(input("\nDO YOU WANT TO SEE THE DETAILS OF THE UPDATED DETAILS ? ( Y / N ):"))
                print("MEDICINE NAME\tPRICE\tQUANTITY")
                print(".............\t.....\t........")
               
                if y == "y":
                    print( )
                    print(a[z],end="\t")
                    print(b[z],end=
                          "\t")
                    print(c[z], end=" ") 
                else:
                    print("                       \n!!!!!NOT PRINTING THE DETAILS!!!!!")
            else:
                continue
        else:
            g=int(input("\nENTER THE PRICE:"))
            h=int(input("ENTER THE QUANTITY:"))
            a.append(f)
            b.append(g)
            c.append(h)
            g=str(input("\nDO YOU WANT TO SEE THE DETAILS OF THE MEDICINES?( Y / N ):"))
            if g== "y":
                print( )
                print("medicine name:",a[len(a)-1])
                print("price:",b[len(b)-1])
                print("quantity:",c[len(c)-1])
           
            else:
                print("!!!!!\nNOT PRINTING THE DETAILS!!!!!")
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    elif e==2:
        print( )
        i=str(input("ENTER THE MEDICINE NAME:"))
        if i in a:
            print( )
            j=int(input("ENTER THE QUANTITY:"))
            k=a.index(i)
            if (j <=c[k]):
                c[k]-=j

                print("\nMEDICINE IS IN STOCK")
                print("\n                           !!!!BEFORE SELLING THE MEDICINE PLEASE CHECK THE EXPIRY DATE OF THE MEDICINE!!!!")
                print( )
                z=str(input("DO YOU WANT TO PRINT THE RECIEPT?( Y / N ):"))
                if z=="y":
                    print( )
                    print("""
                                    RECEIPT
                                  ...........
                              
                            MEDICINE NAME:""",i)

                    print("                            TOTAL PRICE   :",j*b[k])
                else:
                    continue
                z=str(input("\nDO YOU WANT TO SEE THE DETAILS OF THE SOLD MEDICINE IN THE STOCK? ( Y / N ):"))
                if z=="y":
                    print("\nMEDICINE NAME:",a[k])
                    print("PRICE:",b[k])
                    print("QUANTITY LEFT:",c[k])
                else:
                    print("\n                                          NOT PRINTING THE DETAILS")
            else:

                print("\n                                         THIS NO. OF MEDICINES NOT AVAILABLE")
        else:

            print("\n                                                   MEDICINE NOT AVAILABLE")
            print("\n                                    !!!!PLEASE ADD THE MEDICINE TO THE STOCK FIRST!!!!")
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    elif e==3:
        print( )
        print("MEDICINE NAME\tPRICE\tQUANTITY")
        print(".............\t.....\t........")
        print( )
        for k in range(len(a)):
            print(a[k],end="\t")
            print(b[k],end="\t")
            print(c[k])
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    elif e==4:
        print( )
        f=str(input("ENTER MEDICINE NAME:"))
        if f in a:
            i=a.index(f)
            print( )
            g=int(input("ENTER THE QUANTITY YOU WANT TO MINUS:"))
            if g <=c[i]:
                c[i]-=g
                print("\n                                  EDITED SUCCESFULLY")
                print( )    
                print("\nMEDICINE NAME:",a[i])
                print("QUANTITY LEFT:",c[i])
            else:
                print("\n                  !!!!!THIS NO. OF MEDICINE IS NOT AVAILABLE IN THE STOCK!!!!!")
        else:
            print( )
            print("                                     !!!!!ENTERED MEDICINE IS NOT IN THE STOCK!!!!!")
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    elif e==5:
        print( )
        g=str(input("MEDICINE NAME:"))
        if g in a:
            i=a.index(g)
            print("""\nYOU WANT TO EDIT
                    1==PRICE
                    2==QUANTITY
                    """)
            print( )
            f=int(input("ENTER YOUR CHOICE:"))
            if(f==1):
                h=int(input("\nENTER THE NEW PRICE:"))
                b[i]=h
                print( )
                print("                                             UPDATED SUCCESFULLY")
                z=str(input("DO YOU WANT TO SEE THE DETAILS OF EDITED MEDICINE ? ( Y / N ):"))
                if z=="y":
                    print("\nMEDICINE NAME:",a[i])
                    print("NEW PRICE:",b[i])
                else:
                    print("                             \n !!!!! NOT PRINTING THE DETAILS !!!!!")
            elif f==2:
                print( )
                print("""
                            1=INCREASE QUANTITY
                            2=DECREASE QUANTITY
                            """)
                p=int(input("ENTER YOUR CHOICE:"))
                if p==1:
                    print( )
                    h=int(input("ENTER THE INCREMENT IN THE QUANTITY:"))
                    c[i]+=h
                    print( )
                    print("                                             UPDATED SUCCESFULLY")
                else:
                    i=a.index(g)
                    print( )
                    h=int(input("ENTER THE DECREMENT IN THE QUANTITY:"))
                    if h<=c[i]:
                        c[i]-=h
                        print( )
                        print("                                             UPDATED SUCCESFULLY")
                    else:
                        print("\n                     !!!!!THIS NO. OF MEDICINE IS NOT AVAILABLE IN THE STOCK!!!!!")
                z=str(input("DO YOU WANT TO SEE THE DETAILS OF THE EDITED MEDICINE ? ( Y / N ):"))
                if z=="y":
                    print("\nMEDICINE NAME:",a[i])
                    print("NEW QUANTITY:",c[i])
                else:
                    print("                                  !!!!! NOT PRINTING THE DETAILS!!!!!") 
        else:
            print( )
            print("                                      !!!!!MEDICINE NOT IN THE STOCK!!!!!")
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    elif e==6:
        print( )
        print("THANK YOU FOR USING THIS SOFTWARE") 
        break
    print( )
