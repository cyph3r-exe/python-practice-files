"""
 Write a user defined function test( fname) where fname is the name of the 
binary file that stores names and phone numbers. The function should accept 
a name and display the corresponding phone number.
"""

import pickle as pc

def test(fname):
    L = input("Enter a name: ")
    try:
        while fname:
            G = pc.load(fname)
            #Assuming data is in [Name, Number] format 
            for i in G:
                if i[0] == L:
                    print(f"Corresponding Number is = {i[1]}")
                else:
                    continue
    except:
        print("File ended")
    fname.close()
