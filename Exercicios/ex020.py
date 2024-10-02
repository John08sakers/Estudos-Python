from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
list = [ a1, a2, a3, a4]
shuffle(list)
print(f'A onde de apresentação será:\n {list}')