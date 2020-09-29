SALARIO=float(input(''))
if 0<SALARIO<=2000:
    print('Isento')
elif 2000<SALARIO<=3000:
    ISENTO=SALARIO-2000
    PAGA=0.08*ISENTO
    print(f'R$ {PAGA:.2f}')
elif 3000<SALARIO<=4500:
    ISENTO=SALARIO-3000
    IMP=0.08*1000
    PAGA=(ISENTO*0.18)+IMP
    print(f'R$ {PAGA:.2f}')
elif SALARIO>4500:
    ISENTO=SALARIO-4500
    IMP1=0.08*1000
    IMP2=0.18*1500
    PAGA=(0.28*ISENTO)+IMP1+IMP2
    print(f'R$ {PAGA:.2f}')

    

    
