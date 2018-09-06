#faça um programa que leia um angulo e mostre o seu seno, coseno e tangente

from math import radians, sin, cos, tan

a = radians(float(input('Digite o seu ângulo: ')))
print('O valor de seu seno é {:.2f}, coseno é {:.2f} tangene é {:.2f}'.format(sin(a), cos(a), tan(a)))