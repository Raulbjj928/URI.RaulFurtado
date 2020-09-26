OPCAO=input('').split()
A,B=OPCAO
A=int(A)
B=int(B)
if A==1:
    C=B*4
    print(f'Total: R$ {float(C):.2f}')
elif A==2:
    C=B*4.5
    print(f'Total: R$ {float(C):.2f}')
elif A==3:
    C=B*5
    print(f'Total: R$ {float(C):.2f}')
elif A==4:
    C=B*2
    print(f'Total: R$ {float(C):.2f}')
elif A==5:
    C=B*1.5
    print(f'Total: R$ {float(C):.2f}')