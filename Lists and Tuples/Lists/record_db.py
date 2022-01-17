record_list=[]
y=int(input('Enter no.of records to be entered'))
for x in range(1,y+1,1):
     name=input('Enter name: ')
     roll_num=int(input("Enter roll number: "))
     sub=input("Enter subject: ")
     score=float(input("Enter score: "))
     record_list.append([name,roll_num,sub,score])
print(record_list)
q=1
for p in record_list:
          print('record',q)
          print(p)
          print('Name',p[0],sep='=')
          print('Roll number',p[1],sep='=')
          print('Subject',p[2],sep='=')
          print('Score',p[3],sep='=',end='\n\n\n')
          q=q+1
