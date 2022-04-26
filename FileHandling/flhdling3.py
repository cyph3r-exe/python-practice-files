def writingInputOnce():
    F1 = open("Hello.text", 'w')
    a = input("Enter a string: ")
    F1.write(a)
    F1.close()

def readingInput():
    F = open("Hello.txt", 'r')
    A = F.readlines()
    try:
        while (F):
            A = F.readlines()
            for i in A:
                B = i.split()
                for y in B:
                    if y == 'The':
                        print(i)
                    else:
                        continue            
    except:
        print("End of File")
    F.close()
        

writingInputOnce()
readingInput()
