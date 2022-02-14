#Debangshu Roy, Roll Number 39
#To check out the github repo used 
#visit https://github.com/cyph3r-exe/python-practice-files/tree/main/Tkinter
#Made using standard python V-10.2 (As of January 16th)
#and latest Visual Studio code (2022) [bear theme]

#Importing everything in the tkinter library
from tkinter import *
from tkinter import messagebox
from os import *
import random

#initialising window root 
root = Tk()

#Set Title 
root.title("Velocity Bus Booking")

myLabel1 = Label(root, text="⚡⚡⚡⚡Welcome to Velocity Bus Booking⚡⚡⚡⚡", padx=50, pady=20)
myLabel1.pack()

#Number of Passengers label
passengerLabel = Label(root, text="> > > Enter Number of Passengers  ", pady=10)
passengerLabel.pack(anchor = W)

#Number of Passenger Entry point
no_of_travellers = Entry(root,)
no_of_travellers.pack(anchor = W)

#Date of travel label 
dateLabel = Label(root, text="> > > Enter the Date you want to travel: 📅 (DD/MM/YYYY) ",pady=10)
dateLabel.pack(anchor = W)

#date of travel entry point 
dateEntry = Entry(root, )
dateEntry.pack(anchor = W)

#Various Choices made by the user.
passengerNumber = (no_of_travellers.get())
Choice1 = IntVar()
Choice1.set(1)
Choice2 = IntVar()
Choice2.set(1)
Choice3 = IntVar()
Choice3.set(1)
Choice4 = IntVar()
Choice4.set(1)

#Places to visit label 
locationLabel = Label(root, text="> > > Choose a location to visit ")
locationLabel.pack(anchor = W)

#Location list with price 
Location = [
    ("Shimla - Rs. 1715", 1715),
    ("Manali - Rs. 2580", 2680),
    ("Nainital - Rs. 1590", 1590),
    ("Ladakh - Rs. 3085", 3085),
]

#Loop to show the various Radio choice buttons. 
for text, mode in Location:
    Radiobutton(root, text=text, variable=Choice2, value=mode, pady=10).pack(anchor=W)

#List and loop to show the various Radio buttons
BusType = [
    ("Classic - Rs. 500", 500),
    ("Standard - Rs. 750", 750),
    ("Luxury - Rs. 1000", 1000),
    ("VIP - Rs. 2000", 2000),
    ]

#Label for the bus type to be chosen
busLabel = Label(root, text="> > > Choose a bus type to travel in ")
busLabel.pack(anchor = W)

#loop to show the various choices chosen in bustype
for text, mode in BusType:
    Radiobutton(root, text=text, variable=Choice3, value=mode, pady=10).pack(anchor=W)

#Choice for AirConditioning in Bus 
AirCondition = [
    ("AC - Rs. 1000", 1000),
    ("Non-AC - Rs. 0", 0 )
]
#Label for AC or Non AC bus 
acLabel = Label(root, text="> > > Choose AC or Non-AC bus ")
acLabel.pack(anchor = W)

#Loop to show the various choices chosen in AirCondition
for text, mode in AirCondition:
    Radiobutton(root, text=text, variable=Choice4, value=mode, pady=10).pack(anchor=W) 

#Warning window before continuing 
def finalWarning():
    warningResponse = messagebox.askyesno("Caution","Do you really want to continue? ")
    Label(root, text=warningResponse).pack()
    if warningResponse == 1:
        clicked()

#Billing window to show the complete bill
def clicked():
    level1 = Toplevel()
    level1.title("Velocity Billing")
    bill = Label(level1, text="⚡⚡⚡⚡Billing⚡⚡⚡⚡", padx=50, pady=20)
    bill.pack()
    billsecond = Label(level1, text="Thank You for using our Services", padx=50, pady=20)
    billsecond.pack()
    global r1
    global r2
    r1 = random.randint(1, 10)
    r2 = random.randint(2, 20)
    billingIDlabel = Label(level1, text=f"Your Billing ID is: {r1}A{r2}B", pady=5)
    billingIDlabel.pack()
    JourneyDate = Label(level1, text=f"Your Journey Date is: {dateEntry.get()}", pady=5)
    JourneyDate.pack()

    if Choice2.get() == 1715:
        zindagi1 = Label(level1, text="You are travelling to Shimla", pady=5)
        zindagi1.pack()
    elif Choice2.get() == 2680:
        zindagi2 = Label(level1, text="You are travelling to Manali", pady=5)
        zindagi2.pack()
    elif Choice2.get() == 1590:
        zindagi3 = Label(level1, text="You are travelling to Nainital", pady=5)
        zindagi3.pack()
    elif Choice2.get() == 3085:
        zindagi4 = Label(level1, text="You are travelling to Ladakh", pady=5)
        zindagi4.pack()

    if Choice3.get() == 500:
        life1 = Label(level1, text="You are travelling in a Classic bus", pady=5)
        life1.pack()
    elif Choice3.get() == 750:
        life2 = Label(level1, text="You are travelling in a Standard bus", pady=5)
        life2.pack()
    elif Choice3.get() == 1000:
        life3 = Label(level1, text="You are travelling in a Luxury bus", pady=5)
        life3.pack()
    elif Choice3.get() == 2000:
        life4 = Label(level1, text="You are travelling in a VIP bus", pady=5)
        life4.pack()
    
    if Choice4.get() == 1000:
        whylife1 = Label(level1, text=" You are travelling in an AC bus", pady=5)
        whylife1.pack()
    elif Choice4.get() == 0:
        whylife2 = Label(level1, text="You are travelling in a Non AC bus ", pady=5)
        whylife2.pack()
    
    FinalBill = Label(level1, text=f"Your Total Bill is: Rs.{(Choice1.get() + Choice2.get() + Choice3.get() + Choice4.get())}", pady=5)
    FinalBill.pack()
    Finalthankyou = Label(level1, text="Hope you have a safe journey")
    Finalthankyou.pack()
    Contactus = Label(level1, text="Contact us at 👉 contact@velocitybooking.com")
    Contactus.pack()
    payMent = Button(level1, text = "Pay")
    payMent.pack()
    goBackbutton = Button(level1, text = "Go Back", command = level1.destroy)
    goBackbutton.pack()

