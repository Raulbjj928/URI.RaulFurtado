DI=int(input().split()[1])
HORA1=input().split(':')
HI=int(HORA1[0])
MI=int(HORA1[1])
SI=int(HORA1[2])

DF=int(input().split()[1])
HORA2=input().split(':')
HF=int(HORA2[0])
MF=int(HORA2[1])
SF=int(HORA2[2])

DIAS=DF-DI
HORAS=HF-HI

if HORAS<0:
    HORAS=HORAS+24
    DIAS=DIAS-1
MIN=MF-MI
if MIN<0:
    MIN=MIN+60
    HORAS=HORAS-1
SEG=SF-SI
if SEG<0:
    SEG=SEG+60
    MIN=MIN-1

print(DIAS,'dia(s)')
print(HORAS,' hora(s)')
print(MIN,' minuto(s)')
print(SEG,' segundo(s)')

