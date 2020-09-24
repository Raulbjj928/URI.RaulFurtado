VALORES=input('').split()
A,B,C=VALORES
A=int(A)
B=int(B)
C=int(C)
MAB=int((A+B+(abs(A-B)))/2)
MBC=int((B+C+(abs(B-C)))/2)
MCA=int((C+A+(abs(C-A)))/2)
if MAB>C:
    print(f'{MAB} eh o maior')
elif MBC>A:
    print(f'{MBC} eh o maior')
elif MCA>B:
    print(f'{MCA} eh o maior')
