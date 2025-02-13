import math
print('Calculando o valor da hipotenusa.')
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hipotenusa = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))


'''print('Calculando o valor da hipotenusa.')
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
'''