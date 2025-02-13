frase = str(input('Digite uma frase: ')).strip()

n = frase.upper()

print('A letra "A" aparece {} vezes na frase.'.format(n.count('A')))

n1 = n.find('A')
print('Posição que "A" aparece a primeira vez: {}'.format(n1 + 1))

n2 = n.rfind('A')
print('Posição que "A" aparece a ultima vez: {}'.format(n2 + 1))