import csv
import os
from tkinter import *

def modifyLocation():
            modloc = Tk()
            modloc.title('Modify Location')

            G = open("locationdata.csv", "r")
            G1 = open("temp.csv", "w", newline='')
            read = csv.reader(G)
            write = csv.writer(G1)

            for x in read:

                display = Label(modloc, text=f"Location {x[0]} \n Price {x[1]}")
                display.grid(row=0, column=0)

            entermodLocation = Label(modloc, text="Enter Location you want to edit")
            entermodLocation.grid(row=1, column=0)
            entermodLocation_entry = Entry(modloc)
            entermodLocation_entry.grid(row=1, column=1)
            
            def locationmodifyFinal():
                locmod = Tk()
                locmod.title('Edit Location and Price')

                G.seek(0)

                def writingFunction():
                    write.writerow(xyz)
                    locmod.destroy()

                for xyz in read:
                    if xyz[0] == entermodLocation_entry.get():
                        newLoc = Label(locmod, text="Enter New Location: ")
                        newLoc.grid(row=0, column=0)
                        newLoc_entry = Entry(locmod)
                        newLoc_entry.grid(row=0, column=1)
                        newlocPrice = Label(locmod, text="Enter New Price")
                        newlocPrice.grid(row=1, column=0)
                        newlocPrice_entry = Entry(locmod)
                        newlocPrice_entry.grid(row=1, column=1)
                        xyz[0] = newLoc_entry.get()
                        xyz[1] = newlocPrice_entry.get()
                        finaleditButton = Button(locmod, text="Confirm", command=writingFunction)
                        finaleditButton.grid(row=2, column=1)
                
                    else:
                        write.writerow(xyz)
                        continue
                        
                G.close()
                G1.close()
                os.remove("locationdata.csv")
                os.rename("temp.csv", "locationdata.csv")    

            editButton = Button(modloc, text="Edit", command=locationmodifyFinal)
            editButton.grid(row=2, column=1)


modifyLocation()