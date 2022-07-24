#Debangshu Roy and Hemang Vats 
#Velocity bus booking (Front end [GUI]). Refer to X link 
#for discord interface and commands. 
#The Database is centralised and the whole app is based oon the idea 
#of being decentralised and transparent

#importing required modules
import os
import csv
from tkinter import *
from tkinter import messagebox

#MainBookingPageData

def MainBookingPage():
    root= Tk()
    root.title('VBB Booking')
    root.geometry("800x500")

    F = open("userdata.csv", "r")
    read = list(csv.reader(F))

    F1 = open("locationdata.csv", "r")
    rdr = list(csv.reader(F1))

    F2 = open("Bustypedata.csv", "r")
    ddr = list(csv.reader(F2))

    for i in read:
        if w == i[3]:
            welcome_label = Label(root, text=f"Welcome {i[0]} {i[1]}", font=("Helvetica", 30, "bold", "italic"), fg="#ffc800", bg="#000000")
            welcome_label.pack()
            
            #varaibles
            x = 1
            z = 1

            for i in rdr:
                loc_label = Label(root, text=f"Location - {i[0]} : Price {i[1]} Choice Number: {x}")
                loc_label.pack()
                x += 1

            locbookinglabel = Label(root, text="Enter any one choice number: ")
            locbookinglabel.pack()
            bookingchoice = Entry(root)
            bookingchoice.pack()
            
            for y in ddr:
                bt_label = Label(root, text=f"Bus Type = {y[0]} : Price  = {y[1]} : Choice Number: {z} ")
                bt_label.pack()
                z += 1

            btannounce = Label(root, text="Enter any one choice number")
            btannounce.pack()
            bt_entry = Entry(root)
            bt_entry.pack()

            travelnum = Label(root, text="Number of people travelling (In Numbericals)" )
            travelnum.pack()
            travelnumEntry = Entry(root)
            travelnumEntry.pack()

            def BillWindow():
                bw = Tk()
                bw.title('Billing Window')
                bw.geometry("800x500")

                #backend calculation
                awc = bookingchoice.get()
                _cAWC = int(awc)
                rdrcwc = (rdr[_cAWC])
                bwc = bt_entry.get()
                _bWC = int(bwc)
                ddrbwc = (ddr[_bWC])
                cwc = travelnumEntry.get()
                _cCWC = int(cwc)
                print(cwc)
                print(type(rdrcwc[1]))
                tolSum = ((int(rdrcwc[1]))+(int(ddrbwc[1])))*(_cCWC)
                print(tolSum)

                ChoiceLabel1 = Label(bw, text="Your choice is as follows: \n")
                ChoiceLabel1.pack()
                bwLocationLabel = Label(bw, text=f"Location: {rdrcwc[0]}")
                bwLocationLabel.pack()
                bwBt = Label(bw, text=f"Bus Choice:  {ddrbwc[0]}")
                bwBt.pack()
                no_ofPeople_travelling = Label(bw, text=f"Number of people travelling {_cCWC}")
                no_ofPeople_travelling.pack()
                bwPriceLabel = Label(bw, text=f"Total Price: {tolSum}")
                bwPriceLabel.pack()

            confirmButton = Button(root, text="Confirm and Proceed", command=BillWindow)
            confirmButton.pack()

