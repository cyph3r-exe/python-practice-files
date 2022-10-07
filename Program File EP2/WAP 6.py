#Debangshu  Roy 
# XII - B 
# 40

import pickle
import os
def add(s):
    F=open("A.dat",'ab')
    pickle.dump(s,F)
    F.close()
def display():
    try:
        F=open("A.dat",'rb')
        while F:
            real=pickle.load(F)
            op=real.values()
            m=list(op)
            print()
            print("B.Id-",m[0],"\nArrival-",m[1],"\nDestination-",m[2],"\nDate of journey-",m[3],"\nFare-",m[4])
    except:
        print("Done")
def dis(k):
    try:
        F=open("A.dat",'rb')
        while F:
            real=pickle.load(F)
            o=real.values()
            m=list(o)
            if real["B.Id"]==k:
                print("B.Id-",m[0],"\nArrival-",m[1],"\nDestination-",m[2],"\nDate of journey-",m[3],"\nFare-",m[4])
    except:
        print()
        print("Done")
    F.close()
def dele(k):
    try:
        F=open("A.dat",'rb')
        F1=open("B.dat",'wb')
        while F:
            c=pickle.load(F)
            if c["B.Id"]==k:
                continue
            else:
                pickle.dump(c,F1)
    except:
        print("All done")
    F.close()
    F1.close()
    os.remove("A.dat")
    os.rename("B.dat","A.dat")
def modify(k):
    try:
        F=open("A.dat",'rb')
        F1=open("B.dat",'wb')
        while F:
            c=pickle.load(F)
            if c["B.Id"]==k:
                r=k
                t=input("Enter new Arrival: ")
                y=input("Enter new Destination: ")
                u=input("Enter new date of journey: ")
                i=float(input("Enter Fare: "))
                dic["B.Id"]=r
                dic["Arrival"]=t
                dic["Destination"]=y
                dic["DOJ"]=u
                dic["Fare"]=i
                pickle.dump(dic,F1)
            else:
                pickle.dump(c,F1)
    except:
        print("All done")
    F.close()
    F1.close()
    os.remove("A.dat")
    os.rename("B.dat","A.dat")
d={1:"1.Add",2:"2.Modify",3:"3.Delete",4:"4.Display"}
dic={}
b="yes"
while b=="yes":
    for x in d:
        print(d[x])
    print()
    choice1=input("Choose from above menu: ")
    if choice1=="1":
        print()
        r=int(input("Enter ID: "))
        t=input("Enter Arrival: ")
        y=input("Enter Destination: ")
        u=input("Enter date of journey: ")
        i=float(input("Enter Fare: "))
        dic["B.Id"]=r
        dic["Arrival"]=t
        dic["Destination"]=y
        dic["DOJ"]=u
        dic["Fare"]=i
        add(dic)
    if choice1=="2":
        print()
        k=int(input("Enter ID of the data: "))
        modify(k)
    if choice1=="3":
        print()
        k=int(input("Enter ID of the data: "))
        dele(k)
    if choice1=="4":
        print()
        print("1.Selective display\n2.Complete display")
        print()
        z=int(input("Choose:  "))
        print()
        if z==1:
            k=int(input("Enter of the record you want to see: "))
            dis(k)
        if z==2:
            display()
    print()
    b=input("Do you want to continue: ")
    if b=="yes":
        continue
    else:
        break

"""
TEST OUTPUT
1.Add
2.Modify
3.Delete
4.Display

Choose from above menu: 1

Enter ID: 12
Enter Arrival: kal
Enter Destination: parso
Enter date of journey: 202002020
Enter Fare: 4500

Do you want to continue: y

1.Add
2.Modify
3.Delete
4.Display

Choose from above menu: 1

Enter ID: 24
Enter Arrival: Aaj
Enter Destination: tarso
Enter date of journey: 09384230
Enter Fare: 60000

1.Add
2.Modify
3.Delete
4.Display

Choose from above menu: 2

Enter ID of the data: 24
Enter new Arrival: Mum
Enter new Destination: Dad
Enter new date of journey: 202002
Enter Fare: 50000
All done

Do you want to continue: yes
1.Add
2.Modify
3.Delete
4.Display
"""