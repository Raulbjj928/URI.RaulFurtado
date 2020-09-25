linha1 = input('').split()
linha2 = input('').split()

x1,y1=linha1
x2,y2=linha2

x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
a=(x2-x1)**2
b=(y2-y1)**2
d=(a+b)**0.5
print(f'{d:.4f}')