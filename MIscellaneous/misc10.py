a=True
b=False
c=True

if not a or b:
    print("Apple")
elif not a or not b or not c:
    print ("Beetle")
elif not a or b or not b and a:
    print("Catty")
else:
    print("Drama")
    
