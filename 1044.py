VALORES=input('').split()
A,B=VALORES
A=int(A)
B=int(B)

if A>B:
    AM=(A%B)
    if AM==0:
        print("Sao Multiplos")
    else:
        print( "Nao sao Multiplos")
elif B>A:
    BM=(B%A)
    if BM==0:
        print("Sao Multiplos")
    else:
        print( "Nao sao Multiplos")