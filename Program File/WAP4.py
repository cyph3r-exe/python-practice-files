#Debangshu Roy 
#WAP to accept marks in three subjects and display the average marks and percentage. Assuming MM = 80

a = int(input("Please enter your english marks"))
b = int(input("Please enter your Physics marks"))
c = int(input("Please enter your Maths marks"))


def average(av_first, av_second, av_third):
    calc = (av_first + av_second + av_third)/3
    print(calc)


def percentage(first, second, third):
    f = first+second+third
    g = f/240
    h = g*100
    print(h)


wow = int(input("What do you want to print? If percentage, then type the number 1 and if average then type the number 2"))

if wow == 2:
    average(a, b, c)
else: percentage(a, b, c)  
