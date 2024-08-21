r = float(input('Qual valor voce possui? R$ '))
cd = float(input('Qual o valor da cotação do dolar? R$ '))
ce = float(input('Qual o valor da cotação do euro? EU$ '))
d = r / cd
e = r /ce
print('Com R$ {:.2f} voce pode comprar US$ {:.2f} e EU$ {:.2f}.'.format(r, d, e))
