salario = float(input('Digite o salário do funcionario: '))
aumento = salario * 15/100
NovoSalario = salario + aumento
print('O novo salário do funcionário com 15% de aumento é de R${:.2f}'.format(NovoSalario))