def adminSelectionPage():
    add = Tk()
    add.title('Admin Selection Page')
    add.geometry("800x500")

    def additionSelection():
        addition = Tk()
        addition.title('Choose To Add')
        #location
        def addLocationScreen():
            loc = Tk()
            loc.title('Add Location')
            loc.geometry("800x500")

            addLocationLabel = Label(loc, text="Add Any Location")
            addLocationLabel.grid(row=0, column=0)
            addLocationEntry = Entry(loc)
            addLocationEntry.grid(row=0, column=1)

            addpriceLabel = Label(loc, text="Add a price. ")
            addpriceLabel.grid(row=1, column=0)
            addpriceEntry = Entry(loc)
            addpriceEntry.grid(row=1, column=1)    

            def finalAddconfirmation():
                F = open("locationdata.csv", "a", newline='')
                write = csv.writer(F)
                L = [addLocationEntry.get(), addpriceEntry.get()]
                write.writerow(L)
                F.close()

            finalAddButton = Button(loc, text="Add", command=finalAddconfirmation)
            finalAddButton.grid(row=2, column=1)
             
        #location button 
        locationButton = Button(addition, text="Add Location", command=addLocationScreen)
        locationButton.grid(row=0, column=0)

        #bustype
        def addBustypeScreen():
            bus = Tk()
            bus.title('Admin Selection Page')
            bus.geometry("800x500")

            addBustypeLabel = Label(bus, text="Add Any Bus type")
            addBustypeLabel.grid(row=0, column=0)
            addBustypeEntry = Entry(bus)
            addBustypeEntry.grid(row=0, column=1)

            addpriceLabel = Label(bus, text="Add a price")
            addpriceLabel.grid(row=1, column=0)
            addpriceEntry = Entry(bus)
            addpriceEntry.grid(row=1, column=1)    

            def finaladdition():
                F = open("Bustypedata.csv", "a", newline='')
                write = csv.writer(F)
                L = [addBustypeEntry.get(), addpriceEntry.get()]
                write.writerow(L)
                F.close()
                
            finalAddButton = Button(bus, text="Add", command=finaladdition)
            finalAddButton.grid(row=2, column=1)

        #bustype button 
        bustypeButton = Button(addition, text="Add Bus Type", command=addBustypeScreen)
        bustypeButton.grid(row=1, column=0)

    def modification():
        #location edit
        def modifyLocation():
            modloc = Tk()
            modloc.title('Modify Location')

            G = open("locationdata.csv", "r")
            read = csv.reader(G)

            for z in read:
                locationLabel = Label(modloc, text=f"Location {z[0]} Price {z[1]}")
                locationLabel.pack()
            
            modLocationLabel = Label(modloc, text="Which one do you wish to edit.")
            modLocationLabel.pack()
            modLocation = Entry(modloc)
            modLocation.pack()
            G.close()
            
            def finalLocationEdit():
                newLoc = Tk()
                newLoc.title('Edit Location')
                F = open("locationdata.csv", 'r+')
                F1 = open("temp.csv", "a", newline='')
                re = csv.reader(F)
                wr = csv.writer(F1)

                for x in re:
                    if x[0] == modLocation.get():
                        newLocationLabel = Label(newLoc, text="Enter new Location")
                        newLocationLabel.grid(row=0, column=0)
                        newLocationEntry = Entry(newLoc)
                        newLocationEntry.grid(row=0, column=1)
                        newLocationPrice = Label(newLoc, text="Enter new price ")
                        newLocationPrice.grid(row=1, column=0)
                        newLocationpriceEntry = Entry(newLoc)
                        newLocationpriceEntry.grid(row=1, column=1)

                        def locationBackendFinal():
                            x[0] = newLocationEntry.get()
                            x[1] = newLocationpriceEntry.get()
                            wr.writerow(x)
                            messagebox.showinfo("Edited", "The modification is successful")
                            modloc.destroy()
                            newLoc.destroy()
                            mod.destroy()
                            F.close()
                            F1.close()
                            os.remove("locationdata.csv")
                            os.rename("temp.csv", "locationdata.csv")        

                        finalMod = Button(newLoc, text="Confirm Edit", command=locationBackendFinal)
                        finalMod.grid(row=2, column=1)

                    else:
                        wr.writerow(x)
                        continue           
                        
            modlocButton = Button(modloc, text="Edit", command=finalLocationEdit)
            modlocButton.pack()
        def modifyBus():
            modbt = Tk()
            modbt.title('Modify Location')

            G = open("locationdata.csv", "r")
            read = csv.reader(G)

            for z in read:
                locationLabel = Label(modbt, text=f"Location {z[0]} Price {z[1]}")
                locationLabel.pack()
            
            modbtLabel = Label(modbt, text="Which one do you wish to edit.")
            modbtLabel.pack()
            modbt = Entry(modbt)
            modbt.pack()
            G.close()
            def finalbusEdit():
                newBus = Tk()
                newBus.title('Edit Bus Type')
                H = open("Bustypedata.csv", 'r+')
                H1 = open("temp.csv", "a", newline='')
                re = csv.reader(H)
                wr = csv.writer(H1)

                for op in re:
                    if op[0] == modbt.get():
                        newBusationLabel = Label(newBus, text="Enter new Bus Type")
                        newBusationLabel.grid(row=0, column=0)
                        newBusationEntry = Entry(newBus)
                        newBusationEntry.grid(row=0, column=1)
                        newBusationPrice = Label(newBus, text="Enter new price ")
                        newBusationPrice.grid(row=1, column=0)
                        newBusationpriceEntry = Entry(newBus)
                        newBusationpriceEntry.grid(row=1, column=1)

                        def busBackendFinal():
                            op[0] = newBusationEntry.get()
                            op[1] = newBusationpriceEntry.get()
                            wr.writerow(op)
                            messagebox.showinfo("Edited", "The modification is successful")
                            modbt.destroy()
                            newBus.destroy()
                            H.close()
                            H1.close()
                            os.remove("Bustypedata.csv")
                            os.rename("temp.csv", "Bustypedata.csv")        
                        finalMod = Button(newBus, text="Confirm Edit", command=busBackendFinal)
                        finalMod.grid(row=2, column=1)

                    else:
                        wr.writerow(op)
                        continue           
                        
            modbusButton = Button(modbt, text="Edit", command=finalbusEdit)
            modbusButton.pack()

        mod = Tk()
        mod.title('Choose Modication')

        modButton1 = Button(mod, text="Modify Location and Price", command=modifyLocation)
        modButton1.grid(row=0, column=0)
        modButton2 = Button(mod, text="Modify Bustype", command=modifyBus)
        modButton2.grid(row=0, column=1)


    additionButton = Button(add, text="Add",width=20, bg="#000000", fg="#ff0000", command=additionSelection)
    additionButton.grid(row=0, column=0)
    modificationButton = Button(add, text="Modify", width=20, bg="#000000", fg="#ff0000", command=modification)
    modificationButton.grid(row=0, column=1)
    deletionButton = Button(add, text="Delete", width=20, bg="#000000", fg="#ff0000")
    deletionButton.grid(row=0, column=2)

