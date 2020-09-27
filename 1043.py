VALORES=input('').split()
A,B,C=VALORES
A=float(A)
B=float(B)
C=float(C)
PERIMETRO=A+B+C
AREA=((A+B)*C)/2
if (A+B)>C and (A+C)>B and (B+C)>A:
    print(F'Perimetro = {PERIMETRO:.1f}')
else:
    print(f'Area = {AREA:.1f}')