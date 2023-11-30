import pickle
f=open("Student.dat","rb+")
a=input("Enter the student ID")
try:
    while True:
        s=pickle.load(f)
        st=f.tell()
        for i in s:
            print(i)
            if i[0]==a:
                f.seek(st)
                n=input("Enter the name")
                d=int(input("Enter the marks"))
                l=[n,d]
                pickle.dump(l,f)
except EOFError:
    print("hello mummy")
    f.close()

"""
import pickle
f1=open("Student.dat","ab")
n=int(input("How many records you want to enter"))
while n>0:
    a=int(input("Eneter the student ID:"))
    b=input("Enetr the name")
    c=int(input("Enter the marks"))
    l=[a,b,c]
    n=n-1
    pickle.dump(l,f1)
f1.close()
"""