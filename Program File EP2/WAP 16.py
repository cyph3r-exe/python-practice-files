# Debangshu Roy 
# XII-B
# 40
# Binary file converted to Sql used as a database and connected via python connectivity or mysql.connector file.
import mysql.connector 
def menu():
    print("""Please select your action
1. ADD
2. MODIFY
3. DELETE
4. DISPLAY
5. EXIT""")
def add():
    db=mysql.connector.connect(host='localhost',user='root',password='cyph3r@pc',database='cyph3r')
    cursor=db.cursor()
    try:
        Id=int(input('Enter patient id:'))
        name=input("Enter patient's name:")
        dot=input('Enter date of test(yyyy-mm-dd):')
        result=input('Enter result of RTPCR test:')
        l=str(Id)+','+'\''+name+'\''+','+'\''+dot+'\''+','+'\''+result+'\''
        a='insert into patient values'+'('+l+')'
        cursor.execute(a)
    except:
        print('Enter valid values')
    finally:
        db.commit()
def display():
    try:
        db=mysql.connector.connect(host='localhost',user='root',password='cyph3r@pc',database='cyph3r')
        cursor=db.cursor()
        cursor.execute('select * from patient')
        results=cursor.fetchall()
        for x in results:
            for y in x:
                print(y)
            print()
    except:
        print()
def selective(patientID):
    db=mysql.connector.connect(host='localhost',user='root',password='cyph3r@pc',database='cyph3r')
    cursor=db.cursor()
    cursor.execute('select * from patient where patient_id='+str(patientID))
    r=cursor.fetchall()
    for x in r:
            for y in x:
                print(y)
def delete(patientID):
    try:
        db=mysql.connector.connect(host='localhost',user='root',password='cyph3r@pc',database='cyph3r')
        cursor=db.cursor()
        cursor.execute('delete from patient where patient_id='+str(patientID))
        print('record deleted!')
        db.commit()
    except:
        print('record does not exist!')
def modify(patientID,old):
    try:
        db=mysql.connector.connect(host='localhost',user='root',password='cyph3r@pc',database='cyph3r')
        cursor=db.cursor()
        if old==1:
            pname=input('Enter new patient name: ')
            cursor.execute('update patient set patient_name='+'\''+pname+'\''+'where patient_id='+str(patientID))
        elif old==2:
            dot=input('Enter new date of test(yyyy-mm-dd): ')
            cursor.execute('update patient set dot='+'\''+dot+'\''+'where patient_id='+str(patientID))
        elif old==3:
            result=input('Enter new test result: ')
            cursor.execute('update patient set result='+'\''+result+'\''+'where patient_id='+str(patientID))
    except:
        print('record does not exist!')
    finally:
              db.commit()
            
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
            patientID=input('Enter the patient id for which you need to edit the data:')
            print("""
1. Patient's Name
2. Date Of Test
3. Result Of RTPCR Test""")
            old=int(input('Enter the number of the data you want to edit:'))
        except:
            x='Enter valid values'
        if (old>4) and (old<1):
            print('Enter valid choice')
            continue
        else:
            modify(patientID,old)
            print('The data is modified')
            continue
    elif no==3:
        try:
            patientID=input("Enter the patient's id for which you need to delete the data:")
        except:
            x='Enter valid values'
        delete(patientID)
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
            patientID=input("Enter the patient's id of the data which you need to display:")
            selective(patientID)
            continue
    elif no==5:
        print('Thank you for joining in')
        break
    else:
        print('Please enter valid number')
        continue
    
                    
                
    
    
        
        
    
    
    
