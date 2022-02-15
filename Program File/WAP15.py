#Debangshu Roy 
#WAP to print the followingseries and find its sum
#1,-9,25,-49...,n
#n is a input by user
num=int(input("Enter a number: "))
count=0
sumseries = 0
for x in range(1,num+1,2):
    count+=1
    if count%2==0:
        sumseries + ((-1)*(2))
        print("-",(2), sep="")

    else:
            sumseries = sumseries+(2)
            print(2)
print("Sum is", sumseries)