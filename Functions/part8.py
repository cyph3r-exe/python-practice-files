#Write a Python program which accepts the radius of a 
# circle from the user and compute the area

def test(r):
    area = 2 * 3.14 * r*r
    return area

x = int(input("Enter the radius of the circle: "))
b1 = test(x)
print(f"{b1} unit square is the area of the circle")