#Billing button
OutputButton = Button(root, text="Get Bill", command=clicked)
OutputButton.pack()

#Window with multiple inner windows for the admin portal
#Admin portal password window
def adminPassword():
    pwd = Toplevel()
    pwd.title("Access Admin Panel")
    WelcomeAdmin = Label(pwd, text="Welcome Admin1, Please enter password to continue")
    WelcomeAdmin.pack()
    global encryptedpassword
    encryptedpassword = "MohiniArora@z3nith"
    EntryPassword = Entry(pwd,)
    EntryPassword.pack()

    #Main admin panel window after correct password is entered 
    def mainAdminPanel():
        top = Toplevel()
        top.title("Admin Panel")
        adminPanelWelcome = Label(top, text="Welcome to the Admin Panel", pady=30)
        adminPanelWelcome.pack()

        #Window to add the location to the existing list of locations
        def AddLocationFunction():
            lc = Toplevel()
            AddLocationLabel1 = Label(lc, text="Add Location", pady=10)
            AddLocationLabel1.pack()
            LocationName = Entry(lc, )
            LocationName.pack()
            AddLocationLabel2 = Label(lc, text="Enter Location Price", pady=10)
            AddLocationLabel2.pack()
            LocationPrice = Entry(lc,)
            LocationPrice.pack()

            #function to do the backend work and display a warning message
            def FinalAddLocationFunction():
                tl = Toplevel()
                tl.title("Final Call")
                FinalCallforAddLocation = messagebox.askokcancel("Caution","Do you really want to add a new location? ")
                Label(tl, text=FinalCallforAddLocation)
                if FinalCallforAddLocation == 1:
                    Location.append((LocationName.get(), LocationPrice.get()))
                    tl.destroy()
                    lc.destroy()
                else:
                    tl.destroy()
                    lc.destroy()
            
            #Location addition final button 
            AddLocationButton = Button(lc, text = "Add", command = FinalAddLocationFunction)
            AddLocationButton.pack()
        
        #window to do front end and backend of addition of bus class
        def AddClassFunction():
            bc = Toplevel()
            bc.title("Add Class")
            AddClassLabel1 = Label(bc, text = "Add Class Name", pady=10)
            AddClassLabel1.pack()
            ClassName = Entry(bc, )
            ClassName.pack()
            AddClassLabel2 = Label(bc, text = "Add Class Price", pady=10)
            AddClassLabel2.pack()
            ClassPrice = Entry(bc,)
            ClassPrice.pack()

            #final backend 
            def FinalAddClassFunction():
                bb = Toplevel()
                bb.title("Final Call")
                FinalCallforAddClass = messagebox.askokcancel("Caution", "Do you really want to add a new Bus Class? ")
                Label(bb, text=FinalCallforAddClass)
                if FinalCallforAddClass == 1:
                    BusType.append(ClassName.get(), ClassPrice.get())
                    bb.destroy()
                    bc.destroy()
                else:
                    bb.destroy()
                    bc.destroy()
                
                #Addition of class button 
                AddClassButton = Button(bc, text = "Add", command = FinalAddClassFunction)
                AddClassButton.pack()

        #button to open to location addition window 
        AddLocation = Button(top, text = "Add Location", pady=5, command = AddLocationFunction)
        AddLocation.pack()

        #button to open the case addition window 
        AddBusType = Button(top, text = "Add Bus class", pady=5, command = AddClassFunction)
        AddBusType.pack()
        
    #function to start the admin (backend)
    def InsideadminPanel():
        if EntryPassword.get() == encryptedpassword:
            mainAdminPanel()
        else:
            messagebox.showerror("Password was incorrect. Try again!")
    
    #button to open the root admin panel 
    enterPassword = Button(pwd, text = "Login", command = InsideadminPanel)
    enterPassword.pack()

#button to open the root admin panel (password panel)
adminPanelaccessible = Button(root, text="Admin Panel",  command = adminPassword)
adminPanelaccessible.pack()

#completing the window instance and running the above code
root.mainloop() 