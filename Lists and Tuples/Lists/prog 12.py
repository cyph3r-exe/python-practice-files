import pickle
def writebin():
    items={}
    file=open("PRODUCT.dat","ab")
    ask = 'y' #Change 1 
    while True:
        val1=input("Enter product code\t")
        val2=input("Enter product description\t")
        val3=int(input("Enter product stock\t"))
        items['prod code']=val1
        items['prod description']=val2
        items['stock']=val3
        ask=input("do you want to enter a val?(y/n)\t")
        if ask=='y' or ask == 'Y': #change 2 
            continue #change 3
        else:
            break #change 4
    pickle.dump(items,file)
    file.close()
    
writebin()
def update():
    fin=open("PRODUCT.dat","rb+")
    flag=0
    key=input("Enter product code\t")
    try:
        while True:
            bytes=fin.tell()
            rec=pickle.load(fin)
            if rec['prof code']==key:
                flag=1
                print("FOUND")
                new_stock=int(input("Enter new stock price\t"))
                rec['stock']=new_stock
                fin.seek(bytes)
                pickle,dump(rec,fin)
    except EOFError:
        if flag==0:
            print("NOT FOUND")
        fin.close()
update()

def reader():
    fin=open("PRODUCT.dat","rb+")
    try:
        while True:
            rec=pickle.load(fin)
            print(rec)
    except EOFError:
        fin.close()
reader()

    
        
