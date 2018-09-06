#faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa

import math
co = float(input('Digite o comprimento do cateto oposto'))
ca = float(input('Digite o comprimento do cateto adjacente'))

print('o calculo da himotenusa é {:.2f}'.format(math.hypot(co, ca)))