#list comprehension
if __name__ == '__main__':
    x = int(input())    #first dimension
    y = int(input())    #second dimension
    z = int(input())    #third dimension
    n = int(input())    #max sum
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k)!=n)])
