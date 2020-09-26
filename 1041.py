VALORES=input('').split()
X,Y=VALORES
X=float(X)
Y=float(Y)
if X>0 and Y>0:
    print('Q1')
elif X<0 and Y>0:
    print('Q2')
elif X<0 and Y<0:
    print('Q3')
elif X>0 and Y<0:
    print('Q4')
elif X==0 and (Y<0 or Y>0):
    print('Eixo Y')
elif Y==0 and (X<0 or X>0):
    print('Eixo X')
elif X==0 and Y==0:
    print('Origem')
