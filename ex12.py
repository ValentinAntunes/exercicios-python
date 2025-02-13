preco = float(input('Digite o preço do produto: '))
Desconto = preco * 5/100
NovoPreco = preco - Desconto
print('O valor do produto com desconto de 5% é R${:.2f}'.format(NovoPreco))
