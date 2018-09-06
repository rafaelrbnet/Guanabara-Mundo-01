# crie um programa que leia um valor real qualquer e mostre na tela a sua porção inteira.

import math

n = float(input('Digite um número rela qualquer: '))

print('O numero inteiro de {} é {}'.format(n, math.trunc(n)))