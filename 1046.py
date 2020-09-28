HORARIOS=input('').split()
H1,H2=HORARIOS
H1=int(H1)
H2=int(H2)
if H1 >H2:
    HORA1=24-(H1-H2)
    print(f'O JOGO DUROU {HORA1} HORA(S)')
elif H2>H1:
    HORA2=28-(H2-H1)
    print(f'O JOGO DUROU {HORA2} HORA(S)')
elif H1==H2 or H2==H1:
    print(f'O JOGO DUROU 24 HORA(S)')