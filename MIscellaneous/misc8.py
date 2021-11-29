#checking answers for practice test

a = 30 

def call(x):
    global a 
    if x % 2 == 0:
        x = x + a
    else:
        x = x - a
    return(x)

print(call(67), end="#")