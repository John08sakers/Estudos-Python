sal = float(input('Digite o valor do salário: R$ '))
aum = float(input('Digite a porcentagem do aumento: % '))
novo = sal + (sal*aum/100)
print(f'O salário de R$ {sal:.2f} com aumento de {aum:.1f}% vai passar a ser R$ {novo:.2f}.')
