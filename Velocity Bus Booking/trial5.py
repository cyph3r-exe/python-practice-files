import os 
import csv
from tkinter import *
from tkinter import messagebox

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
        newBus.title('Edit Location')
        H = open("Bustypedata.csv", 'r+')
        H1 = open("temp.csv", "a", newline='')
        re = csv.reader(H)
        wr = csv.writer(H1)

        for op in re:
            if op[0] == modbt.get():
                newBusationLabel = Label(newBus, text="Enter new Location")
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