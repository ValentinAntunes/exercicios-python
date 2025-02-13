carteira = float(input('Quantos reais você possui? '))
dolar = carteira / 5.42
print('Considerando a cotação atual, 1 dólar = 5,42')
print('Você pode comprar ${:.2f} Dólares.'.format(dolar))