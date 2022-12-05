#x = "some random integer"
#y = x[0]
#v = y.title()
#x = x.replace(y,v)
#print(x)

a = "This is my sentence"
b = a.split()
c = []
for i in b:
    j = i[0]
    k = j.title()
    i = i.replace(j,k)
    c.append(i)

print(' '.join(c))