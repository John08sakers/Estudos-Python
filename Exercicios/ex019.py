from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro alun: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
esc = choice(lista)
print(f'O aluno escolhido foi {esc}.')
