#Q27 Write a function in python that counts the number of three
#lettered words in a text file 

def countfunct():
    count = 0
    F = open(file="prose.txt", mode='r')
    #file= and mode= are optional
    G = F.readlines()
    for i in G:
        H = i.split()
        for j in H:
            if len(j) >= 3:
                count += 1
            else:
                continue

