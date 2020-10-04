N=int(input(''))
D=0
F=0
for i in range(1,N+1):
    X=int(input(''))
    if X >=10 and X <=20:
        D=D+1
    else:
        F=F+1
print(D,'in')
print(F,'out')