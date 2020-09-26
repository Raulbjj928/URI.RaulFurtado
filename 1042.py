VALORES=input('').split()
A,B,C=VALORES
A=int(A)
B=int(B)
C=int(C)
#definindo o maior entre os valores
if B<A>C:
    MAIOR=A
if A<B>C:
    MAIOR=B
if B<C>A:
    MAIOR=C
#definindo o valor do meio
if B>A>C or C>A>B:
    MEIO=A
if A>B>C or C>B>A:
    MEIO=B
if B>C>A or A>C>B:
    MEIO=C
#definindo o menor valor
if B<MEIO<MAIOR:
    MENOR=B
if A<MEIO<MAIOR:
    MENOR=A
if C<MEIO<MAIOR:
    MENOR=C

print(f'{MENOR}')
print(f'{MEIO}')
print(f'{MAIOR}')
print()
print(f'{A}')
print(f'{B}')
print(f'{C}')
