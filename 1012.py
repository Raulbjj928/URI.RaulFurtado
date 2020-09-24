valores=(input('')).split()
A,B,C=valores
PI=3.14159
AT=(float(A)*float(C))/2
AC=PI*(float(C))**2
ATRAP=(float(A)+float(B))*(float(C))/2
AQ=(float(B))**2
AR=(float(A)*float(B))
print(f'TRIANGULO: {AT:.3f}')
print(f'CIRCULO: {AC:.3f}')
print(f'TRAPEZIO: {ATRAP:.3f}')
print(f'QUADRADO: {AQ:.3f}')
print(f'RETANGULO: {AR:.3f}')
