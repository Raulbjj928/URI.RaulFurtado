VALOR=int(input(''))
if (VALOR % 2 != 0):
    for i in range(VALOR,VALOR+12,2):
        print(i)
else:
    for i in range(VALOR+1,VALOR+12,2):
        print(i)
        