VALORES=input('').split()
NUM1,NUM2,NUM3=VALORES
NUM1=float(NUM1)
NUM2=float(NUM2)
NUM3=float(NUM3)
#definindo o " A " como o maior entre os valores
if NUM2<=NUM1>=NUM3:
    A=NUM1
    B=NUM2
    C=NUM3
    A=float(A)
    B=float(B)
    C=float(C)
if NUM1<=NUM2>=NUM3:
    A=NUM2
    B=NUM1
    C=NUM3
    A=float(A)
    B=float(B)
    C=float(C)
if NUM2<=NUM3>=NUM1:
    A=NUM3
    B=NUM2
    C=NUM1
    A=float(A)
    B=float(B)
    C=float(C)
#fazendo as operações
if A>=(B+C):
    print('NAO FORMA TRIANGULO')
elif (A+B)>C and (A+C)>B and (B+C)>A:
    if A**2==(B**2 + C**2):
        print('TRIANGULO RETANGULO')
    if A**2>(B**2 + C**2):
        print(' TRIANGULO OBTUSANGULO')
    if A**2<(B**2 + C**2):
        print('TRIANGULO ACUTANGULO')
    if A==B==C:
        print('TRIANGULO EQUILATERO')
    if A == B != C or B == C != A or A == C != B:
        print('TRIANGULO ISOSCELES')
