dias=int(input(''))
anos=dias//365
sobra=dias-(anos*365)

meses=sobra//30
sobra=sobra-(meses*30)

dias=sobra

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
