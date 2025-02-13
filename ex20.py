import random

a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))

lista = [a, b, c, d]
random.shuffle(lista)

print('Ordem de apresentação: {}'.format(lista))
