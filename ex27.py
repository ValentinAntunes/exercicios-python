nome = str(input('Digite o seu nome: ')).strip()
print('Prazer em te conhecer!')

n = nome.split()

print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n) - 1]))
