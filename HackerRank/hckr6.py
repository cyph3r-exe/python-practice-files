def is_leap(year):
    leap = False
    
    if (year / 4) % 2 == 0:
        leap = True
    elif (year / 100) % 2 == 0:
        if (year / 400) % 2 == 0:
            leap = True
        leap = False        
    
    return leap

year = int(input())
print(is_leap(year))