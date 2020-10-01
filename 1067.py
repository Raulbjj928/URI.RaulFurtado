VALOR = int(input())
if(VALOR % 2 == 0):
  for i in range(VALOR):
    if(i % 2 != 0):
      print(i)
else:
  for i in range(VALOR + 1):
    if(i % 2 != 0):
      print(i)