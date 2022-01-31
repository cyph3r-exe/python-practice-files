mylist = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(mylist)):
    if i % 2 == 0:
        print(mylist[i])
    
print("")

#del mylist[3:]
#del mylist[:5]
del mylist[::5]
print(mylist)
