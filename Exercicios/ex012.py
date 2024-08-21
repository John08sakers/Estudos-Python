prod = float(input('Qual o valor do produto : R$ '))
desc = float(input('Qual o valor do desconto : % '))
val = prod - (prod*desc/100)
print('O produto que custava R$ {:.2f}, com o desconto de {:.1f}% vai custar R$ {:.2f}.'.format(prod, desc, val))
