l1 = input('').split()
l2 = input('').split()
peca1, num1, valor1 = l1
num2, num2, valor2 = l2
total = (int(num1) * float(valor1)) + (int(num2) * float(valor2))
print(f'VALOR A PAGAR: R$ {total:.2f}')
