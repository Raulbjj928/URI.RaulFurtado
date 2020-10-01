PAR=0
IMPAR=0
POS=0
NEG=0

for i in range(5):
    VALOR=int(input(''))
    if VALOR%2==0:
        PAR=PAR+1
    if VALOR%2!=0:
        IMPAR=IMPAR+1
    if VALOR>0:
        POS=POS +1
    if VALOR<0:
        NEG=NEG+1

print(PAR,'valor(es) par(es)')
print(IMPAR,'valor(es) impar(es)')
print(POS,'valor(es) positivo(s)')
print(NEG,'valor(es) negativo(s)')