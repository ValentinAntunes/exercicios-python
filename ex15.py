km = float(input('Quantos Km foram percorridos pelo carro alugado? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = (dias * 60) + (km * 0.15)
print('O custo final do carro alugado é de R${:.2f}'.format(valor))