LISTA=[]
for i in range(1,101):
    N=int(input(''))
    LISTA.append(N)
MAIOR=max(LISTA)
POS=LISTA.index(MAIOR)
print(MAIOR)
print(POS+1)