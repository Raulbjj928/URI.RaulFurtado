VALORES=input('').split()
A,B,C=VALORES
A=float(A)
B=float(B)
C=float(C)
D=(B**2)-(4*A*C)
E=2*A

if (E==0) or (D<0) :
    print('Impossivel calcular')
else:
    X1=(-B+(D**(1/2)))/E
    X2=(-B-(D**(1/2)))/E
    print(f'R1 = {X1:.5f}')
    print(f'R2 = {X2:.5f}')