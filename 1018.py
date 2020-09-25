#Valor em dinheiro
v=int(input(''))
#divisão inteira atribuindo a variavel
n100=v//100
#atribuindo a sobra ao 'n'
n=v-n100*100
# Passando para a proxima etapa/nota e repetindo o processo
n50=n//50
n=n-n50*50

n20=n//20
n=n-n20*20

n10=n//10
n=n-n10*10

n5=n//5
n=n-n5*5

n2=n//2
n=n-n2*2

n1=n//1
n=n-n1*1
print(v)
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')
