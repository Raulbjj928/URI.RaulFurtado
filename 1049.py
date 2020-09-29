DICA1=input('').lower()
DICA2=input('').lower()
DICA3=input('').lower()
if DICA1=='vertebrado' and DICA2=='ave' and DICA3=='carnivoro':
    ANIMAL='aguia'
if DICA1=='vertebrado' and DICA2=='ave' and DICA3=='onivoro':
    ANIMAL='pomba'
if DICA1=='vertebrado' and DICA2=='mamifero' and DICA3=='onivoro':
    ANIMAL='homem'
if DICA1=='vertebrado' and DICA2=='mamifero' and DICA3=='herbivoro':
    ANIMAL='vaca'
if DICA1=='invertebrado' and DICA2=='inseto' and DICA3=='hematofago':
    ANIMAL= 'pulga'
if DICA1=='invertebrado' and DICA2=='inseto' and DICA3=='herbivoro':
    ANIMAL='lagarta'
if DICA1=='invertebrado' and DICA2=='anelideo' and DICA3=='hematofago':
    ANIMAL='sanguessuga'
if DICA1=='invertebrado' and DICA2=='anelideo' and DICA3=='onivoro':
    ANIMAL='minhoca'
print(ANIMAL)
