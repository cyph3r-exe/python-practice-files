"""
Creating some co-ordinates with nested loops.
Output will be something like 
(0,1)
(0,2)
(0,3)
(1,0)
(1,1) and so on. 
"""

#Initiationg the loop 
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")