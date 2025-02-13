cidade = str(input('Digite o nome da cidade: '))

n = cidade.upper()

n1 = n.split()
print('A cidade começa com o nome SANTO ? ', end='')

print('SANTO' in n1[0])
