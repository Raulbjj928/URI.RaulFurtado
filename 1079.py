N=int(input(''))
for i in range(1,N+1):
        VALORES=input('').split()
        A,B,C=VALORES
        A=float(A)
        B=float(B)
        C=float(C)
        X = ((A*2)+(B*3)+(C*5))/10
        print(f'{X:.1f}')