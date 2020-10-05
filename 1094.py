N=int(input(''))
COELHO=[]
RATO=[]
SAPO=[]
for i in range(1,N+1):
        TIPO=input('').upper().split()
        A,B=TIPO
        A=int(A)
        B=str(B)
        if B =='C':
            COELHO.append(A)
        if B=='R':
            RATO.append(A)
        if B =='S':
            SAPO.append(A)

TOTAL=sum(COELHO+RATO+SAPO)
TC=sum(COELHO)
TR=sum(RATO)
TS=sum(SAPO)
PC=float(TC/TOTAL)*100
PR=float(TR/TOTAL)*100
PS=float(TS/TOTAL)*100
print(f'Total: {TOTAL} cobaias')
print(f'Total de coelhos: {TC}')
print(f'Total de ratos: {TR}')
print(f'Total de sapos: {TS}')
print(f'Percentual de coelhos: {PC:.2f} %')
print(f'Percentual de ratos: {PR:.2f} %')
print(f'Percentual de sapos: {PS:.2f} %')
