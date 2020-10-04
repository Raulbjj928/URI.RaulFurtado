SOMA=0
VALOR1=int(input(''))
VALOR2=int(input(''))
if VALOR1<=VALOR2:
    A=VALOR1
    B=VALOR2
else:
    A=VALOR2
    B=VALOR1
if A % 2 != 0:
    for i in range(A+2,B,2):
        SOMA+=i
elif A % 2 == 0:
    for i in range(A+1,B,2):
        SOMA+=i
print(SOMA)