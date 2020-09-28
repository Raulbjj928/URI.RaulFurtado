HORARIO=input('').split()
H1,M1,H2,M2=HORARIO
H1=int(H1)
M1=int(M1)
H2=int(H2)
M2=int(M2)

if H1>H2:
    HORA=(24-H1)+H2
    if M1>M2 :
        MINUTO=(60-M1)+M2
        HORA=(23-H1)+H2
    elif M2>M1:
        MINUTO=M2-M1
    elif M1==M2:
        MINUTO=0
if H2>H1:
    HORA=H2-H1
    if M1>M2 :
        MINUTO=60-(M1-M2)
        HORA=HORA-1
    elif M2>M1:
        MINUTO=M2-M1   
    elif M1==M2:
        MINUTO=0
if H1==H2:
    HORA=24
    if M1>=M2:
        MINUTO=(60-M1)+M2
        HORA=23
        if MINUTO==60:
            MINUTO=0
            HORA=24
    elif M2>M1:
        MINUTO=M2-M1
        HORA=0
    
print(f'O JOGO DUROU {HORA} HORA(S) E {MINUTO} MINUTO(S)')
        
    
