VALORES=input('').split()
N1,N2,N3,N4=VALORES
N1=float(N1)
N2=float(N2)
N3=float(N3)
N4=float(N4)
MEDIA=((N1*2)+(N2*3)+(N3*4)+(N4))/10
print(f'Media: {MEDIA:.1F}')
if MEDIA>=7.0:
    print("Aluno aprovado.")
elif MEDIA<5.0:
    print("Aluno reprovado.")
elif MEDIA>=5.0 and MEDIA<=6.9:
    print("Aluno em exame.")
    NE=float(input(''))
    print(f'Nota do exame: {NE:.1F}')
    MEDIAFINAL=(MEDIA+NE)/2
    if MEDIAFINAL>=5.0:
        print("Aluno aprovado." )
    elif MEDIAFINAL<5.0:
        print("Aluno reprovado." )
    print(f'Media final: {MEDIAFINAL:.1f}')
