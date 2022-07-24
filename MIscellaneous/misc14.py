# Hemang Vats , XII-A , to display,add,delete and modify the data from a csv file using list
import csv
import os

def menu():
    print("""Please select your action
1. ADD
2. MODIFY
3. DELETE
4. DISPLAY
5. EXIT""")
def add():
    f=open('data.csv','a',newline='')
    l=[]
    try:
        Id=int(input('Enter patient id:'))
        l.append(Id)
        name=input("Enter patient's name:")
        l.append(name)
        dot=input('Enter date of test:')
        l.append(dot)
        result=input('Enter result of RTPCR test:')
        l.append(result)
        c=csv.writer(f)
        c.writerow(l)
    except:
        print('Enter valid values')
    finally:
        f.close()
def display():
    f=open('data.csv','r',newline='')
    r=csv.reader(f)
    for x in r:
        for y in x:
            print(y)
        print()
    f.close()
def selective(pid):
    f=open('data.csv','r',newline='')
    r=csv.reader(f)
    for x in r:
        if x[0] == pid:
            for y in x:
                print(y)
        else:
            continue
    f.close()
def delete(pid):
    f=open('data.csv','r',newline='')
    f1=open('temp2.csv','w',newline='')
    r=csv.reader(f)
    c=csv.writer(f1)
    for x in r:
        if pid in x:
            continue
        else:
            c.writerow(x)
    f.close()
    f1.close()
    os.remove('data.csv')
    os.rename('temp2.csv','data.csv')
def modify(pid,old):
    f=open('data.csv','r',newline='')
    f1=open('temp2.csv','w',newline='')
    r=csv.reader(f)
    c=csv.writer(f1)
    for x in r:
        if pid in x:
            if old==2:
                name=input("Enter new patient's name:")
                x[1]=name
            elif old==3:
                dot=input('Enter new date of test:')
                x[2]=dot
            else:
                result=input('Enter new result of RTPCR test:')
                x[3]=result
                c.writerow(x)
        else:
            c.writerow(x)
    f.close()
    f1.close()
    os.remove('data.csv')
    os.rename('temp2.csv','data.csv')
x='yes'
while x=='yes':
    menu()
    no=int(input('Enter your choice by entering the number:'))
    if no==1:
        add()
        print('The data is added')
        continue
    elif no==2:
        try:
            pid=int(input('Enter the patient id for which you need to edit the data:'))
            print("""1. Patient's ID
2. Patient's Name
3. Date Of Test
4. Result Of RTPCR Test""")
            old=int(input('Enter the number of the data you want to edit:'))
        except:
            x='Enter valid values'
        if (old>5) and (old<1):
            print('Enter valid choice')
            continue
        else:
            modify(pid,old)
            print('The data is modified')
            continue
    elif no==3:
        try:
            pid=int(input("Enter the patient's id for which you need to delete the data:"))
        except:
            x='Enter valid values'
        delete(pid)
        print('The data is deleted')
        continue
    elif no==4:
        print("""1. COMPLETE
2. SELECTIVE""")
        try:
            num=int(input('Enter the number corresponding to your choice:'))
        except:
            x='Enter valid values'
        if num==1:
            display()
        elif num==2:
            pid=int(input("Enter the patient's id of the data which you need to display:"))
            selective(pid)
            continue
    elif no==5:
        print('Thank you for joining in')
        break
    else:
        print('Please enter valid number')
        continue
    
                    
                