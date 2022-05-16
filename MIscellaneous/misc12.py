num=100
def test(a,b=10):
    if num%a==0:
        b=b+5
    else:
        b=b-5
    print("Inside the function", a,b,num,sep='*')
    return b
P=5
Q=20
test(P,Q)
test(num)
test(num,P)
