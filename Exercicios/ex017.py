from math import hypot
co = float(input('Difite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hp = hypot(co,ca)
print(f'A hipotenusa vai medir {hp:.2f}.')
