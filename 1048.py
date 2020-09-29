V=float(input(''))
if 0<V<=400:
    NOVO=((15/100)*V)+V
    REAJUSTE=(15/100)*V
    PERCENTO=15
elif 400<V<=800:
    NOVO=((12/100)*V)+V
    REAJUSTE=(12/100)*V
    PERCENTO=12
elif 800<V<=1200:
    NOVO=((10/100)*V)+V
    REAJUSTE=(10/100)*V
    PERCENTO=10
elif 1200<V<=2000:
    NOVO=((7/100)*V)+V
    REAJUSTE=(7/100)*V
    PERCENTO=7
else:
    NOVO=((4/100)*V)+V
    REAJUSTE=(4/100)*V
    PERCENTO=4
print(f'Novo salario: {NOVO:.2f}')
print(f'Reajuste ganho: {REAJUSTE:.2f}')
print(f'Em percentual: {int(PERCENTO)} %')