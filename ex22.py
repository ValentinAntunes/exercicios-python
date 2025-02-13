nome = input('Digite seu nome completo: ').strip()

print('Nome completo maiúsculo: {}'.format(nome.upper()))
print('Nome completo minúsculo: {}'.format(nome.lower()))

total = nome.split()
total = ''.join(total)
print('Total de letras em seu nome: {}'.format(len(total)))

primeiro = nome.split()
print('Quantidades de letras no primeiro nome: {}'.format(len(primeiro[0])))

''' 
print('Total de letras em seu nome: {}'.format(len(nome) - nome.count(' ')))
print('Quantidades de letras no primeiro nome: {}'.format(nome.find(' ')))
'''