s=int(input(''))
h=s//3600
s=s-(h*3600)
m=s//60
seg=s-m*60

print(f'{h}:{m}:{seg}')