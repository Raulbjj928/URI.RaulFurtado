valor=float(input(''))
valor=valor+0.001

nota100=valor//100
n=valor-nota100*100

nota50=n//50
n=n-nota50*50

nota20=n//20
n=n-nota20*20

nota10=n//10
n=n-nota10*10

nota5=n//5
n=n-nota5*5

nota2=n//2
n=n-nota2*2

moeda_1=n//1
n=n-moeda_1*1

moeda50=n//0.5
n=n-moeda50*0.5

moeda25=n//0.25
n=n-moeda25*0.25

moeda10=n//0.1
n=n-moeda10*0.1

moeda05=n//0.05
n=n-moeda05*0.05

moeda01=n//0.01
n=n-moeda01*0.01

print(f'NOTAS:')
print(f'{int(nota100)} nota(s) de R$ 100.00')
print(f'{int(nota50)} nota(s) de R$ 50.00')
print(f'{int(nota20)} nota(s) de R$ 20.00')
print(f'{int(nota10)} nota(s) de R$ 10.00')
print(f'{int(nota5)} nota(s) de R$ 5.00')
print(f'{int(nota2)} nota(s) de R$ 2.00')
print(f'MOEDAS:')
print(f'{int(moeda_1)} moeda(s) de R$ 1.00')
print(f'{int(moeda50)} moeda(s) de R$ 0.50')
print(f'{int(moeda25)} moeda(s) de R$ 0.25')
print(f'{int(moeda10)} moeda(s) de R$ 0.10')
print(f'{int(moeda05)} moeda(s) de R$ 0.05')
print(f'{int(moeda01)} moeda(s) de R$ 0.01')
