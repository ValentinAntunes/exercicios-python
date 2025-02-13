import math

a = float(input('Digite o ângulo: '))
print('O Seno de {} é {:.2f}'.format(a, math.sin(math.radians(a))))
print('O Cosseno de {} é {:.2f}'.format(a, math.cos(math.radians(a))))
print('A Tangente de {} é {:.2f}'.format(a, math.tan(math.radians(a))))