def AdminPanelLogin():
    root = Tk()
    root.title('Admin Login')
    root.geometry("800x500")

    admin_password = Label(root, text="Enter your Password", show="*")
    admin_password.grid(row=1,column=0)
    admin_password_entry = Entry(root)
    admin_password_entry.grid(row=1, column=1)
    
    def adminPassword():
        password = "Hem@ng&cyph3r"
        if admin_password_entry.get() == password:
            adminSelectionPage()
            

    conf_button = Button(root, text="Login as Admin", command=adminPassword)
    conf_button.grid(row=2, column=1)   

#csv userdata = [Firstname, Second Name, Email, Username, User password]



def SignInScreen():
    root = Tk()
    root.title('VBB Sign_In')
    root.geometry("800x500")
    
    name_label = Label(root, text="Enter your First name: ")
    name_label.grid(row=0, column=0)
    name_label_entry = Entry(root)
    name_label_entry.grid(row=0, column=1)

    secondname = Label(root, text="Enter your Second name: ")
    secondname.grid(row=1,column=0)
    secondname_entry = Entry(root)
    secondname_entry.grid(row=1, column=1)
    
    email = Label(root, text="Enter your Email: ")
    email.grid(row=2,column=0)
    email_entry = Entry(root)
    email_entry.grid(row=2, column=1)

    username = Label(root, text="Enter your username: ")
    username.grid(row=3, column=0)
    username_entry = Entry(root)
    username_entry.grid(row=3, column=1)

    userpassword = Label(root, text="Enter your password: ", show="*")
    userpassword.grid(row=4, column=0)
    userpassword_entry = Entry(root)
    userpassword_entry.grid(row=4, column=1)

    passwordconf = Label(root, text="Confirm your password: ",show="*")
    passwordconf.grid(row=5, column=0)
    passwordconf_entry = Entry(root)
    passwordconf_entry.grid(row=5, column=1)

    def passwordchecker():
            a = userpassword_entry.get()
            b = passwordconf_entry.get()
            
            if a == b:
                F = open("userdata.csv", "a", newline='')
                write = csv.writer(F)
                L = [name_label_entry.get(), secondname_entry.get(), email_entry.get(), username_entry.get(), userpassword_entry.get()]
                write.writerow(L)
                MainBookingPage()
            else:
                print("nhk")
                return

    sign_buttom = Button(root, text="Sign up", command=passwordchecker)
    sign_buttom.grid(row=6, column=1)

#command=addtodata(user_name, user_password_entry)

def FirstScreen():
    main = Tk()
    main.title('VBB Home')
    main.geometry("800x500")

    def LoginScreen():
        Tk.destroy(main)
        root = Tk()
        root.title('VBB User Login')
        root.geometry("800x500")
    
        user_name_label = Label(root, text="Enter your username: ")
        user_name_label.grid(row=0, column=0)
        user_name = Entry(root)
        user_name.grid(row=0, column=1)

        user_password = Label(root, text="Enter your Password")
        user_password.grid(row=1,column=0)
        user_password_entry = Entry(root)
        user_password_entry.grid(row=1, column=1)

        def LoginTrial():
            F = open("userdata.csv", "r")
            read = csv.reader(F)
            global w
            w = user_name.get()
            global t
            t = user_password_entry.get()
            for x in read:
                if x[3] == w and x[4] == t:
                    MainBookingPage()
                    break
                else:
                    continue       

        login_button = Button(root, text="Login", command=LoginTrial)
        login_button.grid(row=2, column=1)

    #defining image
    bg = PhotoImage(file="trial.png")
    my_label = Label(main, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    #labels 
    FirstLabel = Label(main, text="Welcome to Velocity Bus Booking", font=("Helvetica", 30, "italic"), fg="#ffc800", bg="#000000")
    FirstLabel.pack()

    Secondlabel = Label(main, text="Please select", font=("Helvetica", 20, "italic"), fg="#ffc800", bg="#000000")
    Secondlabel.pack()

    #defnining buttons frame
    buttons_frame = Frame(main, bg="#000000")
    buttons_frame.pack(pady=10)

    #buttons
    AdminButton = Button(buttons_frame, text="Admin Panel", command=AdminPanelLogin)
    AdminButton.grid(row=0, column=0, padx=20)

    CustomerLoginButton = Button(buttons_frame, text="Customer Login", command=LoginScreen)
    CustomerLoginButton.grid(row=0, column=1, padx=20)

    CustomerSignInButton = Button(buttons_frame, text="Customer Sign-Up", command=SignInScreen)
    CustomerSignInButton.grid(row=0, column=2, padx=20)

    #running 
    main.mainloop()

FirstScreen()