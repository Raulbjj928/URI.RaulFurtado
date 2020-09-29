PAR=[]
V1=int(input(''))
V2=int(input(''))
V3=int(input(''))
V4=int(input(''))
V5=int(input(''))


if V1%2==0:
    PAR.append(V1)
if V2%2==0:
    PAR.append(V2)
if V3%2==0:
    PAR.append(V3)
if V4%2==0:
    PAR.append(V4)
if V5%2==0:
    PAR.append(V5)

print(len(PAR),'valores pares')