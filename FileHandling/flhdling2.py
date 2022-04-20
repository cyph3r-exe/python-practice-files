#WAP to increase the balance by 10% whose CID is passed as argument 
# to the function

import pickle as pc
def test(CID):
    F = open("bank.dat", 'rb+')
    try:
        while (F):
            A = pc.load(F)
            if CID == A[0]:
                B = A[2] * (0.1) + A[2]
                A.pop()
                A.append(B)
            else:
                continue
    except:
        print("End of File")
    F.close()