N=int(input(''))
if N%2 !=0:
    for i in range(2,N,2):
        X=i**2
        print(f'{i}^2 = {X}')
else:
    for i in range(2,N+1,2):
        X=i**2
        print(f'{i}^2 = {X}')