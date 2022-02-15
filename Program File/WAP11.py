#WAP to accept 10 numbers from the user and display the largest and the smallest number.
#Debangshu Roy 

import time 
import os

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
d = int(input("Enter another number: "))
e = int(input("Enter another number: "))
f = int(input("Enter another number: "))
g = int(input("Enter another number: "))
h = int(input("Enter another number: "))
i = int(input("Enter another number: "))
j = int(input("Enter another number: "))
k = int(input("Enter another number: "))

def largest(a, b, c, d, e, f, g, h, i, j, k,):

    if a > b and a > c and a > d and a > e and a > f and a > g and a > h and a > i and a > j and a > k:
        print(a, "is the largest number")
    elif b > a and b > c and b > d and b > e and b > f and b > g and b > h and b > i and b > j and b > k:
        print(b, "is the largest number")
    elif c > a and c > b and c > d and c > e and c > f and c > g and c > h and c > i and c > j and c > k:
        print(c, "is the largest number")
    elif d > a and d > b and d > c and d > e and d > f and d > g and d > h and d > i and d > j and d > k:
        print(d, "is the largest number")
    elif e > a and d > b and e > c and e > d and e > f and e > g and e > h and e > i and e > j and e > k:
        print(e, "is the greatest number")
    elif f > a and f > b and f > c and f > d and f > e and f > g and f > h and f > i and f > j and f > k:
        print(f, "is the largest number")
    elif g > a and g > b and g > c and g > d and g > e and g > f and g > h and g > i and g > j and g > k:
        print(g, "is the largest number")
    elif h > a and h > b and h > c and h > d and h > e and h > f and h > g and h > i and h > j and h > k:
        print(h, "is the largest number")
    elif i > a and i > b and i > c and i > d and i > e and i > f and i > g and i > h and i > j and i > k:
        print(i, "is the largest number")
    elif k > a and k > b and k > c and k > d and k > e and k > f and k > g and k > h and k > i and k > j:
        print(k, "is the largest number")
    elif j > a and j > b and j > c and j > d and j > e and j > f and j > g and j > h and j > i and j > k:
        print(j, "is the largest number")
    else:
        print("There was some error in your code. Please run again")
        time.sleep(4)
        os.exit

def smallest(a, b, c, d, e, f, g, h, i, j, k,):

    if a < b and a < c and a < d and a < e and a < f and a < g and a < h and a < i and a < j and a < k:
        print(a, "is the smallest number")
    elif b < a and b < c and b < d and b < e and b < f and b < g and b < h and b < i and b < j and b < k:
        print(b, "is the smallest number")
    elif c < a and c < b and c < d and c < e and c < f and c < g and c < h and c < i and c < j and c < k:
        print(c, "is the smallest number")
    elif d < a and d < b and d < c and d < e and d < f and d < g and d < h and d < i and d < j and d < k:
        print(d, "is the smallest number")
    elif e < a and d < b and e < c and e < d and e < f and e < g and e < h and e < i and e < j and e < k:
        print(e, "is the smallest number")
    elif f < a and f < b and f < c and f < d and f < e and f < g and f < h and f < i and f < j and f < k:
        print(f, "is the smallest number")
    elif g < a and g < b and g < c and g < d and g < e and g < f and g < h and g < i and g < j and g < k:
        print(g, "is the smallest number")
    elif h < a and h < b and h < c and h < d and h < e and h < f and h < g and h < i and h < j and h < k:
        print(h, "is the smallest number")
    elif i < a and i < b and i < c and i < d and i < e and i < f and i < g and i < h and i < j and i < k:
        print(i, "is the smallest number")
    elif k < a and k < b and k < c and k < d and k < e and k < f and k < g and k < h and k < i and k < j:
        print(k, "is the smallest number")
    elif j < a and j < b and j < c and j < d and j < e and j < f and j < g and j < h and j < i and j < k:
        print(j, "is the smallest number")
    else:
        print("There was some error in your code. Please run again")
        time.sleep(4)
        os.exit

checker = int(input("Press 1 if you want to know the largest number. Print 2 if you want to know the smallest number"))

if checker == 1:
    largest(a,b,c,d,e,f,g,h,i,j,k)
elif checker == 2:
    smallest(a,b,c,d,e,f,g,h,i,j,k)
else:
    print("There was some error in your code. Please run again")
    time.sleep(4)
    os.exit

